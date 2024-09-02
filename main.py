from CRUD import SearchForUser,SelectAllRegistersFromFlowTable,InsertRegisterIntoFlowTable, SearchFlow, UpdateFlow
from datetime import date
import os

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
            os.system('clear')
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
            elif FirstOptionSelected == '2':
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
            elif FirstOptionSelected == '3':
                newAttrArray = []
                os.system('clear')
                IdFlow = input('Enter the ID: ')
                FlowInfo = SearchFlow(user_id,IdFlow)
                print(FlowInfo)
                while True:
                    newTitle = input(f"Title ('{FlowInfo[7]}'): ")
                    if newTitle == "":newAttrArray.append(FlowInfo[7])
                    else: newAttrArray.append(newTitle)

                    newAmount = input(f"Amount ('${str(FlowInfo[1])}'): ")
                    if newAmount == "":newAttrArray.append(FlowInfo[1])
                    else: newAttrArray.append(float(newAmount))

                    newIsExpense = input(f"Is Expense?({FlowInfo[6]}): ")
                    if newIsExpense == "": newAttrArray.append(FlowInfo[6])
                    else: newAttrArray.append(newIsExpense)

                    newDate = input(f"Date ('{FlowInfo[2]}') 'Format('MM-DD-YYYY'): ")
                    if newDate == "": newAttrArray.append(FlowInfo[2])
                    else:newAttrArray.append(newDate)

                    os.system('clear')
                    print(f"""
Title: {newAttrArray[0]}
Amount: {newAttrArray[1]}
Is Expense: {newAttrArray[2]}
Date: {newAttrArray[3]}
""")
                    UpdateConfirmation = input("\nDo you want to safe? Y/N:  ")
                    if UpdateConfirmation.upper() == 'Y':
                        DateUpdate = date.today()
                        newAttrArray.append(DateUpdate)                 
                        UpdateFlow(IdFlow,newAttrArray)
                        break
                    else:
                        print('saliendo')
                        break
            else:
                break
            print("Do you want to something more or exit?")
            SecondOption = input("1: Do other action.\nEnter other key to Exit\n")
            if SecondOption != '1': break

    else: print("No encontrado")
