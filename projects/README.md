# Projects

## Jupyter-Service

I put a simple jupyter notebook server in a deployment, with multiple replicas. I also define a service (node-port) which allows the user to access this from the outside. This is about as simple as it gets.

## dashboard-v1

I create a custom image with a dash server in it and a bubble map. The setup serves this dash board to the user.

## dashboard-db

I do exaclty as above, but in the backend I have a postgres server giving the data to the dashboard. This is a way to demonstrate a simple architecture that has multiple components that need to talk to each other.
Both of the images are custom images.