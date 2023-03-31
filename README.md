# sf_docker_7.8.7

This app download favicon specified site
You should specify url start with http. For example: https://mail.ru

First build docker image from Dockerfile

Run container mounting /tmp/favicons container to host to save results:

```
docker run --rm --mount type=bind,src=/tmp/favicons,dst=/tmp/favicons <IMAGE> <ULR>
```
