#Program for creating a table...
#OracleCreateTableEx1.py
import oracledb as orc #step1
def createtable():
    try:
        con=orc.connect("system/roshan@localhost/XE")#step2
        cur=con.cursor()#step3
        #step 4 creating table
        tc="create table temp(no number(2) primary key,name varchar2(10) not null)"
        cur.execute(tc)
        #Step 5
        print("Table created successfully in oracle")
    except orc.DatabaseError as db:
        print("Problem in oracle in DB",db)
#Main program
createtable()