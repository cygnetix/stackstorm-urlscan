# URL Scan Integration Pack

Intergration with the https://urlscan.io web service. Currently it allows for URLs to be submitted and a link to their results, and a screenshot, to be returned.

## Configuration

Copy the example configuration in [urlscan.yaml.example](./urlscan.yaml.example) to `/opt/stackstorm/configs/urlscan.yaml` and populated it with a valid apikey.

It should contain:

* ``apikey`` - An apikey obtained by signing up for an account on https://urlscan.io.
* ``verify`` - Determines if SSL is validated (defautls to on)

## Actions

* ``scan_url`` - Submits the url to the urlscan.io service and returns a link to the results.
