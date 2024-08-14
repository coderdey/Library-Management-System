#main
import basetables
import tmembers as members
import tstaffrecord as staff
import tbookcatalog as books
import tissuedbooks as issued
import twishlist as wishlist
import treviews as reviews

import datetime
import pyfiglet
from prettytable import PrettyTable, from_db_cursor
import mysql.connector as m
mydb=m.connect(host='localhost', user='root', passwd='pass123', database='library', auth_plugin='mysql_native_password')
mycursor=mydb.cursor()

def memberstable() :
    while True :
        print('''\n=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu''')
        ch = int(input('enter choice:\t'))
        if ch==1 :
            members.showmembers()
        elif ch==2 :
            members.searchmembers()
        elif ch==3 :
            members.insertmembers()
        elif ch==4 :
            members.updatemembers()
        elif ch==5 :
            members.deletemembers()
        elif ch==6 :
            break
        else :
            print('\nPLEASE ENTER VALID CHOICE!')


def stafftable() :
    while True :
        print('''\n=====================================
       LIBRARY STAFF DETAILS         
=====================================
1. display staff member details
2. search for staff member details
3. insert staff member details
4. update staff member details
5. delete staff member details
6. return to previous menu''')
        ch = int(input('enter choice:\t'))
        if ch==1 :
            staff.showstaff()
        elif ch==2 :
            staff.searchstaff()
        elif ch==3 :
            staff.insertstaff()
        elif ch==4 :
            staff.updatestaff()
        elif ch==5 :
            staff.deletestaff()
        elif ch==6 :
            break
        else :
            print('Please enter valid choice!')


def bookstable() :
    while True :
        print('''\n=====================================
        LIBRARY BOOKS CATALOG         
=====================================
1. display book details
2. search for book details
3. insert new book
4. update book details
5. delete book details
6. return to previous menu''')
        ch = int(input('enter choice:\t'))
        if ch==1 :
            books.showbooks()
        elif ch==2 :
            books.searchbooks()
        elif ch==3 :
            books.insertbooks()
        elif ch==4 :
            books.updatebooks()
        elif ch==5 :
            books.deletebooks()
        elif ch==6 :
            break
        else :
            print('\nPLEASE ENTER VALID CHOICE!')


def wishlistuser(userid) :
    while True :
        print('''\n=====================================
        USER WISHLIST DETAILS         
=====================================
1. request a book
2. view your wishlist
3. search your wishlist
4. return to previous menu''')
        ch = int(input('enter choice:\t'))
        if ch==1:
            wishlist.insertbooks(userid)
        elif ch==2:
            wishlist.showwishlistuser(userid)
        elif ch==3:
            wishlist.searchwishlistuser(userid)
        elif ch==4:
            break
        else :
            print('\nPLEASE ENTER VALID CHOICE!')


def wishlistadmin() :
    while True :
        print('''\n=====================================
           WISHLIST DETAILS          
=====================================
1. request a book
2. view wishlist
3. search your wishlist
4. update wishlist book details
5. return to previous menu''')
        ch = int(input('enter choice:\t'))
        if ch==1:
            userid=int(input('enter member id:\t'))
            wishlist.insertbooks(userid)
        elif ch==2:
            wishlist.showwishlistadmin()
        elif ch==3:
            wishlist.searchwishlistadmin()
        elif ch==4:
            wishlist.updatewishlist()
        elif ch==5:
            break
        else :
            print('\nPLEASE ENTER VALID CHOICE!')


def issuedadmin():
    while True :
        print('''\n=====================================
         ISSUED BOOKS DETAILS        
=====================================
1. issue a book
2. return a book
3. show issued books
4. view issued history
5. search issued books
6. return to previous menu''')
        ch=int(input('enter choice:\t'))
        if ch==1:
            issued.insertbooks()
        elif ch==2:
            issued.deletebooks()
        elif ch==3:
            issued.showissuedbooks()
        elif ch==4:
            issued.showissuedhistoryadmin()
        elif ch==5:
            issued.searchbooks()
        elif ch==6:
            break
        else:
            print('\nPLEASE ENTER VALID CHOICE!')


def reviewsuser(userid):
    while True :
        print('''\n=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. write book review
2. update book reviews
3. search reviews
4. view book reviews
5. delete book review
6. return to previous menu''')
        ch=int(input('enter choice:\t'))
        if ch==1:
            show=input('would you like to see the books available in library before writing a review (y/n):\t')
            if show.lower()=='y':
                books.showbooks()
                reviews.insertreview(userid)
            else: reviews.insertreview(userid)            
        elif ch==2:
            reviews.updatereview(userid)
        elif ch==3:
            reviews.searchreviewuser(userid)
        elif ch==4:
            reviews.showreviewuser(userid)
        elif ch==5:
            reviews.deletereview(userid)
        elif ch==6:
            break
        else:
            print('\nPLEASE ENTER VALID CHOICE!')


def reviewsadmin():
    while True :
        print('''\n=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. view book reviews
2. search reviews
3. update book reviews
4. delete book review
5. return to previous menu''')
        ch=int(input('enter choice:\t'))
        if ch==1:
            reviews.showreviewadmin()            
        elif ch==2:
            reviews.searchreviewadmin()
        elif ch==3:
            userid=int(input('enter user id:\t'))
            q = 'select * from reviews where user_id = "{}"'.format(userid)
            mycursor.execute(q)
            data = mycursor.fetchall()
            if not data:
                print('no reviews found under this user')
                continue
            reviews.updatereview(userid)
        elif ch==4:
            userid=int(input('enter user id to delete their review:\t'))
            reviews.deletereview(userid)
        elif ch==5:
            break
        else:
            print('\nPLEASE ENTER VALID CHOICE!')


def manageaccount(userid):
    while True :
        print('''\n=====================================
       LIBRARY ACCOUNT DETAILS       
=====================================
1. view account
2. insert account details
3. update account details
4. delete account
5. return to previous menu''')
        ch = int(input('enter choice:\t'))
        if ch==1 :
            members.showaccount(userid)
        elif ch==2 :
            members.insertaccount(userid)
        elif ch==3:
            members.updatemembers()
        elif ch==4 :
            members.deleteaccount(userid)
        elif ch==5 :
            break
        else :
            print('\nPLEASE ENTER VALID CHOICE!')
    


def mainadmin() :
    while True :
        print('''\n=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT''')
        ch=int(input('enter choice:\t'))
        if ch==1:
            memberstable()
        elif ch==2:
            stafftable()
        elif ch==3:
            bookstable()
        elif ch==4:
            issuedadmin()
        elif ch==5:
            wishlistadmin()
        elif ch==6:
            reviewsadmin()
        elif ch==7:
            break
        else:
            print('\nPLEASE ENTER VALID CHOICE!')


def mainuser(userid):
    while True:
        print('''\n=====================================
          CHOOSE A FIELD:       
=====================================
1. ISSUE BOOKS
2. RETURN BOOKS
3. ISSUED BOOKS HISTORY
4. WISHLIST
5. BOOK REVIEWS
6. ACCOUNT
7. EXIT''')
        ch=int(input('enter choice:\t'))
        if ch==1:
            show=input('would you like to see the books available in library (y/n):\t')
            if show.lower()=='y':
                issued.showbookcatalog()
                issued.insertbooks()
            else: issued.insertbooks()
        elif ch==2:
            issued.deletebooks()
        elif ch==3:
            issued.showissuedhistoryuser(userid)
        elif ch==4:
            wishlistuser(userid)
        elif ch==5:
            reviewsuser(userid)
        elif ch==6:
            manageaccount(userid)
        elif ch==7:
            print('THANK YOU')
            break
        else:
            print('\nPLEASE ENTER VALID CHOICE!')        
                        

#MAIN PROGRAM
print('⭐'*30)
ascii_text = pyfiglet.figlet_format("WELCOME  TO", font="small")
print(ascii_text)
ascii_text = pyfiglet.figlet_format("OAKS  &  DEY's !", font="small")
print(ascii_text)
print('⭐'*30)
while True:
    print()
    print('='*25)
    print('MENU')
    print('1. ADMINISTRATION')
    print('2. USER SIGN-IN')
    print('3. USER REGISTERATION')
    print('4. EXIT')
    print('='*25)
    print()
    ch=int(input('enter choice:\t'))
    if ch==1 :
        username=input('enter admin username:\t')
        password=input('enter admin password:\t')
        if username=='admin' and password=='DEYLIB18' :
            print('ACCESS PERMITTED!')
            mainadmin()
        else :
            print('ACCESS DENIED!')

    elif ch==2 :
        user=input('enter username:\t')
        pw=input('enter password:\t')
        mycursor.execute('select * from members where username="{}"'.format(user))
        row1=mycursor.fetchone()
        if row1[3]==pw :
            print('successful sign-in')
            userid=row1[0]
            print('user id:\t', userid)
            mainuser(userid)    
        else :
            print('incorrect username/password')

    elif ch==3 :
        user=input('enter username to register:\t')
        mycursor.execute('select * from members where username = "{}"'.format(user))
        row2 = mycursor.fetchone()
        if row2:
            print('username exists, choose another username or try signing in')
            continue
        else:
            pw=input('enter password:\t')
            currentdate = datetime.date.today()
            mycursor.execute('insert into members(username, password, members_since) values ("{}", "{}", "{}")'.format(user,pw,currentdate))
            mydb.commit()
            print('you are now a library member')
            mycursor.execute('select * from members where username="{}"'.format(user))
            row2=mycursor.fetchall()
            userid=row2[0][0]
            print('new user id created:\t', userid)

    elif ch==4 :
        mydb.close()
        print('\n✿ THANK YOU ✿\n')
        print('COME AGAIN TO \n🎄🎄 OAKS & DEY\'s 🎄🎄 \nWE AWAIT YOUR NEXT ENTRY!\n')
        break
    
    else :
        print('\nPLEASE ENTER VALID CHOICE!')
