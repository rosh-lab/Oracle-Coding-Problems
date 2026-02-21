#program for deleting a record...
import oracledb as orc
def deleterecord():
    while True:
        try:
            con=orc.connect("system/roshan@localhost/XE")
            cur=con.cursor()
            #Accept employee number from keyboard
            empno=int(input("Enter employee number: "))
            dq="delete from employee where eno=%d"
            cur.execute(dq %empno)
            con.commit()
            if(cur.rowcount>0):
                print("{} Record deleted from oracle database".format(cur.rowcount))
            else:
                print("Employee number does not exist ")
            print("*"*50)
            ch=input("Do you want to delete another record?(yes/no)")
            if(ch.lower()=="no"):
                print("Thnsx for using this program")
                break
        except orc.DatabaseError as db:
            print("Problem in oracle database",db)
        except ValueError:
            print("Don't enter alnums,strs and symbols for empno")
#Main program
deleterecord()