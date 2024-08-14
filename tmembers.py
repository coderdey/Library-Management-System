#members table
import mysql.connector as m
from prettytable import PrettyTable, from_db_cursor
mydb=m.connect(host='localhost', user='root', passwd='pass123', database='library', auth_plugin='mysql_native_password')
mycursor=mydb.cursor()

'''create table if not exists members(
                     user_id int auto_increment not null primary key,
                     name varchar(200),
                     username varchar(20),
                     password varchar(20),
                     dob date,
                     mail_id varchar(50),
                     phone_num bigint unique,
                     members_since date,
                     books_issued int
                     )'''

def insertmembers():
    print('\nADD NEW MEMBER:-')
    try:
        name=input('enter new members name:\t')
        username=input('create username:\t')
        pw=input('create password:\t')
        dob=input('enter date of birth (yyyy-mm-dd):\t')
        mailid=input('enter email ID:\t')
        pno=int(input('enter phone num (971...):\t'))
        members_since=input('enter date (members since) (yyyy-mm-dd):\t')
        books_issued=int(input('enter no. of books issued:\t'))
        q = 'insert into members (name, username, password, dob, mail_id, phone_num, members_since, books_issued) values ("{}", "{}", "{}", "{}", "{}", "{}", "{}", {})'.format(name, username, pw, dob, mailid, pno, members_since, books_issued)
        mycursor.execute(q)
        mydb.commit()
        print('MEMBER ADDED\n')
        mycursor.execute('select * from members where name="{}"'.format(name))
        row=mycursor.fetchall()
        userid=row[0][0]
        print('new member id created:\t', userid, '\n')
            
    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()
        

def updatemembers():
    try:
        while True:
            memberid=int(input('enter user id:\t'))
            print('''\nUPDATE MEMBERS TABLE:-
1. update mailid
2. update phone num
3. update books issued
4. exit''')
            cho=int(input('enter choice:\t'))

            if cho==1:
                mycursor.execute('select * from members where user_id = {}'.format(memberid))
                row1 = mycursor.fetchone()
                if not row1:
                    print('user ID does not exist, please enter a valid ID')
                    continue
                newmail=input('enter new email ID:\t')
                q='update members set mail_id="{}" where user_id={}'.format(newmail, memberid)
                
            elif cho==2:
                mycursor.execute('select * from members where user_id = {}'.format(memberid))
                row1 = mycursor.fetchone()
                if not row1:
                    print('user ID does not exist, please enter a valid ID')
                    continue
                newpno=int(input('enter new phone num:\t'))
                q = 'update members set phone_num={} where user_id={}'.format(newpno, memberid)
                
            elif cho==3:
                mycursor.execute('select * from members where user_id = {}'.format(memberid))
                row1 = mycursor.fetchone()
                if not row1:
                    print('user ID does not exist, please enter a valid ID')
                    continue
                newnum=int(input('append number of books issued:\t'))
                q = 'update members set books_issued=books_issued + {} where user_id={}'.format(newnum, memberid)

            elif cho==4: break
            else: print('enter valid choice!')
            
            mycursor.execute(q)
            mydb.commit()
            print('RECORD UPDATED\n')

    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()


def deletemembers():
    try:
        print('\nDELETE MEMBER:-\t')
        while True:
            memberid = int(input('enter user ID to be deleted:\t'))
            mycursor.execute('select * from members where user_id = {}'.format(memberid))
            row1 = mycursor.fetchone()
            if not row1:
                print('user ID does not exist, please enter a valid ID')
                continue
            q = 'delete from members where user_id={}'.format(memberid)
            mycursor.execute(q)
            mydb.commit()
            print('RECORD DELETED\n')
            break
        
    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()


def searchmembers():
    print('\nSEARCH MEMBER DETAILS:-')
    memberid = int(input('enter user ID to search:\t'))
    q = 'select * from members where user_id = {}'.format(memberid)
    mycursor.execute(q)
    data = mycursor.fetchall()
    if data:
        print('RECORD FOUND:')
        Y = PrettyTable()
        Y.field_names = [i[0] for i in mycursor.description]
        Y.add_rows(data)
        print(Y)
    else: print('RECORD NOT FOUND\n')


def showmembers():
    Y = PrettyTable()
    mycursor.execute('select * from members')
    data=mycursor.fetchall()
    Y.field_names = [i[0] for i in mycursor.description]
    for record in data:
        Y.add_row(record)    
    print("\nMEMBERS DETAILS:\n")
    print(Y)


#for user to manage account
def showaccount(userid): #not working
    Y = PrettyTable()
    mycursor.execute('select * from members where user_id="{}"'.format(userid))
    data=mycursor.fetchall()
    Y.field_names = [i[0] for i in mycursor.description]
    for record in data:
        Y.add_row(record)    
    print("\nACCOUNT DETAILS:\n")
    print(Y)


def insertaccount(userid):
    try:
        while True:
            print('''\nINSERT ACCOUNT DETAILS:-
1. insert name
2. insert date of birth
3. insert email ID
4. insert phone num
5. exit''')
            cho=int(input('enter choice:\t'))
            if cho==1:
                memberid=userid
                name=input('enter new members name:\t')
                q='update members set name="{}" where user_id={}'.format(name, memberid)
            elif cho==2:
                memberid=userid
                dob=input('enter date of birth (yyyy-mm-dd):\t')
                q='update members set dob="{}" where user_id={}'.format(dob, memberid)
            elif cho==3:
                memberid=userid
                mailid=input('enter email ID:\t')
                q='update members set mail_id="{}" where user_id={}'.format(mailid, memberid)
            elif cho==4:
                memberid=userid
                pno=input('enter phone num (971...):\t')
                q='update members set phone_num={} where user_id={}'.format(pno, memberid)
            elif cho==5: break
            else: print('enter valid choice!')

            mycursor.execute(q)
            mydb.commit()
            print('DETAILS INSERTED\n')
            
    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()
        
        
def updateaccount(userid):
    try:
        while True:
            print('''\nUPDATE ACCOUNT:-
1. update email ID
2. update phone num
3. update books issued
4. exit''')
            cho=int(input('enter choice:\t'))
            if cho==1:
                memberid=userid
                newmail=input('enter new email ID:\t')
                q='update members set mail_id="{}" where user_id={}'.format(newmail, memberid)
            elif cho==2:
                memberid=userid
                newpno=int(input('enter new phone num:\t'))
                q='update members set phone_num={} where user_id={}'.format(newpno, memberid)
            elif cho==3:
                memberid=userid
                newnum=int(input('append number of books issued:\t'))
                q='update members set books_issued=books_issued + {} where user_id={}'.format(newnum, memberid)
            elif cho==4: break
            else: print('enter valid choice!')
            
            mycursor.execute(q)
            mydb.commit()
            print('RECORD UPDATED\n')

    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()


def deleteaccount(userid):
    try:
        while True:
            print('\nDELETE ACCOUNT:-')
            ask=input('''are you sure you want to delete your account?
you will lose all existing data, (y/n):\t''')
            if ask.lower()=='y':
                memberid = userid
                q = 'delete from members where user_id={}'.format(memberid)
                mycursor.execute(q)
                mydb.commit()
                print('ACCOUNT DELETED')
                break
            else:
                print('ACCOUNT NOT DELETED')
                break

    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()
