

class Order:
    # Custom class with all variables in the __init__()
    def __init__(
        self,
        reference_number,
        vehicle_requirements,
        client_name,
        
        capacity,
        custom_fields,
        customer_location,
        additional_instructions,
        task,
        priority
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
     
    def import_orders(dict):
        data = dict
        imported = []
        for td in data:
            order = Order(reference_number = td['orderreference'],
            task = td['task'],
            priority = td['priority'],
            vehicle_requirements = td['vehiclerequirements'],
            additional_instructions = td['additionalInstructions'],
            client_name = td['clientName'],
            customer_location = {'referenceNumber': td['orderreference'],'address': td['customerLocationAddress']},
            capacity = td['capacity'],
            custom_fields = {
                'date': td['date'],
                'territory': td['schedulingZoneName'],
                'cost': float(td['cost']),
                'sellingPrice': td['sellingPrice'],
                'accountnumber': td['accountnumber'],
                'company': td['company'],
                'charisma': td['charisma']}
            )
            imported.append(order.__dict__)
        return imported

