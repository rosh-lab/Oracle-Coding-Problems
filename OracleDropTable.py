#Program for removing the table from oracle database
#OracleDropTable.py
import oracledb as orc
def droptablename():
    try:
        con = orc.connect("system/roshan@localhost/XE")
        cur = con.cursor()
        # Alter Query...
        dt="drop table student"
        cur.execute(dt)
        print("Table droped successfully in oracle")
    except orc.DatabaseError as db:
        print("Problem in oracle db", db)
# main program
droptablename()