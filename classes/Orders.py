import copy
class Order:
 
    def __init__(
        self,
        reference_number = "str",
        task = "str",
        priority = "str",
        vehicle_requirements = "str",
        client_name = "str",
        capacity = "str",
        custom_fields = {},
        customer_location = {},
        additional_instructions = "str"
        ):
        self.reference_number = reference_number
        self.task = task
        self.priority = priority
        self.vehicle_requirements = vehicle_requirements
        self.additional_instructions = additional_instructions
        self.client_name = client_name
        self.customer_location = customer_location
        self.capacity1 = capacity
        self.custom_fields = custom_fields
     
    def import_orders(self,dict):
        data = dict
        imported = []
        for td in data:
            self.reference_number = td['orderreference']
            self.task = td['task']
            self.priority = td['priority']
            self.vehicle_requirements = td['vehiclerequirements']
            self.additional_instructions = td['additionalInstructions']
            self.client_name = td['clientName']
            self.customer_location = {'referenceNumber': td['orderreference'],'address': td['customerLocationAddress']}
            self.capacity = td['capacity']
            self.custom_fields = {
                'date': td['date'],
                'territory': td['schedulingZoneName'],
                'cost': float(td['cost']),
                'sellingPrice': td['sellingPrice'],
                'accountnumber': td['accountnumber'],
                'company': td['company'],
                'charisma': td['charisma']}
            
            # printing the dictionary after each iteration returns expected results
            # results appended to the list "imported" always uses the same row
            # result = (self.__dict__)
            
            imported.append(copy.deepcopy(self.__dict__))
        return imported
        

