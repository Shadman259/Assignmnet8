
import unittest







class User:
    #attribute
    
    #constructor
    def __init__(self, first, last, ID):
        self.first = first
        self.last = last
        self.ID = ID
        
    #methods
    def setFirst(self, first):
        self.first = first
    def setLast(self, last):
        self.last = last
    def setID(self, ID):
        self.ID = ID
    def getInfo(self):
       print("First Name: ", self.first, "\nLast Name: ", self.last, "\nID: ", self.ID )
    def Search(self):
        print("\nCourse")
        cursor.execute("SELECT * FROM COURSE")
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)
        return True
    def Search_Parameters(self):
        #print("Search by parameters was Successfully Used")
        parameter_option = int(input("Select Parameter\n1. CRN (ID)\n2. Title\n3. Department\n4. Time\n5. Weekday\n6. Credits\n7. Exit\n"))
        if parameter_option == 1:
            u_CRN = input("Enter CRN: ")
            self.search_CRN(u_CRN)
        if parameter_option == 2:
            u_Title = input("Enter Title: ")
            self.search_Title(u_Title)
        if parameter_option == 3:
            u_DEPT = input("Enter Department: ")
            self.search_DEPT(u_DEPT)
        if parameter_option == 4:
            u_Time = input("Enter Time (Ex: 12:30PM): ")
            self.search_Time(u_Time)
        if parameter_option == 5:
            u_Day = input("Enter Weekdays (Ex: T/TR, M/F, W): ")
            self.search_Weekday(u_Day)
        if parameter_option == 6:
            #u_Credits = int(input("Enter Number of Credits: "))
            #print(self.get_integer("Enter Number of Credits: ","The Number of Credits Must be an Integer"))
            u_Credits = self.get_integer("Enter Number of Credits: ","The Number of Credits Must be an Integer")
            self.search_Credits(u_Credits)
            



    def search_CRN(self,u_CRN):
        cursor.execute("SELECT * FROM COURSE WHERE CRN =?", (u_CRN,))
        query_result = cursor.fetchall()
        if query_result:
                for i in query_result:
                    print(i)
                t_f = True
        else:
                print("No CRN of " + u_CRN + " Exists in the System")
                t_f = False
        return t_f
    def search_Title(self,u_Title):
         u_Title = u_Title.capitalize()
         cursor.execute("SELECT * FROM COURSE WHERE TITLE = ?", (u_Title,))
         query_result = cursor.fetchall()
         if query_result:
                for i in query_result:
                    print(i)
                t_f = True
         else:
                print('No Course has Title "' + u_Title + '"')
                t_f = False
         return t_f
    def search_DEPT(self, u_DEPT):
        u_DEPT = u_DEPT.upper()
        cursor.execute("SELECT * FROM COURSE WHERE DEPT = ?", (u_DEPT,))
        query_result = cursor.fetchall()
        if query_result:
            for i in query_result:
                print(i)
            t_f = True
        else:
            print('No Course has Department "' + u_DEPT + '"')
            t_f = False
        return t_f
    def search_Time(self,u_Time):
        u_Time = u_Time.upper()
        cursor.execute("SELECT * FROM COURSE WHERE time = ?", (u_Time,))
        query_result = cursor.fetchall()
        if query_result:
            for i in query_result:
                print(i)
            t_f = True
        else:
            print('No Course in the System Has a Start Time of "' + u_Time +'"')
            print("\n***Make Sure to Enter the Time in this Format: Hour:MinutesAM/PM (Ex: 12:30PM)")
            t_f = False
        return t_f
    def search_Weekday(self, u_Day):
        u_Day = u_Day.upper()
        cursor.execute("SELECT * FROM COURSE WHERE weekday = ?", (u_Day,))
        query_result = cursor.fetchall()
        if query_result:
            for i in query_result:
                print(i)
            t_f = True
        else:
            print('No Course in the System has Weekdays "' + u_Day + '"')
            print("\n***Make Sure to Enter the Weekdays in this Format: Weekday/Weekday  (Ex: T/TR, M/F, W)")
            t_f = False
        return t_f
    def search_Credits(self,u_Credits: int):
        
        cursor.execute("SELECT * FROM COURSE WHERE credits = ?", (u_Credits,))
        query_result = cursor.fetchall()
        if query_result:
            for i in query_result:
                print(i)
            t_f = True
        else:
            print('No Course in the System has "',u_Credits,'" Credits')
            t_f = False
        return t_f
    def get_integer(self,num: str, error_message: str = "") -> int:
        while True:
            try:
                return int(input(num))
            except ValueError:
                print(error_message)
class Student(User):
    #attribute
    #constructor
    def __init__(self, first, last, ID):
        User.__init__(self, first, last, ID)
        
        
    #methods
    def AddCourse(self): 
       # print("Add Course was Successfully Used")
        course_id = self.get_integer("Enter CRN: ","CRN Must be an Integer")
        cursor.execute("SELECT * FROM ENROLLMENT WHERE ENROLLMENT.student_id = ? AND ENROLLMENT.course_id = ?", (self.ID, course_id))
        if cursor.fetchone():
            print(f"Course with CRN {course_id} is already on your schedule.\n")
        else:
           cursor.execute("SELECT * FROM COURSE WHERE CRN = ?", (course_id,))
           if cursor.fetchone():
            cursor.execute("INSERT INTO ENROLLMENT (student_id, course_id) VALUES (?, ?)", (self.ID, course_id))
            conn.commit()
            print(f"Course {course_id} added to your schedule.")
           else:
               print(F"Course with CRN {course_id} does not exist\n")
        
    def RemoveCourse(self): 
      #  print("Remove Course was Successfully Used")
        # course_id = input("Enter the course ID to remove: ")
        # cursor.execute("DELETE FROM ENROLLMENT WHERE student_id = ? AND course_id = ?", (self.ID, course_id))
        # conn.commit()
        # print(f"Course {course_id} removed from your schedule.")
        
        #  print("Remove Courses was Successfully Used")
        u_id = self.get_integer("Enter CRN: ","CRN Must be an Integer")
        cursor.execute("SELECT * FROM ENROLLMENT WHERE course_id = ? AND student_id = ?",(u_id,self.ID))
        if cursor.fetchone():
                cursor.execute("SELECT * FROM ENROLLMENT WHERE course_id = ? AND student_id = ?",(u_id,self.ID))
                query_result = cursor.fetchall()
                for i in query_result:
                    print(i)
                y_n = input("Remove COURSE? (Y/N): ")
                if y_n == "Y":
                    cursor.execute("DELETE FROM ENROLLMENT WHERE course_id = ?",(u_id,))
        else:
                print("Course Does Not Exist")
        conn.commit()




    def Print(self):
      #  print("Print Schedule was Successfully Used")
        cursor.execute("SELECT COURSE.* FROM COURSE, ENROLLMENT WHERE COURSE.CRN = ENROLLMENT.course_id AND ENROLLMENT.student_id = ?", (self.ID,))
        query_result = cursor.fetchall()
        for i in query_result:
             print(i)
    def check_conflicts(self):
        
        cursor.execute("SELECT * FROM COURSE WHERE (time, weekday, semester, year) IN (SELECT COURSE.time, COURSE.weekday, COURSE.semester, COURSE.year FROM COURSE, ENROLLMENT WHERE ENROLLMENT.student_id = ? AND COURSE.CRN = ENROLLMENT.course_id GROUP BY time, weekday, semester, year HAVING COUNT(*) > 1)",(self.ID,))
        if cursor.fetchone():
           print("WARNING: The following courses create conflicts in your schedule\n")
           cursor.execute("SELECT * FROM COURSE WHERE (time, weekday, semester, year) IN (SELECT COURSE.time, COURSE.weekday, COURSE.semester, COURSE.year FROM COURSE, ENROLLMENT WHERE ENROLLMENT.student_id = ? AND COURSE.CRN = ENROLLMENT.course_id GROUP BY time, weekday, semester, year HAVING COUNT(*) > 1)",(self.ID,))
           query_result = cursor.fetchall()
           for i in query_result:
                    print(i)
                            
        else:
            print("There is no conflicts in your schedule\n")

class Instructor(User):
    #attribute
    #constructor
    def __init__(self, first, last, ID):
        User.__init__(self, first, last, ID)
    
    #methods
    def Assemble(self):
      #  print("Print Schedule was Successfully Used")
        u_class = self.get_integer("Enter CRN: ","CRN Must be an Integer")
        u_id = self.get_integer("Enter Student ID: ","Student ID Must be an Integer")
        cursor.execute("SELECT * FROM STUDENT WHERE ID =?", (u_id,))
        query_result = cursor.fetchall()
        for i in query_result:
             print(i)
        y_n = input(f"Add Student to Roster of {u_id}? (Y/N)\n")  
        if y_n == "Y":    
            cursor.execute("""INSERT INTO ENROLLMENT VALUES('%s','%s');""" % (u_id, u_class))
            conn.commit()
    def Print_roster(self):
      #  print("Print Class List was Successfully Used")
        course_id = self.get_integer("Enter CRN: ","CRN Must be an Integer")
        cursor.execute("SELECT STUDENT.* FROM STUDENT JOIN ENROLLMENT ON STUDENT.ID = ENROLLMENT.student_id WHERE ENROLLMENT.course_id = ?", (course_id,))
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)
    def Print_Schedule(self):
        cursor.execute("SELECT COURSE.* FROM COURSE JOIN ENROLLMENT ON COURSE.CRN = ENROLLMENT.course_id WHERE ENROLLMENT.instructor_id = ?",(self.ID,))
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)

class Admin(User):
    #attribute
    #constructor
    def __init__(self, first, last, ID):
        User.__init__(self, first, last, ID)
    
    #methods
    def add_courses(self):
       # print("Add Courses was Successfully Used")
        u_id = self.get_integer("Enter CRN: ","CRN Must be an Integer")
        
        cursor.execute("SELECT * FROM COURSE WHERE CRN = ?",  (u_id,))
        if cursor.fetchone():
            print("CRN already exists")
            u_id = self.get_integer("Enter CRN: ","CRN Must be an Integer")
            cursor.execute("SELECT * FROM COURSE WHERE CRN = ?", (u_id,))
            
        u_title = input("Enter Title: ")
        u_DEPT = input("Enter DEPT (4 Characters): ")
        u_time = input("Enter time (Ex: 8:00AM): ")
        u_week = input("Enter weekdays (Ex: M/F): ")
        u_semester = input("Enter semester: ")
        u_year = input("Enter year: ")
        u_credits = self.get_integer("Enter Credits: ","Credits Must be an Integer")
        cursor.execute("""INSERT INTO COURSE VALUES('%s', '%s', '%s', '%s', '%s', '%s','%s','%s');""" % (u_id, u_title, u_DEPT, u_time,u_week,u_semester,u_year,u_credits))
        print(u_title + " was successfully added\n", )
        conn.commit()
    def remove_courses(self):
      #  print("Remove Courses was Successfully Used")
        u_id = self.get_integer("Enter CRN: ","CRN Must be an Integer")
        cursor.execute("SELECT * FROM COURSE WHERE CRN = ?",(u_id,))
        if cursor.fetchone():
                cursor.execute("SELECT * FROM COURSE WHERE CRN = ?",(u_id,))
                query_result = cursor.fetchall()
                for i in query_result:
                    print(i)
                y_n = input("Remove COURSE? (Y/N): ")
                if y_n == "Y":
                    cursor.execute("DELETE FROM COURSE WHERE CRN = ?",(u_id,))
        else:
                print("Course Does Not Exist")
        conn.commit()

    def remove_user(self):
       # print("Add/Remove Users was Successfully Used\n")
        option = int(input("Select Type of User: \n1. Student\n 2. Instructor\n 3. Admin\n"))
        if option == 1:
            u_id = self.get_integer("Enter ID: ","ID Must be an Integer")
            cursor.execute("SELECT * FROM STUDENT WHERE ID = ?",(u_id,))
            if cursor.fetchone():
                cursor.execute("SELECT * FROM STUDENT WHERE ID = ?",(u_id,))
                query_result = cursor.fetchall()
                for i in query_result:
                    print(i)
                y_n = input("Remove Student? (Y/N): ")
                if y_n == "Y":
                    cursor.execute("DELETE FROM STUDENT WHERE ID = ?",(u_id,))
            else:
                print("Student ID Does Not Exist")
        if option == 2:
            u_id = self.get_integer("Enter ID: ","ID Must be an Integer")
            cursor.execute("SELECT * FROM INSTRUCTOR WHERE ID = ?",(u_id,))
            if cursor.fetchone():
                cursor.execute("SELECT * FROM INSTRUCTOR WHERE ID = ?",(u_id,))
                query_result = cursor.fetchall()
                for i in query_result:
                    print(i)
                y_n = input("Remove INSTRUCTOR? (Y/N): ")
                if y_n == "Y":
                    cursor.execute("DELETE FROM INSTRUCTOR WHERE ID = ?",(u_id,))
            else:
                print("Instructor ID Does Not Exist")     
        if option == 3:
            u_id = self.get_integer("Enter ID: ","ID Must be an Integer")
            cursor.execute("SELECT * FROM ADMIN WHERE ID = ?",(u_id,))
            if cursor.fetchone():
                cursor.execute("SELECT * FROM ADMIN WHERE ID = ?",(u_id,))
                query_result = cursor.fetchall()
                for i in query_result:
                    print(i)
                y_n = input("Remove ADMIN? (Y/N): ")
                if y_n == "Y":
                    cursor.execute("DELETE FROM ADMIN WHERE ID = ?",(u_id,))
            else:
                print("ADMIN ID Does Not Exist")
        conn.commit()
    def link_unlink(self):
        i_id = self.get_integer("Enter Instructor ID: ","ID Must be an Integer")
        cursor.execute("SELECT * FROM INSTRUCTOR WHERE ID = ?",(i_id,))
        if cursor.fetchone():
            cursor.execute("SELECT * FROM INSTRUCTOR WHERE ID = ?",(i_id,))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
            cursor.execute("SELECT COURSE.* FROM COURSE JOIN ENROLLMENT ON COURSE.CRN = ENROLLMENT.course_id WHERE ENROLLMENT.instructor_id = ?",(i_id,))
            query_result = cursor.fetchall()
            for i in query_result:
              print(i)
        course_id = self.get_integer("Enter COURSE ID: ","ID Must be an Integer")
        cursor.execute("SELECT ENROLLMENT WHERE instructor_id = ? AND course_id = ?",(i_id,course_id))
        if cursor.fetchone():
            cursor.execute("UPDATE ENROLLMENT SET instructor_id = ? WHERE instructor_id = ? AND course_id = ?",(0000,i_id,course_id))
            conn.commit()
            print(f"Instructor was successfully unlinked with course (CRN: {course_id})")
        else:
            print(f"Instructor is not linked to course {course_id}")
    def add_user(self):
        #WIP 
         option = int(input("Select Type of User:\n 1. Student\n 2. Instructor\n"))
         if option == 1:
             id = 0
             while id == 0:  
                u_id = self.get_integer("Enter ID: ","ID Must be an Integer")
                cursor.execute("SELECT * FROM STUDENT WHERE ID = ?",(u_id,))
                if cursor.fetchone():
                  print(f"There is already a student with the ID of {u_id}")
                else:
                    id = 1
             u_name = input("Enter First Name: ")
             u_surname = input("Enter Last Name: ")
             u_grad = self.get_integer("Enter Graduation Year: ","The Year Must be an Integer")
             u_major = input("Enter Major (4 Letters): ")
             u_email = input("Enter Email (Username Only): ")
             cursor.execute("""INSERT INTO STUDENT VALUES('%s','%s','%s','%s','%s','%s');""" % (u_id,u_name,u_surname,u_grad,u_major,u_email))
             print(f"Student ({u_id}) was successfully added.")
             conn.commit()
         if option == 2:
             id = 0
             while id == 0:  
                u_id = self.get_integer("Enter ID: ","ID Must be an Integer")
                cursor.execute("SELECT * FROM INSTRUCTOR WHERE ID = ?",(u_id,))
                if cursor.fetchone():
                  print(f"There is already an instructor with the ID of {u_id}")
                else:
                    id = 1
             u_name = input("Enter First Name: ")
             u_surname = input("Enter Last Name: ")
             title_option = int(input("Select Title:\n1. Full Prof.\n2. Associate Prof.\n"))
             if title_option ==1:
                 u_title = "Full Prof."
             elif title_option ==3:
                 u_title = "Associate Prof."
             else:
                 u_title = "Undefined"
             u_year = self.get_integer("Enter Hire Year: ","Hire Year Must be an Integer")
             u_DEPT = input("Enter DEPT (4 letters): ")
             u_email = input("Enter Email (Username Only): ")
             cursor.execute("""INSERT INTO INSTRUCTOR VALUES('%s','%s','%s','%s','%s','%s','%s');""" % (u_id,u_name,u_surname,u_title,u_year,u_DEPT,u_email))
             print(f"INSTRUCTOR ({u_id}) was successfully added.")
             conn.commit()
import sqlite3
conn=sqlite3.connect('assignment3_edit.db')
cursor = conn.cursor()


sql_command = """CREATE TABLE IF NOT EXISTS ENROLLMENT (
student_id INTEGER NOT NULL,
course_id INTEGER NOT NULL
);"""
cursor.execute(sql_command)
conn.commit()


def login(first, last, ID):
    user_type = 0
    first = first.capitalize()
    last = last.capitalize()
    cursor.execute("SELECT * FROM STUDENT WHERE ID = ? AND NAME = ? AND SURNAME = ?", (ID,first,last))
    if cursor.fetchone(): 
        user_type = 1
        print("Logged In\n")
    cursor.execute("SELECT * FROM INSTRUCTOR WHERE ID = ? AND NAME = ? AND SURNAME = ?", (ID, first, last))
    if cursor.fetchone():
        user_type = 2
        print("Logged In\n")
    cursor.execute("SELECT * FROM ADMIN WHERE ID = ? AND NAME = ? AND SURNAME = ?", (ID, first, last))
    if cursor.fetchone():
        user_type = 3
        print("Logged In\n")
    if user_type == 0:
        print("Failed Login. Re-Enter Information\n")
    return user_type




user_type = 0
while user_type == 0: 

    first_name = input('Enter First Name:\n')
    last_name = input('Enter Last Name:\n')
    identification = input("Enter Your ID:\n")
    user_type = login(first_name, last_name, identification)


if user_type == 1:
    User1 = Student(first_name.capitalize(), last_name.capitalize(), identification)
    print("Welcome ", User1.first, " ", User1.last, " (Student)")
    option = int(input('Please Select an Option\n 1. Search Courses\n 2. Add Course to Schedule\n 3. Remove Course From Schedule\n 4. Print Schedule\n5. Get Info\n6. Check Conflicts in Schedule\n7. Log Off\n'))
    while option != 7:
        if option == 1:
            search_option = int(input('Please Select an Option\n 1. Search All Courses\n 2. Search by Parameters\n3. Exit\n'))
            while search_option != 3:
                if search_option == 1:
                    User1.Search()
                if search_option == 2:
                    User1.Search_Parameters()
                search_option = int(input('Please Select an Option\n1. Search All Courses\n2. Search by Parameters\n3. Exit\n'))
        if option == 2:
            User1.AddCourse()
        if option == 3:
            User1.RemoveCourse()
        if option == 4:
            User1.Print()
        if option == 5:
            User1.getInfo()
        if option == 6:
            User1.check_conflicts()
        option = int(input('Please Select an Option\n 1. Search Courses\n 2. Add Course to Schedule\n 3. Remove Course From Schedule\n 4. Print Schedule\n5. Get Info\n6. Check Conflicts in Schedule\n7. Log Off\n'))
elif user_type == 2:
    User2 = Instructor(first_name, last_name, identification)
    print("Welcome ", User2.first, " ", User2.last, " (Instructor)")
    option = int(input('Please Select an Option\n 1. Search Courses\n 2. Assemble Roster\n 3. Print Roster\n 4. Print Info\n 5. Print Schedule\n 6. Log Off\n'))
    while option != 6:
        if option == 1:
            search_option = int(input('Please Select an Option\n 1. Search All Courses\n 2. Search by Parameters\n3. Exit\n'))
            while search_option != 3:
                if search_option == 1:
                    User2.Search()
                if search_option == 2:
                    User2.Search_Parameters()
                search_option = int(input('Please Select an Option\n1. Search All Courses\n2. Search by Parameters\n3. Exit\n'))
        if option == 2:
            User2.Assemble()
        if option == 3:
            User2.Print_roster()
        if option == 4:
          User2.getInfo();
        if option == 5:
           User2.Print_Schedule()
        option = int(input('Please Select an Option\n 1. Search Courses\n 2. Assemble Roster\n 3. Print Roster\n 4. Print Info\n 5. Log Off\n'))
elif user_type == 3:
    User3 = Admin(first_name, last_name, identification)
    print("Welcome ", User3.first, " ", User3.last, " (Admin)")
    option = int(input('Please Select an Option\n1. Search Courses\n2. Add Courses\n3. Remove Courses\n4. Add User\n5. Remove User\n6. Print Info\n7. Link/Unlink Instructors and Courses\n8. Log Off\n'))
    while option != 8:
        if option == 1:
            search_option = int(input('Please Select an Option\n 1. Search All Courses\n 2. Search by Parameters\n3. Exit\n'))
            while search_option != 3:
                if search_option == 1:
                    User3.Search()
                if search_option == 2:
                    User3.Search_Parameters()
                search_option = int(input('Please Select an Option\n1. Search All Courses\n2. Search by Parameters\n3. Exit\n'))
        if option == 2:
            User3.add_courses()
        if option == 3:
            User3.remove_courses()
        if option == 4:
            User3.add_user()
        if option == 5:
            User3.remove_user()
        if option == 6:
            User3.getInfo()
        if option == 7:
            User3.link_unlink()
        option = int(input('Please Select an Option\n1. Search Courses\n2. Add Courses\n3. Remove Courses\n4. Add User\n5. Remove User\n6. Print Info\n7. Link/Unlink Instructors and Courses\n8. Log Off\n'))
    
print ("Logging Off\n\n")

class Test_test_2(unittest.TestCase):
    def test_login(self):
        #Student Logs IN
        s_log = login("Tucker","Moncey","10011")
        self.assertEqual(1,s_log,"Login Error for Student")
        #Student has wrong ID
        s_log_f = login("Tucker","Moncey","10010")
        self.assertEqual(0,s_log_f,"Login Error for inncorrect ID")
        #Instructor logs IN
        i_log = login("Alan","Turing","20004")
        self.assertEqual(2,i_log,"Login Error for Instructor")
        #Instructor enters lowercase name
        i_log_l = login("alan","Turing","20004")
        self.assertEqual(2,i_log_l,"Login Error for Instructor (Lowercase)")
        #Instructor enters name wrong
        i_log_f = login("Alan","Turin","20004")
        self.assertEqual(0,i_log_f,"Wrong Name Works for Instructor (Error)")
        #Admin Logs IN
        a_log = login("Vera","Rubin","30002")
        self.assertEqual(3,a_log,"Login Error for Admin")
        #Admin enters ID of another Admin
        a_log_f = login("Vera","Rubin","30001")
        self.assertEqual(0,a_log_f,"Login Error for Admin (ID)")
        #Admin enters all lowercase
        a_log_l = login("vera","rubin","30002")
        self.assertEqual(3,a_log_l,"Login Error for Admin (Lowercase)")
    def test_search_all(self):
        #Search All
        User1 = Student("Tucker","Moncey","10011")
        course_search = User1.Search()
        self.assertTrue(course_search,"Search All Courses Error")
    def test_search_paramters(self):
        User1 = Student("Tucker","Moncey","10011")
        #Correct CRN
        search_CRN = User1.search_CRN("1002")
        self.assertTrue(search_CRN,"Error for correct CRN")
        #Incorrect CRN
        search = User1.search_CRN("siuhfuh")
        self.assertFalse(search,"Error for incorrect CRN")
        #Valid title (Random caps)
        search= User1.search_Title("miCrocOntrolLers")
        self.assertTrue(search,"Error for correct title (random caps)")
        #Invalid title
        search = User1.search_Title("regrhoegihkgb")
        self.assertFalse(search,"Error for invalid title")
        #Valid DEPT (Random Caps)
        search = User1.search_DEPT("bScO")
        self.assertTrue(search,"Error for valid DEPT")
        #Invalid DEPT
        search = User1.search_DEPT("ioiGeg")
        self.assertFalse(search,"Error for invalid DEPT")
        #Valid Time
        search = User1.search_Time("8:00aM")
        self.assertTrue(search,"Error for valid time")
        #Invalid Time
        search = User1.search_Time("hghrii")
        self.assertFalse(search,"Error for invalid time")
        #Valid Weekday
        search = User1.search_Weekday("t/TR")
        self.assertTrue(search,"Error for valid weekday")
        #Invalid Weekday
        search = User1.search_Weekday("gjij5")
        self.assertFalse(search,"Error for invalid weekday")
        #Valid Credit
        search = User1.search_Credits(4)
        self.assertTrue(search, "Error for valid credits")
        #Invalid Credits
        search = User1.search_Credits(45)
        self.assertFalse(search,"Error for bad credits")
if __name__ == '__main__':
    unittest.main()

conn.close()
