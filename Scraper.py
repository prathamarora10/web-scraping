from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('/Users/prathamarora/Downloads/Python_Projects/webScraping copy 2/chromedriver')
browser.get(START_URL)
time.sleep(10)

def scraper():
    header = ['Proper Name', 'Distannce','Mass','Radius']
    planet_data = []

    for i in range(0, 1):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
    with open("scrapper_3.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(header)
        csvwriter.writerows(planet_data)
        
scraper()