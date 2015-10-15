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

