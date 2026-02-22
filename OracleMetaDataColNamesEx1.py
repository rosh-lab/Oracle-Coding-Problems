#Program for Demonstrating meta-data
#Here---Meta-data=Data about data ,,here data represents records and "About data" represents col names,col names Database datatype etc
import oracledb as orc
def selectmetadata():
    try:
        con=orc.connect("system/roshan@localhost/XE")
        cur=con.cursor()
        sq="select * from employee order by sal desc"
        cur.execute(sq)
        #Get metadta ====One attribute is there in cursor to obtain metadata..called description
        metadata=cur.description #Here description is an pre defined attribute present in cursor object and it gives metadata.
        print("-"*50)
        for colinfo in metadata:
            print(colinfo[0],end=" \t ")
        print()
        print("-"*50)
        print("-"*50)
    except orc.DatabaseError as db:
        print("Problem in Oracle Database",db)
#Main program
selectmetadata()