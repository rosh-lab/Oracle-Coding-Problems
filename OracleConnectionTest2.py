#Program for demonstrating how to get connection from Oracle Database..
#OracleConnectionTest2.py
import oracledb as orc #step1
try:
    con=orc.connect("system/roshan@127.0.0.1/xepdb1") #Step2 IP address
    print("type of con=",type(con))
    print("Python program obtains connection from OracleDB")
except orc.DatabaseError as db:
    print("Problem in Data Base Connection",db)
