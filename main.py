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
            print("What do you want to do?\nSelect C: To check account\nSelect E: To enter a new Register\nAny other letter or number for exit")
            FirstOptionSelected = input()
            if FirstOptionSelected == 'C':
                totalExpenses = 0
                totalIncome = 0
                Flows = SelectAllRegistersFromFlowTable()
                for flow in Flows:
                    if flow[2] == 0:
                        totalIncome+=flow[1]
                    else: totalExpenses +=flow[1]
                    print("{:<30} {:<25} {:<20}".format(*flow))
                print('_____________________________________________________________________')
                print(f'\n\nTotal Expenses: {totalExpenses}\nTotal Income: {totalIncome}')
                print('_________________________________')
                totalFlow = totalIncome - totalExpenses
                print(f'\nTotal Flow: {totalFlow}')
                print('\n\n\n')
            if FirstOptionSelected == 'E':
                FlowTitle = input('Title: ')
                FlowAmount = float(input('Amount: '))
                FlowDescription = input('Description: ')
                DateOption = input('Date: Do you want to enter todays date? Y/N: ')
                if DateOption == 'Y':
                    FlowDate = currentDate
                else:
                    FlowDate = input("Date ('MM-DD-YYYY): ")
                isExpenseOption = input('Is a Expense? Y/N: ')
                if isExpenseOption == 'Y':
                    FlowisExpense = 'True'
                elif isExpenseOption == 'N': FlowisExpense='False'

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
