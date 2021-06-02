#Mike Jerald B. Bentilacion
#Assignment
#Simple Student Information System

import csv

student_attr= ['ID Number', 'Name', 'Year Level',  'Course','Gender']


def Main():
    print("---------------------------------------------------")
    print("   WELCOME IN MSU-IIT STUDENT INFORMATION SYSTEM   ")
    print("---------------------------------------------------")
    print("1. ADD NEW STUDENT")
    print("2. DISPLAY LIST OF STUDENTS")
    print("3. SEARCH A STUDENT")
    print("4. EDIT STUDENT")
    print("5. DELETE A STUDENT")
    print("6. EXIT")
    print()

def Add():
    print("---------------------")
    print("    ADD STUDENT      ")
    print("---------------------")
    
    global student_attr
    
    STD_data = []
    for field in student_attr :
        value = input("Enter " + field + ": ")
        STD_data.append(value)
        
    with open("DATA.CSV" , "a", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([STD_data])
    
    print("Wow! Data added successfully!")
    input("Press any key to continue:")
def View():
    global student_attr 
    
    print("----------------------")
    print("     STUDENT LIST     ")
    print("----------------------")
    
    with open("DATA.CSV","r") as f:
        students = csv.reader(f)
        for row in students:
            for x in row:
                if x != 0:
                    print(x, end=",")
            print()
   
    input("Press any key to continue:")

    
def Search():
    global student_attr
    
    print("------------------------")
    print("     SEARCH STUDENT     ")
    print("------------------------")
    
    student_ID = input("ENTER ID NUMBER :")
    with open('DATA.CSV','r')as f:
        students = csv.reader(f)
        for row in students:
            for x in row:
                if x != 0:
                    if student_ID == x:                    
                        print("ID NUMBER :\t",row[0])
                        print("NAME :\t\t" ,row[1])
                        print("YEAR LEVEL :\t" ,row[2])
                        print("COURSE :\t" ,row[3])
                        print("GENDER :\t" ,row[4])
                        break              
    input("Press any key to continue:")


# Edit student
def Edit():
    global student_attr 

    
    print("------------------------")
    print("     Edit STUDENT     ")
    print("------------------------")
    Std_index = None
    Edit_data = []
    student_ID = input("ENTER ID NUMBER :")
    with open("DATA.CSV", "r", encoding = "utf-8") as f:
        students = csv.reader(f)
        counter = 0
        for row in students:    
            if len(row) > 0:
                if student_ID == row[0]:
                    Std_index = counter
                    print(" Student Found")
                    print("Name :",row[1])
                    STD_data = []
                    for field in student_attr :
                        value = input("Enter " + field + ": ")
                        STD_data.append(value)
                    Edit_data.append(STD_data)
                else:
                    Edit_data.append(row)
                counter += 1
                
    # Check if the record is or not found
    if Std_index is not None:
        with open("DATA.CSV" , "w", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(Edit_data)
    
    else:
        print("Sorry! ID Number could not be found\n") 
    input("Press any key to continue:")

def Delete():
    global student_attr 

    
    print("------------------------")
    print("      DELETE STUDENT    ")
    print("------------------------")
    
    student_ID = input("Enter ID Number of student to remove: ")
    Std_Found = False
    Edit_data = []
    x = input("Are you sure you want to delete(Y or N):")
    if x == "Y":
        with open("DATA.CSV", "r", encoding = "utf-8") as f:
            students = csv.reader(f)
            counter = 0
            for row in students:
                if len(row) > 0:
                    if student_ID != row[0]:
                        Edit_data.append(row)
                        counter += 1
                    else:
                        Std_Found = True
        
        if Std_Found is True:
            with open("DATA.CSV", "w", encoding = "utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(Edit_data)
            print("ID Number:\n ", student_ID, "Removed successfully!")
        
        else:
            print("Oops! ID Number not found")
    else:
        print()

    input("Press any key to continue:")


# Main
while True:
    Main()
    
    choice = input(" Enter the Number:")
    if choice == '1':
        Add()
    elif choice == '2':
        View()
    elif choice == '3':
        Search()
    elif choice == '4':
        Edit()
    elif choice == '5':
        Delete()
    else:
        break


# Termination
print("********************************************************************")
print("*  THE SYSTEM HAS BEEN TERMINATED,THANK YOU FOR USING THE SYSTEM!  *")
print("********************************************************************")



