import mysql.connector
import datetime
import getpass
mydb=mysql.connector.connect(host='localhost',user='root',passwd='00130000004', database='db1')
mycursor=mydb.cursor()
print("Log into Your Account.")
user=input("Enter Username :")
password=getpass.getpass("Enter Password :")
login="select * from login" 
mycursor.execute(login)
outcome=mycursor.fetchall()
for passkey in outcome:
    pass
if user in passkey:
    print("Logged In Succesfully...")
    x=datetime.datetime.now()
    y=x.strftime('%y/%m/%d')
    while True:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='00130000004', database='db1')
        mycursor=mydb.cursor()
        #mycursor.execute("create database db1")
        #mycursor.execute("show databases")
        '''mycursor.execute(create table Deliver(
                        Order_no int not null,
                        Order_Date Date,
                        Customer_Name varchar(30) not null,
                        Delivery_Address varchar(64) not null,
                        City varchar(30) not null,
                        Payment_Method varchar(30) not null,
                        Order_total_INR float(10,2) not null,
                        Order_Status varchar(30) not null,
                        unique(Order_no));)'''
        mycursor.execute("select sum(Order_total_INR) from Deliver")
        to=mycursor.fetchall()
        for i in to[:]:
                turnover=i[0]
        print("\t\t\t Fast Shipping Delivery pvt.ltd.")
        print("\t\t\t   Choose Function ")
        print("Enter '0' for updating order status!!")
        print("Create a new order    -->1")
        print("Show Pending Orders   -->2")
        print("Show Delivered Orders -->3")
        print("Show All Orders       -->4")        
        print("Delete Orders         -->5")
        print("Total turnover",turnover,"INR")
        choice = int(input("Enter Choice          :"))
        if (choice==2):
            mycursor.execute("select count(Order_no) from Deliver where Order_Status='OPEN'")
            result= mycursor.fetchall()
            for j in result:
                j=j
            if i[0]<1:
                print("Currently, There are no pending orders.")
            else:    
                mycursor.execute("select * from Deliver where Order_Status='OPEN'")
                result=mycursor.fetchall()
                for k in result:
                    print(k)
        if (choice==1):
            order_no= int(input("Enter Order number    :"))
            cust_nam= input("Enter Customer  Name   :").capitalize()
            add= input("Enter Delivery Address   :").title()
            city=input("Enter City :").title()
            date=y
            pay=input("Enter Payment Method (COD/Online Payment) :").upper()
            total=float(input("Enter Order Total(inclusive of all taxes) :"))
            status="OPEN"
            cmd1="insert into Deliver values"
            cmd2="('%d','%s','%s','%s','%s','%s','%d','%s')"%(order_no,date,cust_nam,add,city,pay,total,status)
            sqlcommand=cmd1+" "+cmd2
            msg=input("Create (Yes/No) :").capitalize()
            if msg=='Yes'or'y':
                mycursor.execute(sqlcommand)
            else:
                pass
        if (choice==3):
            mycursor.execute("select count(Order_no) from Deliver where Order_Status='CLOSE'")
            result= mycursor.fetchall()
            for j1 in result:
                j1=j1
            if j1[0]>1:
                print("Order PENDING")
            else:    
                mycursor.execute("select * from Deliver where Order_Status='CLOSE'")
                result=mycursor.fetchall()
                for k in result:
                    print(k)
        if choice ==4:
            mycursor.execute("select * from Deliver")
            result= mycursor.fetchall()
            for i2 in result:      
                print(i2)
        if choice ==5:
            mycursor.execute("select * from Deliver")
            result= mycursor.fetchall()
            for x in result:
                print(x)
            dlt1=int(input("Enter Order Number to delete  :"))
            are=input("yes or no    :")
            if (are=='yes'):
                sqlcommand="delete from Deliver where Order_no=('%d')"%(dlt1)
                mycursor.execute(sqlcommand)    
            else:
                pass
        if choice=='0':
            ord_no=int(input("Enter Order number :"))
            st=input("Enter Status (OPEN/CLOSE)  :")
            update="update Deliver set Order_Status=('%s') where Order_no=('%d')"(st,ord_no)
            mycursor.execute(update)
            result= mycursor.fetchall()        
        mydb.commit()
else:
    print("Incorrect Username or Password")


