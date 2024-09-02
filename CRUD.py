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
        query = 'SELECT public."Flow"."Flow_ID", public."Flow"."Flow_Title", public."Flow"."Flow_amount",public."Flow"."Flow_isExpense", public."Flow"."Flow_Created" FROM public."Flow";'
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
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0]
    except Exception as e :
        print(f"ERROR: {e} ")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def SearchFlow(user,id):
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        query = 'SELECT * FROM public."Flow" WHERE public."Flow"."Flow_ID" = ' + "'" + id + "';" 
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0]
    except Exception as e:
        print(f"error : {e}")
        
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def UpdateFlow(id,content):
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        query = 'UPDATE public."Flow" SET "Flow_Title" = ' + f"'{content[0]}' ," + f' "Flow_amount" = {content[1]}, "Flow_isExpense" = ' + f"'{content[2]}', " +  '"Flow_Created" =' + f"'{content[3].strftime('%m-%d-%Y')}', " + '"Flow_Updated" = ' + f"'{content[4].strftime('%m-%d-%Y')}' WHERE " + 'public."Flow"."Flow_ID" = ' + f"'{id}' ;" 
        print(query)
        cursor.execute(query)
        conn.commit()
        print("Updated")
    except Exception as e:
        print(f"Error {e}")
    
    finally:
        if conn: conn.close()
        if cursor : cursor.close()
        
# SearchFlow('id','de8fd116-82b5-4d92-90a9-0b9aad562922')

# InsertRegisterIntoFlowTable('Pool',30.0,'08-08-2024','08-08-2024','Playing pool after work','6cd25856-9a49-4a39-b9bb-3448c216c74c','True')