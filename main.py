
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


def EntryData(tablesStrc,tblNumber,tablNames):
    colsName = tuple(tablesStrc[tblNumber].keys())
    colsPseudo = tuple(tablesStrc[tblNumber].values())
    values = []
    for col in range(len(colsName)):
        print(colsPseudo[col].split('-')[0])
        if colsPseudo[col].split('-')[1] == 'F':print('is Float')
        elif colsPseudo[col].split('-')[1] == 'I':print('is Integer')
        elif colsPseudo[col].split('-')[1] == 'S':print('is String')
        elif colsPseudo[col].split('-')[1] == 'B':print('is Boolean')
        elif 'K' in colsPseudo[col].split('-')[1] :
            colFK = colsPseudo[col].split('-')[1][1]
            foreignTable = db.Read(tablNames.get(colFK)[1])
            print(tabulate(foreignTable))
        elif colsPseudo[col].split('-')[1] == 'D':print('is Date format')
        elif colsPseudo[col].split('-')[1] == 'NF':print('is No input Float')
        print(' ')
         

        # if 'UUID' in colsPseudo[col] and col == 0:values.append(str(uuid.uuid4()))
        # elif 'NonIn' in colsPseudo[col] and 'Total Payment' in colsPseudo[col] :
        #     if values[3] > 40:
        #         val1 = values[4] * (values[3]*1.5 -20)
        #         # val1 = values[4]*(40 + (values[3]-40)*1.5)
        #         values.append(val1)
        #     else: values.append(values[3]*values[4])
        # elif 'NonIn' in colsPseudo[col] and 'Total Deduction' in colsPseudo[col] :
        #     val2 = values[6] + values[7] +values[8] + values[9]
        #     values.append(val2)
        # elif 'NonIn' in colsPseudo[col] and 'Percentage' in colsPseudo[col] :
        #     val3 = (values[10]*100)/values[5]
        #     values.append(val3)
        # elif 'NonIn' in colsPseudo[col] and 'Net Pay' in colsPseudo[col] :
        #     values.append(values[5] - values[10])
        # elif 'Updated' in colsPseudo[col]:
        #     values.append(date.today().strftime("%m-%d-%Y")) 


        # else:
        #     valueInput = input(f"Enter {colsPseudo[col]}: ")
        #     if 'int' in colsPseudo[col]: 
        #         values.append(int(valueInput))
        #     elif 'float' in colsPseudo[col]: values.append(float(valueInput))
            
        #     else: values.append(valueInput)

    # return values
    

    



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
        "1": {
        # {"check_id": "ID",                                        #0
              "check_start": "Start Date: -D",                                    #1
              "check_end":"End Date: -D",                                         #2
              "check_total_hours":"Total Hours: -F",                      #3
              "check_regular_payment":"Reg Payment: -F",                  #4
              "check_total_payment":"Total Payment: -NF",            #5
              "check_net_payment":"Net Pay: -NF",                     #12
              "check_date" : "Date Check:  -D",
              "check_federal_tax":"Federal Tax:  -F",                      #6
              "check_medicare":"Medicare: -F",                            #7
              "check_soc_sec":"Social Security: -F",                      #8
              "check_city_tax":"City Tax: -F",                            #9
              "check_total_deduction":"Total Deduction: -NF",        #10
              "check_percentage":"Percentage: -NF",                  #11
              },               

        "2": {
            # "flow_id":"ID (UUID)",
              "flow_title":"Title: -S",
              "flow_amount":"Amount: -F)",
              "flow_created":"Date Created: -D",
              "flow_updated":"Date Updated: -D",
              "flow_description":"Description: -S",
              "flow_user":"User: -K7", 
              "flow_is_expense":"Expense: -B",
              "flow_is_credit":"is Credit: -B",
              "flow_is_cash":"is Cash: -B",
              "flow_card":"Card: -K3",
              "flow_category":"Category: -K4"},

        "3": {"cardname":"Card Name: -S"},

        "4": {"categoryname":"Category Name: -S"},

        "5": {
            # "car_service_id": "ID (UUID)",
              "car_id": "Car ID: -K",
              "car_service_title": "Title: -S",
              "car_service_cost":"Cost: -F",
              "car_service_date_created":"Date Created: -D",
              "car_service_date_update": "Date Updated: -D",
              "car_service_description": "Description: -S",
              "car_odometer": "Car ODO: -I",
              "car_tag" : "Category: -K0"

        } 

                }
    
    carCategory = ['Gas','Maintenance','Repair', 'Others']
    #Table Name and pseudo name
    #(PSEUDONAMES  |  TABLENAME)
    tableNames = {
        "1": ("Checks","checks"),
        "2": ("Transactions","flow"),
        "3": ("Cards","cards"),
        "4": ("Categories","categories"),
        "5": ("Cars Services", "carservices"),
        "6": ("Car List","carlists"),
        "7" : ("Users","users")
    }

    # 6cd25856-9a49-4a39-b9bb-3448c216c74c-- USER ID

    while True:
        print("Select One option of the menu: \n1) Checks\n2) Transactions\n3) Cards \n4) Categories \n5) Cars \n6) Car Registers \nq) Quit")
        selectedOption = input("\n")
        #TRY Catch for the type error and index out of range
        if selectedOption == 'q':
            break
        try:
    
            #Here im getting the Table Name and the pseudoName
            print(f"What do you want to do with the {tableNames.get(selectedOption)[0]}?")
            actionOption = input("1)Create a new record\n2)Read Registers\n3)Update Register\n4)Delete Register\nq)Exit App\n other option back to previous menu.")
            print(actionOption)
            if actionOption == '1':
                if tableStructure.get(selectedOption) and tableNames.get(selectedOption):
                    #Verificando que la tabla existe en el diccionario
                    tableKeys = tuple(tableStructure.get(selectedOption).keys())
                    # Entry Data gets the all the table structures dictionary and the number of the table to insert
                    finalValues = EntryData(tableStructure,selectedOption,tableNames)
                    # print(finalValues)
                    #db.Create(tableNames.get(selectedOption)[1],tableKeys,finalValues)
                    if selectedOption == '1':
                        if input("Do you want to add this check to the transactions table? Y/N: ").capitalize() == 'Y':
                            flow_check = [str(uuid.uuid4()),
                                          finalValues[12],
                                          finalValues[13],
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
                            #Insert into DB
                            #db.Create(tableNames.get("2")[1],tuple(tableStructure.get("2").keys()),flow_check)
                            
                        else: print("Not saved ")
                    elif selectedOption == '5':
                        if input("Do you want to add this check to the transactions table? Y/N: ").capitalize() == 'Y':
                            xtrainfo_iscredit = input("Was Credit? Y/N: \n")
                            xtrainfo_iscard = input("Was Card? Y/N: \n")
                            xtrainfo_cardinfo = input("Card Number? 1 or 2: \n")
                            
                            
                            
                            flow_check = [str(uuid.uuid4()),
                                          finalValues[3],
                                          finalValues[4],
                                          date.today().strftime("%m-%d-%Y"),
                                          f"{finalValues[6]}",
                                          "6cd25856-9a49-4a39-b9bb-3448c216c74c",
                                          "True",
                                          f"{finalValues[2]} ",
                                          f"{xtrainfo_iscredit}",
                                          f"{xtrainfo_iscard}",
                                          f"{xtrainfo_cardinfo}",
                                          "5"
                                          ]
                            #Insert into DB 
                            #db.Create(tableNames.get("2")[1],tuple(tableStructure.get("2").keys()),flow_check)



            elif actionOption == '2':
                if tableNames.get(selectedOption):
                    returnValues= db.Read(tableNames.get(selectedOption)[1])
                    print(tabulate(returnValues, headers=tuple(tableStructure.get(selectedOption).values() ) ))

                    # print(  tuple(tableStructure.get(selectedOption).values() ))
                    
        except Exception as e:
            print(e)
            break

        
    







#Need to add the option to list all (Done)
#Try to improve the code using dictionaries 
#Link user for username  (Default)
#Edit flow or record (Edit Flow)
#List of Checks
#Show statistics
        


#Car ID 5f3637b4-b983-4370-bb84-33e659a07a4c
    

#THE UUID FIELD AUTO ENTER AND GENERATE
#Customize each input data 