#Program for altering employee table column sizes...
#OracleAlterWithModify.py
import oracledb as orc
def alterwithmodify():
    try:
        con=orc.connect("system/roshan@localhost/XE")
        cur=con.cursor()
        #Alter Query...
        aq="alter table employee modify(eno number(4),name varchar2(16),compname varchar2(16))"
        cur.execute(aq)
        print("Table altered successfully in oracle")
    except orc.DatabaseError as db:
        print("Problem in oracle db",db)
#main program
alterwithmodify()