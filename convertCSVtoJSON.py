import csv
import json

def mk_int(s):
    s = s.strip()
    return int(s) if s else 0

def mk_float(s):
    s = s.strip()
    return float(s) if s else 0

csvfile = open('summaries.csv', 'r')

reader = csv.DictReader(csvfile)
data = []
counter = 1
for row in reader:
	assessment = {}
	assessment['application'] = {}
	assessment['application'] = {
	"application.name": row['application.name'],
	"application.identifier": row['application.identifier'],
	"application.planningAuthorityID": row['application.planningAuthorityID']
	}
	assessment['property'] = {}
	assessment['property'] = {
	"property.addressPrimary": row['property.addressPrimary'],
	"property.centroidLatLng": row['property.centroidLatLng'],
	#"property.boundaryPolygon": row['property.boundaryPolygon']
	}
	assessment['proposal'] = []
	assessment['proposal'] = {
	"proposal.residentialUnits": mk_int(row['proposal.residentialUnits']), 
	"proposal.habitableRooms": mk_int(row['proposal.habitableRooms']), 
	"proposal.commercialArea": mk_float(row['proposal.commercialArea']), 
	"proposal.storeysMax": mk_int(row['proposal.storeysMax']), 
	"proposal.viabilityAssessmentScenarioDate": row['proposal.viabilityAssessmentScenarioDate'],
	"proposal.grossDevelopmentValue": mk_int(row['proposal.grossDevelopmentValue']),
	"proposal.constructionCostsTotal": mk_int(row['proposal.constructionCostsTotal']),
	"proposal.professionalFeesTotal": mk_int(row['proposal.professionalFeesTotal']),
	"proposal.marketingAndLettingFeesTotal": mk_int(row['proposal.marketingAndLettingFeesTotal']),
	"proposal.financeCostTotal": mk_int(row['proposal.financeCostTotal']),
	"proposal.planningObligationsCostTotal": mk_int(row['proposal.planningObligationsCostTotal']),
	"proposal.developerProfitTotal": mk_int(row['proposal.developerProfitTotal']),
	"proposal.residualLandValue": mk_int(row['proposal.residualLandValue']),
	"proposal.benchmarkLandValue": mk_int(row['proposal.benchmarkLandValue']),
	"proposal.totalCosts": mk_int(row['proposal.totalCosts']),
	"proposal.viabilityAssessmentAuthor": row['proposal.viabilityAssessmentAuthor'],
	"proposal.viabilityAssessmentOnBehalfOf": row['proposal.viabilityAssessmentOnBehalfOf'],
	"proposal.viabilityScenarioName": row['proposal.viabilityScenarioName']
	}
	data.append(assessment)
	counter += 1

print("Finished processing",counter,"lines.")

with open('summaries.json', 'w') as outfile:
    json.dump(data, outfile, indent="\t")
