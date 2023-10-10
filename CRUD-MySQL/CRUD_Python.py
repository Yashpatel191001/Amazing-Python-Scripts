import pymysql
##Please enter the respective details in the info given below! (don't change host and user if using default SQL configuration)
#------------------------------------------#
info = {'host':'localhost','user':'root','password':'EnterYours','database':'EnterDataBaseName'}
#------------------------------------------#
conn = pymysql.connect(host=info['host'],user=info['user'],password=info['password'],database=info['database'])
cursor = conn.cursor()
#1. Create:
def create_sql_table(table_name,col_names,datatypes):
    #Enter table name to be created
    str = 'CREATE TABLE '+table_name+'( '
    idx = -1
    for i in col_names:
        idx+=1
        if idx < len(col_names)-1:
            str = str+i+' '+datatypes[idx]+', '
        else:
            str = str+i+' '+datatypes[idx]
    str = str+')'
    cursor.execute(str)
    conn.commit()
    print('Table '+table_name+' Created!\n')

#2. Read:
def read_sql_table(table_name,col_names,condition):
    #Enter table name to be read:
    cursor = conn.cursor()
    str = 'SELECT '
    idx = -1
    for i in col_names:
        idx+=1
        if idx<len(col_names)-1:
            str = str+i+', '
        else:
            str = str + i
    str = str + ' FROM '+table_name
    if len(condition)>0:
        str = str + ' WHERE '
        for i in condition:
            str = str + i
    str = str+' ;'
    cursor.execute(str)
    conn.commit()
    results = cursor.fetchall()
    print('Search Results are: \n')
    for row in results:
        print(row)
    print('\n')

#3. Update:

#3.1 Insert
def insert_sql_table(table_name, col_names, vals):
    # Enter table name for data to be inserted into:
    str = 'INSERT INTO  '+table_name+'( '
    idx = -1
    for i in col_names:
        idx += 1
        if idx < len(col_names)-1:
            str = str+i+', '
        else:
            str = str+i+' '
    str = str+') VALUES ( '
    idx = -1
    for i in vals:
        idx += 1  
        if idx < len(vals)-1:
            str = str+i+', '
        else:
            str = str+i+' '
    str = str+' );'
    cursor.execute(str)
    conn.commit()
    print('Insertion into Table '+table_name+' Complete!\n')
    
#3.2 Update
def update_sql_table(table_name, col_name,val,condition):
    # Enter table name for data to be inserted into:
    str = 'UPDATE  '+table_name+' SET '+col_name+' = '+val+' WHERE '+condition
    cursor.execute(str)
    conn.commit()
    print('Table '+table_name+' Updated!\n')

#4. Delete:


def delete_sql_table(table_name, condition):
    # Enter table name for data to be inserted into:
    str = 'DELETE FROM '+table_name+' WHERE '+condition
    cursor.execute(str)
    conn.commit()
    print('Deletion in Table '+table_name+' Complete!\n')

#--------------TRIAL------------------#
#1. Create
create_sql_table('SResidency_Friends',['Name','Age'],['VARCHAR(60)','INT'])

insert_sql_table('SResidency_Friends', ['Name', 'Age'], ["'Rashmitha'", '20'])
insert_sql_table('SResidency_Friends', ['Name', 'Age'], ["'Rachitha'", '25'])
insert_sql_table('SResidency_Friends', ['Name', 'Age'], ["'Atah'", '15'])
insert_sql_table('SResidency_Friends', ['Name', 'Age'], ["'Aanya'", '14'])
insert_sql_table('SResidency_Friends', ['Name', 'Age'], ["'Bharath'", '19'])

#2. Read
read_sql_table('SResidency_Friends', ['Name', 'Age'], ['Age > 19'])

#3. Update
update_sql_table('SResidency_Friends', 'Name', "'Bharat'", 'Age = 19')

#4. Delete
delete_sql_table('SResidency_Friends','Age<15')