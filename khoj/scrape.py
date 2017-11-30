# import all the required modules for scraping
from bs4 import BeautifulSoup
import requests
import datetime
from .models import *

#from .database import InsertDatabase

class Scraper():

    def __init__(self, q, _lt, userrange):
        self.q = q
        self._lt = _lt
        self.userrange = userrange

    
    #define scrape()
    def scrape(self):
        # create the base url
        BASE_URL = "https://www.bhetincha.com/search/?"
        BASE_WEB_URL = "https://www.bhetincha.com/"

        # ask the user what they want to search
        #TODO: PASS THESE VALUES FROM ANOTHER FUNCTION
        q = self.q
        _lt = self._lt
        userrange = self.userrange

        # create the search url that we'll use for scraping the website
        url = BASE_URL + "q=" + q + "&_lt=" + _lt

        for i in range(userrange):
            ### SCRAPER ###
            source = requests.get(url).text

            soup = BeautifulSoup(source, 'lxml')

            # return master_list containing business_list
            master_list = []

            # no of business counter
            j = 0

            # get the list of items from the page

            for item in soup.find_all('div', class_="list"):
                # print(item)

                # get the list-item
                # item = soup.find('div', class_='list')

                #get the image url
                img = str(item.find('div', class_='list_img').img)
                imgu = img.split("\"")[3]
                if "https://" in img: 
                    img_url = "Image Not Available"
                else:
                    img_url = BASE_WEB_URL + imgu

                # get the business type
                business_type = item.find('div', class_="list_cat").text

                # get the name of the business
                business_name = item.find('div', class_="list_title").a.text

                # get services of the business
                business_services = item.find('div', class_="list_desc").text.lstrip()

                other_infos = []
                i = 0
                # get other data
                for other_item in item.find_all('div', class_='list-info-item'):
                    other_infos.insert(i,other_item.text.lstrip())
                    # other_info = other_item.text.lstrip()
                    # print(other_info)
                    
                # finally add all the information in the business_list list
                business = []
                business.insert(0,img_url)
                business.insert(1,business_type)
                business.insert(2,business_name)
                business.insert(3,business_services)
                business.insert(4,other_infos)
                master_list.insert(j, business)
                j = j + 1


            # TODO: insert the above information into the database

            for infos in master_list:
                bimg = infos[0].encode("utf-8")
                btype = infos[1].encode("utf-8")
                bname = infos[2].replace("'", "").encode("utf-8")
                bservices = infos[3].encode("utf-8")
                try:
                    # there are spaces in phone no and dashes
                    # convert the string data type into int
                    bphoneno = int(infos[4][2].replace(" - ", "")).encode("utf-8")
                except:
                    bphoneno = 0

                # see if the address is available
                try:
                    baddress = infos[4][3].encode("utf-8")
                except:
                    baddress = "Address Not Available"

                # see if the owner is available
                try:
                    bowner = infos[4][4].encode("utf-8")
                except:
                    bowner = "Owner Not Available"

                bemail = "Not Available"
                bwebsite = "Not Available"
                
                # add to the database
                # do the check before adding 
                if Post.objects.filter(bname = str(bname)).exists():
                    print(str(bname) + " is already in the Database")
                    print("\n")
                
                else:
                    Post(None, bimg, btype, bname, bservices, bphoneno, baddress, bowner, bemail, bwebsite).save()
                    print("INSERTED " + str(bname) + " into the Database")
                    print("*"*100)
                


                # ### insert the data into the database development server ### 
                # id = InsertDatabase(bimg, btype, bname, bservices, bphoneno, baddress, bowner, bemail, bwebsite)
                
                # # first check if the data is already in the database if not insert it into the database
                # if(id.data_in_database() == True):
                #     print(bname + " is ALREADY in the Database")
                #     print("*"*100 + " \n")
                # if(id.data_in_database() == False):
                #     id.insert_into_database()

        