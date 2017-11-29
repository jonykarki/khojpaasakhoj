# import the module
import psycopg2 as db
import datetime

# create a class called database
class InsertDatabase():

    def __init__(self, bimg, btype, bname, bservices, bphoneno, baddress, bowner, bemail, bwebsite):
        self.bimg = bimg
        self.btype = btype
        self.bname = bname
        self.bservices = bservices
        self.bphoneno = bphoneno
        self.baddress = baddress
        self.bowner = bowner
        self.bemail = bemail
        self.bwebsite = bwebsite

        #connect to the database
        self.conn = db.connect('dkc2gr094item')

        # get the cursor
        self.c = self.conn.cursor()

    # insert into the database
    def insert_into_database(self):
        self.c.execute("INSERT INTO khoj_post VALUES (NULL, '{}','{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}' )"
                                    .format(self.bimg, self.btype, self.bname, self.bservices, self.bphoneno, self.baddress, self.bowner, self.bemail, self.bwebsite, datetime.datetime.now()))

        self.conn.commit()
        self.conn.close()
        print("INSERTED " + self.bname + " into database!!!")
        print("*"*100 + " \n")

    # check if the data is already in the database
    def data_in_database(self):
        self.c.execute("SELECT * FROM khoj_post WHERE bname=? AND bphoneno=?", (self.bname, self.bphoneno))
        self.result = self.c.fetchone()
        if(self.result == None):
            return False
        if(self.result != None):
            return True