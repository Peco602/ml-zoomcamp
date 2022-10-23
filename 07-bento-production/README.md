# Homework 6

The virtual environment must be first initialized:

```
$ pipenv install
$ pipenv shell
```

## Question 1

- What's the version of BentoML you installed?

```bash
$ bentoml --version
bentoml, version 1.0.7
```

## Question 2

- How big approximately is the saved BentoML model?

```bash
$ bentoml models list
 Tag                                 Module           Size        Creation Time       
 credit_risk_model:sdg5vqcsvopkm64z  bentoml.xgboost  197.77 KiB  2022-10-23 01:20:34
```

## Question 3

Say you have the following data that you're sending to your service:

```python
{
  "name": "Tim",
  "age": 37,
  "country": "US",
  "rating": 3.14
}
```

- What would the pydantic class look like? You can name the class `UserProfile`.

```python
from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: int
    country: str
    rating: float
```

## Question 4

We've prepared a model for you that you can import using:

```bash
$ curl -O https://s3.us-west-2.amazonaws.com/bentoml.com/mlzoomcamp/coolmodel.bentomodel
$ bentoml models import coolmodel.bentomodel
```

What version of scikit-learn was this model trained with?

```bash
$ bentoml models list
 Tag                                   Module           Size        Creation Time       
 credit_risk_model:it5biecsi6pkm64z    bentoml.xgboost  197.77 KiB  2022-10-22 13:22:37 
 mlzoomcamp_homework:qtzdz3slg6mwwdu5  bentoml.sklearn  5.79 KiB    2022-10-13 13:42:14 
$ bentoml models get mlzoomcamp_homework:qtzdz3slg6mwwdu5
name: mlzoomcamp_homework
version: qtzdz3slg6mwwdu5
module: bentoml.sklearn  
labels: {}               
options: {}              
metadata: {}             
context:                 
  framework_name: sklearn
  framework_versions:    
    scikit-learn: 1.1.1  
  bentoml_version: 1.0.7 
  python_version: 3.9.12 
signatures:              
  predict:               
    batchable: false     
api_version: v1          
creation_time: '2022-10-13T20:42:14.411084+00:00'                              
```

## Question 5

Create a bento out of this scikit-learn model. The output type for this endpoint should be `NumpyNdarray()`.

Send this array to the Bento:

```
[[6.4,3.5,4.5,1.2]]
```

You can use curl or the Swagger UI. What value does it return?

```bash
$ bentoml serve cool_service.py:svc
...
$ curl -X POST -H "Content-Type: application/json" -d '[[6.4,3.5,4.5,1.2]]' http://localhost:3000/classify
{"result":1}
```

## Question 6

Update your bento's runner tag and test with both models. Which model allows more traffic (more throughput) as you ramp up the traffic?

Hint 1: Remember to turn off and turn on your bento service between changing the model tag. Use Ctl-C to close the service in between trials.

Hint 2: Increase the number of concurrent users to see which one has higher throughput

Which model has better performance at higher volumes?

```bash
$ curl -O https://s3.us-west-2.amazonaws.com/bentoml.com/mlzoomcamp/coolmodel2.bentomodel
$ bentoml models import coolmodel2.bentomodel
$ bentoml models list
 Tag                                   Module           Size        Creation Time       
 credit_risk_model:sdg5vqcsvopkm64z    bentoml.xgboost  197.77 KiB  2022-10-23 01:20:34 
 mlzoomcamp_homework:jsi67fslz6txydu5  bentoml.sklearn  5.82 KiB    2022-10-14 07:48:43 
 mlzoomcamp_homework:qtzdz3slg6mwwdu5  bentoml.sklearn  5.79 KiB    2022-10-13 13:42:14
$ pipenv install scikit-learn==1.1.1
$ bentoml serve cool_service.py:svc --production
$ locust -H http://localhost:3000
```

|   | Max users | # Requests | # Fails | Median (ms) | 90%ile (ms) | 99%ile (ms) | Average (ms) | Min (ms) | Max (ms) | Average size (bytes) | Current RPS | Current Failures/s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model 1 | 100 | 6345 | 2 | 160 | 850 | 2500 | 342 | 8 | 6149 | 12 | 74.9 | 0 |
| Model 1 | 500 | 6870 | 6 | 330 | 1800 | 11000 | 925 | 14 | 29548 | 12 | 82.6 | 0.2 |
| Model 1 | 750 | 6392 | 1 | 350 | 1500 | 5500 | 667 | 9 | 9050 | 12 | 82.5 | 0 |
| Model 2 | 100 | 5063 | 34 | 240 | 1900 | 4200 | 664 | 8 | 5350 | 13 | 55.8 | 1 |
| Model 2 | 500 | 4939 | 6 | 550 | 2700 | 8900 | 1119 | 9 | 12399 | 12 | 63.9 | 0 |
| Model 2 | 750 | 4652 | 10 | 570 | 2800 | 6400 | 1125 | 9 | 10701 | 12 | 60.6 | 0.4 |

The best is model one.
