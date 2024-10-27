import mysql.connector

# Database connection
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Meerut@321",
    database="stud_management",
    auth_plugin='mysql_native_password'
)

# Creating a cursor object
cursorObject = dataBase.cursor()

def register_user():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    phone_number = input("Enter your phone number: ")

    sql = "INSERT INTO users (username, password_hash, phone_number) VALUES (%s, %s, %s)"
    val = (username, password, phone_number)  # Storing plain text password
    try:
        cursorObject.execute(sql, val)
        dataBase.commit()
        print("User registered successfully.\n")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    sql = "SELECT password_hash FROM users WHERE username = %s"
    cursorObject.execute(sql, (username,))
    result = cursorObject.fetchone()

    if result and result[0] == password:  # Checking plain text password
        print("Login successful!\n")
        return True
    else:
        print("Invalid username or password.\n")
        return False

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter the age: "))
    course = input("Enter the Course: ")
    sql = "INSERT INTO s_students (roll_number, s_name, age, course) VALUES (%s, %s, %s, %s)"
    val = (student_id, name, age, course)
    cursorObject.execute(sql, val)
    dataBase.commit()
    print("Student added successfully.\n")

def update_student():
    student_id = input("Enter Student ID to update: ")
    name = input("Enter new Student Name: ")
    age = int(input("Enter the age: "))
    course = input("Enter the Course: ")
    sql = "UPDATE s_students SET s_name = %s, age = %s, course = %s WHERE roll_number = %s"
    val = (name, age, course, student_id)
    cursorObject.execute(sql, val)
    dataBase.commit()
    print("Student updated successfully.\n")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    sql = "DELETE FROM s_students WHERE roll_number = %s"
    val = (student_id,)
    cursorObject.execute(sql, val)
    dataBase.commit()
    print("Student deleted successfully.\n")

def view_students():
    query = "SELECT * FROM s_students"
    cursorObject.execute(query)
    myresult = cursorObject.fetchall()
    print("Student Records:")
    for x in myresult:
        print(x)
    print()

def main():
    while True:
        print("Welcome to the Student Management System")
        print("1. Register ")
        print("2. Login ")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            if login_user():
                while True:
                    print("1. Add Student")
                    print("2. Update Student")
                    print("3. Delete Student")
                    print("4. View Students")
                    print("5. Logout")

                    action = input("Enter your choice: ")

                    if action == '1':
                        add_student()
                    elif action == '2':
                        update_student()
                    elif action == '3':
                        delete_student()
                    elif action == '4':
                        view_students()
                    elif action == '5':
                        print("Logging out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

    # Closing database connection
    dataBase.close()

if __name__ == "__main__":
    main()
