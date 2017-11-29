from django.test import TestCase
from .scrape import Scraper
# Create your tests here.


data = Scraper("restaurant", "thamel", 1)
data.scrape()