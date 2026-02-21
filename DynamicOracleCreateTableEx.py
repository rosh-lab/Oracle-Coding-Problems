#Program for creating a table dynamically...
#DynamicOracleCreateTableEx1.py
import oracledb as orc #step1
def createtable():
    try:
        con=orc.connect("system/roshan@localhost/XE")#step2
        cur=con.cursor()#step3
        #step 4 creating table
        tc=input("Enter Query for creating a table in Oracle-SQl:")
        cur.execute(tc)
        #Step 5
        print("Table created successfully in oracle")
    except orc.DatabaseError as db:
        print("Problem in oracle in DB",db)
#Main program
createtable()