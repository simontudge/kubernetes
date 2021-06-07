# Projects

## Jupyter-Service

I put a simple jupyter notebook server in a deployment, with multiple replicas. I also define a service (node-port) which allows the user to access this from the outside. This is about as simple as it gets.

## Other

Think of some other project that uses what we have learnt.

Ideas, something with flask? What about putting your running app in docker containers and k8.

Something with Dash, make a dashboard of something. I want at least two components to make it interesting enough.

Running app? The front end you already have, and this is a pain to build in any case. Re-write the backend in flask. Two pods, which you can put in two deployments. Run them both?

Then do you want some kind of database, redis or something else, just to add something more interesting? Maybe we could simply log the requests sent?