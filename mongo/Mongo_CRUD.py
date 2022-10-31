import pymongo

def insertData(name, roll_no, email, marks, age):
    stud_collection.insert_one({"Name": name, "Roll_no": roll_no, "Email": email, "Marks": marks, "Age": age})

def displayData():
    data = stud_collection.find()
    for d in data:
        print(d)

def displayDataById(roll_no):
    data = stud_collection.find({'Roll_no': roll_no})
    list = []
    for d in data:
        print(d)
        list.append(d)
    return list

def updateData(prev, next):
    #print("Data")
    stud_collection.update_one(prev, next)

def deleteData(roll_no):
    stud_collection.delete_one({'Roll_no': roll_no})

if __name__ == "__main__":
    print("Welcome to MongoDB crud app")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['demo1']
    stud_collection = db['student']

    while(1):
        print("\nMenu")
        print("1. insert data")
        print("2. Update data")
        print("3. Delete data")
        print("4. Display data")
        print("5. Search data")
        print("6. Exit")
        choice = int(input("Enter a choice:"))
        if choice == 1:
            name = input("Enter name:")
            roll_no = int(input("Enter roll no:"))
            email = input("Enter email")
            marks = int(input("Enter marks:"))
            age = input("Enter age:")
            insertData(name, roll_no, email, marks, age)
            print("inserted")
        elif choice == 2:
            roll_no = int(input("Enter roll no:"))
            print("Current Data:")
            d1 = displayDataById(roll_no)
            print(d1)
            print("Enter new data:")
            name = input("Enter name:")
            roll_no = int(input("Enter the roll no:"))
            email = input("Enter email:")
            marks = int(input("Enter marks:"))
            age = input("Enter age:")
            prev = {"Roll_no": roll_no}
            next = {"$set": {"Name": name, "Roll_no": roll_no, "Email": email, "Marks": marks, "Age": age}}
            updateData(prev, next)
            print("updated")
        elif choice == 3:
            roll_no = int(input("Enter roll no:"))
            deleteData(roll_no)
            print("deleted")
        elif choice == 4:
            print("\n Available data")
            displayData()
            print()
        elif choice == 5:
            roll_no = int(input("Enter roll no:"))
            data = displayDataById(roll_no)
            print("found")
        elif choice == 6:
            print("\nprogram finished")
            exit(1)