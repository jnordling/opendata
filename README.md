## ArcGIS Open Data Bindings

### Overview
ArcGIS Open Data provides JSON export in the DCAT format, this module is a python API to access datasets and its resources via python.

### Getting Started
```sh
pip install git+https://github.com/jnordling/opendata.git
```

```python
from opendata import opendata as od

url = 'http://data.globalforestwatch.org/data.json'
conn = od.Connect(url)
data = od.Data(conn)
datasets = data.getOpenDataDatasets()
for dataset in datasets:
    title  = data.getDatasetTitle(dataset)
    print title
```
### Methods for a dataset

Method | Description
------------ | -------------
getDatasetsList() | Returns a list of dataset dictionaries
getDatasetTitle(dataset)| Returns the title of a dataset
getDatasetDescription(dataset)| Returns the description of a dataset
getDatasetPublisher(dataset)| Return the Publisher 
getDatasetKeywords(dataset)| comming soon
getDatasetLandingPage(dataset)| comming soon
getDatasetDateIssued(dataset)| comming soon
getDatasetDateModified(dataset)| comming soon
getDatasetContact(dataset)| comming soon
getDatasetResources(dataset)| comming soon
getDatasetSpatial(dataset)| comming soon
getDatasetTheme(dataset)| comming soon
getDatasetThumbnail(dataset)| comming soon
getDatasetAGOLItemID(dataset)| comming soon
getDatasetItemThumbnail(id,url)| comming soon
getResourcesTitle(resource)| comming soon

### Methods for a resource of a dataset
Method | Description
------------ | -------------
getResourcesURL(resource)| comming soon
getResourcesMediaType(resource)| comming soon
getResourcesFormat(resource)| comming soon
 