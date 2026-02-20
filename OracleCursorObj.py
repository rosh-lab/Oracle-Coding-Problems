#Program for demoonstrating how to create cursor object..
#OracleCursorObj.py
import oracledb as orc
def getcursor():
    try:
        con=orc.connect("system/roshan@localhost:1521/xepdb1") #Step2
        print("type of con=",type(con))
        print("Python program obtains connection from Oracle db")
        print("===========================================")
        cur=con.cursor()#Step3
        print("type of cur=",type(cur))
        print("Python program Created cursor object")
        print("============================================")
    except orc.DatabaseError as db:
        print("Database Error:",db)
#Main program
getcursor()