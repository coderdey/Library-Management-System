Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: D:\g12\cs\sql stuff\MAIN.py
success
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
__      _____ _    ___ ___  __  __ ___    _____ ___  
\ \    / / __| |  / __/ _ \|  \/  | __|  |_   _/ _ \ 
 \ \/\/ /| _|| |_| (_| (_) | |\/| | _|     | || (_) |
  \_/\_/ |___|____\___\___/|_|  |_|___|    |_| \___/ 
                                                     

  ___   _   _  __     _   _  _ ___     ___  _____   ___ ___   _ 
 / _ \ /_\ | |/ /    /_\ | \| |   \   |   \| __\ \ / ( ) __| | |
| (_) / _ \| ' <    / _ \| .` | |) |  | |) | _| \ V /|/\__ \ |_|
 \___/_/ \_\_|\_\  /_/ \_\_|\_|___/   |___/|___| |_|   |___/ (_)
                                                                

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	1
enter admin username:	ADMIN
enter admin password:	123
ACCESS DENIED!

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	1
enter admin username:	admin
enter admin password:	DEYLIB18
ACCESS PERMITTED!

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	1

=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	3

ADD NEW MEMBER:-
enter new members name:	jojo siwa
enter date of birth (yyyy-mm-dd):	2000-1-1
enter email ID:	jojo@gmail.com
enter phone num (971...):	508181818
enter date (members since) (yyyy-mm-dd):	2023-1-1
enter no. of books issued:	18
MEMBER ADDED


=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	1

MEMBERS DETAILS:

+---------+----------------+----------+------------+------------+-------------------------+--------------+---------------+--------------+
| user_id |      name      | username |  password  |    dob     |         mail_id         |  phone_num   | members_since | books_issued |
+---------+----------------+----------+------------+------------+-------------------------+--------------+---------------+--------------+
|   110   | rachel zegler  | rachelz  |  rach@123  | 2000-11-09 |   rachelzeze@gmail.com  |  502328475   |   2020-09-22  |      17      |
|   112   |    liz sill    | lizsill  |  liz@456   | 2002-12-09 |     lizzie@gmail.com    |  554629857   |   2021-04-02  |      12      |
|   113   |   geeta harr   |  geetah  |  gee@789   | 1999-01-19 |     geegee@gmail.com    |  506482837   |   2020-04-23  |      28      |
|   114   |  riya pritam   |  riyap   |  riya@987  | 1977-06-30 |    riripri@gmail.com    |  558769876   |   2017-10-14  |      38      |
|   115   |  jayant singh  | jayants  |  jay@654   | 1994-02-26 |  jayantsingh@gmail.com  |  508761234   |   2023-03-03  |      9       |
|   116   | shreya ghoshal | shreyag  | shreya@321 | 2001-07-31 | shreshreghosh@gmail.com |  509997654   |   2023-11-12  |      20      |
|   117   |  tina sharma   |  tinash  |  tina@111  | 1990-05-15 |     tinash@gmail.com    |  508852387   |   2015-08-07  |      22      |
|   119   |   adi singh    | adisingh |   adi123   | 2000-08-12 |     adiadi@gmail.com    |     None     |   2023-11-30  |     None     |
|   120   |  rahul khanna  |   None   |    None    | 1999-09-12 |   rahulkhan@gmail.com   | 971558838432 |   2020-07-01  |      3       |
|   121   |    sha boom    |   None   |    None    | 2000-08-08 |    shaboom@gmail.com    | 971508273828 |   2023-09-09  |      8       |
|   124   |   jojo siwa    |   None   |    None    | 2000-01-01 |      jojo@gmail.com     |  508181818   |   2023-01-01  |      18      |
+---------+----------------+----------+------------+------------+-------------------------+--------------+---------------+--------------+

=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	4
enter user id:	121

UPDATE MEMBERS TABLE:-
1. update mailid
2. update phone num
3. update books issued
4. exit
enter choice:	4

=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	5

DELETE MEMBER:-	
enter user ID to be deleted:	120
RECORD DELETED


=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	5

DELETE MEMBER:-	
enter user ID to be deleted:	121
RECORD DELETED


=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	5

DELETE MEMBER:-	
enter user ID to be deleted:	122
user ID does not exist, please enter a valid ID
enter user ID to be deleted:	124
RECORD DELETED


=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	6

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	7

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	4

✿ THANK YOU ✿

COME AGAIN TO 
🎄🎄 OAK AND DEY'S 🎄🎄 
WE AWAIT YOUR NEXT ENTRY!


====================================== RESTART: D:\g12\cs\sql stuff\MAIN.py ======================================
success
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
__      _____ _    ___ ___  __  __ ___    _____ ___  
\ \    / / __| |  / __/ _ \|  \/  | __|  |_   _/ _ \ 
 \ \/\/ /| _|| |_| (_| (_) | |\/| | _|     | || (_) |
  \_/\_/ |___|____\___\___/|_|  |_|___|    |_| \___/ 
                                                     

  ___   _   _  __   __        ___  _____   ___ ___   _ 
 / _ \ /_\ | |/ /  / _|___   |   \| __\ \ / ( ) __| | |
| (_) / _ \| ' <   > _|_ _|  | |) | _| \ V /|/\__ \ |_|
 \___/_/ \_\_|\_\  \_____|   |___/|___| |_|   |___/ (_)
                                                       

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	
====================================== RESTART: D:\g12\cs\sql stuff\MAIN.py ======================================
success
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
__      _____ _    ___ ___  __  __ ___    _____ ___  
\ \    / / __| |  / __/ _ \|  \/  | __|  |_   _/ _ \ 
 \ \/\/ /| _|| |_| (_| (_) | |\/| | _|     | || (_) |
  \_/\_/ |___|____\___\___/|_|  |_|___|    |_| \___/ 
                                                     

  ___   _   _  __       __        ___  _____   ___ ___   _ 
 / _ \ /_\ | |/ / ___  / _|___   |   \| __\ \ / ( ) __| | |
| (_) / _ \| ' < (_-<  > _|_ _|  | |) | _| \ V /|/\__ \ |_|
 \___/_/ \_\_|\_\/__/  \_____|   |___/|___| |_|   |___/ (_)
                                                           

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	
====================================== RESTART: D:\g12\cs\sql stuff\MAIN.py ======================================
success
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
__      _____ _    ___ ___  __  __ ___    _____ ___  
\ \    / / __| |  / __/ _ \|  \/  | __|  |_   _/ _ \ 
 \ \/\/ /| _|| |_| (_| (_) | |\/| | _|     | || (_) |
  \_/\_/ |___|____\___\___/|_|  |_|___|    |_| \___/ 
                                                     

  ___   _   _  _____    __        ___  _____   ___      _ 
 / _ \ /_\ | |/ / __|  / _|___   |   \| __\ \ / ( )___ | |
| (_) / _ \| ' <\__ \  > _|_ _|  | |) | _| \ V /|/(_-< |_|
 \___/_/ \_\_|\_\___/  \_____|   |___/|___| |_|   /__/ (_)
                                                          

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	1
enter admin username:	
====================================== RESTART: D:\g12\cs\sql stuff\MAIN.py ======================================
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
__      _____ _    ___ ___  __  __ ___    _____ ___  
\ \    / / __| |  / __/ _ \|  \/  | __|  |_   _/ _ \ 
 \ \/\/ /| _|| |_| (_| (_) | |\/| | _|     | || (_) |
  \_/\_/ |___|____\___\___/|_|  |_|___|    |_| \___/ 
                                                     

  ___   _   _  _____    __        ___  _____   ___      _ 
 / _ \ /_\ | |/ / __|  / _|___   |   \| __\ \ / ( )___ | |
| (_) / _ \| ' <\__ \  > _|_ _|  | |) | _| \ V /|/(_-< |_|
 \___/_/ \_\_|\_\___/  \_____|   |___/|___| |_|   /__/ (_)
                                                          

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	
====================================== RESTART: D:\g12\cs\sql stuff\MAIN.py ======================================
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
__      _____ _    ___ ___  __  __ ___    _____ ___  
\ \    / / __| |  / __/ _ \|  \/  | __|  |_   _/ _ \ 
 \ \/\/ /| _|| |_| (_| (_) | |\/| | _|     | || (_) |
  \_/\_/ |___|____\___\___/|_|  |_|___|    |_| \___/ 
                                                     

  ___   _   _  _____    __        ___  _____   ___      _ 
 / _ \ /_\ | |/ / __|  / _|___   |   \| __\ \ / ( )___ | |
| (_) / _ \| ' <\__ \  > _|_ _|  | |) | _| \ V /|/(_-< |_|
 \___/_/ \_\_|\_\___/  \_____|   |___/|___| |_|   /__/ (_)
                                                          

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	1
enter admin username:	admin
enter admin password:	admin
ACCESS DENIED!

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	1
enter admin username:	admin
enter admin password:	DEYLIB18
ACCESS PERMITTED!

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	1

=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	1

MEMBERS DETAILS:

+---------+----------------+----------+------------+------------+-------------------------+-----------+---------------+--------------+
| user_id |      name      | username |  password  |    dob     |         mail_id         | phone_num | members_since | books_issued |
+---------+----------------+----------+------------+------------+-------------------------+-----------+---------------+--------------+
|   110   | rachel zegler  | rachelz  |  rach@123  | 2000-11-09 |   rachelzeze@gmail.com  | 502328475 |   2020-09-22  |      17      |
|   112   |    liz sill    | lizsill  |  liz@456   | 2002-12-09 |     lizzie@gmail.com    | 554629857 |   2021-04-02  |      12      |
|   113   |   geeta harr   |  geetah  |  gee@789   | 1999-01-19 |     geegee@gmail.com    | 506482837 |   2020-04-23  |      28      |
|   114   |  riya pritam   |  riyap   |  riya@987  | 1977-06-30 |    riripri@gmail.com    | 558769876 |   2017-10-14  |      38      |
|   115   |  jayant singh  | jayants  |  jay@654   | 1994-02-26 |  jayantsingh@gmail.com  | 508761234 |   2023-03-03  |      9       |
|   116   | shreya ghoshal | shreyag  | shreya@321 | 2001-07-31 | shreshreghosh@gmail.com | 509997654 |   2023-11-12  |      20      |
|   117   |  tina sharma   |  tinash  |  tina@111  | 1990-05-15 |     tinash@gmail.com    | 508852387 |   2015-08-07  |      22      |
|   119   |   adi singh    | adisingh |   adi123   | 2000-08-12 |     adiadi@gmail.com    |    None   |   2023-11-30  |     None     |
+---------+----------------+----------+------------+------------+-------------------------+-----------+---------------+--------------+

=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	3

ADD NEW MEMBER:-
enter new members name:	manna dey
create username:	mannadey
create password:	manman
enter date of birth (yyyy-mm-dd):	2000-1-1
enter email ID:	manman@gmail.com
enter phone num (971...):	506262626
enter date (members since) (yyyy-mm-dd):	2023-1-1
enter no. of books issued:	8
an error occurred: "1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'dob, mail_id, phone_num, members_since, books_issued) values ("manna dey", "mann' at line 1"


=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	
====================================== RESTART: D:\g12\cs\sql stuff\MAIN.py ======================================
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
__      _____ _    ___ ___  __  __ ___    _____ ___  
\ \    / / __| |  / __/ _ \|  \/  | __|  |_   _/ _ \ 
 \ \/\/ /| _|| |_| (_| (_) | |\/| | _|     | || (_) |
  \_/\_/ |___|____\___\___/|_|  |_|___|    |_| \___/ 
                                                     

  ___   _   _  _____    __        ___  _____   ___      _ 
 / _ \ /_\ | |/ / __|  / _|___   |   \| __\ \ / ( )___ | |
| (_) / _ \| ' <\__ \  > _|_ _|  | |) | _| \ V /|/(_-< |_|
 \___/_/ \_\_|\_\___/  \_____|   |___/|___| |_|   /__/ (_)
                                                          

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	1
enter admin username:	admin
enter admin password:	admin
ACCESS DENIED!

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	1
enter admin username:	admin
enter admin password:	DEYLIB18
ACCESS PERMITTED!

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	1

=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	1

MEMBERS DETAILS:

+---------+----------------+----------+------------+------------+-------------------------+-----------+---------------+--------------+
| user_id |      name      | username |  password  |    dob     |         mail_id         | phone_num | members_since | books_issued |
+---------+----------------+----------+------------+------------+-------------------------+-----------+---------------+--------------+
|   110   | rachel zegler  | rachelz  |  rach@123  | 2000-11-09 |   rachelzeze@gmail.com  | 502328475 |   2020-09-22  |      17      |
|   112   |    liz sill    | lizsill  |  liz@456   | 2002-12-09 |     lizzie@gmail.com    | 554629857 |   2021-04-02  |      12      |
|   113   |   geeta harr   |  geetah  |  gee@789   | 1999-01-19 |     geegee@gmail.com    | 506482837 |   2020-04-23  |      28      |
|   114   |  riya pritam   |  riyap   |  riya@987  | 1977-06-30 |    riripri@gmail.com    | 558769876 |   2017-10-14  |      38      |
|   115   |  jayant singh  | jayants  |  jay@654   | 1994-02-26 |  jayantsingh@gmail.com  | 508761234 |   2023-03-03  |      9       |
|   116   | shreya ghoshal | shreyag  | shreya@321 | 2001-07-31 | shreshreghosh@gmail.com | 509997654 |   2023-11-12  |      20      |
|   117   |  tina sharma   |  tinash  |  tina@111  | 1990-05-15 |     tinash@gmail.com    | 508852387 |   2015-08-07  |      22      |
|   119   |   adi singh    | adisingh |   adi123   | 2000-08-12 |     adiadi@gmail.com    |    None   |   2023-11-30  |     None     |
+---------+----------------+----------+------------+------------+-------------------------+-----------+---------------+--------------+

=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	3

ADD NEW MEMBER:-
enter new members name:	manna dey
create username:	mannadey
create password:	manman
enter date of birth (yyyy-mm-dd):	1999-1-1
enter email ID:	manman@gmail.com
enter phone num (971...):	509191919
enter date (members since) (yyyy-mm-dd):	2023-1-1
enter no. of books issued:	8
MEMBER ADDED


=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	2

SEARCH MEMBER DETAILS:-
enter user ID to search:	
====================================== RESTART: D:\g12\cs\sql stuff\MAIN.py ======================================
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
__      _____ _    ___ ___  __  __ ___    _____ ___  
\ \    / / __| |  / __/ _ \|  \/  | __|  |_   _/ _ \ 
 \ \/\/ /| _|| |_| (_| (_) | |\/| | _|     | || (_) |
  \_/\_/ |___|____\___\___/|_|  |_|___|    |_| \___/ 
                                                     

  ___   _   _  _____    __        ___  _____   ___      _ 
 / _ \ /_\ | |/ / __|  / _|___   |   \| __\ \ / ( )___ | |
| (_) / _ \| ' <\__ \  > _|_ _|  | |) | _| \ V /|/(_-< |_|
 \___/_/ \_\_|\_\___/  \_____|   |___/|___| |_|   /__/ (_)
                                                          

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	1
enter admin username:	admin
enter admin password:	DEYLIB18
ACCESS PERMITTED!

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	1

=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	3

ADD NEW MEMBER:-
enter new members name:	satyajit ray
create username:	satyajitr
create password:	sat123
enter date of birth (yyyy-mm-dd):	1999-9-9
enter email ID:	satyajit@gmail.com
enter phone num (971...):	506216262
enter date (members since) (yyyy-mm-dd):	2020-2-2
enter no. of books issued:	19
MEMBER ADDED

new member id created:	 126 


=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	2

SEARCH MEMBER DETAILS:-
enter user ID to search:	126
RECORD FOUND:
+---------+--------------+-----------+----------+------------+--------------------+-----------+---------------+--------------+
| user_id |     name     |  username | password |    dob     |      mail_id       | phone_num | members_since | books_issued |
+---------+--------------+-----------+----------+------------+--------------------+-----------+---------------+--------------+
|   126   | satyajit ray | satyajitr |  sat123  | 1999-09-09 | satyajit@gmail.com | 506216262 |   2020-02-02  |      19      |
+---------+--------------+-----------+----------+------------+--------------------+-----------+---------------+--------------+

=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	4
enter user id:	126

UPDATE MEMBERS TABLE:-
1. update mailid
2. update phone num
3. update books issued
4. exit
enter choice:	1
enter new email ID:	satsat@gmail.com
RECORD UPDATED

enter user id:	0

UPDATE MEMBERS TABLE:-
1. update mailid
2. update phone num
3. update books issued
4. exit
enter choice:	4

=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	5

DELETE MEMBER:-	
enter user ID to be deleted:	119
RECORD DELETED


=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	1

MEMBERS DETAILS:

+---------+----------------+-----------+------------+------------+-------------------------+-----------+---------------+--------------+
| user_id |      name      |  username |  password  |    dob     |         mail_id         | phone_num | members_since | books_issued |
+---------+----------------+-----------+------------+------------+-------------------------+-----------+---------------+--------------+
|   110   | rachel zegler  |  rachelz  |  rach@123  | 2000-11-09 |   rachelzeze@gmail.com  | 502328475 |   2020-09-22  |      17      |
|   112   |    liz sill    |  lizsill  |  liz@456   | 2002-12-09 |     lizzie@gmail.com    | 554629857 |   2021-04-02  |      12      |
|   113   |   geeta harr   |   geetah  |  gee@789   | 1999-01-19 |     geegee@gmail.com    | 506482837 |   2020-04-23  |      28      |
|   114   |  riya pritam   |   riyap   |  riya@987  | 1977-06-30 |    riripri@gmail.com    | 558769876 |   2017-10-14  |      38      |
|   115   |  jayant singh  |  jayants  |  jay@654   | 1994-02-26 |  jayantsingh@gmail.com  | 508761234 |   2023-03-03  |      9       |
|   116   | shreya ghoshal |  shreyag  | shreya@321 | 2001-07-31 | shreshreghosh@gmail.com | 509997654 |   2023-11-12  |      20      |
|   117   |  tina sharma   |   tinash  |  tina@111  | 1990-05-15 |     tinash@gmail.com    | 508852387 |   2015-08-07  |      22      |
|   125   |   manna dey    |  mannadey |   manman   | 1999-01-01 |     manman@gmail.com    | 509191919 |   2023-01-01  |      8       |
|   126   |  satyajit ray  | satyajitr |   sat123   | 1999-09-09 |     satsat@gmail.com    | 506216262 |   2020-02-02  |      19      |
+---------+----------------+-----------+------------+------------+-------------------------+-----------+---------------+--------------+

=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	6

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	2

=====================================
       LIBRARY STAFF DETAILS         
=====================================
1. display staff member details
2. search for staff member details
3. insert staff member details
4. update staff member details
5. delete staff member details
6. return to previous menu
enter choice:	1

STAFF MEMBERS DETAILS:

+----------+--------------+------------+-----------------------+-----------+--------+---------------+
| staff_id |  staff_name  |    dob     |        mail_id        | phone_num | salary | working_hours |
+----------+--------------+------------+-----------------------+-----------+--------+---------------+
|   301    | raj malhotra | 1990-08-22 |    rajmal@gmail.com   | 508763456 | 5000.0 |  10 am - 6 pm |
|   302    | arjun verma  | 1995-04-15 |  arjunverma@gmail.com | 554629857 | 5500.0 |  9 am - 5 pm  |
|   303    | neha sharma  | 1988-11-19 |    nehash@gmail.com   | 506482837 | 6000.0 |  11 am - 7 pm |
|   304    | ananya singh | 1983-06-30 | ananyasingh@gmail.com | 558769876 | 7000.0 |  8 am - 4 pm  |
|   305    | mohit patel  | 1994-02-26 |  mohitpatel@gmail.com | 509997654 | 6000.0 |  10 am - 6 pm |
|   306    | kavya gupta  | 1985-07-31 |    kavyag@gmail.com   | 508852387 | 5500.0 |  9 am - 5 pm  |
+----------+--------------+------------+-----------------------+-----------+--------+---------------+

=====================================
       LIBRARY STAFF DETAILS         
=====================================
1. display staff member details
2. search for staff member details
3. insert staff member details
4. update staff member details
5. delete staff member details
6. return to previous menu
enter choice:	3

ADD NEW STAFF MEMBER:-
enter new staff name:	jior verma
enter date of birth (yyyy-mm-dd):	2000-12-1
enter email ID:	jiorjior@gmail.com
enter phone num (971...):	509191919
enter salary (in USD):	2200
enter working hours (from -- to --):	5 am to 5 pm
STAFF MEMBER ADDED
new staff id created:	 308 


=====================================
       LIBRARY STAFF DETAILS         
=====================================
1. display staff member details
2. search for staff member details
3. insert staff member details
4. update staff member details
5. delete staff member details
6. return to previous menu
enter choice:	2

SEARCH STAFF MEMBER DETAILS:-
enter staff ID to search:	308
RECORD FOUND:
+----------+------------+------------+--------------------+-----------+--------+---------------+
| staff_id | staff_name |    dob     |      mail_id       | phone_num | salary | working_hours |
+----------+------------+------------+--------------------+-----------+--------+---------------+
|   308    | jior verma | 2000-12-01 | jiorjior@gmail.com | 509191919 | 2200.0 |  5 am to 5 pm |
+----------+------------+------------+--------------------+-----------+--------+---------------+

=====================================
       LIBRARY STAFF DETAILS         
=====================================
1. display staff member details
2. search for staff member details
3. insert staff member details
4. update staff member details
5. delete staff member details
6. return to previous menu
enter choice:	4
enter staff ID:	308
UPDATE STAFF RECORD:-
1. update email ID
2. update phone number
3. update salary
4. update working hours
5. exit
enter choice:	4
enter new working hours (from -- to --):	5 am to 12 pm
RECORD UPDATED

enter staff ID:	0
UPDATE STAFF RECORD:-
1. update email ID
2. update phone number
3. update salary
4. update working hours
5. exit
enter choice:	5

=====================================
       LIBRARY STAFF DETAILS         
=====================================
1. display staff member details
2. search for staff member details
3. insert staff member details
4. update staff member details
5. delete staff member details
6. return to previous menu
enter choice:	5

DELETE STAFF MEMBER:-	
enter staff ID to be deleted:	302
RECORD DELETED


=====================================
       LIBRARY STAFF DETAILS         
=====================================
1. display staff member details
2. search for staff member details
3. insert staff member details
4. update staff member details
5. delete staff member details
6. return to previous menu
enter choice:	1

STAFF MEMBERS DETAILS:

+----------+--------------+------------+-----------------------+-----------+--------+---------------+
| staff_id |  staff_name  |    dob     |        mail_id        | phone_num | salary | working_hours |
+----------+--------------+------------+-----------------------+-----------+--------+---------------+
|   301    | raj malhotra | 1990-08-22 |    rajmal@gmail.com   | 508763456 | 5000.0 |  10 am - 6 pm |
|   303    | neha sharma  | 1988-11-19 |    nehash@gmail.com   | 506482837 | 6000.0 |  11 am - 7 pm |
|   304    | ananya singh | 1983-06-30 | ananyasingh@gmail.com | 558769876 | 7000.0 |  8 am - 4 pm  |
|   305    | mohit patel  | 1994-02-26 |  mohitpatel@gmail.com | 509997654 | 6000.0 |  10 am - 6 pm |
|   306    | kavya gupta  | 1985-07-31 |    kavyag@gmail.com   | 508852387 | 5500.0 |  9 am - 5 pm  |
|   308    |  jior verma  | 2000-12-01 |   jiorjior@gmail.com  | 509191919 | 2200.0 | 5 am to 12 pm |
+----------+--------------+------------+-----------------------+-----------+--------+---------------+

=====================================
       LIBRARY STAFF DETAILS         
=====================================
1. display staff member details
2. search for staff member details
3. insert staff member details
4. update staff member details
5. delete staff member details
6. return to previous menu
enter choice:	6

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	3

=====================================
        LIBRARY BOOKS CATALOG         
=====================================
1. display book details
2. search for book details
3. insert new book
4. update book details
5. delete book details
6. return to previous menu
enter choice:	1

BOOK CATALOG:

+-----+---------+---------------------------------------+------------------------+-----------------------+------------------+--------------+-----------+---------------+
| sno | book_id |                 title                 |      author_name       |         genre         | publication_date | availability | frequency |      ISBN     |
+-----+---------+---------------------------------------+------------------------+-----------------------+------------------+--------------+-----------+---------------+
|  1  |   123   |         the fault in our stars        |       john green       |        romance        |    2012-01-10    |  available   |     17    | 9780143567592 |
|  2  |   456   |         to kill a mockingbird         |       harper lee       |        fiction        |    1960-07-11    |    issued    |     7     | 9780061120084 |
|  3  |   789   |                  1984                 |     george orwell      |       dystopian       |    1949-06-08    |    issued    |     1     | 9780140817744 |
|  4  |   101   |            the great gatsby           |  f. scott fitzgerald   |        classic        |    1925-04-10    |    issued    |     8     | 9780333791035 |
|  5  |   202   |          pride and prejudice          |      jane austen       |        romance        |    1813-01-28    |    issued    |     11    | 9780141439518 |
|  6  |   303   |         the catcher in the rye        |     j.d. salinger      |     coming of age     |    1951-07-16    |    issued    |     3     | 9780241950432 |
|  7  |   404   | harry potter and the sorcerer's stone |      j.k. rowling      |        fantasy        |    1997-06-26    |  available   |     3     | 9780439362139 |
|  8  |   505   |            the hunger games           |    suzanne collins     |       dystopian       |    2008-09-14    |  available   |     2     | 9780439023481 |
|  9  |   606   |             the alchemist             |      paulo coelho      |        fiction        |    1988-01-01    |    issued    |     2     | 9780061122415 |
|  10 |   707   |        the shawshank redemption       |      stephen king      |         drama         |    1982-11-04    |    issued    |     3     | 9780751514624 |
|  11 |   808   |           gone with the wind          |   margaret mitchell    |   historical fiction  |    1936-06-30    |  available   |     1     | 9780582418059 |
|  12 |   909   |     one hundred years of solitude     | gabriel garcia marquez |    magical realism    |    1967-05-30    |  available   |     1     | 9780060114183 |
|  13 |   1010  |         the lord of the rings         |     j.r.r. tolkien     |        fantasy        |    1954-07-29    |    issued    |     8     | 9788845292613 |
|  14 |   1111  |           the da vinci code           |       dan brown        |        mystery        |    2003-03-18    |    issued    |     3     | 9780307474278 |
|  15 |   1212  |       the count of monte cristo       |    alexandre dumas     |       adventure       |    1844-08-28    |  available   |     1     | 9780199219650 |
|  16 |   1313  |            brave new world            |     aldous huxley      |       dystopian       |    1932-02-02    |  available   |     1     | 9780582060166 |
|  17 |   1414  |       the picture of dorian gray      |      oscar wilde       |     gothic fiction    |    1890-07-20    |  available   |     2     | 9789875503229 |
|  18 |   1515  |            the jungle book            |    rudyard kipling     | children's literature |    1894-11-25    |  available   |     24    | 9780194227469 |
|  20 |   1717  |               the hobbit              |     j.r.r. tolkien     |        fiction        |    1937-09-21    |  available   |     3     | 9780007525508 |
|  21 |   1900  |         better than the movies        |      lynn painter      |        romance        |    2000-10-10    |  available   |     1     | 9781928192819 |
+-----+---------+---------------------------------------+------------------------+-----------------------+------------------+--------------+-----------+---------------+

=====================================
        LIBRARY BOOKS CATALOG         
=====================================
1. display book details
2. search for book details
3. insert new book
4. update book details
5. delete book details
6. return to previous menu
enter choice:	4
enter book ID:	1900
UPDATE BOOK CATALOG:-
1. update title
2. update genre
3. update availability
4. update ISBN
5. exit
enter choice:	3
enter updated availability:	issued
RECORD UPDATED

enter book ID:	0
UPDATE BOOK CATALOG:-
1. update title
2. update genre
3. update availability
4. update ISBN
5. exit
enter choice:	5

=====================================
        LIBRARY BOOKS CATALOG         
=====================================
1. display book details
2. search for book details
3. insert new book
4. update book details
5. delete book details
6. return to previous menu
enter choice:	2

SEARCH BOOK DETAILS:-
enter book ID to search:	1900
RECORD FOUND:
+-----+---------+------------------------+--------------+---------+------------------+--------------+-----------+---------------+
| sno | book_id |         title          | author_name  |  genre  | publication_date | availability | frequency |      ISBN     |
+-----+---------+------------------------+--------------+---------+------------------+--------------+-----------+---------------+
|  21 |   1900  | better than the movies | lynn painter | romance |    2000-10-10    |    issued    |     1     | 9781928192819 |
+-----+---------+------------------------+--------------+---------+------------------+--------------+-----------+---------------+

=====================================
        LIBRARY BOOKS CATALOG         
=====================================
1. display book details
2. search for book details
3. insert new book
4. update book details
5. delete book details
6. return to previous menu
enter choice:	6

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	4

=====================================
         ISSUED BOOKS DETAILS        
=====================================
1. issue a book
2. return a book
3. show issued books
4. view issued history
5. search issued books
6. return to previous menu
enter choice:	1

ISSUE A BOOK:-
enter book ID:	1900
book is already issued by someone else, choose another book
enter book ID:	123
enter user ID:	310
enter valid user ID
enter user ID:	125
an error occurred: "1062 (23000): Duplicate entry '9780143567592' for key 'issuedbooks.ISBN'"


=====================================
         ISSUED BOOKS DETAILS        
=====================================
1. issue a book
2. return a book
3. show issued books
4. view issued history
5. search issued books
6. return to previous menu
enter choice:	
=================================== RESTART: D:\g12\cs\sql stuff\basetables.py ===================================
mycursor.execute('drop table issuedbooks')
                    
mycursor.execute('drop table issuedhistory')
                    

=================================== RESTART: D:\g12\cs\sql stuff\basetables.py ===================================

====================================== RESTART: D:\g12\cs\sql stuff\MAIN.py ======================================
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
__      _____ _    ___ ___  __  __ ___    _____ ___  
\ \    / / __| |  / __/ _ \|  \/  | __|  |_   _/ _ \ 
 \ \/\/ /| _|| |_| (_| (_) | |\/| | _|     | || (_) |
  \_/\_/ |___|____\___\___/|_|  |_|___|    |_| \___/ 
                                                     

  ___   _   _  _____    __        ___  _____   ___      _ 
 / _ \ /_\ | |/ / __|  / _|___   |   \| __\ \ / ( )___ | |
| (_) / _ \| ' <\__ \  > _|_ _|  | |) | _| \ V /|/(_-< |_|
 \___/_/ \_\_|\_\___/  \_____|   |___/|___| |_|   /__/ (_)
                                                          

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	1
enter admin username:	admin
enter admin password:	DEYLIB18
ACCESS PERMITTED!

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	4

=====================================
         ISSUED BOOKS DETAILS        
=====================================
1. issue a book
2. return a book
3. show issued books
4. view issued history
5. search issued books
6. return to previous menu
enter choice:	1

ISSUE A BOOK:-
enter book ID:	123
enter user ID:	125
BOOK ISSUED


=====================================
         ISSUED BOOKS DETAILS        
=====================================
1. issue a book
2. return a book
3. show issued books
4. view issued history
5. search issued books
6. return to previous menu
enter choice:	2

RETURN A BOOK:	
enter book ID to be returned:	1900
book ID has not been issued, please enter a valid book ID
enter book ID to be returned:	123
an error occurred: "Unread result found"


=====================================
         ISSUED BOOKS DETAILS        
=====================================
1. issue a book
2. return a book
3. show issued books
4. view issued history
5. search issued books
6. return to previous menu
enter choice:	3

ISSUED BOOKS:

+---------+---------+---------------------------------------+---------------+-------------+
| user_id | book_id |               book_name               |      ISBN     | issued_date |
+---------+---------+---------------------------------------+---------------+-------------+
|   117   |   123   |         the fault in our stars        | 9780143567592 |  2021-03-15 |
|   116   |   789   |                  1984                 | 9780140817744 |  2021-05-20 |
|   110   |   404   | harry potter and the sorcerer's stone | 9780439362139 |  2022-01-10 |
|   112   |   1515  |            the jungle book            | 9780194227469 |  2021-08-05 |
|   125   |   123   |         the fault in our stars        | 9780143567592 |  2023-12-04 |
+---------+---------+---------------------------------------+---------------+-------------+
show extended table (y/n):	n

=====================================
         ISSUED BOOKS DETAILS        
=====================================
1. issue a book
2. return a book
3. show issued books
4. view issued history
5. search issued books
6. return to previous menu
enter choice:	4

ISSUED HISTORY:

+---------+---------+---------------------------------------+---------------+-------------+
| user_id | book_id |               book_name               |      ISBN     | issued_date |
+---------+---------+---------------------------------------+---------------+-------------+
|   117   |   123   |         the fault in our stars        | 9780143567592 |  2021-03-15 |
|   116   |   789   |                  1984                 | 9780140817744 |  2021-05-20 |
|   110   |   404   | harry potter and the sorcerer's stone | 9780439362139 |  2022-01-10 |
|   112   |   1515  |            the jungle book            | 9780194227469 |  2021-08-05 |
|   125   |   123   |         the fault in our stars        | 9780143567592 |  2023-12-04 |
+---------+---------+---------------------------------------+---------------+-------------+
show extended table (y/n):	n

=====================================
         ISSUED BOOKS DETAILS        
=====================================
1. issue a book
2. return a book
3. show issued books
4. view issued history
5. search issued books
6. return to previous menu
enter choice:	1

ISSUE A BOOK:-
enter book ID:	1900
book is already issued by someone else, choose another book
enter book ID:	
an error occurred: "invalid literal for int() with base 10: ''"


=====================================
         ISSUED BOOKS DETAILS        
=====================================
1. issue a book
2. return a book
3. show issued books
4. view issued history
5. search issued books
6. return to previous menu
enter choice:	6

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	3

=====================================
        LIBRARY BOOKS CATALOG         
=====================================
1. display book details
2. search for book details
3. insert new book
4. update book details
5. delete book details
6. return to previous menu
enter choice:	6

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	4

=====================================
         ISSUED BOOKS DETAILS        
=====================================
1. issue a book
2. return a book
3. show issued books
4. view issued history
5. search issued books
6. return to previous menu
enter choice:	1

ISSUE A BOOK:-
enter book ID:	123
book is already issued by someone else, choose another book
enter book ID:	505
enter user ID:	125
BOOK ISSUED


=====================================
         ISSUED BOOKS DETAILS        
=====================================
1. issue a book
2. return a book
3. show issued books
4. view issued history
5. search issued books
6. return to previous menu
enter choice:	2

RETURN A BOOK:	
enter book ID to be returned:	123
an error occurred: "Unread result found"


=====================================
         ISSUED BOOKS DETAILS        
=====================================
1. issue a book
2. return a book
3. show issued books
4. view issued history
5. search issued books
6. return to previous menu
enter choice:	2

RETURN A BOOK:	
enter book ID to be returned:	789
BOOK RETURNED


=====================================
         ISSUED BOOKS DETAILS        
=====================================
1. issue a book
2. return a book
3. show issued books
4. view issued history
5. search issued books
6. return to previous menu
enter choice:	3

ISSUED BOOKS:

+---------+---------+---------------------------------------+---------------+-------------+
| user_id | book_id |               book_name               |      ISBN     | issued_date |
+---------+---------+---------------------------------------+---------------+-------------+
|   117   |   123   |         the fault in our stars        | 9780143567592 |  2021-03-15 |
|   110   |   404   | harry potter and the sorcerer's stone | 9780439362139 |  2022-01-10 |
|   112   |   1515  |            the jungle book            | 9780194227469 |  2021-08-05 |
|   125   |   123   |         the fault in our stars        | 9780143567592 |  2023-12-04 |
|   125   |   505   |            the hunger games           | 9780439023481 |  2023-12-04 |
+---------+---------+---------------------------------------+---------------+-------------+
show extended table (y/n):	y

ISSUED BOOKS:

+---------+---------+---------------------------------------+---------------+-------------+-----------------+-----------------------+-----------+
| user_id | book_id |               book_name               |      ISBN     | issued_date |   author_name   |         genre         | frequency |
+---------+---------+---------------------------------------+---------------+-------------+-----------------+-----------------------+-----------+
|   117   |   123   |         the fault in our stars        | 9780143567592 |  2021-03-15 |    john green   |        romance        |     18    |
|   110   |   404   | harry potter and the sorcerer's stone | 9780439362139 |  2022-01-10 |   j.k. rowling  |        fantasy        |     3     |
|   112   |   1515  |            the jungle book            | 9780194227469 |  2021-08-05 | rudyard kipling | children's literature |     24    |
|   125   |   123   |         the fault in our stars        | 9780143567592 |  2023-12-04 |    john green   |        romance        |     18    |
|   125   |   505   |            the hunger games           | 9780439023481 |  2023-12-04 | suzanne collins |       dystopian       |     3     |
+---------+---------+---------------------------------------+---------------+-------------+-----------------+-----------------------+-----------+

=====================================
         ISSUED BOOKS DETAILS        
=====================================
1. issue a book
2. return a book
3. show issued books
4. view issued history
5. search issued books
6. return to previous menu
enter choice:	4

ISSUED HISTORY:

+---------+---------+---------------------------------------+---------------+-------------+
| user_id | book_id |               book_name               |      ISBN     | issued_date |
+---------+---------+---------------------------------------+---------------+-------------+
|   117   |   123   |         the fault in our stars        | 9780143567592 |  2021-03-15 |
|   116   |   789   |                  1984                 | 9780140817744 |  2021-05-20 |
|   110   |   404   | harry potter and the sorcerer's stone | 9780439362139 |  2022-01-10 |
|   112   |   1515  |            the jungle book            | 9780194227469 |  2021-08-05 |
|   125   |   123   |         the fault in our stars        | 9780143567592 |  2023-12-04 |
|   125   |   505   |            the hunger games           | 9780439023481 |  2023-12-04 |
+---------+---------+---------------------------------------+---------------+-------------+
show extended table (y/n):	n

=====================================
         ISSUED BOOKS DETAILS        
=====================================
1. issue a book
2. return a book
3. show issued books
4. view issued history
5. search issued books
6. return to previous menu
enter choice:	5

SEARCH ISSUED BOOK DETAILS:-
enter book ID to search:	505
RECORD FOUND:
+---------+---------+------------------+---------------+-------------+
| user_id | book_id |    book_name     |      ISBN     | issued_date |
+---------+---------+------------------+---------------+-------------+
|   125   |   505   | the hunger games | 9780439023481 |  2023-12-04 |
+---------+---------+------------------+---------------+-------------+

=====================================
         ISSUED BOOKS DETAILS        
=====================================
1. issue a book
2. return a book
3. show issued books
4. view issued history
5. search issued books
6. return to previous menu
enter choice:	6

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	5

=====================================
           WISHLIST DETAILS          
=====================================
1. request a book
2. view wishlist
3. search your wishlist
4. update wishlist book details
5. return to previous menu
enter choice:	1
enter member id:	125

REQUEST A BOOK:-
enter book title:	milk and honey
enter ISBN:	9781818181818
enter author name:	rupi kaur
enter genre:	poetry
BOOK REQUESTED


=====================================
           WISHLIST DETAILS          
=====================================
1. request a book
2. view wishlist
3. search your wishlist
4. update wishlist book details
5. return to previous menu
enter choice:	2

WISHLIST:

+-----+---------+------------------------+---------------+----------------+---------------------+-----------+
| sno | user_id |         title          |      ISBN     |  author_name   |        genre        |   status  |
+-----+---------+------------------------+---------------+----------------+---------------------+-----------+
|  1  |   121   | the fault in our stars | 9780143567592 |   john green   |       romance       | purchased |
|  2  |    2    | to kill a mockingbird  | 9780061120084 |   harper lee   |       fiction       | purchased |
|  3  |    92   | all the bright places  | 9780385755887 | jennifer niven | young adult fiction |  pending  |
|  4  |    4    |     the book thief     | 9781101934180 |  markus zusak  |  historical fiction |  pending  |
|  5  |   110   | love and misadventure  | 9781726352617 |   lang leav    |    romance poetry   |  pending  |
|  6  |   125   |     milk and honey     | 9781818181818 |   rupi kaur    |        poetry       |  pending  |
+-----+---------+------------------------+---------------+----------------+---------------------+-----------+

=====================================
           WISHLIST DETAILS          
=====================================
1. request a book
2. view wishlist
3. search your wishlist
4. update wishlist book details
5. return to previous menu
enter choice:	4

UPDATE WISHLIST:-
1. update ISBN
2. update status
3. exit
enter choice:	2
enter ISBN:	9781101934180
enter status (pending/purchased):	purchased
RECORD UPDATED


UPDATE WISHLIST:-
1. update ISBN
2. update status
3. exit
enter choice:	3

=====================================
           WISHLIST DETAILS          
=====================================
1. request a book
2. view wishlist
3. search your wishlist
4. update wishlist book details
5. return to previous menu
enter choice:	3

SEARCH WISHLIST BOOK DETAILS:-
enter title to search:	the book thief
RECORD FOUND:
+-----+---------+----------------+---------------+--------------+--------------------+-----------+
| sno | user_id |     title      |      ISBN     | author_name  |       genre        |   status  |
+-----+---------+----------------+---------------+--------------+--------------------+-----------+
|  4  |    4    | the book thief | 9781101934180 | markus zusak | historical fiction | purchased |
+-----+---------+----------------+---------------+--------------+--------------------+-----------+

=====================================
           WISHLIST DETAILS          
=====================================
1. request a book
2. view wishlist
3. search your wishlist
4. update wishlist book details
5. return to previous menu
enter choice:	5

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	6

=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. view book reviews
2. search reviews
3. update book reviews
4. delete book review
5. return to previous menu
enter choice:	1

BOOK REVIEWS:

SNO:	 1
USER ID:	 114
TITLE:	 the fault in our stars
RATING:	 4
REVIEW:
 a heartwarming journey through the pains of love and loss, leaving a lasting impact on the soul. a must-read for those seeking a profound emotional experience.
REVIEW DATE:	 2021-09-10
SNO:	 2
USER ID:	 116
TITLE:	 all the bright places
RATING:	 4
REVIEW:
 an emotionally charged narrative that delves deep into the human psyche, providing a raw and authentic portrayal of mental health struggles. a poignant and thought-provoking read.
REVIEW DATE:	 2023-03-14
SNO:	 3
USER ID:	 110
TITLE:	 the jungle book
RATING:	 3
REVIEW:
 a nostalgic adventure that transports readers to the enchanting world of mowgli and his animal companions. filled with wonder and imagination, it's a tale that captivates readers of all ages.
REVIEW DATE:	 2022-05-18

=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. view book reviews
2. search reviews
3. update book reviews
4. delete book review
5. return to previous menu
enter choice:	
====================================== RESTART: D:\g12\cs\sql stuff\MAIN.py ======================================
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
__      _____ _    ___ ___  __  __ ___    _____ ___  
\ \    / / __| |  / __/ _ \|  \/  | __|  |_   _/ _ \ 
 \ \/\/ /| _|| |_| (_| (_) | |\/| | _|     | || (_) |
  \_/\_/ |___|____\___\___/|_|  |_|___|    |_| \___/ 
                                                     

  ___   _   _  _____    __        ___  _____   ___      _ 
 / _ \ /_\ | |/ / __|  / _|___   |   \| __\ \ / ( )___ | |
| (_) / _ \| ' <\__ \  > _|_ _|  | |) | _| \ V /|/(_-< |_|
 \___/_/ \_\_|\_\___/  \_____|   |___/|___| |_|   /__/ (_)
                                                          

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	admin
Traceback (most recent call last):
  File "D:\g12\cs\sql stuff\MAIN.py", line 346, in <module>
    ch=int(input('enter choice:\t'))
ValueError: invalid literal for int() with base 10: 'admin'

====================================== RESTART: D:\g12\cs\sql stuff\MAIN.py ======================================
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
__      _____ _    ___ ___  __  __ ___    _____ ___  
\ \    / / __| |  / __/ _ \|  \/  | __|  |_   _/ _ \ 
 \ \/\/ /| _|| |_| (_| (_) | |\/| | _|     | || (_) |
  \_/\_/ |___|____\___\___/|_|  |_|___|    |_| \___/ 
                                                     

  ___   _   _  _____    __        ___  _____   ___      _ 
 / _ \ /_\ | |/ / __|  / _|___   |   \| __\ \ / ( )___ | |
| (_) / _ \| ' <\__ \  > _|_ _|  | |) | _| \ V /|/(_-< |_|
 \___/_/ \_\_|\_\___/  \_____|   |___/|___| |_|   /__/ (_)
                                                          

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	1
enter admin username:	admin
enter admin password:	DEYLIB18
ACCESS PERMITTED!

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	6

=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. view book reviews
2. search reviews
3. update book reviews
4. delete book review
5. return to previous menu
enter choice:	1

BOOK REVIEWS:

SNO:	 1
USER ID:	 114
TITLE:	 the fault in our stars
RATING:	 4
REVIEW:
 a heartwarming journey through the pains of love and loss, leaving a lasting impact on the soul. a must-read for those seeking a profound emotional experience.
REVIEW DATE:	 2021-09-10
SNO:	 2
USER ID:	 116
TITLE:	 all the bright places
RATING:	 4
REVIEW:
 an emotionally charged narrative that delves deep into the human psyche, providing a raw and authentic portrayal of mental health struggles. a poignant and thought-provoking read.
REVIEW DATE:	 2023-03-14
SNO:	 3
USER ID:	 110
TITLE:	 the jungle book
RATING:	 3
REVIEW:
 a nostalgic adventure that transports readers to the enchanting world of mowgli and his animal companions. filled with wonder and imagination, it's a tale that captivates readers of all ages.
REVIEW DATE:	 2022-05-18

=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. view book reviews
2. search reviews
3. update book reviews
4. delete book review
5. return to previous menu
enter choice:	
====================================== RESTART: D:\g12\cs\sql stuff\MAIN.py ======================================
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
__      _____ _    ___ ___  __  __ ___    _____ ___  
\ \    / / __| |  / __/ _ \|  \/  | __|  |_   _/ _ \ 
 \ \/\/ /| _|| |_| (_| (_) | |\/| | _|     | || (_) |
  \_/\_/ |___|____\___\___/|_|  |_|___|    |_| \___/ 
                                                     

  ___   _   _  _____    __        ___  _____   ___      _ 
 / _ \ /_\ | |/ / __|  / _|___   |   \| __\ \ / ( )___ | |
| (_) / _ \| ' <\__ \  > _|_ _|  | |) | _| \ V /|/(_-< |_|
 \___/_/ \_\_|\_\___/  \_____|   |___/|___| |_|   /__/ (_)
                                                          

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	1
enter admin username:	admin
enter admin password:	DEYLIB18
ACCESS PERMITTED!

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	6

=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. view book reviews
2. search reviews
3. update book reviews
4. delete book review
5. return to previous menu
enter choice:	1

BOOK REVIEWS:

SNO:	 1
USER ID:	 114
TITLE:	 the fault in our stars
RATING:	 4
REVIEW:
 a heartwarming journey through the pains of love and loss, leaving a lasting impact on the soul. a must-read for those seeking a profound emotional experience.
REVIEW DATE:	 2021-09-10

SNO:	 2
USER ID:	 116
TITLE:	 all the bright places
RATING:	 4
REVIEW:
 an emotionally charged narrative that delves deep into the human psyche, providing a raw and authentic portrayal of mental health struggles. a poignant and thought-provoking read.
REVIEW DATE:	 2023-03-14

SNO:	 3
USER ID:	 110
TITLE:	 the jungle book
RATING:	 3
REVIEW:
 a nostalgic adventure that transports readers to the enchanting world of mowgli and his animal companions. filled with wonder and imagination, it's a tale that captivates readers of all ages.
REVIEW DATE:	 2022-05-18


=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. view book reviews
2. search reviews
3. update book reviews
4. delete book review
5. return to previous menu
enter choice:	3
enter member id:	0
enter book title:	the jungle book

UPDATE REVIEW:-
1. update rating
2. update review
3. exit
enter choice:	1
an error occurred: "1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'jungle book' at line 1"


=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. view book reviews
2. search reviews
3. update book reviews
4. delete book review
5. return to previous menu
enter choice:	3
enter member id:	110
enter book title:	the jungle book

UPDATE REVIEW:-
1. update rating
2. update review
3. exit
enter choice:	1
an error occurred: "1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'jungle book' at line 1"


=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. view book reviews
2. search reviews
3. update book reviews
4. delete book review
5. return to previous menu
enter choice:	
====================================== RESTART: D:\g12\cs\sql stuff\MAIN.py ======================================
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
__      _____ _    ___ ___  __  __ ___    _____ ___  
\ \    / / __| |  / __/ _ \|  \/  | __|  |_   _/ _ \ 
 \ \/\/ /| _|| |_| (_| (_) | |\/| | _|     | || (_) |
  \_/\_/ |___|____\___\___/|_|  |_|___|    |_| \___/ 
                                                     

  ___   _   _  _____    __        ___  _____   ___      _ 
 / _ \ /_\ | |/ / __|  / _|___   |   \| __\ \ / ( )___ | |
| (_) / _ \| ' <\__ \  > _|_ _|  | |) | _| \ V /|/(_-< |_|
 \___/_/ \_\_|\_\___/  \_____|   |___/|___| |_|   /__/ (_)
                                                          

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	1
enter admin username:	admin
enter admin password:	DEYLIB18
ACCESS PERMITTED!

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	6

=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. view book reviews
2. search reviews
3. update book reviews
4. delete book review
5. return to previous menu
enter choice:	3
enter member id:	1
enter book title:	the jungle book

UPDATE REVIEW:-
1. update rating
2. update review
3. exit
enter choice:	1
enter rating (out of 5):	5
an error occurred: "Replacement index 2 out of range for positional args tuple"


=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. view book reviews
2. search reviews
3. update book reviews
4. delete book review
5. return to previous menu
enter choice:	3
enter member id:	
====================================== RESTART: D:\g12\cs\sql stuff\MAIN.py ======================================
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
__      _____ _    ___ ___  __  __ ___    _____ ___  
\ \    / / __| |  / __/ _ \|  \/  | __|  |_   _/ _ \ 
 \ \/\/ /| _|| |_| (_| (_) | |\/| | _|     | || (_) |
  \_/\_/ |___|____\___\___/|_|  |_|___|    |_| \___/ 
                                                     

  ___   _   _  _____    __        ___  _____   ___      _ 
 / _ \ /_\ | |/ / __|  / _|___   |   \| __\ \ / ( )___ | |
| (_) / _ \| ' <\__ \  > _|_ _|  | |) | _| \ V /|/(_-< |_|
 \___/_/ \_\_|\_\___/  \_____|   |___/|___| |_|   /__/ (_)
                                                          

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	1
enter admin username:	admin
enter admin password:	DEYLIB18
ACCESS PERMITTED!

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	6

=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. view book reviews
2. search reviews
3. update book reviews
4. delete book review
5. return to previous menu
enter choice:	3
enter member id:	1
enter book title:	the jungle book

UPDATE REVIEW:-
1. update rating
2. update review
3. exit
enter choice:	1
enter rating (out of 5):	4
RECORD UPDATED

enter book title:	
====================================== RESTART: D:\g12\cs\sql stuff\MAIN.py ======================================
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
__      _____ _    ___ ___  __  __ ___    _____ ___  
\ \    / / __| |  / __/ _ \|  \/  | __|  |_   _/ _ \ 
 \ \/\/ /| _|| |_| (_| (_) | |\/| | _|     | || (_) |
  \_/\_/ |___|____\___\___/|_|  |_|___|    |_| \___/ 
                                                     

  ___   _   _  _____    __        ___  _____   ___      _ 
 / _ \ /_\ | |/ / __|  / _|___   |   \| __\ \ / ( )___ | |
| (_) / _ \| ' <\__ \  > _|_ _|  | |) | _| \ V /|/(_-< |_|
 \___/_/ \_\_|\_\___/  \_____|   |___/|___| |_|   /__/ (_)
                                                          

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	1
enter admin username:	admin
enter admin password:	DEYLIB18
ACCESS PERMITTED!

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	6

=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. view book reviews
2. search reviews
3. update book reviews
4. delete book review
5. return to previous menu
enter choice:	3
enter user id:	1
no reviews found under this user

=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. view book reviews
2. search reviews
3. update book reviews
4. delete book review
5. return to previous menu
enter choice:	3
enter user id:	110
enter book title:	the jungle book

UPDATE REVIEW:-
1. update rating
2. update review
3. exit
enter choice:	1
enter rating (out of 5):	5
RECORD UPDATED

enter book title:	0

UPDATE REVIEW:-
1. update rating
2. update review
3. exit
enter choice:	3

=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. view book reviews
2. search reviews
3. update book reviews
4. delete book review
5. return to previous menu
enter choice:	5

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	7

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	3
enter username to register:	shreya ghoshal
enter password:	shreshreghosh
you are now a library member
new user id created:	 127

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	1
enter admin username:	admin
enter admin password:	DEYLIB18
ACCESS PERMITTED!

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	1

=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	1

MEMBERS DETAILS:

+---------+----------------+----------------+---------------+------------+-------------------------+-----------+---------------+--------------+
| user_id |      name      |    username    |    password   |    dob     |         mail_id         | phone_num | members_since | books_issued |
+---------+----------------+----------------+---------------+------------+-------------------------+-----------+---------------+--------------+
|   110   | rachel zegler  |    rachelz     |    rach@123   | 2000-11-09 |   rachelzeze@gmail.com  | 502328475 |   2020-09-22  |      17      |
|   112   |    liz sill    |    lizsill     |    liz@456    | 2002-12-09 |     lizzie@gmail.com    | 554629857 |   2021-04-02  |      12      |
|   113   |   geeta harr   |     geetah     |    gee@789    | 1999-01-19 |     geegee@gmail.com    | 506482837 |   2020-04-23  |      28      |
|   114   |  riya pritam   |     riyap      |    riya@987   | 1977-06-30 |    riripri@gmail.com    | 558769876 |   2017-10-14  |      38      |
|   115   |  jayant singh  |    jayants     |    jay@654    | 1994-02-26 |  jayantsingh@gmail.com  | 508761234 |   2023-03-03  |      9       |
|   116   | shreya ghoshal |    shreyag     |   shreya@321  | 2001-07-31 | shreshreghosh@gmail.com | 509997654 |   2023-11-12  |      20      |
|   117   |  tina sharma   |     tinash     |    tina@111   | 1990-05-15 |     tinash@gmail.com    | 508852387 |   2015-08-07  |      22      |
|   125   |   manna dey    |    mannadey    |     manman    | 1999-01-01 |     manman@gmail.com    | 509191919 |   2023-01-01  |      10      |
|   126   |  satyajit ray  |   satyajitr    |     sat123    | 1999-09-09 |     satsat@gmail.com    | 506216262 |   2020-02-02  |      19      |
|   127   |      None      | shreya ghoshal | shreshreghosh |    None    |           None          |    None   |   2023-12-04  |     None     |
+---------+----------------+----------------+---------------+------------+-------------------------+-----------+---------------+--------------+

=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	5

DELETE MEMBER:-	
enter user ID to be deleted:	127
RECORD DELETED


=====================================
       LIBRARY MEMBERS DETAILS       
=====================================
1. display member details
2. search for member details
3. insert member details
4. update member details
5. delete member details
6. return to previous menu
enter choice:	6

=====================================
   TABLES TO PERFORM OPERATIONS ON:       
=====================================
1. MEMBERS TABLE
2. STAFF TABLE
3. BOOK CATALOG TABLE
4. ISSUED BOOKS TABLE
5. WISHLIST TABLE
6. REVIEWS TABLE
7. EXIT
enter choice:	7

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	3
enter username to register:	lulu lemon
enter password:	lulu123
you are now a library member
new user id created:	 128

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	2
enter username:	lulu lemon
enter password:	lulu123
successful sign-in
user id:	 128

=====================================
          CHOOSE A FIELD:       
=====================================
1. ISSUE BOOKS
2. RETURN BOOKS
3. ISSUED BOOKS HISTORY
4. WISHLIST
5. BOOK REVIEWS
6. ACCOUNT
7. EXIT
enter choice:	1
would you like to see the books available in library (y/n):	y

BOOK CATALOG:

+-----+---------+---------------------------------------+------------------------+-----------------------+------------------+--------------+-----------+---------------+
| sno | book_id |                 title                 |      author_name       |         genre         | publication_date | availability | frequency |      ISBN     |
+-----+---------+---------------------------------------+------------------------+-----------------------+------------------+--------------+-----------+---------------+
|  3  |   789   |                  1984                 |     george orwell      |       dystopian       |    1949-06-08    |  available   |     1     | 9780140817744 |
|  7  |   404   | harry potter and the sorcerer's stone |      j.k. rowling      |        fantasy        |    1997-06-26    |  available   |     3     | 9780439362139 |
|  11 |   808   |           gone with the wind          |   margaret mitchell    |   historical fiction  |    1936-06-30    |  available   |     1     | 9780582418059 |
|  12 |   909   |     one hundred years of solitude     | gabriel garcia marquez |    magical realism    |    1967-05-30    |  available   |     1     | 9780060114183 |
|  15 |   1212  |       the count of monte cristo       |    alexandre dumas     |       adventure       |    1844-08-28    |  available   |     1     | 9780199219650 |
|  16 |   1313  |            brave new world            |     aldous huxley      |       dystopian       |    1932-02-02    |  available   |     1     | 9780582060166 |
|  17 |   1414  |       the picture of dorian gray      |      oscar wilde       |     gothic fiction    |    1890-07-20    |  available   |     2     | 9789875503229 |
|  18 |   1515  |            the jungle book            |    rudyard kipling     | children's literature |    1894-11-25    |  available   |     24    | 9780194227469 |
|  20 |   1717  |               the hobbit              |     j.r.r. tolkien     |        fiction        |    1937-09-21    |  available   |     3     | 9780007525508 |
+-----+---------+---------------------------------------+------------------------+-----------------------+------------------+--------------+-----------+---------------+

ISSUE A BOOK:-
enter book ID:	1515
enter user ID:	128
BOOK ISSUED


=====================================
          CHOOSE A FIELD:       
=====================================
1. ISSUE BOOKS
2. RETURN BOOKS
3. ISSUED BOOKS HISTORY
4. WISHLIST
5. BOOK REVIEWS
6. ACCOUNT
7. EXIT
enter choice:	3

ISSUED HISTORY:

+---------+---------+-----------------+---------------+-------------+
| user_id | book_id |    book_name    |      ISBN     | issued_date |
+---------+---------+-----------------+---------------+-------------+
|   128   |   1515  | the jungle book | 9780194227469 |  2023-12-04 |
+---------+---------+-----------------+---------------+-------------+
show extended table (y/n):	n

=====================================
          CHOOSE A FIELD:       
=====================================
1. ISSUE BOOKS
2. RETURN BOOKS
3. ISSUED BOOKS HISTORY
4. WISHLIST
5. BOOK REVIEWS
6. ACCOUNT
7. EXIT
enter choice:	5

=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. write book review
2. update book reviews
3. search reviews
4. view book reviews
5. delete book review
6. return to previous menu
enter choice:	1
would you like to see the books available in library before writing a review (y/n):	n

WRITE A BOOK REVIEW:-
enter book title:	the jungle book
enter rating (out of 5):	5
enter a short review (max 150 words):	the jungle book is an amazing book for all ages and people. i highly recommend as a light-hearted read.
BOOK REVIEW ADDED


=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. write book review
2. update book reviews
3. search reviews
4. view book reviews
5. delete book review
6. return to previous menu
enter choice:	3

SEARCH YOUR REVIEWS:-
enter title to search:	the jungle book
Traceback (most recent call last):
  File "D:\g12\cs\sql stuff\MAIN.py", line 371, in <module>
    mainuser(userid)
  File "D:\g12\cs\sql stuff\MAIN.py", line 325, in mainuser
    reviewsuser(userid)
  File "D:\g12\cs\sql stuff\MAIN.py", line 198, in reviewsuser
    reviews.searchreviewuser(userid)
  File "D:\g12\cs\sql stuff\treviews.py", line 86, in searchreviewuser
    title = int(input('enter title to search:\t'))
ValueError: invalid literal for int() with base 10: 'the jungle book'

====================================== RESTART: D:\g12\cs\sql stuff\MAIN.py ======================================
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
__      _____ _    ___ ___  __  __ ___    _____ ___  
\ \    / / __| |  / __/ _ \|  \/  | __|  |_   _/ _ \ 
 \ \/\/ /| _|| |_| (_| (_) | |\/| | _|     | || (_) |
  \_/\_/ |___|____\___\___/|_|  |_|___|    |_| \___/ 
                                                     

  ___   _   _  _____    __        ___  _____   ___      _ 
 / _ \ /_\ | |/ / __|  / _|___   |   \| __\ \ / ( )___ | |
| (_) / _ \| ' <\__ \  > _|_ _|  | |) | _| \ V /|/(_-< |_|
 \___/_/ \_\_|\_\___/  \_____|   |___/|___| |_|   /__/ (_)
                                                          

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	2
enter username:	lulu lemon
enter password:	lulu123
successful sign-in
user id:	 128

=====================================
          CHOOSE A FIELD:       
=====================================
1. ISSUE BOOKS
2. RETURN BOOKS
3. ISSUED BOOKS HISTORY
4. WISHLIST
5. BOOK REVIEWS
6. ACCOUNT
7. EXIT
enter choice:	5

=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. write book review
2. update book reviews
3. search reviews
4. view book reviews
5. delete book review
6. return to previous menu
enter choice:	3

SEARCH YOUR REVIEWS:-
enter title to search:	the jungle book
RECORD FOUND:
SNO:	 4
USER ID:	 128
TITLE:	 the jungle book
RATING:	 5
REVIEW:
 the jungle book is an amazing book for all ages and people. i highly recommend as a light-hearted read.
REVIEW DATE:	 2023-12-04


=====================================
        BOOK REVIEWS DETAILS         
=====================================
1. write book review
2. update book reviews
3. search reviews
4. view book reviews
5. delete book review
6. return to previous menu
enter choice:	6

=====================================
          CHOOSE A FIELD:       
=====================================
1. ISSUE BOOKS
2. RETURN BOOKS
3. ISSUED BOOKS HISTORY
4. WISHLIST
5. BOOK REVIEWS
6. ACCOUNT
7. EXIT
enter choice:	6

=====================================
       LIBRARY ACCOUNT DETAILS       
=====================================
1. view account
2. insert account details
3. update account details
4. delete account
5. return to previous menu
enter choice:	2

INSERT ACCOUNT DETAILS:-
1. insert name
2. insert date of birth
3. insert email ID
4. insert phone num
5. exit
enter choice:	1
enter new members name:	lulu lemon
DETAILS INSERTED


INSERT ACCOUNT DETAILS:-
1. insert name
2. insert date of birth
3. insert email ID
4. insert phone num
5. exit
enter choice:	2
enter date of birth (yyyy-mm-dd):	2001-12-12
DETAILS INSERTED


INSERT ACCOUNT DETAILS:-
1. insert name
2. insert date of birth
3. insert email ID
4. insert phone num
5. exit
enter choice:	3
enter email ID:	lululem@gmail.com
DETAILS INSERTED


INSERT ACCOUNT DETAILS:-
1. insert name
2. insert date of birth
3. insert email ID
4. insert phone num
5. exit
enter choice:	5

=====================================
       LIBRARY ACCOUNT DETAILS       
=====================================
1. view account
2. insert account details
3. update account details
4. delete account
5. return to previous menu
enter choice:	1

ACCOUNT DETAILS:

+---------+------------+------------+----------+------------+-------------------+-----------+---------------+--------------+
| user_id |    name    |  username  | password |    dob     |      mail_id      | phone_num | members_since | books_issued |
+---------+------------+------------+----------+------------+-------------------+-----------+---------------+--------------+
|   128   | lulu lemon | lulu lemon | lulu123  | 2001-12-12 | lululem@gmail.com |    None   |   2023-12-04  |     None     |
+---------+------------+------------+----------+------------+-------------------+-----------+---------------+--------------+

=====================================
       LIBRARY ACCOUNT DETAILS       
=====================================
1. view account
2. insert account details
3. update account details
4. delete account
5. return to previous menu
enter choice:	4

DELETE ACCOUNT:-
are you sure you want to delete your account?
you will lose all existing data, (y/n):	n
ACCOUNT NOT DELETED

=====================================
       LIBRARY ACCOUNT DETAILS       
=====================================
1. view account
2. insert account details
3. update account details
4. delete account
5. return to previous menu
enter choice:	5

=====================================
          CHOOSE A FIELD:       
=====================================
1. ISSUE BOOKS
2. RETURN BOOKS
3. ISSUED BOOKS HISTORY
4. WISHLIST
5. BOOK REVIEWS
6. ACCOUNT
7. EXIT
enter choice:	4

=====================================
        USER WISHLIST DETAILS         
=====================================
1. request a book
2. view your wishlist
3. search your wishlist
4. return to previous menu
enter choice:	2

YOUR WISHLIST BOOKS:

+-----+---------+-------+------+-------------+-------+--------+
| sno | user_id | title | ISBN | author_name | genre | status |
+-----+---------+-------+------+-------------+-------+--------+
+-----+---------+-------+------+-------------+-------+--------+

=====================================
        USER WISHLIST DETAILS         
=====================================
1. request a book
2. view your wishlist
3. search your wishlist
4. return to previous menu
enter choice:	4

=====================================
          CHOOSE A FIELD:       
=====================================
1. ISSUE BOOKS
2. RETURN BOOKS
3. ISSUED BOOKS HISTORY
4. WISHLIST
5. BOOK REVIEWS
6. ACCOUNT
7. EXIT
enter choice:	2

RETURN A BOOK:	
enter book ID to be returned:	128
book ID has not been issued, please enter a valid book ID
enter book ID to be returned:	
an error occurred: "invalid literal for int() with base 10: ''"


=====================================
          CHOOSE A FIELD:       
=====================================
1. ISSUE BOOKS
2. RETURN BOOKS
3. ISSUED BOOKS HISTORY
4. WISHLIST
5. BOOK REVIEWS
6. ACCOUNT
7. EXIT
enter choice:	1
would you like to see the books available in library (y/n):	y

BOOK CATALOG:

+-----+---------+---------------------------------------+------------------------+--------------------+------------------+--------------+-----------+---------------+
| sno | book_id |                 title                 |      author_name       |       genre        | publication_date | availability | frequency |      ISBN     |
+-----+---------+---------------------------------------+------------------------+--------------------+------------------+--------------+-----------+---------------+
|  3  |   789   |                  1984                 |     george orwell      |     dystopian      |    1949-06-08    |  available   |     1     | 9780140817744 |
|  7  |   404   | harry potter and the sorcerer's stone |      j.k. rowling      |      fantasy       |    1997-06-26    |  available   |     3     | 9780439362139 |
|  11 |   808   |           gone with the wind          |   margaret mitchell    | historical fiction |    1936-06-30    |  available   |     1     | 9780582418059 |
|  12 |   909   |     one hundred years of solitude     | gabriel garcia marquez |  magical realism   |    1967-05-30    |  available   |     1     | 9780060114183 |
|  15 |   1212  |       the count of monte cristo       |    alexandre dumas     |     adventure      |    1844-08-28    |  available   |     1     | 9780199219650 |
|  16 |   1313  |            brave new world            |     aldous huxley      |     dystopian      |    1932-02-02    |  available   |     1     | 9780582060166 |
|  17 |   1414  |       the picture of dorian gray      |      oscar wilde       |   gothic fiction   |    1890-07-20    |  available   |     2     | 9789875503229 |
|  20 |   1717  |               the hobbit              |     j.r.r. tolkien     |      fiction       |    1937-09-21    |  available   |     3     | 9780007525508 |
+-----+---------+---------------------------------------+------------------------+--------------------+------------------+--------------+-----------+---------------+

ISSUE A BOOK:-
enter book ID:	789
enter user ID:	128
BOOK ISSUED


=====================================
          CHOOSE A FIELD:       
=====================================
1. ISSUE BOOKS
2. RETURN BOOKS
3. ISSUED BOOKS HISTORY
4. WISHLIST
5. BOOK REVIEWS
6. ACCOUNT
7. EXIT
enter choice:	3

ISSUED HISTORY:

+---------+---------+-----------------+---------------+-------------+
| user_id | book_id |    book_name    |      ISBN     | issued_date |
+---------+---------+-----------------+---------------+-------------+
|   128   |   1515  | the jungle book | 9780194227469 |  2023-12-04 |
|   128   |   789   |       1984      | 9780140817744 |  2023-12-04 |
+---------+---------+-----------------+---------------+-------------+
show extended table (y/n):	n

=====================================
          CHOOSE A FIELD:       
=====================================
1. ISSUE BOOKS
2. RETURN BOOKS
3. ISSUED BOOKS HISTORY
4. WISHLIST
5. BOOK REVIEWS
6. ACCOUNT
7. EXIT
enter choice:	7
THANK YOU

=========================
MENU
1. ADMINISTRATION
2. USER SIGN-IN
3. USER REGISTERATION
4. EXIT
=========================

enter choice:	4

✿ THANK YOU ✿

COME AGAIN TO 
🎄🎄 OAKS & DEY's 🎄🎄 
WE AWAIT YOUR NEXT ENTRY!

