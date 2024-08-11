import sqlite3
import unittest

# Database connection
conn = sqlite3.connect('assignment3_edit.db')
cursor = conn.cursor()

# User class definition
class User:
    def __init__(self, first, last, ID):
        self.first = first
        self.last = last
        self.ID = ID
        
    def getInfo(self):
        print("First Name: ", self.first, "\nLast Name: ", self.last, "\nID: ", self.ID)

# Student class inherits from User
class Student(User):
    def __init__(self, first, last, ID):
        super().__init__(first, last, ID)
        
    # Method definitions here...

import sqlite3

# Database connection
conn = sqlite3.connect('assignment3_edit.db')
cursor = conn.cursor()

# User table setup
sql_command = """
CREATE TABLE IF NOT EXISTS ENROLLMENT (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL
);
"""
cursor.execute(sql_command)
conn.commit()

class User:
    def __init__(self, first, last, ID):
        self.first = first
        self.last = last
        self.ID = ID

    def setFirst(self, first):
        self.first = first

    def setLast(self, last):
        self.last = last

    def setID(self, ID):
        self.ID = ID

    def getInfo(self):
        print("First Name: ", self.first, "\nLast Name: ", self.last, "\nID: ", self.ID)

    def Search(self):
        print("\nCourse")
        cursor.execute("SELECT * FROM COURSE")
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)
        return True

    def Search_Parameters(self):
        parameter_option = int(input("Select Parameter\n1. CRN (ID)\n2. Title\n3. Department\n4. Time\n5. Weekday\n6. Credits\n7. Exit\n"))
        if parameter_option == 1:
            u_CRN = input("Enter CRN: ")
            self.search_CRN(u_CRN)
        elif parameter_option == 2:
            u_Title = input("Enter Title: ")
            self.search_Title(u_Title)
        elif parameter_option == 3:
            u_DEPT = input("Enter Department: ")
            self.search_DEPT(u_DEPT)
        elif parameter_option == 4:
            u_Time = input("Enter Time (Ex: 12:30PM): ")
            self.search_Time(u_Time)
        elif parameter_option == 5:
            u_Day = input("Enter Weekdays (Ex: T/TR, M/F, W): ")
            self.search_Weekday(u_Day)
        elif parameter_option == 6:
            u_Credits = self.get_integer("Enter Number of Credits: ", "The Number of Credits Must be an Integer")
            self.search_Credits(u_Credits)

    def search_CRN(self, u_CRN):
        cursor.execute("SELECT * FROM COURSE WHERE CRN =?", (u_CRN,))
        query_result = cursor.fetchall()
        if query_result:
            for i in query_result:
                print(i)
            return True
        else:
            print("No CRN of " + u_CRN + " Exists in the System")
            return False

    def search_Title(self, u_Title):
        u_Title = u_Title.capitalize()
        cursor.execute("SELECT * FROM COURSE WHERE TITLE = ?", (u_Title,))
        query_result = cursor.fetchall()
        if query_result:
            for i in query_result:
                print(i)
            return True
        else:
            print('No Course has Title "' + u_Title + '"')
            return False

    def search_DEPT(self, u_DEPT):
        u_DEPT = u_DEPT.upper()
        cursor.execute("SELECT * FROM COURSE WHERE DEPT = ?", (u_DEPT,))
        query_result = cursor.fetchall()
        if query_result:
            for i in query_result:
                print(i)
            return True
        else:
            print('No Course has Department "' + u_DEPT + '"')
            return False

    def search_Time(self, u_Time):
        u_Time = u_Time.upper()
        cursor.execute("SELECT * FROM COURSE WHERE time = ?", (u_Time,))
        query_result = cursor.fetchall()
        if query_result:
            for i in query_result:
                print(i)
            return True
        else:
            print('No Course in the System Has a Start Time of "' + u_Time +'"')
            print("\n***Make Sure to Enter the Time in this Format: Hour:MinutesAM/PM (Ex: 12:30PM)")
            return False

    def search_Weekday(self, u_Day):
        u_Day = u_Day.upper()
        cursor.execute("SELECT * FROM COURSE WHERE weekday = ?", (u_Day,))
        query_result = cursor.fetchall()
        if query_result:
            for i in query_result:
                print(i)
            return True
        else:
            print('No Course in the System has Weekdays "' + u_Day + '"')
            print("\n***Make Sure to Enter the Weekdays in this Format: Weekday/Weekday  (Ex: T/TR, M/F, W)")
            return False

    def search_Credits(self, u_Credits: int):
        cursor.execute("SELECT * FROM COURSE WHERE credits = ?", (u_Credits,))
        query_result = cursor.fetchall()
        if query_result:
            for i in query_result:
                print(i)
            return True
        else:
            print('No Course in the System has "', u_Credits, '" Credits')
            return False

    def get_integer(self, num: str, error_message: str = "") -> int:
        while True:
            try:
                return int(input(num))
            except ValueError:
                print(error_message)

class Student(User):
    def __init__(self, first, last, ID):
        super().__init__(first, last, ID)

    def AddCourse(self):
        course_id = self.get_integer("Enter CRN: ", "CRN Must be an Integer")
        cursor.execute("SELECT * FROM ENROLLMENT WHERE student_id = ? AND course_id = ?", (self.ID, course_id))
        if cursor.fetchone():
            print(f"Course with CRN {course_id} is already on your schedule.\n")
        else:
            cursor.execute("SELECT * FROM COURSE WHERE CRN = ?", (course_id,))
            if cursor.fetchone():
                cursor.execute("INSERT INTO ENROLLMENT (student_id, course_id) VALUES (?, ?)", (self.ID, course_id))
                conn.commit()
                print(f"Course {course_id} added to your schedule.")
            else:
                print(f"Course with CRN {course_id} does not exist\n")

    def RemoveCourse(self):
        u_id = self.get_integer("Enter CRN: ", "CRN Must be an Integer")
        cursor.execute("SELECT * FROM ENROLLMENT WHERE course_id = ? AND student_id = ?", (u_id, self.ID))
        if cursor.fetchone():
            y_n = input("Remove COURSE? (Y/N): ")
            if y_n.upper() == "Y":
                cursor.execute("DELETE FROM ENROLLMENT WHERE course_id = ? AND student_id = ?", (u_id, self.ID))
                conn.commit()
                print("Course removed from schedule.")
        else:
            print("Course Does Not Exist")

    def Print(self):
        cursor.execute("SELECT COURSE.* FROM COURSE, ENROLLMENT WHERE COURSE.CRN = ENROLLMENT.course_id AND ENROLLMENT.student_id = ?", (self.ID,))
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)

    def check_conflicts(self):
        cursor.execute("SELECT * FROM COURSE WHERE (time, weekday, semester, year) IN (SELECT COURSE.time, COURSE.weekday, COURSE.semester, COURSE.year FROM COURSE, ENROLLMENT WHERE ENROLLMENT.student_id = ? AND COURSE.CRN = ENROLLMENT.course_id GROUP BY time, weekday, semester, year HAVING COUNT(*) > 1)", (self.ID,))
        if cursor.fetchone():
            print("WARNING: The following courses create conflicts in your schedule\n")
            cursor.execute("SELECT * FROM COURSE WHERE (time, weekday, semester, year) IN (SELECT COURSE.time, COURSE.weekday, COURSE.semester, COURSE.year FROM COURSE, ENROLLMENT WHERE ENROLLMENT.student_id = ? AND COURSE.CRN = ENROLLMENT.course_id GROUP BY time, weekday, semester, year HAVING COUNT(*) > 1)", (self.ID,))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
        else:
            print("There are no conflicts in your schedule\n")

class Instructor(User):
    def __init__(self, first, last, ID):
        super().__init__(first, last, ID)

    def Assemble(self):
        u_class = self.get_integer("Enter CRN: ", "CRN Must be an Integer")
        u_id = self.get_integer("Enter Student ID: ", "Student ID Must be an Integer")
        cursor.execute("SELECT * FROM STUDENT WHERE ID =?", (u_id,))
        if cursor.fetchone():
            y_n = input(f"Add Student to Roster of {u_id}? (Y/N)\n")
            if y_n.upper() == "Y":
                cursor.execute("INSERT INTO ENROLLMENT (student_id, course_id) VALUES (?, ?)", (u_id, u_class))
                conn.commit()
                print("Student added to the roster.")
        else:
            print("Student ID does not exist.")

    def Print_roster(self):
        course_id = self.get_integer("Enter CRN: ", "CRN Must be an Integer")
        cursor.execute("SELECT STUDENT.* FROM STUDENT JOIN ENROLLMENT ON STUDENT.ID = ENROLLMENT.student_id WHERE ENROLLMENT.course_id = ?", (course_id,))
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)

    def Print_Schedule(self):
        cursor.execute("SELECT COURSE.* FROM COURSE JOIN ENROLLMENT ON COURSE.CRN = ENROLLMENT.course_id WHERE ENROLLMENT.instructor_id = ?", (self.ID,))
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)

class LoginSystem:
    def __init__(self):
        self.users = {}  # Holds user credentials

    def create_user(self, username, password):
        self.users[username] = password  # Store username and password

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print(f"Welcome, {username}!")
            return True
        else:
            print("Invalid username or password.")
            return False

# Initialize login system
login_system = LoginSystem()

# Adding some test users
login_system.create_user("student1", "pass123")
login_system.create_user("instructor1", "pass456")

# Main menu
def main_menu():
    while True:
        print("\n1. Login\n2. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login_system.login(username, password):
                # Here you can implement user-specific actions based on the role
                user_role = username.split("1")[0]  # Simplistic role determination
                if user_role == "student":
                    student = Student("John", "Doe", 1)  # Example Student
                    student.Print()
                elif user_role == "instructor":
                    instructor = Instructor("Jane", "Smith", 2)  # Example Instructor
                    instructor.Print_roster()
            else:
                print("Login failed. Please try again.")
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run main menu
main_menu()

# Close database connection
conn.close()

