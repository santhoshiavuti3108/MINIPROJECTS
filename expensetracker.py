#expense tracker

#create a class for expense tracker
class Expensetracker:
    #self indicates current object
    def __init__(self):
        #create a empty list for expences
        self.expenses=[]
    # to add expenses function is defined
    def add.expenses():
        #take user input to add name and amount
        name=input("enter expense name:")
        amount=float(input("enter expense amount:"))
        #append=adds the data to self.expenses list
        self.expenses.append({"Expense name:"name , "Expense amount"amount})
        #this added sucessfully to the list 
        print("\n expense added sucessfully!")
    # to view expences function is defined
    def view.expenses():
        # check weather the list is empty
        if len(self.expenses)==0:
            #if list is empty 
            print("expenses not found!")
            #return=ends the program if list is empty
            return
         # total variable to calculte expenses   
        total=0
        # dispaly menu
        print("\n-------EXPENSE TRACKER-------")
        # for loop for every expense
        #enumerate= item + index/serial number
            for i,expenses in enumerate(self.expenses,start=1):
                print(i,".",expense["name"],"-rs.",expenses["amount"])
                #add amount to total
                total=total+expenses["amount"]
                #print total expenses
                print("------------------------------------")
                print("total expenses,total")
                print()
# create object for class      
tracker = Expensetracker() 
#loop for infinate calculation or inputs
while True:
    #display menu
    print("------Expensive Tracker------")
    print("1.add expense")
    print("2.view expense")
    print("3.exit")
    # ask for user choice
    choice=input("enter your choice:")
    # use if else statments
    if choice=="1":
        tracker.add_expenses()
    elif choice=="2":
        tracker.view_expences()
    elif choice=="3":
        print("thank you")
        break #ends the code and exits
    else:
        print("invalid choice! please try again.\n")




    

