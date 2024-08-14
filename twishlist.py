#wishlist table
import mysql.connector as m
from prettytable import PrettyTable, from_db_cursor
mydb=m.connect(host='localhost', user='root', passwd='pass123', database='library', auth_plugin='mysql_native_password')
mycursor=mydb.cursor()

'''create table if not exists wishlist(
                 sno int auto_increment not null primary key,
                 user_id int not null,
                 title varchar(200),
                 ISBN varchar(14) not null unique,
                 author_name varchar(100),                 
                 genre varchar(50),
                 status varchar(30) default 'pending'
                 )'''

#for admin/user to request a book
def insertbooks(userid):
    print('\nREQUEST A BOOK:-')    
    try:
        title=input('enter book title:\t')
        isbn=input('enter ISBN:\t')
        author=input('enter author name:\t')
        genre=input('enter genre:\t')            
        q = 'insert into wishlist (user_id, title, ISBN, author_name, genre) values ({}, "{}", {}, "{}", "{}")'.format(userid, title, isbn, author, genre)
        mycursor.execute(q)
        mydb.commit()
        print('BOOK REQUESTED\n')

    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()
        

#for admin to view ALL wishlist books
def showwishlistadmin():
    Y = PrettyTable()
    mycursor.execute('select * from wishlist')
    Y = from_db_cursor(mycursor)
    print("\nWISHLIST:\n")
    print(Y)
    

#for admin to search for wishlist books
def searchwishlistadmin():
    print('\nSEARCH WISHLIST BOOK DETAILS:-')
    title = input('enter title to search:\t')
    q = 'select * from wishlist where title = "{}"'.format(title)
    mycursor.execute(q)
    data = mycursor.fetchall()
    if data:
        print('RECORD FOUND:')
        Y = PrettyTable()
        Y.field_names = [i[0] for i in mycursor.description]
        Y.add_rows(data)
        print(Y)
    else: print('RECORD NOT FOUND\n')


#for admin to update details of wishlist book
def updatewishlist():
    try:
        while True:
            print('''\nUPDATE WISHLIST:-
1. update ISBN
2. update status
3. exit''')
            cho=int(input('enter choice:\t'))
        
            if cho==1:
                title=input('enter book title:\t')
                mycursor.execute('select * from wishlist where title = "{}"'.format(title))
                row1 = mycursor.fetchone()
                if not row1:
                    print('book does not exist, please enter a valid title')
                    continue
                newisbn=input('enter new ISBN:\t')
                q='update wishlist set ISBN="{}" where title="{}"'.format(newisbn, title)
                
            elif cho==2:
                isbn=input('enter ISBN:\t')
                mycursor.execute('select * from wishlist where ISBN = {}'.format(isbn))
                row2 = mycursor.fetchone()
                if not row2:
                    print('book ISBN does not exist, please enter a valid ID')
                    continue
                newstat=input('enter status (pending/purchased):\t')
                q='update wishlist set status="{}" where ISBN="{}"'.format(newstat, isbn)

            elif cho==3: break
            else: print('enter valid choice!')
            
            mycursor.execute(q)
            mydb.commit()
            print('RECORD UPDATED\n')
        
    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()

        
#for user to search in their wishlist
def searchwishlistuser(userid):
    print('\nSEARCH WISHLIST BOOK DETAILS:-')
    title = input('enter title to search:\t')
    q = 'select * from wishlist where title = "{}" and user_id = {}'.format(title, userid)
    mycursor.execute(q)
    data = mycursor.fetchall()
    if data:
        print('RECORD FOUND:')
        Y = PrettyTable()
        Y.field_names = [i[0] for i in mycursor.description]
        Y.add_rows(data)
        print(Y)
    else: print('RECORD NOT FOUND\n')


#for user to see what book they have requested = USER SPECIFIC
def showwishlistuser(userid):
    Y = PrettyTable()
    mycursor.execute('select * from wishlist where user_id = "{}"'.format(userid))
    Y = from_db_cursor(mycursor)
    print("\nYOUR WISHLIST BOOKS:\n")
    print(Y)
