import uuid 
import psycopg2

db_params = {
    'dbname': 'Expenses_Register',
    'user': 'postgres',
    'password': 'Marcelomanda2020',
    'host': 'localhost',
    'port': '5432'
}
cursor = None
conn= None

def InsertRegisterIntoFlowTable(Title,Amount,DateCreated,DateUpdate,Desciption,User,isExpense):
    try:
        conn  = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        newUUID = str(uuid.uuid4())
        query = 'INSERT INTO "Flow" ("Flow_ID", "Flow_Title","Flow_amount","Flow_Created","Flow_Updated","Flow_Description","Flow_User","Flow_isExpense") VALUES (' + f"'{newUUID}','{Title}',{Amount},'{DateCreated}','{DateUpdate}','{Desciption}','{User}','{isExpense}');"
        cursor.execute(query)
        conn.commit()
        print('Register Created!')
    except Exception as e:
        print(f"The error is : {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def SelectAllRegistersFromFlowTable():
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        query = 'SELECT public."Flow"."Flow_Title", public."Flow"."Flow_amount",public."Flow"."Flow_isExpense", public."Flow"."Flow_Created" FROM public."Flow";'
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def SearchForUser(user,password):
    try: 
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        query = 'SELECT * FROM public."Users" WHERE public."Users"."User_Username" = ' + "'" + user + "';"
        print(query)
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0
                      ]
    except Exception as e :
        print(f"ERROR: {e} ")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# InsertRegisterIntoFlowTable('Pool',30.0,'08-08-2024','08-08-2024','Playing pool after work','6cd25856-9a49-4a39-b9bb-3448c216c74c','True')