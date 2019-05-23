# Elastic Demos

This folder has the Canvas workpads, slides and other Elastic Search-related items we've presented.

## Elastic{on} Presentation - Seattle May 23rd 2019

Slides and related canvas workpads as presented at the Seattle Elastic conference are in the `/seattle-elasticon-may19` folder.

'Enterprise' Dashboard

![enterprise dashboard](https://raw.githubusercontent.com/tmobile/elastic-demos/master/seattle-elasticon-may19/ezgif-2-0e687b9c4ecc.gif)

## Elastic Meetup - Seattle March 2019

The meetup demo walks through building a Canvas workpad running from mock sample data that looks like:

![dashboard example](https://raw.githubusercontent.com/tmobile/elastic-demos/master/images/tmo-example-dash.gif)

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
