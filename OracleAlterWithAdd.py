#Program for altering employee table by adding new column
#OracleAlterWithAdd.py
import oracledb as orc
def alterwithadd():
    try:
        con=orc.connect("system/roshan@localhost/XE")
        cur=con.cursor()
        #Alter Query...
        aq="alter table employee add(compname varchar2(1) not null)"
        cur.execute(aq)
        print("Table altered with add successfully in oracle")
    except orc.DatabaseError as db:
        print("Problem in oracle db",db)
#main program
alterwithadd()