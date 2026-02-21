#Program for removing the table from oracle database
#DynamicOracleDropTable.py
import oracledb as orc
def droptablename():
    try:
        con = orc.connect("system/roshan@localhost/XE")
        cur = con.cursor()
        cur.execute("drop table %s" %input("Enter the table name to drop:"))
        print("Table droped successfully in oracle")
    except orc.DatabaseError as db:
        print("Problem in oracle db", db)
# main program
droptablename()