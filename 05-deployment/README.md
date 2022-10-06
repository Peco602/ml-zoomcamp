# Homework 5

## Question 1

- What's the version of pipenv you installed?

```bash
$ pipenv --version
pipenv, version 2022.9.4
```

## Question 2

- Use Pipenv to install Scikit-Learn version 1.0.2
- What's the first hash for scikit-learn you get in Pipfile.lock?

```bash
$ pipenv shell
$ pipenv install scikit-learn==1.0.2
...
$ grep scikit-learn Pipfile.lock -A 2
        "scikit-learn": {
            "hashes": [
                "sha256:08ef968f6b72033c16c479c966bf37ccd49b06ea91b765e1cc27afefe723920b",
```

## Question 3

- What's the probability that this client will get a credit card?

```bash
$ PREFIX=https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/course-zoomcamp/cohorts/2022/05-deployment/homework
$ wget $PREFIX/model1.bin
$ wget $PREFIX/dv.bin
$ md5sum model1.bin dv.bin
3f57f3ebfdf57a9e1368dcd0f28a4a14  model1.bin
6b7cded86a52af7e81859647fa3a5c2e  dv.bin
$ pipenv run python prediction_local.py
0.16213414434326598
```

## Question 4

- What's the probability that this client will get a credit card?

Launch the prediction service:

```bash
$ pipenv run python prediction_service.py
 * Serving Flask app 'credit-card'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:9696
 * Running on http://10.27.128.74:9696
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 746-548-029
```

Execute the prediction test:

```bash
$ pipenv run python prediction_test.py
{'credit_card': True, 'credit_card_probability': 0.9282218018527452}
```

## Question 5

- So what's the size of this base image?

```bash
$ sudo docker pull svizor/zoomcamp-model:3.9.12-slim
...
$ sudo docker images | grep zoomcamp
svizor/zoomcamp-model   3.9.12-slim   571a6fdc554b   3 days ago   125MB
```

## Question 6

- What's the probability that this client will get a credit card now?

Launch the prediction service:

```bash
$ sudo docker build -t mlzoomcamp-homerwork5:latest .
...
$ sudo docker run -p 9696:9696 mlzoomcamp-homerwork5:latest
```

Execute the prediction test:

```bash
$ pipenv run python prediction_test.py
{'credit_card': True, 'credit_card_probability': 0.7692649226628628}
```

