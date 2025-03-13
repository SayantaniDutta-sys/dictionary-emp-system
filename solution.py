# Solution


employees = {}

def add_employee(emp_id, name, age, department):
    if emp_id in employees:
        print("Employee ID already exists!")
        return
    if not name.isalpha():
        print("Invalid name! Use only alphabets.")
        return
    if not age.isdigit() or int(age) <= 0:
        print("Invalid age! Enter a positive integer.")
        return
    employees[emp_id] = {"name": name, "age": int(age), "department": department}
    print("Employee added successfully!")

def view_employees():
    if not employees:
        print("No employees found!")
        return
    print("\nList of Employees:")
    for emp_id, details in employees.items():
        print(f"{emp_id}: {details['name']} - {details['age']} - {details['department']}")

def search_employee(emp_id):
    if emp_id in employees:
        details = employees[emp_id]
        print(f"Employee Found: {emp_id} - {details['name']} - {details['age']} - {details['department']}")
    else:
        print("Employee not found!")

def update_employee(emp_id, name=None, age=None, department=None):
    if emp_id not in employees:
        print("Employee not found!")
        return
    if name and not name.isalpha():
        print("Invalid name! Use only alphabets.")
        return
    if age and (not age.isdigit() or int(age) <= 0):
        print("Invalid age! Enter a positive integer.")
        return
    if name:
        employees[emp_id]["name"] = name
    if age:
        employees[emp_id]["age"] = int(age)
    if department:
        employees[emp_id]["department"] = department
    print("Employee updated successfully!")

def delete_employee(emp_id):
    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted successfully!")
    else:
        print("Employee not found!")

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            department = input("Enter Department: ")
            add_employee(emp_id, name, age, department)
        elif choice == "2":
            view_employees()
        elif choice == "3":
            emp_id = input("Enter Employee ID to search: ")
            search_employee(emp_id)
        elif choice == "4":
            emp_id = input("Enter Employee ID to update: ")
            name = input("Enter new Name (or press Enter to skip): ")
            age = input("Enter new Age (or press Enter to skip): ")
            department = input("Enter new Department (or press Enter to skip): ")
            update_employee(emp_id, name if name else None, age if age else None, department if department else None)
        elif choice == "5":
            emp_id = input("Enter Employee ID to delete: ")
            delete_employee(emp_id)
        elif choice == "6":
            print("Exiting Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

main()
