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
datasets = data.getDatasetsList()
for dataset in datasets:
    title  = data.getDatasetTitle(dataset)
    itemID = data.getDatasetAGOLItemID(dataset)
    item = data.getDatasetAGOLItem(itemID)
    print item.thumbnail
```
### Methods for a dataset

Method | Description
------------ | -------------
getDatasetsList() | Returns a list of dataset dictionaries
getDatasetTitle(dataset)| Returns the title of a dataset
getDatasetDescription(dataset)| Returns the description of a dataset
getDatasetPublisher(dataset)| Returns the publisher of dataset
getDatasetKeywords(dataset)| Returns a list of the keywords of the dataset
getDatasetUrl(dataset)| Returns the Landing Page of the dataset 
getDatasetDateIssued(dataset)| Returns dataset issued date
getDatasetDateModified(dataset)| Returns the date the dataset was modified 
getDatasetContact(dataset)| Returns the contact name of the dataset
getDatasetSpatial(dataset)| Returns the spatial extent of the dataset
getDatasetTheme(dataset)| Return the them of the dataset
getDatasetAGOLItemID(dataset)| Returns the ArcGIS online ID for the dataset

### Methods for a resource of a dataset
Method | Description
------------ | -------------
getDatasetResources(dataset)| Return a list of resource dictionaries
getResourcesTitle(resource)| Returns the title of the resource
getResourcesURL(resource)| Returns a url of the resource
getResourcesMediaType(resource)| Returns the Media Type of the data
getResourcesFormat(resource)| Returns the format of the data

### AgolItem Object Attribute
Property | Description
------------ | -------------
item.id |
item.owner |
item.created |
item.modified |
item.name |
item.title |
item.url |
item.type |
item.typeKeywords |
item.description |
item.tags |
item.snippet |
item.thumbnail |
item.extent |
item.spatialReference |
item.accessInformation |
item.licenseInfo |
item.culture |
item.access |
item.industries |
item.languages |
item.largeThumbnail |
item.banner |
item.screenshots |
item.listed |
item.size |
item.numComments |
item.numRatings |
item.avgRating |
item.numViews |
 