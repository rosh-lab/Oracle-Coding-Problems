#Program for reading the records from employee table---fetchone()
#OracleSelectEx1.py
import oracledb as orc
def selectrecords():
    try:
        con=orc.connect("system/roshan@localhost/XE")
        cur=con.cursor()
        sq="select * from employee"
        cur.execute(sq)
        #Get the record
        print("*"*50)
        while(True):
            record=cur.fetchone()
            if(record!=None):
                for val in record:
                    print("{}".format(val),end="\t\t")
                print()
            else: 
                print("*"*50)
                break
    except orc.DatabaseError as db:
        print("Problem in Oracle Database",db)
#Main program
selectrecords()