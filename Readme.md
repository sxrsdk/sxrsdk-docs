# Documentation for Samsung XR SDK

Samsung XR SDK documentation is generated with [mkdocs](http://www.mkdocs.org/)

## Install

To view and publish the documentation, you have to install mkdocs first

1. Install [Python](https://www.python.org/)
2. Install [pip](https://pip.pypa.io/en/stable/installing/)
3. Install [mkdocs](http://www.mkdocs.org/) and [mkdocs-material](http://squidfunk.github.io/mkdocs-material/) using following command
```
pip install mkdocs
pip install mkdocs-material
pip install BeautifulSoup
```

## Editing

You can edit Samsung XR SDK documentation with any editor and review it with any browser.


1. Start a local server by
```
mkdocs serve
```
2. Open http://127.0.0.1:8000/ in a browser
3. Edit the file of your choice and the browser will auto update based on your edits


## Deployment
Use the following command to publish document

use -v to specify version of SXR SDK release
use -deploy to specify where to upload the release

A release version of Samsung XR SDK documentation site will be generated in the `site` folder

```
python publish.py -v 5.0 -deploy github
```
