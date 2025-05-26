# Docker environment for local development


We have prepared a Dockerfile that sets up an environment similar to the grading environment for each language. Please use it for development purposes.
However, we do not guarantee that the behavior will be exactly the same as in the environment where the evaluation is performed.

With the top of this repository as the current directory, build and use the image as follows.

Example (Go language):
```
$ docker build --platform linux/amd64 -t local_tester -f docker/go/Dockerfile docker/go
$ docker run --rm -it -v $(pwd):/work -w /work local_tester

Hereafter, perform the necessary operations in docker
```


## For Windows users

For Windows, write the absolute path of the current directory converted to UNIX format instead of `$(pwd)`.

Example : UNIX format of `c:¥Users¥user1¥src` is `/c/Users/user1/src`.


## For Apple Silicon Mac users using Python

Due to library compatibility issues, there are two versions of the Dockerfile. Please build the image as follows.

### If you don't use PyTorch

Build using `Dockerfile_mac` without specifying the --platform.

```
$ docker build -t local_tester -f docker/python/Dockerfile_mac docker/python
```

In this environment, PyTorch is excluded because it cannot be installed properly.

### If you use PyTorch

Build using `Dockerfile_mac_torch`.

```
$ docker build --platform linux/amd64 -t local_tester -f docker/python/Dockerfile_mac_torch docker/python
```

In this environment, TensorFlow is excluded because it does not work properly.

Note that execution will be slower due to amd64 emulation.
