from opendata import opendata as od

url = 'http://data.globalforestwatch.org/data.json'
conn = od.Connect(url)
data = od.Data(conn)
datasets = data.getDatasetsList()
for dataset in datasets:
    title  = data.getDatasetTitle(dataset)
    # Returns the Item ID for ArcGIS online
    itemID = data.getDatasetAGOLItemID(dataset)

    # Creating a AGOL Item
    item = data.getDatasetAGOLItem(itemID)
    # Accessing the Item thumbnail.

    print item.thumbnail

