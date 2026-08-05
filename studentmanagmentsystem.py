# student mangment system
#create a class
#class = student & object = student
class Student:
# define init() - it is called whenever an object is created
# it stores student data
    def __init__(self,roll_no,name,marks):# self=refer to current object
        self.roll_no=roll_no # stores roll no
        self.name=name
        self.marks=marks
    def display(self):# display student details
        print("roll_no:",self.roll_no)
        print("name:",self.name)
        print("marks:",self.marks)

students=[]
# create empty student list
while True:
    # display menu
    print("\n---student managment system---")
    print("1.add student")
    print("2.view students")
    print("3.search student")
    print("4.exit")
    # ask user choice
    choice=(int(input("enter your choice:")))

    if choice==1:
    #add student
    # ask user input
     # user input for student details
        roll_no=int(input("enter your roll_no:"))
        name=input("enter your name:")
        marks=float(input("enter your marks:"))
        #student details stored in student variable
        student=Student(roll_no,name,marks)
        # append= adds the unique data to the list
        students.append(student)
        print("student is successfully added!")
    elif choice==2:
    # view students
    # len= student list length 
        if len(students)==0:
            print(" no student record found ")
        else:
            # checks if the student is there in list
            for student in students:
                # display the data
                student.display()
                print()
    elif choice==3:
    #search student
        roll=int(input("enter student roll_no: "))
        #found= variable to find the student in list
        found=False
        for student in students:
            if student.roll_no == roll:# compare
                student.display()
                found=True
                break
                # break=stop searching because found=true
            if not found:
                print("not found!")
    elif choice==4:
    #exit 
        print("exiting program...")
        break# terminates while loop
    else:
        print("invalid choice")