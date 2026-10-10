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
    try:
        quantity = int(input("Enter resources quantity: "))
    except ValueError:
        print("Quantity must be a valid number") 
        return
    if quantity <= 0:
        print("Quantity must be greater than zero")
        return       

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


#add_resources()  
#print(resources)  


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
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Quantity must be a valid number")
        return    

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

def return_resource():
    fellow_id = input("Enter fellow ID: ")
    resource_id = input("Enter resource ID: ")
    try:
        quantity = int(input("Enter quantity to return: "))
    except ValueError:
        print("Quantity must be a valid number")
        return    

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

    found_record = None

    for record in borrow_records:
        if record["fellow_id"] == fellow_id and record["resource_id"] == resource_id:
            found_record = record
            break

    if found_record is None:
        print("No borrow record found")
        return 

    if quantity <= 0:
        print("Quantity must be greater than zero")
        return    

    if quantity > found_record["quantity"]:
        print("Return quantity exceeds borrowed quantity")
        return 

    found_record["quantity"] -= quantity

    found_resource["available"] += quantity   

    if found_record["quantity"] == 0:
        borrow_records.remove(found_record)

def inventory_report():

    total_units = 0
    available_units = 0

    for resource in resources:
        total_units += resource["total"]
        available_units += resource["available"]

    borrow_units = total_units - available_units   
    print("Total unit", total_units)
    print("Available unit", available_units)
    print("Borrow units", borrow_units)    




while True:
    print("\n1. Add a resource")
    print("2. List resources")
    print("3. Borrow a resource")
    print("4. Return a resource")
    print("5. Inventory report")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "6":
        print("Goodbye!")
        break
       
    elif choice == "1":
        add_resources()
    elif choice == "2":
        list_resources()
    elif choice == "3":
        borrow_resources()
    elif choice == "4":
        return_resource()
    elif choice == "5":
        inventory_report()
    else:
        print("Invalid option. Please choose 1-6")        








        

        