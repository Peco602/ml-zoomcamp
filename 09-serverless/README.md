# Homework 9

## Question 1

What's the size of the converted model?

```
43 Mb
```

## Question 2

To be able to use this model, we need to know the index of the input and the index of the output.

What's the output index for this model?

```
13
```

## Question 3

Now we need to turn the image into numpy array and pre-process it.

After the pre-processing, what's the value in the first pixel, the R channel?

```
0.5529412
```

## Question 4

Now let's apply this model to this image. What's the output of the model?

```
0.82448614
```

## Question 5

Download the base image svizor42/zoomcamp-dino-dragon-lambda:v2. You can easily make it by using docker pull command.

So what's the size of this base image?

```bash
$ docker pull svizor42/zoomcamp-dino-dragon-lambda:v2
$ docker images | grep svizor42/zoomcamp-dino-dragon-lambda
svizor42/zoomcamp-dino-dragon-lambda   v2                20ef58b21a05   8 days ago    639MB
```

## Question 6

What's the output from the model?

```bash
$ docker build -t custom-dino-dragon-lambda:latest .
$ docker run -p 8080:8080 custom-dino-dragon-lambda:latest
$ python test.py
[0.31950676441192627]
```