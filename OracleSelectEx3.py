#Program for reading the records from employee table---fetchall()
#OracleSelectEx3.py
import oracledb as orc
def selectrecords():
    try:
        con=orc.connect("system/roshan@localhost/XE")
        cur=con.cursor()
        sq="select * from employee order by eno asc"
        cur.execute(sq)
        #Get the record
        print("*"*50)
        records=cur.fetchall()
        for record in records: #For reverse order we use....[::-1]
            for val in record:
                print(val,end="\t")
            print()
        print("*"*50)
    except orc.DatabaseError as db:
        print("Problem in Oracle Database",db)
#Main program
selectrecords()
#Order by ----gives data in ascending order by default....
#asc===for ascending order
#desc===for desending order
