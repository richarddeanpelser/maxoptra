import requests
from Schemas import Tag
   
class MaxAPI:
    headers = {'Authorization': 'Bearer 123', 'Content-Type': 'application/json'}
    base_url = 'https://stoplight.io/mocks/maxoptra/api-v6-documentation/13517567'
    # orderreference = 'string'
    tags = Tag
    def __init__(self):
        self.headers
        self.base_url        
    
    def get(self,tag):
        r = requests.get(f'{self.base_url}/{tag}', headers = self.headers)
        res_json = r.json()
        #return json.dumps(res_json, indent =4)
        return res_json['data']

    def exists(self,reference_number,data=[]):
        if reference_number in data:
            return True
        else: 
            return False

    def post(self,tag,json_data):
        print(f'{self.base_url}/{tag}')
        r = requests.post(f'{self.base_url}/{tag}', headers = self.headers, json = json_data)
        return r.status_code
        # # status = max.post(max.tags.orders(),json_data[0])





   
# max = MaxAPI()
# json_data = max.get(max.tags.orders())  
# print(max.exists('one'))
# # print(status)
# print(json_data)



              

# Function to read the json file from disk




  

# json_template = json_reader('json_templates/template.json')

# r = requests.get(f'{url}/{orderreference}',headers = headers)
# res_json = r.json()
# x = requests.post(url, headers = headers, json = json_template)

# Use status code for logic to determine if an order exists
# print(r.status_code)
#print(x.status_code)
#print(res_str_data)

# Add try and except for empty json response if order does not exist
# res_str_data = str(res_json['data']['referenceNumber'])
#print(res_str_data)

 