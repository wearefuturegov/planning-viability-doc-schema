import csv
import json

csvfile = open('summaries.csv', 'r')
jsonfile = open('summaries.json', 'w')

fieldnames = ("first","second","third")
#reader = csv.DictReader(csvfile, fieldnames)
# for row in reader:
# 	json.dump(row, jsonfile)
# 	jsonfile.write('\n')

data = []

assessment = {}
assessment['application'] = {}
assessment['application'] = { "application.name": "a", "application.identifier": "ID"}
assessment['property'] = {}
assessment['property'] = { "property.addressPrimary": "b","property.centroidLatLng": "c"}
assessment['proposal'] = []
assessment['proposal'] = {"proposal.residentialUnits": 1}

data.append(assessment)

assessment = {}
assessment['application'] = {}
assessment['application'] = { "application.name": "1", "application.identifier": "ID"}
assessment['property'] = {}
assessment['property'] = { "property.addressPrimary": "2","property.centroidLatLng": "3"}
assessment['proposal'] = []
assessment['proposal'] = {"proposal.residentialUnits": 4}

data.append(assessment)


#data['applications'].append({'thing': 'a', 'thing2': 'b'})

print(json.dumps(data, indent=4))

with open('summaries.json.txt', 'w') as outfile:
    json.dump(data, outfile)

#import pandas as pd
#csv_file = pd.DataFrame(pd.read_csv("summaries.csv", sep = ",", header = 0, index_col = False))
#csv_file.to_json("summaries.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)