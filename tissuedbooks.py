#issued books + issued books history table
import datetime
import mysql.connector as m
from prettytable import PrettyTable, from_db_cursor
mydb=m.connect(host='localhost', user='root', passwd='pass123', database='library', auth_plugin='mysql_native_password')
mycursor=mydb.cursor()

'''create table if not exists issuedbooks(
                     user_id int not null,
                     book_id int,
                     book_name varchar(200),
                     ISBN varchar(14) not null,
                     issued_date date,
                     foreign key (book_name, ISBN) references bookcatalog(title, ISBN)
                     )'''

'''create table if not exists issuedhistory(
                     user_id int not null,
                     book_id int,
                     book_name varchar(200),
                     ISBN varchar(14) not null,
                     issued_date date,
                     foreign key (book_name, ISBN) references bookcatalog(title, ISBN)
                     )'''

#for user to issue a book
def insertbooks():
    print('\nISSUE A BOOK:-')
    try:
        while True:
            #to check if book is available
            bookid=int(input('enter book ID:\t'))
            mycursor.execute('select * from bookcatalog where book_id = {}'.format(bookid))
            row1 = mycursor.fetchone()
            if not row1:
                print('book ID does not exist, please enter a valid book ID')
                continue
            elif row1[6] == 'issued':
                print('book is already issued by someone else, choose another book')
                continue
            else: break
            
        while True:
            currentdate = datetime.date.today()
            memberid=int(input('enter user ID:\t'))
            mycursor.execute('select * from members where user_id={}'.format(memberid))
            row2=mycursor.fetchone()
            #to check if user ID is valid
            if row2:
                mycursor.execute('''
                            insert into issuedbooks (user_id, book_id, book_name, ISBN, issued_date)
                            select {}, {}, bc.title, bc.ISBN, "{}"
                            from bookcatalog bc
                            where bc.book_id = {}
                            '''.format(memberid, bookid, currentdate, bookid))
                mycursor.execute('update members set books_issued=books_issued + 1 where user_id={}'.format(memberid)) #updates no. of issued books in tmembers
                mycursor.execute('update bookcatalog set frequency=frequency + 1 where book_id={}'.format(bookid)) #updates no. of times book has been issued in tbookcatalog
                mycursor.execute('update bookcatalog set availability="issued" where book_id={}'.format(bookid)) #updates status of book in tbookcatalog
                mycursor.execute('select * from issuedbooks')
                row3=mycursor.fetchall()
                mycursor.execute('insert into issuedhistory (user_id, book_id, book_name, ISBN, issued_date) VALUES ({}, {}, "{}", "{}", "{}")'.format(
                        memberid, bookid, row3[-1][2], row3[-1][3], currentdate)) #adds record to tissuedhistory
                mydb.commit()
                print('BOOK ISSUED\n')
                break
            else:
                print('enter valid user ID')
                continue

    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()


#for user to return a book
def deletebooks():
    try:
        print('\nRETURN A BOOK:\t')
        while True:
            bookid = int(input('enter book ID to be returned:\t'))
            mycursor.execute('select * from issuedbooks where book_id = {}'.format(bookid))
            row = mycursor.fetchone()
            if not row:
                print('book ID has not been issued, please enter a valid book ID')
                continue
            q = 'delete from issuedbooks where book_id={}'.format(bookid)
            mycursor.execute(q)
            mycursor.execute('update bookcatalog set availability="available" where book_id={}'.format(bookid))
            mydb.commit()
            print('BOOK RETURNED\n')
            break
    
    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()


#for user to choose what book to issue = only available books
def showbookcatalog():
    Y = PrettyTable()
    mycursor.execute('select * from bookcatalog where availability="available"')
    Y = from_db_cursor(mycursor)
    print("\nBOOK CATALOG:\n")
    print(Y)


#for user to view their issued history
def showissuedhistoryuser(userid):
    Y = PrettyTable()
    mycursor.execute('select * from issuedhistory where user_id={}'.format(userid))
    Y = from_db_cursor(mycursor)
    print("\nISSUED HISTORY:\n")
    print(Y)

    cont=input('show extended table (y/n):\t')
    if cont.lower()=='y':
        Y = PrettyTable()
        mycursor.execute('''
                select ih.*, bc.author_name, bc.genre, bc.frequency
                from issuedhistory ih
                join bookcatalog bc on ih.book_id=bc.book_id
                where user_id={}
                '''.format(userid))
        Y = from_db_cursor(mycursor)
        print("\nISSUED HISTORY:\n")
        print(Y)

   
#for admin to view issued history
def showissuedhistoryadmin():
    Y = PrettyTable()
    mycursor.execute('select * from issuedhistory')
    Y = from_db_cursor(mycursor)
    print("\nISSUED HISTORY:\n")
    print(Y)

    cont=input('show extended table (y/n):\t')
    if cont.lower()=='y':
        Y = PrettyTable()
        mycursor.execute('''
                select ih.*, bc.author_name, bc.genre, bc.frequency
                from issuedhistory ih
                join bookcatalog bc on ih.book_id=bc.book_id
                ''')
        Y = from_db_cursor(mycursor)
        print("\nISSUED HISTORY:\n")
        print(Y)


#for admin to search for issued books
def searchbooks():
    print('\nSEARCH ISSUED BOOK DETAILS:-')
    bookid = int(input('enter book ID to search:\t'))
    q = 'select * from issuedbooks where book_id = {}'.format(bookid)
    mycursor.execute(q)
    data = mycursor.fetchall()
    if data:
        print('RECORD FOUND:')
        Y = PrettyTable()
        Y.field_names = [i[0] for i in mycursor.description]
        Y.add_rows(data)
        print(Y)
    else: print('RECORD NOT FOUND\n')


#for admin to see what books have been issued
def showissuedbooks():
    Y = PrettyTable()
    mycursor.execute('select * from issuedbooks')
    Y = from_db_cursor(mycursor)
    print("\nISSUED BOOKS:\n")
    print(Y)

    cont=input('show extended table (y/n):\t')
    if cont.lower()=='y':
        Y = PrettyTable()
        mycursor.execute('''
                select ib.*, bc.author_name, bc.genre, bc.frequency
                from issuedbooks ib
                join bookcatalog bc on ib.book_id=bc.book_id
                ''')
        Y = from_db_cursor(mycursor)
        print("\nISSUED BOOKS:\n")
        print(Y)
