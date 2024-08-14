#book catalog table
import mysql.connector as m
from prettytable import PrettyTable, from_db_cursor
mydb=m.connect(host='localhost', user='root', passwd='pass123', database='library', auth_plugin='mysql_native_password')
mycursor=mydb.cursor()

'''create table if not exists bookcatalog(
                     sno int auto_increment not null primary key,
                     book_id int not null unique,
                     title varchar(200),
                     author_name varchar(100),
                     genre varchar(50),
                     publication_date date,
                     availability varchar(30),
                     ISBN varchar(14) not null unique
                     )'''

def insertbooks():
    print('\nADD NEW BOOK:-')
    try:
        bookid=int(input('enter book ID:\t'))
        title=input('enter book title:\t')
        author=input('enter author name:\t')
        genre=input('enter genre:\t')
        pubd=input('enter publication date (yyy-mm-dd):\t')
        avail=input('enter availability:\t')
        isbn=input('enter ISBN:\t')
        q = 'insert into bookcatalog (book_id, title, author_name, genre, publication_date, availability, ISBN) values ({}, "{}", "{}", "{}", "{}", "{}", "{}")'.format(bookid, title, author, genre, pubd, avail, isbn)
        mycursor.execute(q)
        mydb.commit()
        print('BOOK ADDED\n')

    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()


def updatebooks():
    try:
        while True:
            bookid=int(input('enter book ID:\t'))
            print('''UPDATE BOOK CATALOG:-
1. update title
2. update genre
3. update availability
4. update ISBN
5. exit''')
            cho=int(input('enter choice:\t'))
        
            if cho==1:
                mycursor.execute('select * from bookcatalog where book_id = {}'.format(bookid))
                row1 = mycursor.fetchone()
                if not row1:
                    print('book ID does not exist, please enter a valid ID')
                    continue
                newtitle=input('enter updated title:\t')
                q='update bookcatalog set title="{}" where book_id={}'.format(newtitle, bookid)

            elif cho==2:
                mycursor.execute('select * from bookcatalog where book_id = {}'.format(bookid))
                row2 = mycursor.fetchone()
                if not row2:
                    print('book ID does not exist, please enter a valid ID')
                    continue
                gen=input('enter updated genre:\t')
                q='update bookcatalog set genre="{}" where book_id={}'.format(gen, bookid)

            elif cho==3:
                mycursor.execute('select * from bookcatalog where book_id = {}'.format(bookid))
                row3 = mycursor.fetchone()
                if not row3:
                    print('book ID does not exist, please enter a valid ID')
                    continue
                avail=input('enter updated availability:\t')
                q='update bookcatalog set availability="{}" where book_id={}'.format(avail, bookid)

            elif cho==4:
                mycursor.execute('select * from bookcatalog where book_id = {}'.format(bookid))
                row4 = mycursor.fetchone()
                if not row4:
                    print('book ID does not exist, please enter a valid ID')
                    continue
                isbn=input('enter updated ISBN (13-digit):\t')            
                q='update bookcatalog set ISBN="{}" where book_id={}'.format(isbn, bookid)

            elif cho==5: break
            else: print('enter valid choice!')

            mycursor.execute(q)
            mydb.commit()
            print('RECORD UPDATED\n')

    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()
        

def deletebooks():
    try:
        print('\nDELETE BOOK:-\t')        
        while True:
            bookid = int(input('enter book ID to be deleted:\t'))
            mycursor.execute('select * from bookcatalog where book_id = {}'.format(bookid))
            row = mycursor.fetchone()
            if not row:
                print('please enter a valid book ID')
                continue
            q = 'delete from bookcatalog where book_id={}'.format(bookid)
            mycursor.execute(q)
            mydb.commit()
            print('RECORD DELETED\n')
            break

    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()
        

def searchbooks():
    print('\nSEARCH BOOK DETAILS:-')
    bookid = int(input('enter book ID to search:\t'))
    q = 'select * from bookcatalog where book_id = {}'.format(bookid)
    mycursor.execute(q)
    data = mycursor.fetchall()
    if data:
        print('RECORD FOUND:')
        Y = PrettyTable()
        Y.field_names = [i[0] for i in mycursor.description]
        Y.add_rows(data)
        print(Y)
    else: print('RECORD NOT FOUND\n')


def showbooks():
    Y = PrettyTable()
    mycursor.execute('select * from bookcatalog')
    Y = from_db_cursor(mycursor)
    print("\nBOOK CATALOG:\n")
    print(Y)
