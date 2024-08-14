#table creation (static)

def membersval():
    mycursor.execute('insert into members values(110, "rachel zegler", "rachelz", "rach@123", "2000-11-9", "rachelz@gmail.com", 502328475, "2020-9-22", 17)')
    mycursor.execute('insert into members values(112, "liz sill", "lizsill", "liz@456", "2002-12-9", "lizzie@gmail.com", 554629857, "2021-4-2", 12)')
    mycursor.execute('insert into members values(113, "geeta harr", "geetah", "gee@789", "1999-1-19", "geegee@gmail.com", 506482837, "2020-4-23", 25)')
    mycursor.execute('insert into members values(114, "riya pritam", "riyap", "riya@987", "1977-6-30", "riripri@gmail.com", 558769876, "2017-10-14", 38)')
    mycursor.execute('insert into members values(115, "jayant singh", "jayants", "jay@654", "1994-2-26", "jayantsingh@gmail.com", 508761234, "2023-3-3", 9)')
    mycursor.execute('insert into members values(116, "shreya ghoshal", "shreyag", "shreya@321", "2001-7-31", "shreshreghosh@gmail.com", 509997654, "2023-11-12", 20)')
    mycursor.execute('insert into members values(117, "tina sharma", "tinash", "tina@111", "1990-5-15", "tinash@gmail.com", 508852387, "2015-8-7", 22)')
    mycursor.execute('insert into members values(118, "raj malhotra", "rajmal", "raj@222", "1985-8-22", "rajmal@gmail.com", 508763456, "2012-6-10", 29)')
    mydb.commit()


def booksval():
    mycursor.execute('insert into bookcatalog values(1, 123, "the fault in our stars", "john green", "romance", "2012-01-10", "issued", 16, "9780143567592")')
    mycursor.execute('insert into bookcatalog values(2, 456, "to kill a mockingbird", "harper lee", "fiction", "1960-07-11", "available", 5, "9780061120084")')
    mycursor.execute('insert into bookcatalog values(3, 789, "1984", "george orwell", "dystopian", "1949-06-08", "issued", 1, "9780140817744")')
    mycursor.execute('insert into bookcatalog values(4, 101, "the great gatsby", "f. scott fitzgerald", "classic", "1925-04-10", "available", 7, "9780333791035")')
    mycursor.execute('insert into bookcatalog values(5, 202, "pride and prejudice", "jane austen", "romance", "1813-01-28", "available", 10, "9780141439518")')
    mycursor.execute('insert into bookcatalog values(6, 303, "the catcher in the rye", "j.d. salinger", "coming of age", "1951-07-16", "available", 2, "9780241950432")')
    mycursor.execute('insert into bookcatalog values(7, 404, "harry potter and the sorcerer\'s stone", "j.k. rowling", "fantasy", "1997-06-26", "issued", 2, "9780439362139")')
    mycursor.execute('insert into bookcatalog values(8, 505, "the hunger games", "suzanne collins", "dystopian", "2008-09-14", "available", 1, "9780439023481")')
    mycursor.execute('insert into bookcatalog values(9, 606, "the alchemist", "paulo coelho", "fiction", "1988-01-01", "available", 1, "9780061122415")')
    mycursor.execute('insert into bookcatalog values(10, 707, "the shawshank redemption", "stephen king", "drama", "1982-11-04", "available", 2, "9780751514624")')
    mycursor.execute('insert into bookcatalog values(11, 808, "gone with the wind", "margaret mitchell", "historical fiction", "1936-06-30", "available", 1, "9780582418059")')
    mycursor.execute('insert into bookcatalog values(12, 909, "one hundred years of solitude", "gabriel garcia marquez", "magical realism", "1967-05-30", "available", 1, "9780060114183")')
    mycursor.execute('insert into bookcatalog values(13, 1010, "the lord of the rings", "j.r.r. tolkien", "fantasy", "1954-07-29", "available", 7, "9788845292613")')
    mycursor.execute('insert into bookcatalog values(14, 1111, "the da vinci code", "dan brown", "mystery", "2003-03-18", "available", 2, "9780307474278")')
    mycursor.execute('insert into bookcatalog values(15, 1212, "the count of monte cristo", "alexandre dumas", "adventure", "1844-08-28", "available", 1, "9780199219650")')
    mycursor.execute('insert into bookcatalog values(16, 1313, "brave new world", "aldous huxley", "dystopian", "1932-02-02", "available", 1, "9780582060166")')
    mycursor.execute('insert into bookcatalog values(17, 1414, "the picture of dorian gray", "oscar wilde", "gothic fiction", "1890-07-20", "available", 2, "9789875503229")')
    mycursor.execute('insert into bookcatalog values(18, 1515, "the jungle book", "rudyard kipling", "children\'s literature", "1894-11-25", "issued", 23, "9780194227469")')
    mycursor.execute('insert into bookcatalog values(19, 1616, "a tale of two cities", "charles dickens", "historical fiction", "1859-04-30", "available", 2, "9780582030473")')
    mycursor.execute('insert into bookcatalog values(20, 1717, "the hobbit", "j.r.r. tolkien", "fantasy", "1937-09-21", "available", 1, "9780007525508")')
    mydb.commit()


def issuedval():
    mycursor.execute('''
            insert into issuedbooks (user_id, book_id, book_name, ISBN, issued_date)
            select {}, {}, bc.title, bc.ISBN, "{}"
            from bookcatalog bc
            where bc.book_id = {}
            '''.format(117, 123, '2021-03-15', 123))
    mycursor.execute('''
            insert into issuedbooks (user_id, book_id, book_name, ISBN, issued_date)
            select {}, {}, bc.title, bc.ISBN, "{}"
            from bookcatalog bc
            where bc.book_id = {}
            '''.format(116, 789, '2021-05-20', 789))
    mycursor.execute('''
            insert into issuedbooks (user_id, book_id, book_name, ISBN, issued_date)
            select {}, {}, bc.title, bc.ISBN, "{}"
            from bookcatalog bc
            where bc.book_id = {}
            '''.format(110, 404, '2022-01-10', 404))
    mycursor.execute('''
            insert into issuedbooks (user_id, book_id, book_name, ISBN, issued_date)
            select {}, {}, bc.title, bc.ISBN, "{}"
            from bookcatalog bc
            where bc.book_id = {}
            '''.format(112, 1515, '2021-08-05', 1515))
    mydb.commit()


def issuedhistoryval():
    mycursor.execute('insert into issuedhistory select * from issuedbooks')
    mydb.commit()


def staffval():
    mycursor.execute('insert into staffrecord (staff_id, staff_name, dob, mail_id, phone_num, salary, working_hours) values(301, "raj malhotra", "1990-08-22", "rajmal@gmail.com", 508763456, 5000.00, "10 am - 6 pm")')
    mycursor.execute('insert into staffrecord (staff_id, staff_name, dob, mail_id, phone_num, salary, working_hours) values(302, "arjun verma", "1995-04-15", "arjunverma@gmail.com", 554629857, 5500.00, "9 am - 5 pm")')
    mycursor.execute('insert into staffrecord (staff_id, staff_name, dob, mail_id, phone_num, salary, working_hours) values(303, "neha sharma", "1988-11-19", "nehash@gmail.com", 506482837, 6000.00, "11 am - 7 pm")')
    mycursor.execute('insert into staffrecord (staff_id, staff_name, dob, mail_id, phone_num, salary, working_hours) values(304, "ananya singh", "1983-06-30", "ananyasingh@gmail.com", 558769876, 7000.00, "8 am - 4 pm")')
    mycursor.execute('insert into staffrecord (staff_id, staff_name, dob, mail_id, phone_num, salary, working_hours) values(305, "mohit patel", "1994-02-26", "mohitpatel@gmail.com", 509997654, 6000.00, "10 am - 6 pm")')
    mycursor.execute('insert into staffrecord (staff_id, staff_name, dob, mail_id, phone_num, salary, working_hours) values(306, "kavya gupta", "1985-07-31", "kavyag@gmail.com", 508852387, 5500.00, "9 am - 5 pm")')
    mydb.commit()


def wishlistval():
    mycursor.execute('insert into wishlist (user_id, title, ISBN, author_name, genre, status) values(121, "the fault in our stars", "9780143567592", "john green", "romance", "purchased")')
    mycursor.execute('insert into wishlist (user_id, title, ISBN, author_name, genre, status) values(2, "to kill a mockingbird", "9780061120084", "harper lee", "fiction", "purchased")')
    mycursor.execute('insert into wishlist (user_id, title, ISBN, author_name, genre, status) values(92, "all the bright places", "9780385755887", "jennifer niven", "young adult fiction", "pending")')
    mycursor.execute('insert into wishlist (user_id, title, ISBN, author_name, genre, status) values(4, "the book thief", "9781101934180", "markus zusak", "historical fiction", "pending")')
    mydb.commit()


def reviewsval():
    mycursor.execute('insert into reviews values(1, 114, "the fault in our stars", 4, "a heartwarming journey through the pains of love and loss, leaving a lasting impact on the soul. a must-read for those seeking a profound emotional experience.", "2021-09-10")')
    mycursor.execute('insert into reviews values(2, 116, "all the bright places", 4, "an emotionally charged narrative that delves deep into the human psyche, providing a raw and authentic portrayal of mental health struggles. a poignant and thought-provoking read.", "2023-03-14")')
    mycursor.execute('insert into reviews values(3, 110, "the jungle book", 3, "a nostalgic adventure that transports readers to the enchanting world of mowgli and his animal companions. filled with wonder and imagination, it\'s a tale that captivates readers of all ages.", "2022-05-18")')
    mydb.commit()


try:
    import mysql.connector as m
    mydb=m.connect(host='localhost', user='root', passwd='pass123', auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()

    #if mydb.is_connected(): print('successful connection')
    #else: print('unsuccessful connection')
        
    mycursor.execute('create database if not exists library')
    mycursor.execute('use library')


    #members = details about library users who have membership
    mycursor.execute('''create table if not exists members(
                         user_id int auto_increment not null primary key,
                         name varchar(200),
                         username varchar(20),
                         password varchar(20),
                         dob date,
                         mail_id varchar(50),
                         phone_num bigint unique,
                         members_since date,
                         books_issued int
                         )''')


    #staffrecord = details about library staff members
    mycursor.execute('''create table if not exists staffrecord(
                         staff_id int auto_increment not null primary key,
                         staff_name varchar(100),
                         dob date,
                         mail_id varchar(50),
                         phone_num bigint unique,
                         salary float,
                         working_hours varchar(30)
                         )''')


    #bookcatalog = details about books available at library - only shows 20
    mycursor.execute('''create table if not exists bookcatalog(
                         sno int auto_increment not null primary key,
                         book_id int not null unique,
                         title varchar(200),
                         author_name varchar(100),
                         genre varchar(50),
                         publication_date date,
                         availability varchar(30),
                         frequency int default 1,
                         ISBN varchar(14) not null unique,
                         index bookindex (title, ISBN)
                         )''')


    #issuedbooks = details about which book has been issued by which user
    mycursor.execute('''create table if not exists issuedbooks(
                         user_id int not null,
                         book_id int,
                         book_name varchar(200),
                         ISBN varchar(14) not null,
                         issued_date date,
                         foreign key (book_name, ISBN) references bookcatalog(title, ISBN)
                         )''')


    #issuedhistory = copy of issuedbooks but stores all deleted records too
    mycursor.execute('''create table if not exists issuedhistory(
                         user_id int not null,
                         book_id int,
                         book_name varchar(200),
                         ISBN varchar(14) not null,
                         issued_date date,
                         foreign key (book_name, ISBN) references bookcatalog(title, ISBN)
                         )''')


    #wishlist = books that different users want
    mycursor.execute('''create table if not exists wishlist(
                     sno int auto_increment not null primary key,
                     user_id int not null,
                     title varchar(200),
                     ISBN varchar(14) not null unique,
                     author_name varchar(100),                 
                     genre varchar(50),
                     status varchar(30) default 'pending'
                     )''')


    #reviews = by users
    mycursor.execute('''create table if not exists reviews(
                       sno int auto_increment not null primary key,
                       user_id int,
                       title varchar(300),
                       rating int,
                       review varchar(800),
                       review_date date
                       )''')


    mydb.commit()


except m.Error as e:
    print('an error occurred: "{}"\n'.format(e))
    mydb.rollback()
