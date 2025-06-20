
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
        elif 'Updated' in colsPseudo[col]:
            values.append(date.today().strftime("%m-%d-%Y")) 


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

        "4": {"categoryname":"Category Name (text)"},

        "5": {"car_service_id": "ID (UUID)",
              "car_id": "Car ID (PK)",
              "car_service_title": "Title ",
              "car_service_cost":"Cost (float)",
              "car_service_date_created":"Date: ",
              "car_service_date_update": "Date Updated",
              "car_service_description": "Description (Text)",
              "car_odometer": "Car ODO (int)",
              "car_tag" : "Category (enum)"

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
        "6": ("Car List","carlists")
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
            print(actionOption)
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
                            db.Create(tableNames.get("2")[1],tuple(tableStructure.get("2").keys()),flow_check)
                            
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
                            db.Create(tableNames.get("2")[1],tuple(tableStructure.get("2").keys()),flow_check)



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