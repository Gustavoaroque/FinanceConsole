from CRUD import SearchForUser,SelectAllRegistersFromFlowTable,InsertRegisterIntoFlowTable
from datetime import date

if __name__ == '__main__':
    print("Welcome to the Flow manager.\n")
    print("Please enter your username and password")

    username = input("Username:")
    password = input("Password:")

    currentUser = SearchForUser(user=username,password=password)
    user_id = currentUser[0]
    user_username = currentUser[1]
    currentDate = date.today()
    currentDate = currentDate.strftime('%m-%d-%Y')

    if currentUser :
        while(True):
            #Clear screen 
            print("What do you want to do?\nSelect 1: To check account\nSelect 2: To enter a new Register\nSelect 3: To Edit a Register\nAny other letter or number for exit")
            FirstOptionSelected = input()
            if FirstOptionSelected == '1':
                totalExpenses = 0
                totalIncome = 0
                Flows = SelectAllRegistersFromFlowTable()
        
                print(f"{'ID':<40} {'TITLE':<35} {'AMOUNT ($)':<20} {'IS EXPENSE':<20} {'DATE':<20}\n")

                for flow in Flows:
                    if flow[3] == 0:
                        totalIncome+=flow[2]
                    else: totalExpenses +=flow[2]
                    print(f"\n{flow[0]:<40} {flow[1]:<35} {flow[2]:<20} {flow[3]:<20} {flow[4].strftime('%m-%d-%Y'):<20}")
                print('_'*140)
                print(f'\n\nTotal Expenses: {totalExpenses}\nTotal Income: {totalIncome}')
                totalFlow = totalIncome - totalExpenses
                print('______________________________________')
                print(f'\nTotal Flow: {round(totalFlow,2)}')
                print('\n\n\n')
            if FirstOptionSelected == '2':
                FlowTitle = input('Title: ')
                FlowAmount = float(input('Amount: '))
                FlowDescription = input('Description: ')
                DateOption = input('Date: Do you want to enter todays date? Y/N: ')
                if DateOption.upper() == 'Y':
                    FlowDate = currentDate
                else:
                    FlowDate = input("Date ('MM-DD-YYYY): ")
                isExpenseOption = input('Is a Expense? Y/N: ')
                if isExpenseOption.upper() == 'Y':
                    FlowisExpense = 'True'
                elif isExpenseOption.upper() == 'N': FlowisExpense='False'

                print("\n\n\nCheck all the data:\n")
                print(f"User: {user_id} == {user_username}\nTitle: {FlowTitle}\nAmount = ${FlowAmount}\nDate: {FlowDate}\nDescription: {FlowDescription}\nisExpense: {FlowisExpense}")
                InsertRegisterIntoFlowTable(Title=FlowTitle,Amount=FlowAmount,DateCreated=FlowDate,DateUpdate=FlowDate,Desciption=FlowDescription,User=user_id,isExpense=FlowisExpense)
                # print("Register created!")

            print("Do you want to something more or exit?")
            SecondOption = input("C: Do other action.\nEnter other key to Exit\n")
            if SecondOption == 'C':
                print("\n\n\n")
            else:break
    else: print("No encontrado")
