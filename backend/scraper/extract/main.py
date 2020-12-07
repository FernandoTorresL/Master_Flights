import argparse
import logging
#import csv
#import datetime
#import time

# Import config file
from common import config

#Import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select

# Get a reference to logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def _website_scraper(website_uid):
    # Get the url of the website (parameter)
    host = config()['websites'][website_uid]['url']
    logging.info('Beginning scraper for {}'.format(host))

    driver = webdriver.Chrome(executable_path='../../../../../chromedriver/v87/chromedriver')

    # Get the site (driver)
    driver.get(host)

    driver.close()
    logging.info('Ending scraper for {}'.format(host))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Build the list of choices
    websites_choices = list(config()['websites'].keys())
    parser.add_argument('website',
                        help='Argument: The website that you want to scrape',
                        type=str,
                        choices=websites_choices)

    # Parser the arguments
    args = parser.parse_args()
    _website_scraper(args.website)
