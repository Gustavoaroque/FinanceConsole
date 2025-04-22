
# from Database import InsertNewCar,InsertNewCarService, InsertNewSubscription,InserCheck,InsertFlow,GetAllFlow,UpdateFlow, GetAllSubs, GetAllChecks, InsertCard, InsertCategory,GetAllCards,GetAllCategories
from tabulate import tabulate
from datetime import date
import os 
import uuid 
from dotenv import load_dotenv
import os
from Database import DatabaseManager
from pathlib import Path

env_path = Path('.')/'credentials.env'

load_dotenv(dotenv_path=env_path)




# def test():
#     getListCat = GetAllCategories()
#     arr = []
#     for Cat in getListCat:
#         print(Cat[1])
#         arr.append(Cat[1])
#     CatSelection = input("")
#     if CatSelection in arr:
#         print("True")
#     else: print("False")

# def AddTransaction():
#     print("\n\n\n")
#     FlowTitle = input("Flow Title: ")
#     FlowDate = input("Flow Date: ")
#     FlowAmount = float(input("Amount: "))
#     FlowIsExpense = input("Is Expense?: ")
#     FlowUser = input("User default(6cd25856-9a49-4a39-b9bb-3448c216c74c): ")
#     FlowDesc = input("Description: ")
#     print("Category (Values: ")
#     #GetCategory



#     FlowIsCredit = input("Is Credit?: (true/flase) ")

#     #Code section to improve the boolean selection
#     FlowUser = "6cd25856-9a49-4a39-b9bb-3448c216c74c"
#     InsertFlow(FlowTitle,FlowAmount,FlowDate,FlowDesc,FlowUser,FlowIsExpense,FlowIsCredit)


#     print("\n\n\n Finish")

# def AddCard():
#     #Add a additional information/details about the card in case that the user has two or more cards of the same card issuer
#     #Add the user feature so the program can display only the cards of THIS User
#     print("\n\n\n\n")
#     while True:
#         CardName = input("Card Name (Visa/MasterCard, etc): ")
#         print(f"Do you want to save this card {CardName} ? ")
#         promptComfirm = input("Y/N? ")
#         if promptComfirm.capitalize() == 'Y':
#             InsertCard(CardName)
#             break
#         elif promptComfirm.capitalize() == 'N':
#             break
#         else:
#             print("Please enter a Valid Option.")
            
# def AddCategory():
#     print("\n\n\n")
#     while True:
#         categoryName = input("Name of the Category: ")
#         print(f"Do you want to save this catogory name : {categoryName} ?" )
#         promptComfirm = input("Y/N? ")
#         if promptComfirm.capitalize() == 'Y':
#             InsertCategory(categoryName)
#             break
#         elif promptComfirm.capitalize() == 'N':
#             break
#         else:
#             print("Please enter a Valid Option.")
        

# def AddCar():
#     print("\n\n\n")
#     CarBrand = input("Car Brand:")
#     CarModel = input("Car Model: ")
#     CarYear = int(input("Car Year: "))
#     Car_Owner = input("Car Owner: ")


#     print("\n\n\n")

#     print(f"The follow car info: {CarBrand} {CarModel} {CarYear} and the owner is {Car_Owner}.")

#     InsertNewCar(CarBrand,CarModel,CarYear,Car_Owner)

# def AddCarLog():
#     print("\n\n\n")
#     CarID = input("Car ID: ")
#     CarServiceTitle = input("Service Title: ")
#     CarServiceDateCreated = input("Date Created: ")
#     CarServiceDateUpdate = input("Date Updated: ")
#     CarServiceCost = float(input('Service Cost: '))
#     CarServiceDescription = input("Description (optional): ")
    
#     print("\n\n\n")

#     print(f"{CarServiceTitle} on {CarServiceDateCreated} cost {CarServiceCost} ")

#     InsertNewCarService(CarID,CarServiceTitle,CarServiceDateCreated,CarServiceCost,CarServiceDescription)


# def AddMonthlySubs():
#     print("\n\n\n")
#     SubscriptionTitle = input("Title: ")
#     SubscriptionPayDate = input("Payment Date: ")
#     SubscriptionAmout = float(input("Subscription Cost: "))
#     SubscriptionStarted = input("Date Start: ")
#     # isEnded = input("Is still running? Y/N")

#     SubscriptionDescription = input("Description (optional): ")
    

#     print("\n\n\n")
#     print(f"Sub: {SubscriptionTitle} paydate: {SubscriptionPayDate} cost: {SubscriptionAmout} Subscription dstarted on : {SubscriptionStarted}")

#     InsertNewSubscription(SubscriptionTitle,SubscriptionPayDate,SubscriptionAmout,SubscriptionStarted,SubsEnded="",SubsIsActive="True", SubsDescription=SubscriptionDescription)
# def AddCheck():
#     print("Adding a check...\n")
#     CheckPeriodStart = input("Date Start: ")
#     CheckPeriodEnds = input("Date Ends: ")
#     CheckTotalHours = float(input("Total hours: "))
#     CheckPayHour = float(input("Hour pay rate: "))
#     if CheckTotalHours > 40:
#         payment = CheckPayHour*(40 + 1.5*(CheckTotalHours-40) )
#     else: payment = CheckTotalHours * CheckPayHour

#     #print(f"Check Info:\n{CheckPeriodStart} - {CheckPeriodEnds}\nTotal Hours: {CheckTotalHours}---> Overtime hours: {CheckTotalHours - 40} \nHour Regular Rate: {CheckPayHour}, Overtime: {CheckPayHour*1.5} \nTotal payment before deductions: {payment}")

#     print("\n\nDeductions:")
#     FederalTax = float(input("Federal tax: "))
#     Medicare = float(input("Medicare: "))
#     SocNumber = float(input("Social Security: "))
#     CityTax = float(input("Total City tax: "))
    
#     # totalDeduction = float(input("Total Deduction: "))
#     sum = FederalTax + Medicare + SocNumber + CityTax
#     Percentage = (sum*100.0)/(payment)

#     # print(f"\n\n\ntotal ded:{sum}\nPercentage: {Percentage}")

#     InserCheck(CheckPeriodStart,CheckPeriodEnds,CheckTotalHours,CheckPayHour,payment,FederalTax,Medicare,SocNumber,CityTax,sum,Percentage)

#     SaveCheckFlag = input("Do you want to save this Check on the Flow/Transaction Register?")
#     if SaveCheckFlag.upper() == 'Y':
#         title = f"Check_{CheckPeriodStart}_{CheckPeriodEnds}"
#         netPay = payment - sum
#         desc = f"Pay Check from {CheckPeriodStart} to {CheckPeriodEnds}"
#         date = input("Date Created: ")

#         InsertFlow(title,netPay,date,desc,User='6cd25856-9a49-4a39-b9bb-3448c216c74c',isExpense='False',isCredit='False')
#         print("Save in Flow")
#         #This should be a function so i can reuse it when i call it with the car log
#         #Here we save it as Check_dateStart_to_dateEnd, the amount, and isExpense False
#     else:
#         print("None and Return")

# def EditRecordFlow(flows):
#     print("\n\n\n")
#     FlowIdEdit = input("Enter ID: ")
    
#     for flow in flows:
#         if flow[0] == FlowIdEdit:
#             FlowToEdit = flow
#             findit = 1
#             break
#         else: findit = 0

#     if findit == 1 :
#         fields = []
#         print("Enter to leave the field as before.")
        
#         FlowTitle = input(f"Title ({FlowToEdit[1]}): ")
#         if FlowTitle == "":fields.append(FlowToEdit[1])
#         else: fields.append(FlowTitle)
    
#         FlowAmount = input(f"Amount ({FlowToEdit[2]}: ")
#         if FlowAmount == "": fields.append(FlowToEdit[2])
#         else: fields.append(float(FlowAmount))

#         FlowDateCreated = input(f"Date Created ('MM-DD-YY') ({FlowToEdit[3]}): ")
#         if FlowDateCreated == "": fields.append(FlowToEdit[3])
#         else: fields.append(FlowDateCreated)

#         FlowIsExpense = input(f"Is Expense? ({FlowToEdit[4]}): ")
#         if FlowIsExpense == "": fields.append(FlowToEdit[4])
#         else: fields.append(FlowIsExpense)

#         FlowIsCredit = input(f"Is Credit? ({FlowToEdit[5]}): ")
#         if FlowIsCredit == "": fields.append(FlowToEdit[5])
#         else: fields.append(FlowIsCredit)


#         fields.append( date.today().strftime("%Y-%d-%m"))
#         fields.append(FlowToEdit[0])

#         UpdateFlow(fields)

        
        
            
    



# def ListAllTransaction(UserID):
#     transaction = GetAllFlow()
#     print(tabulate(transaction,headers=["Flow ID","Title", "Amount $ ","Date Created","Expense","Credit"],tablefmt="fancy_grid"))
#     #total(income,expense,credit,debit)
#     total = [0.0,0.0,0.0,0.0]
#     for flow in transaction:
#         if flow[4]:
#             #Is expense
#             total[1] = total[1] + flow[2]
#             if flow[5]:
#                 total[2] = total[2] + flow[2]
#             else:
#                 total[3]= total[3] + flow[2]
#         else:
#             #Is income
#             total[0] = total[0] + flow[2]
#     print(f"Total Income: ${total[0]}\nTotal Expense: ${total[1]}\nTotal Credit: ${total[2]}\nTotal Debit: ${total[3]}")

#     while True:
#         optionVar = input(" 1 : Back to main menu\n 2 : Edit a record\n")
#         if optionVar == '1':
#             os.system('clear')
#             break
#         elif optionVar == '2':
#             EditRecordFlow(transaction)
#             break
        
# def ListAllChecks():
#     checksList = GetAllChecks()
#     CheckHeader = ['ID','Start','End','Hours','Pay','Total','FedTax','Medicare','SocSec','CityTax','Total Tax','Tax%']
#     print(tabulate(checksList,headers=CheckHeader,tablefmt='grid'))


# def ListAllSubs():
#     Subs = GetAllSubs()
#     print(tabulate(Subs,headers=['ID','Title','Cost','Pay Date','Start Date','End Date','is active','Description']))

# def ListAllCards():
#     Cards = GetAllCards()
#     print(tabulate(Cards, headers=['ID','Title']))

# def ListAllCategories():
#     Categories = GetAllCategories()
#     # print(tabulate(Categories, headers=['ID','Title']))
#     print(Categories[1])
#     print(type(Categories))


def EntryData(tableStrc):
    colsName = tuple(tableStrc.keys())
    colsPseudo = tuple(tableStrc.values())
    values = []
    for col in range(len(colsName)):
        if 'UUID' in colsPseudo[col] and col == 0:values.append(str(uuid.uuid4()))
        elif 'NonIn' in colsPseudo[col] and 'Total Payment' in colsPseudo[col] :
            if values[3] > 40:
                val1 = values[4] * (values[3]*1.5 -20)
                # val1 = values[4]*(40 + (values[3]-40)*1.5)
                values.append(val1)
            else: values.append(values[3]*values[4])
        elif 'NonIn' in colsPseudo[col] and 'Total Deduction' in colsPseudo[col] :
            val2 = values[6] + values[7] +values[8] + values[9]
            values.append(val2)
        elif 'NonIn' in colsPseudo[col] and 'Percentage' in colsPseudo[col] :
            val3 = (values[10]*100)/values[5]
            values.append(val3)
        elif 'NonIn' in colsPseudo[col] and 'Net Pay' in colsPseudo[col] :
            values.append(values[5] - values[10])
        else:
            valueInput = input(f"Enter {colsPseudo[col]}: ")
            if 'int' in colsPseudo[col]: 
                values.append(int(valueInput))
            elif 'float' in colsPseudo[col]: values.append(float(valueInput))
            
            else: values.append(valueInput)
    return values
    

    



if __name__ == '__main__':
    print("\n\nWelcome to your personal App")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")

    db = DatabaseManager(db_name,db_user,db_password,db_host,db_port)

    tableStructure = {
        #Table Structure/ and pseudo names
        # "1": {"CheckID":"Check ID (UUID PK)", "CheckStart": "Start Date", "CheckeEnd":"End Date", "CheckTotalHours":"Total Hours (float)", "CheckRegularPayment":"Reg Payment (float)","CheckTotalPayment":"Total Payment (float)","CheckFederalTax":"Federal Tax (float)","CheckMedicare":"Medicare (float)","CheckSocSec":"Social Security (float)","CheckCityTax":"City Tax (float)","CheckTotalDeduction":"Total Deduction (float)","CheckPercentage":"Percentage (float)"},
        # "2": {"Flow_ID":"Transaction ID (UUID PK)","Flow_amount":"Amount (float)","Flow_Created":"Date Created","Flow_Updated":"Date Updated","Flow_Description":"Description (Text)","Flow_User":"User (UUID)", "Flow_isExpense":"Expense (bool)","Flow_Title":"Title (Text)","Flow_isCredit":"is Credit(bool)","Flow_isCash":"is Cash(bool)","Flow_Card":"Card (int)","Flow_Category":"Category (int)" },
        # "3": {"cardID":"ID (int PK)","cardName":"Card Name (text)"},
        # "4": {"categoryID":"Category ID (int PK)","categoryName":"Category Name (text)"}  
        "1": {"check_id": "ID (UUID)",                                        #0
              "check_start": "Start Date",                                    #1
              "check_end":"End Date",                                         #2
              "check_total_hours":"Total Hours (float)",                      #3
              "check_regular_payment":"Reg Payment (float)",                  #4
              "check_total_payment":"Total Payment (float) NonIn",            #5
              "check_federal_tax":"Federal Tax (float)",                      #6
              "check_medicare":"Medicare (float)",                            #7
              "check_soc_sec":"Social Security (float)",                      #8
              "check_city_tax":"City Tax (float)",                            #9
              "check_total_deduction":"Total Deduction (float) NonIn",        #10
              "check_percentage":"Percentage (float) NonIn",                  #11
              "check_net_payment":"Net Pay (float) NonIn",                     #12
              "check_date" : "Date Check"
              },               

        "2": {"flow_id":"ID (UUID)",
              "flow_amount":"Amount (float)",
              "flow_created":"Date Created",
              "flow_updated":"Date Updated",
              "flow_description":"Description (Text)",
              "flow_user":"User (UUID)", 
              "flow_is_expense":"Expense (bool)",
              "flow_title":"Title (Text)",
              "flow_is_credit":"is Credit(bool)",
              "flow_is_cash":"is Cash(bool)",
              "flow_card":"Card (int)",
              "flow_category":"Category (int)"},

        "3": {"cardname":"Card Name (text)"},

        "4": {"categoryname":"Category Name (text)"}  
                }
    #Table Name and pseudo name
    #(PSEUDONAMES  |  TABLENAME)
    tableNames = {
        "1": ("Checks","checks"),
        "2": ("Transactions","flow"),
        "3": ("Cards","cards"),
        "4": ("Categories","categories"),
        "5": ("Cars", "carlist"),
        "6": ("Car Services","carservices")
    }

    # 6cd25856-9a49-4a39-b9bb-3448c216c74c-- USER ID

    while True:
        print("Select One option of the menu: \n1) Checks\n2) Transactions\n3)Cards \n4)Categories \n5)Cars \n6)Car Registers \nq)Quit")
        selectedOption = input("\n")
        #TRY Catch for the type error and index out of range
        if selectedOption == 'q':
            break
        try:
    
            #Here im getting the Table Name and the pseudoName
            print(f"What do you want to do with the {tableNames.get(selectedOption)[0]}?")
            actionOption = input("1)Create a new record\n2)Read Registers\n3)Update Register\n4)Delete Register\nq)Exit App\n other option back to previous menu.")
        
            if actionOption == '1':
                if tableStructure.get(selectedOption) and tableNames.get(selectedOption):
                    #Verificando que la tabla existe en el diccionario
                    tableKeys = tuple(tableStructure.get(selectedOption).keys())
                    finalValues = EntryData(tableStructure[selectedOption])
                    print(finalValues)
                    db.Create(tableNames.get(selectedOption)[1],tableKeys,finalValues)
                    if selectedOption == '1':
                        if input("Do you want to add this check to the transactions table? Y/N: ").capitalize() == 'Y':
                            flow_check = [str(uuid.uuid4()),
                                          finalValues[12],
                                          date.today().strftime("%m-%d-%Y"),
                                          date.today().strftime("%m-%d-%Y"),
                                          f"Payment date: {finalValues[13]}",
                                          "6cd25856-9a49-4a39-b9bb-3448c216c74c",
                                          "False",
                                          f"PayCheck Best One {finalValues[13]} ",
                                          "False",
                                          "False",
                                          "2",
                                          "3"
                                          ]
                            db.Create(tableNames.get("2")[1],tuple(tableStructure.get("2").keys()),flow_check)
                            
                        else: print("Not saved ")

            elif actionOption == '2':
                if tableNames.get(selectedOption):
                    returnValues= db.Read(tableNames.get(selectedOption)[1])
                    print(tabulate(returnValues))
                    
        except Exception as e:
            print(e)
            break

        
    







#Need to add the option to list all (Done)
#Try to improve the code using dictionaries 
#Link user for username  (Default)
#Edit flow or record (Edit Flow)
#List of Checks
#Show statistics
        

    
    

#THE UUID FIELD AUTO ENTER AND GENERATE
#Customize each input data 