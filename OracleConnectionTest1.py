#Program for demonstrating how to get connection from Oracle Database..
#OracleConnectionTest1.py
import oracledb as orc #step1
try:
    con=orc.connect("system/roshan@localhost/XE") #Step2 DNS
    print("type of con=",type(con))
    print("Python program obtains connection from OracleDB")
except orc.DatabaseError as db:
    print("Problem in Data Base Connection",db)