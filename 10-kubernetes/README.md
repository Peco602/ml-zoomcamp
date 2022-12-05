# Homework 10

## Question 1

Run it to test that it's working locally:

```bash
$ docker build -t zoomcamp-model:v001 .
$ docker run -it --rm -p 9696:9696 zoomcamp-model:v001
```

And in another terminal, execute q6_test.py file:

```bash
$ python q6_test.py
{'get_card': True, 'get_card_probability': 0.7692649226628628}
```

## Question 2

What's the version of kind that you have?

```bash
$ kind --version
kind version 0.17.0
```

## Question 3

What's the smallest deployable computing unit that we can create and manage in Kubernetes (kind in our case)?

```
Pod
```

## Question 4

What's the Type of the service that is already running there?

```bash
$ kubectl get svc
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   2m13s
```

## Question 5

To be able to use the docker image we previously created (zoomcamp-model:v001), we need to register it with kind.

What's the command we need to run for that?

```bash
$ kind load docker-image zoomcamp-model:v001
```

## Question 6

What is the value for `<Port>`?

```
9696
```

```bash
$ kubectl apply -f kube-config/deployment.yaml
deployment.apps/credit-card created
$ kubectl get pods
NAME                           READY   STATUS             RESTARTS   AGE
credit-card-7f4b74588d-896zp   1/1     Running   0          6s
```

## Question 7

What do we need to write instead of `<???>`?

```
credit-card
```

```bash
$ kubectl apply -f kube-config/service.yaml
service/credit-card createdkubectl delete hpa credit-card-hpa
$ kubectl get svc
NAME          TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
credit-card   LoadBalancer   10.96.68.119   <pending>     80:30879/TCP   18s
kubernetes    ClusterIP      10.96.0.1      <none>        443/TCP        13m
```

## Testing the service

```bash
$ kubectl port-forward service/credit-card 9696:80
Forwarding from 127.0.0.1:9696 -> 9696
Forwarding from [::1]:9696 -> 9696
```

And in another terminal, execute q6_test.py file:

```bash
$ python q6_test.py
{'get_card': True, 'get_card_probability': 0.7692649226628628}
```

## Autoscaling

Use the following command to create the HPA:

```bash
$ kubectl autoscale deployment credit-card --name credit-card-hpa --cpu-percent=20 --min=1 --max=3
horizontalpodautoscaler.autoscaling/credit-card-hpa autoscaled
$ kubectl get hpa
NAME              REFERENCE                TARGETS         MINPODS   MAXPODS   REPLICAS   AGE
credit-card-hpa   Deployment/credit-card   <unknown>/20%   1         3         0          13s
```

## Increase the load

```bash
$ python q6_test_loop.py
```

## Question 8 (optional)

Run kubectl get hpa credit-card-hpa --watch command to monitor how the autoscaler performs. Within a minute or so, you should see the higher CPU load; and then - more replicas. What was the maximum amount of the replicas during this test?

```bash
$ get hpa --watch
NAME              REFERENCE                TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
credit-card-hpa   Deployment/credit-card   1%/20%    1         3         1          2h
credit-card-hpa   Deployment/credit-card   1%/20%    1         3         1          2h
credit-card-hpa   Deployment/credit-card   3%/20%    1         3         1          2h
credit-card-hpa   Deployment/credit-card   21%/20%   1         3         1          2h
credit-card-hpa   Deployment/credit-card   20%/20%   1         3         1          2h
credit-card-hpa   Deployment/credit-card   24%/20%   1         3         1          2h
credit-card-hpa   Deployment/credit-card   24%/20%   1         3         2          2h
credit-card-hpa   Deployment/credit-card   10%/20%   1         3         2          2h
credit-card-hpa   Deployment/credit-card   11%/20%   1         3         2          2h
credit-card-hpa   Deployment/credit-card   10%/20%   1         3         2          2h
credit-card-hpa   Deployment/credit-card   8%/20%    1         3         2          2h
credit-card-hpa   Deployment/credit-card   9%/20%    1         3         2          2h
credit-card-hpa   Deployment/credit-card   11%/20%   1         3         2          2h
credit-card-hpa   Deployment/credit-card   2%/20%    1         3         2          2h
credit-card-hpa   Deployment/credit-card   9%/20%    1         3         2          2h
credit-card-hpa   Deployment/credit-card   10%/20%   1         3         2          2h
```