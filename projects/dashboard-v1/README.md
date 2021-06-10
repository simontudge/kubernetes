# Map dashboard using kubernetes

This is a toy example in which i put a dash dashboard server with a bubble map in a container. The code for making the container is also here, but this has been pushed to docker hub, so you can run everything building the image yourself.

If the image is built and you have minikube up and running that you can simply create the two files in `./setup` and then run somthing like

```BASH
minikub service map-app --url
```

to get a URL to veiw the service.