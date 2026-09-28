import pandas as pd
import numpy as np
import time

class Employee_Management:
    records = {}
    csv_file = 'Employee_Records.csv'

    @staticmethod
    def load_records():
        if not pd.io.common.file_exists(Employee_Management.csv_file):
            return

        try:
            saved_records = pd.read_csv(Employee_Management.csv_file)
        except pd.errors.EmptyDataError:
            return

        if 'Name' not in saved_records.columns:
            return

        for _, row in saved_records.iterrows():
            name = row.pop('Name')
            Employee_Management.records[name] = row.dropna().to_dict()

    @staticmethod
    def save_records():
        data = pd.DataFrame.from_dict(Employee_Management.records, orient='index')
        data.index.name = 'Name'
        data.reset_index().to_csv(Employee_Management.csv_file, index=False)

    def add_employee_details():
        name = input('Enter the name of the Employee: ').capitalize()
        age = int(input('Enter the age of the Employee: '))
        department = input('Enter the department of the Employee: ').capitalize()
        salary = float(input('Enter the salary of the Employee: '))
        emp_id = max((details['ID'] for details in Employee_Management.records.values()), default=0) + 1
        doj = input('Enter the date of joining of the Employee (YYYY-MM-DD): ')
        gender = input('Enter the gender of the Employee (M/F): ').upper()
        if gender not in ['M', 'F']:
            print("Invalid gender input. Please enter 'M' for Male or 'F' for Female.")
            return

        Employee_Management.records[name] = {'Age': age, 'Department': department, 'Salary': salary, 'ID': emp_id, 'Date of Joining': doj, 'Gender': gender}
        Employee_Management.save_records()
        print(f"Employee {name} added successfully.")

    def display_employee_details():
        if not Employee_Management.records:
            print("No employee records found.")
            return

        return pd.DataFrame(Employee_Management.records).T

    def update_employee_details():
        name = input('Enter the name of the Employee to update: ').capitalize()
        if name in Employee_Management.records:
            age = int(input('Enter the new age of the Employee: '))
            department = input('Enter the new department of the Employee: ').capitalize()
            salary = float(input('Enter the new salary of the Employee: '))
            doj = input('Enter the new date of joining of the Employee (YYYY-MM-DD): ')

            Employee_Management.records[name] = {'Age': age, 'Department': department, 'Salary': salary, 'ID': Employee_Management.records[name]['ID'], 'Date of Joining': doj, 'Gender': Employee_Management.records[name]['Gender']}
            Employee_Management.save_records()
            Employee_Management.save_records()
            print(f"Employee {name} updated successfully.")
        else:
            print(f"Employee {name} not found.")

    def update_specific_employee_details():
        name = input('Enter the name of the Employee to update: ').capitalize()
        if name in Employee_Management.records:
            print("What would you like to update?")
            print("1. Age")
            print("2. Department")
            print("3. Salary")
            print("4. Date of Joining")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                age = int(input('Enter the new age of the Employee: '))
                Employee_Management.records[name]['Age'] = age
            elif choice == '2':
                department = input('Enter the new department of the Employee: ').capitalize()
                Employee_Management.records[name]['Department'] = department
            elif choice == '3':
                salary = float(input('Enter the new salary of the Employee: '))
                Employee_Management.records[name]['Salary'] = salary
            elif choice == '4':
                doj = input('Enter the new date of joining of the Employee (YYYY-MM-DD): ')
                Employee_Management.records[name]['Date of Joining'] = doj
            else:
                print("Invalid choice.")
                return

            print(f"Employee {name} updated successfully.")
        else:
            print(f"Employee {name} not found.")

    def delete_employee_details():
        name = input('Enter the name of the Employee to delete: ').capitalize()
        if name in Employee_Management.records:
            del Employee_Management.records[name]
            Employee_Management.save_records()
            print(f"Employee {name} deleted successfully.")
        else:
            print(f"Employee {name} not found.")

    def specific_employee_details():
        name = input('Enter the name of the Employee to view details: ').capitalize()
        if name in Employee_Management.records:
            return pd.DataFrame(Employee_Management.records[name], index=[name])
        else:
            print(f"Employee {name} not found.")

    def specific_department_details():
        department = input('Enter the department to view employee details: ').capitalize()
        df = pd.DataFrame(Employee_Management.records).T
        dept_df = df[df['Department'] == department]
        if not dept_df.empty:
            return dept_df
        else:
            print(f"No employees found in the {department} department.")

    def details():
        choice = input("Press 1 to view the names of the employees\n 2 to view the details of salary of emplyees along with their name and Id\n 3 to view the department details of employees along with the name and ID\n 4 to view the age details of employees along with the name and ID\n 5 to view the date of joining details of employees along with the name and ID\n\n Your Choice: ")
        if choice == '1':
            print("Employee Names:")
            for name in Employee_Management.records.keys():
                print(name)
        elif choice == '2':
            df = pd.DataFrame(Employee_Management.records).T
            print(df[['Salary', 'ID']])
        elif choice == '3':
            df = pd.DataFrame(Employee_Management.records).T
            print(df[['Department', 'ID']]) 
        elif choice == '4':
            df = pd.DataFrame(Employee_Management.records).T
            print(df[['Age', 'ID']]) 
        elif choice == '5':
            df = pd.DataFrame(Employee_Management.records).T
            print(df[['Date of Joining', 'ID']]) 
        else:
            print("Invalid choice.")

    def sort_employee_details():
        choice = input("Press 1 to sort by Age\n 2 to sort by Salary\n 3 to sort by Department\n 4 to sort by Date of Joining\n\n Your Choice: ")
        df = pd.DataFrame(Employee_Management.records).T
        if choice == '1':
            sorted_df = df.sort_values(by='Age')
            print(sorted_df)
        elif choice == '2':
            sorted_df = df.sort_values(by='Salary')
            print(sorted_df)
        elif choice == '3':
            sorted_df = df.sort_values(by='Department')
            print(sorted_df)
        elif choice == '4':
            sorted_df = df.sort_values(by='Date of Joining')
            print(sorted_df)
        else:
            print("Invalid choice.")

    def find_min_max_employee_details():
        choice = input("Press 1 to find the employee with minimum Age\n 2 to find the employee with maximum Age\n 3 to find the employee with minimum Salary\n 4 to find the employee with maximum Salary\n\n Your Choice: ")
        df = pd.DataFrame(Employee_Management.records).T
        if choice == '1':
            min_age_employee = df[df['Age'] == df['Age'].min()]
            print(min_age_employee)
        elif choice == '2':
            max_age_employee = df[df['Age'] == df['Age'].max()]
            print(max_age_employee)
        elif choice == '3':
            min_salary_employee = df[df['Salary'] == df['Salary'].min()]
            print(min_salary_employee)
        elif choice == '4':
            max_salary_employee = df[df['Salary'] == df['Salary'].max()]
            print(max_salary_employee)
        else:
            print("Invalid choice.")

    def clear_all_employee_details():
        Employee_Management.records.clear()
        Employee_Management.save_records()
        print("All employee records have been cleared.")

#Driver Code
Employee_Management.load_records()
print("Welcome to the Employee Management System")
repeat = 'y'
while repeat.lower() == 'y':
    print(" 1. Add Employee Details")
    print(" 2. Display Employee Details")
    print(" 3. Update Employee Details")
    print(" 4. Delete Employee Details")
    print(" 5. Search Employee Details")
    print(" 6. Sort Employee Details")
    print(" 7. Find Minimum/Maximum Employee Details")
    print(" 8. Clear All Employee Details")
    choice = input("Enter your choice (1-8): ")
    print("\n")
    if choice == '1':
        Employee_Management.add_employee_details()
    elif choice == '2':
        print(Employee_Management.display_employee_details())
    elif choice == '3':
        Employee_Management.update_employee_details()
    elif choice == '4':
        Employee_Management.delete_employee_details()
    elif choice == '5':
        print(" 1. Search by Name")
        print(" 2. Search by Department")
        search_choice = input("Enter your choice (1-2): ")
        if search_choice == '1':
            print(Employee_Management.specific_employee_details())
        elif search_choice == '2':
            print(Employee_Management.specific_department_details())
        else:
            print("Invalid choice.")
    elif choice == '6':
        Employee_Management.sort_employee_details()
    elif choice == '7':
        Employee_Management.find_min_max_employee_details()
    elif choice == '8':
        Employee_Management.clear_all_employee_details()
    else:
        print("Invalid choice.")
    repeat = input("Do you want to continue? (y/n): ")
    while repeat.lower() not in ['y', 'n']:
        repeat = input("Invalid input. Please enter 'y' to continue or 'n' to exit: ")

print("\n")
print("Saving employee records to Employee_Records.csv...")
Employee_Management.save_records()
time.sleep(2)
print("Thank you for using the Employee Management System.")