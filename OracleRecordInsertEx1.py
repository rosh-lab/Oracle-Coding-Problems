#Program which will read employee values from keyboard and insert as a record in employee table..
#OracleRecordInsertEx1.py==>>
import oracledb as orc
def recordinsert():
    try:
        con=orc.connect("system/roshan@127.0.0.1/XE")
        cur=con.cursor()
        #Design the DML query and insert
        iq="insert into employee values(500,'Rosh',2.5,'TCS')"
        cur.execute(iq)
        con.commit()
        print("Record inserted in oracle successfully")
    except orc.DatabaseError as db:
        print("Problem in oracle database",db)
#Main program
recordinsert()