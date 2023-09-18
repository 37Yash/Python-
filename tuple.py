# Function to create an employee tuple
def create_employee(name, employee_id, department, salary):
    employee_info = (name, employee_id, department, salary)
    return employee_info

# Function to display employee information
def display_employee(employee_info):
    name, employee_id, department, salary = employee_info
    print("Employee Information:")
    print("Name:", name)
    print("Employee ID:", employee_id)
    print("Department:", department)
    print("Salary:", salary)

# Main program
if __name__ == "__main__":
    # Create employee tuples
    employee1 = create_employee("John Doe", 101, "HR", 50000)
    employee2 = create_employee("Jane Smith", 102, "Engineering", 60000)
    employee3 = create_employee("Bob Johnson", 103, "Sales", 55000)

    # Display employee information
    display_employee(employee1)
    display_employee(employee2)
    display_employee(employee3)
