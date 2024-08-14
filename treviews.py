#reviews table - fix display review
import datetime
import mysql.connector as m
from prettytable import PrettyTable, from_db_cursor
mydb=m.connect(host='localhost', user='root', passwd='pass123', database='library', auth_plugin='mysql_native_password')
mycursor=mydb.cursor()

'''create table if not exists reviews(
                   sno int auto_increment not null primary key,
                   user_id int,
                   title varchar(300),
                   rating int,
                   review varchar(800),
                   review_date date
                   )'''

#for user to write a review
def insertreview(userid):
    print('\nWRITE A BOOK REVIEW:-')
    try:
        while True:
            title=input('enter book title:\t')
            mycursor.execute('select * from bookcatalog where title = "{}"'.format(title))
            row1 = mycursor.fetchone()
            if not row1:
                print('book does not exist in library, please enter a valid title')
                continue
            rating=int(input('enter rating (out of 5):\t'))
            review=input('enter a short review (max 150 words):\t')
            currentdate = datetime.date.today()
            q = 'insert into reviews (user_id, title, rating, review, review_date) values ({}, "{}", {}, "{}", "{}")'.format(userid, title, rating, review, currentdate)
            mycursor.execute(q)
            mydb.commit()
            print('BOOK REVIEW ADDED\n')
            break

    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()


#for admin/user to update book reviews
def updatereview(userid):
    try:
        while True:
            title=input('enter book title:\t')
            print('''\nUPDATE REVIEW:-
1. update rating
2. update review
3. exit''')
            cho=int(input('enter choice:\t'))
        
            if cho==1:
                mycursor.execute('select * from reviews where title = "{}"'.format(title))
                row1 = mycursor.fetchone()
                if not row1:
                    print('book review does not exist, please enter valid book title')
                    continue
                newrate=input('enter rating (out of 5):\t')
                q='update reviews set rating={} where title="{}" and user_id = "{}"'.format(newrate, title, userid)

            elif cho==2:
                mycursor.execute('select * from reviews where title = "{}"'.format(title))
                row2 = mycursor.fetchone()
                if not row2:
                    print('book review does not exist, please enter valid book title')
                    continue
                newrev=input('enter new short review (max 150 words):\t')
                q='update reviews set review="{}" where title="{}" and user_id = "{}"'.format(newrev, title, userid)

            elif cho==3: break
            else: print('enter valid choice!')
            
            mycursor.execute(q)
            mydb.commit()
            print('RECORD UPDATED\n')
            
    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()
        

#for user to search their reviews
def searchreviewuser(userid):
    print('\nSEARCH YOUR REVIEWS:-')
    title = input('enter title to search:\t')
    q = 'select * from reviews where title = "{}" and user_id = "{}"'.format(title, userid)
    mycursor.execute(q)
    data = mycursor.fetchall()
    if data:
        print('RECORD FOUND:')
        for i in data:
            print('SNO:\t',i[0])
            print('USER ID:\t',i[1])
            print('TITLE:\t',i[2])
            print('RATING:\t',i[3])
            print('REVIEW:\n',i[4])
            print('REVIEW DATE:\t',i[5])
            print()
    else: print('RECORD NOT FOUND\n')


#for user to see their review = USER SPECIFIC
def showreviewuser(userid):
    Y = PrettyTable()
    mycursor.execute('select * from reviews where user_id = "{}"'.format(userid))
    data=mycursor.fetchall()
    print("\nYOUR BOOK REVIEWS:\n")
    if data:
        for i in data:
            print('SNO:\t',i[0])
            print('USER ID:\t',i[1])
            print('TITLE:\t',i[2])
            print('RATING:\t',i[3])
            print('REVIEW:\n',i[4])
            print('REVIEW DATE:\t',i[5])
            print()
    else: print('NIL\n')


#for admin/user to delete their book review
def deletereview(userid):
    try:
        print('\nDELETE REVIEW:-\t') 
        while True:
            title = input('enter title to search:\t')
            mycursor.execute('select * from reviews where title = "{}" and user_id = "{}"'.format(title, userid))
            row = mycursor.fetchone()
            if not row:
                print('NO REVIEWS FOUND\n')
                break
            else:
                q = 'delete from reviews where title = "{}" and user_id = "{}"'.format(title, userid)
                mycursor.execute(q)
                mydb.commit()
                print('REVIEW DELETED\n')
                
    except Exception as e:
        print('an error occurred: "{}"\n'.format(e))
        mydb.rollback()
    

#for admin/user to view ALL reviews
def showreviewadmin():
    Y = PrettyTable()
    mycursor.execute('select * from reviews')
    data=mycursor.fetchall()
    print("\nBOOK REVIEWS:\n")
    if data:
        for i in data:
            print('SNO:\t',i[0])
            print('USER ID:\t',i[1])
            print('TITLE:\t',i[2])
            print('RATING:\t',i[3])
            print('REVIEW:\n',i[4])
            print('REVIEW DATE:\t',i[5])
            print()
    else: print('NIL\n')


#for admin to search for book reviews
def searchreviewadmin():
    print('\nSEARCH BOOK REVIEWS:-')
    title = input('enter title to search:\t')
    q = 'select * from reviews where title = "{}"'.format(title)
    mycursor.execute(q)
    data = mycursor.fetchall()
    if data:
        print('RECORD FOUND:')
        for i in data :
            print("SNO:\t",i[0])
            print("USER ID:\t",i[1])
            print("TITLE:\t",i[2])
            print("RATING:\t",i[3])
            print("REVIEW:\n",i[4])
            print("REVIEW DATE:\t",i[5])
            print()
    else: print('RECORD NOT FOUND\n')
