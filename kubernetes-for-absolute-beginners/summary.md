# Kubernetes Documentation

I’m following the course “Kubernetes for Absolute Beginners” on Udemy. Here I’ll write a few summary notes.

## Docker

To understand Kubernetes first you need to understand docker. It’s a prerequisite.

Docker is used to make containers. Containers are isolated processes, they are a little bit like virtual machines, except that they are much more light weight. The main difference is that containers share processes with one another, such as the operating system.

For instance you could put a postgres database in one container. You could then put a nginx server in another container. They would share the same linux kernel and probably the same operating system.

Docker lets you create containers easily. Any system that has docker will then be able to run the container that you create regardless of the operating system and setup of the host machine.

The concept of a container is broader than docker. There are other ways of making containers, but docker seems to be the overall most popular one to use. You could use kubernetes with other container making software, but again mostly people use docker, so at least in the first instance you can probably assume that you will use kubernetes and docker together.

## What Kubernetes is for

Docker is useful for building isolated processes. However, it does not really solve the problem of setting up systems, particularly if these systems are spread over many nodes. These are some of the issues that kubernetes solves:

Creating multiple copies of the same container, and potentially doing this dynamically. E.g. a web application, you might want to run more and more copies of this process as you get more users.
Spreading your application across multiple nodes. This is tricky, but kubernetes does it nicely.
Configuring networking, getting different containers to talk to each other and to be able to communicate with the outside world.
Updating apps. You might want to update the version of an app. You can do this easily with kubernetes.

So kubernetes gives you a way to specify all of these things using a command line tool and a series of configuration files.

You can say things like, “give me 5 redis containers, spread over my two nodes”, “or update all of my redis containers to version x” or “scale up the number of containers I have”, or “create a service that allows all redis containers to be accessed at a single ip address” (Of course you don’t specify these instructions in English like this, this is just the idea of what kind of things you can do.

## Architecture

A bit like hadoop kubernetes is actually a bunch of pieces of software. The architecture follows the principle of master and worker nodes. There is one node that manages the orchestration of all the processes, called the master, it has a load of software installed on it, such as an api server, a controller and a scheduler. Other worker nodes have only kubelet installed on them. The exact architecture is not so important to know in detail at this stage.

On your own machine you can have kubectl installed. This is a client for interacting with a kubernetes cluster.

You can install something called minikube locally. This gives you a local kubernetes cluster, that live either in a virtual machine or a docker container. It gives you a single node kubernetes cluster which is very useful for trying things out without worrying about breaking anything. Note that there is an extra layer of confusion here, in that your entire cluster sits in a container itself, and then runs additional containers. This abstraction is largely hidden from you.

## Kubernetes Objects

There are different kinds of objects that we talk about here. Each one is defined by a yaml file.

### PODs

Pods are the most basic unit in Kubernetes. You can put a single container in a pod. It simply wraps a container, and at its most basic level it does not give you much more functionality than a docker container. In principle you can also put more than one container.

You need a docker image already defined, and then in your config you simply point to this image. See `./test-pod` for an example.

### Replica Set

This is a set of more or less identical pods. It helps you in creating multiple copies of the same pod. Multiple pods sit inside one replica set. To define these you simply specify a pod and the number of replicas that you want inside the replica set. This can be scaled up or down. Link to example replica set.

At this point you also see the concept of a selector, an important concept in kubernetes. You specify what labels will count for pods that live in the replica set. In this way the replica set can manage pods that it didn’t create itself.

Note that there is something called a replicator controller. This is in principle depriacted in favour of a replica set, although it is still possible to use them, they do pretty much the same thing.

See `./test-replicator-set` for an example.

### Deployment

Deployment is another layer for a replica set, and works in a similar way. It simply gives you in addition a way to manage the deployment of the replica set. This way you can, for example, update the apps in your replica set. If you update it it will do this sequentially so that your service is not offline. It also acts as a kind of version control, allowing you to roll back to a previous setup if something goes wrong, and provides a history of all changes that you ever did.

See `./deployment` for an example.

### Services

Services let your containers interact with the outside world and with each other. Every pod has an internal IP address, so in theory you could access them with this address. However, these addresses may change, especially if you make more copies of the pods, or delete them. In addition, you don’t really want to think about the individual copies of the same application, so services allow you to treat all pods of a certain kind with one interface.

#### Node Port

This is a kubernetes object that essentially acts as a port forward. So if you build a front end app in a pod (or deployment), then a node port object will do the job of directing your end users to the application.

See `service-node-port` for an example.

#### Cluster IP

Another type of service. It is used mostly for the components to talk to each other, for instance if I put a database in a deployment/replica set. It gives a single interface to all pods of a certain kind. You can access these pods from within your cluster with the name and the port that you define.

There is no self standing example for this one, however, the concept is used in the final project, so see `./micro-service-example` for how this is used.

Note that services also use the idea of a selector to define which pods a service should connect to.

## Example Project from the course

The course then goes on to define an example project. This is a voting and results app. There are 5 containers and 4 services. See the directory for more details.

First we deploy all of the components as pods, see `./micro-service-example` and then we do them all as deployments (which is better practise). See `micro-service-deployments`.

## Kubernetes in the cloud

You can run kubernetes in the cloud easily. The lectures show you three possible solutions. AWS, Google, and Azure (microsoft). Of course you could use any cloud provider, but these are the big ones, and come with pre-configured kubernetes options, so are a good choice. See the lectures for specific details.

## Further courses

There are two further courses, one for admin, and one for developers. Both might be useful, but you should probably start with the developers one to begin with.
