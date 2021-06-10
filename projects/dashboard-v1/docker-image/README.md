# Bubble Plotter

A simple app for making a bubble plot on top of a mapbox map.

## Instructions

Place a csv in the directory ./data. Call it data.csv. The columns that should be there are the following:

lat: latitude
long: longitude
size: numerical column that denotes the size of the bubble.
color: optional, a numerical column to denote another dimention
name: will appear when you hover on the bubble.

Build and run the docker image:

```BASH
docker build -t bubble-map .
docker run -d -p  8050:8050 bubble-map
```

open your browser at localhost:8050.
