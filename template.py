import json
from csv import DictReader


def csv_reader(csv_file_path):
    csv_data = []
    with open(csv_file_path) as csv_file:
        reader = DictReader(csv_file)
        for row in reader:
            csv_data.append(row)
    return csv_data        

              
def json_reader(path):
    with open(path) as json_file:
        return json.load(json_file)

def merge():
    json_template = json_reader('json_templates/template.json')
    csv_data = csv_reader('csvdata/MaxOptra_Collections_20032022.csv')
    merged_data = []
    for cd in csv_data:
        for td in json_template:
            json_template['referenceNumber'] = cd['orderreference']
            json_template['vehicleRequirements'] = cd['vehiclerequirements']
            json_template['clientName'] = cd['clientName']
            json_template['customerLocation']['referenceNumber'] = cd['orderreference']
            json_template['customerLocation']['address'] = cd['customerLocationAddress']
            json_template['capacity1'] = float((cd['capacity']))
            json_template['customFields']['date'] = cd['date']
            json_template['customFields']['territory'] = cd['schedulingZoneName']
            json_template['customFields']['cost'] = cd['cost']
            json_template['customFields']['sellingPrice'] = cd['sellingPrice']
            json_template['customFields']['accountnumber'] = cd['accountnumber']
            json_template['customFields']['company'] = cd['company']
            json_template['customFields']['charisma'] = cd['charisma']
            merged_data.append(json_template)
        
        
    
    return json.dumps(merged_data,indent=4)
    
        ##### Append this to new list and return list

print(merge())


# print(merge())        
# all_data = to_json(merge())
# for a in all_data:
#     print(a)





# all_data = to_json(all_data)
# for a in all_data:
#     print(a)

# if __name__ == '__main__':
    
      
        

