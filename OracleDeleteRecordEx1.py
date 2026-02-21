#program for deleting a record...
import oracledb as orc
def deleterecord():
    try:
        con=orc.connect("system/roshan@localhost/XE")
        cur=con.cursor()
        dq="delete from employee where eno=100"
        cur.execute(dq)
        con.commit()
        if(cur.rowcount>0):
            print("{} Record deleted from oracle database".format(cur.rowcount))
        else:
            print("Employee number does not exist ")
    except orc.DatabaseError as db:
        print("Problem in oracle database",db)
#Main program
deleterecord()