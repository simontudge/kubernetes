As an excercies, do the same as in the project, but deploy the pods as deployments.

To run simply create all of the yaml files here with kubectl create -f ...

Then do this

```BASG
minikube service voter-service --url
minikube service result-service --url

```

Check that the data flows from one app to the other.