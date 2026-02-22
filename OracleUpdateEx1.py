#Program for updating a record...
#OracleUpdateEx1.py
import oracledb as orc
def updaterecord():
    try:
        con=orc.connect("system/roshan@localhost/XE")
        cur=con.cursor()
        uq="update employee set sal=6.7,compname='HCL' where eno=300"
        cur.execute(uq)
        con.commit()
        if(cur.rowcount>0):
            print("{} Record updated in oracle DB".format(cur.rowcount))
        else:
            print("Employee number does not exist")
    except orc.DatabaseError as db:
        print("Problem in oracle DB",db)
#MAin program
updaterecord()