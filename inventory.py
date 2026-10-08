resources = [
    {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
    {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
    {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]

fellows = {
    "F001": "Ada",
    "F002": "John",
    "F003": "Grace"
}

borrow_records = []

def add_resources():

    new_id = input("Enter resources ID: ")
    new_name = input("Enter resources name: ")
    new_category = input("Enter resources category: ")
    quantity = int(input("Enter resources quantity: "))

    for resource in resources:
        if resource["id"] == new_id:
            print("id already exist")
            return

    


    dic = {

        "id": new_id,
        "name": new_name,
        "category": new_category,
        "total": quantity,
        "available": quantity
    }

    resources.append(dic)


add_resources()  
print(resources)  


def list_resources():

    for resource in resources:
        print("ID:", resource["id"])
        print("Name:", resource["name"])
        print("Category:", resource["category"])
        print("Total:", resource["total"])
        print("Available:", resource["available"])
        print()

def borrow_resources():
    fellow_id = input("Enter fellow ID: ")
    resource_id = input("Enter resource ID: ")
    quantity = int(input("Enter quantity: "))

    if fellow_id not in fellows:
        print("Fellow ID not found")
        return 

    found_resource = None    

    for resource in resources:
        if resource["id"] == resource_id:
            found_resource = resource

    if found_resource is None:
        print("Resource ID not found") 
        return   

    if quantity <= 0:
        print("Quantity must be greater than zero")   
        return 

    if quantity > found_resource["available"]:
        print("Insufficient stock")
        return 

    found_resource["available"] -= quantity 

    borrow_records.append({

        "fellow_id": fellow_id,
        "resource_id": resource_id,
        "quantity": quantity
    })
borrow_resources() 

print(resources)
print(borrow_records)    

