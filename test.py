from opendata import opendata as od

url = 'http://data.globalforestwatch.org/data.json'
conn = od.Connect(url)


data = od.Data(conn)

datasets = data.getOpenDataDatasets()

print datasets
for dataset in datasets:
    title  = data.getDatasetTitle(dataset)
    print title
