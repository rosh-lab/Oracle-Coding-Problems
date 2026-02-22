#Program for updating a record...
#DynamicOracleUpdateEx1.py
import oracledb as orc
def updaterecord():
    while(True):
        try:
            con=orc.connect("system/roshan@localhost/XE")
            cur=con.cursor()
            #Accept empno,emp new sal and emp new comp name
            empno=int(input("Enter employee number for updating emp sal and comp name:"))
            empsal=float(input("Enter employee new salary:"))
            cmpname=input("Enter employee new company name:")
            uq="update employee set sal=%f,compname='%s' where eno=%d"
            cur.execute(uq %(empsal,cmpname,empno))
            con.commit()
            if(cur.rowcount>0):
                print("{} Record updated in oracle DB".format(cur.rowcount))
            else:
                print("Employee number does not exist")
            print("*"*50)
            ch=input("Do you want to update another record?(Yes/No):")
            if(ch.lower()=="no"):
                print("Thnxs for using this program")
                break
        except orc.DatabaseError as db:
            print("Problem in oracle DB",db)
        except ValueError:
            print("Don't enter alnums,strs and symbols for empno and empsal")
#MAin program
updaterecord()