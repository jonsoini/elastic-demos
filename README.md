# Elastic Demos

This folder has the Canvas workpads, dummy data script and notes on how to recreate the Canvas demo from the March '19 Seattle Elasticsearch meetup group.

## The Demo

The demo walks through building a Canvas workpad running from mock sample data that looks like:

[img]

## Pre-requisites

This demo assumes you're running Elasticsearch and Kibana 7.x locally, no security applied. If you're not, download both and run them locally with default settings.

## Setup the mock data script

The Canvas demo is set to use the latest data flowing into the cluster. First, setup your template. The mapping below is for Elastic 7.x (no more doc types!)

``` json
PUT dummy_app
{
  "mappings": {
    "properties": {
      "customer.location": {
        "type": "geo_point"
      }
    }
  }
}
```

Then run the dummy_data.py script. You can use something like `watch -n 1 python dummy_data.py` to run it every 1s to POST your dummy data. Be sure to `pip install faker` as a dependency of the script.

If everything is happy you should be generating mock data. See the notes inside the dummy_data.py script for how it works and why it does what it does.

## Load the workpad

Open up kibana and selec the Canvas tab, and then import the workpad JSON. Go to the 2nd screen and you should have data.