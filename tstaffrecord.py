#staff record table
import mysql.connector as m
from prettytable import PrettyTable, from_db_cursor
mydb=m.connect(host='localhost', user='root', passwd='pass123', database='library', auth_plugin='mysql_native_password')
mycursor=mydb.cursor()

'''create table if not exists staffrecord(
                     staff_id int auto_increment not null primary key,
                     staff_name varchar(100),
                     dob date,
                     mail_id varchar(50),
                     phone_num bigint unique,
                     salary float,
                     working_hours varchar(30)
                     )'''

def insertstaff():
    print('\nADD NEW STAFF MEMBER:-')
    try:
        name=input('enter new staff name:\t')
        dob=input('enter date of birth (yyyy-mm-dd):\t')
        mailid=input('enter email ID:\t')
        pno=input('enter phone num (971...):\t')
        sal=float(input('enter salary (in USD):\t'))
        hrs=input('enter working hours (from -- to --):\t')
        q = 'insert into staffrecord (staff_name, dob, mail_id, phone_num, salary, working_hours) values ("{}", "{}", "{}", "{}", {}, "{}")'.format(name, dob, mailid, pno, sal, hrs)
        mycursor.execute(q)
        mydb.commit()
        print('STAFF MEMBER ADDED')
        mycursor.execute('select * from staffrecord where staff_name="{}"'.format(name))
        row=mycursor.fetchall()
        userid=row[0][0]
        print('new staff id created:\t', userid, '\n')

    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()


def updatestaff():
    try:
        while True:
            staffid=int(input('enter staff ID:\t'))
            print('''UPDATE STAFF RECORD:-
1. update email ID
2. update phone number
3. update salary
4. update working hours
5. exit''')
            cho=int(input('enter choice:\t'))
            
            if cho==1:
                mycursor.execute('select * from staffrecord where staff_id = {}'.format(staffid))
                row1 = mycursor.fetchone()
                if not row1:
                    print('staff ID does not exist, please enter a valid ID')
                    continue
                newmail=input('enter new email ID:\t')
                q='update staffrecord set mail_id="{}" where staff_id={}'.format(newmail, staffid)
                
            elif cho==2:
                mycursor.execute('select * from staffrecord where staff_id = {}'.format(staffid))
                row2 = mycursor.fetchone()
                if not row2:
                    print('staff ID does not exist, please enter a valid ID')
                    continue
                newpno=int(input('enter new phone num (971...):\t'))
                q='update staffrecord set phone_num={} where staff_id={}'.format(newpno, staffid)
                
            elif cho==3:
                mycursor.execute('select * from staffrecord where staff_id = {}'.format(staffid))
                row3 = mycursor.fetchone()
                if not row3:
                    print('staff ID does not exist, please enter a valid ID')
                    continue
                sal=input('enter new salary (in USD):\t')
                q='update staffrecord set salary={} where staff_id={}'.format(sal, staffid)
                
            elif cho==4:
                mycursor.execute('select * from staffrecord where staff_id = {}'.format(staffid))
                row4 = mycursor.fetchone()
                if not row4:
                    print('staff ID does not exist, please enter a valid ID')
                    continue
                hrs=input('enter new working hours (from -- to --):\t')
                q='update staffrecord set working_hours="{}" where staff_id={}'.format(hrs, staffid)
                
            elif cho==5: break
            else: print('enter valid choice!')

            mycursor.execute(q)
            mydb.commit()
            print('RECORD UPDATED\n')

    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()
        

def deletestaff():
    try:
        print('\nDELETE STAFF MEMBER:-\t')
        while True:
            staffid = int(input('enter staff ID to be deleted:\t'))
            mycursor.execute('select * from staffrecord where staff_id = {}'.format(staffid))
            row1 = mycursor.fetchone()
            if not row1:
                print('staff ID does not exist, please enter a valid ID')
                continue
            q = 'delete from staffrecord where staff_id={}'.format(staffid)
            mycursor.execute(q)
            mydb.commit()
            print('RECORD DELETED\n')
            break
        
    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()


def searchstaff():
    print('\nSEARCH STAFF MEMBER DETAILS:-')
    staffid = int(input('enter staff ID to search:\t'))
    q = 'select * from staffrecord where staff_id = {}'.format(staffid)
    mycursor.execute(q)
    data = mycursor.fetchall()
    if data:
        print('RECORD FOUND:')
        Y = PrettyTable()
        Y.field_names = [i[0] for i in mycursor.description]
        Y.add_rows(data)
        print(Y)
    else: print('RECORD NOT FOUND\n')


def showstaff():
    Y = PrettyTable()
    mycursor.execute('select * from staffrecord')
    Y = from_db_cursor(mycursor)
    print("\nSTAFF MEMBERS DETAILS:\n")
    print(Y)
