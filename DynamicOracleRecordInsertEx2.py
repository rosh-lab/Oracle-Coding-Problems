#Program which will read employee values from keyboard and insert as a record in employee table dynamically
#DynamicOracleRecordInsertEx2.py==>>
import oracledb as orc
def recordinsert():
    while(True):
        try:
            con=orc.connect("system/roshan@127.0.0.1/XE")
            cur=con.cursor()
            #accept the employees values from KBD
            print("="*50)
            empno=int(input("Enter employee number:"))
            empname=input("Enter employee name:")
            empsal=float(input("Enter employee salary:"))
            cmpname=input("Enter employee company name:")
            print("="*50)
            #Design the DML query and insert
            iq="insert into employee values(%d,'%s',%f,'%s')"
            cur.execute(iq %(empno,empname,empsal,cmpname))
            #  OR
            #cur.execute("insert into employee values(%d,'%s',%f,'%s')"  %(empno,empname,empsal,cmpname))
            con.commit()
            print("{} Record inserted in oracle successfully".format(cur.rowcount)) #Rowcount is an attribute which is used to bring the result to the python program from oracledb
            print("="*50)
            ch=input("Do you want to insert another record?(yes/no):")
            if(ch.lower()=="no"):
                print("Thnxs for using this program")
                break
        except orc.DatabaseError as db:
            print("Problem in oracle database",db)
        except ValueError:
            print("Don't enter alnums,strs and symbols for empno and sal")
#Main program
recordinsert()