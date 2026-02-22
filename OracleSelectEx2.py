#Program for reading the records from employee table---fetchmany()
#OracleSelectEx2.py
import oracledb as orc
def selectrecords():
    try:
        con=orc.connect("system/roshan@localhost/XE")
        cur=con.cursor()
        sq="select * from employee"
        cur.execute(sq)
        #Get the record
        print("*"*50)
        records=cur.fetchmany()
        for record in records: #For reverse order we use....[::-1]
            for val in record:
                print(val,end="\t")
            print()
        print("*"*50)
    except orc.DatabaseError as db:
        print("Problem in Oracle Database",db)
#Main program
selectrecords()
#In oracledb ---if we use fetchmany(0)==>>No record will print
#In cx_oracle---if we use fetchmany(0)===>Then first record will print...
#If we use negative values -8 ,-0===>Then also no record will print..
#If we say 85 more then the records then all records will print...
#If we say only fetchmany()==>then all records will print.