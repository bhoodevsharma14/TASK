from bs4 import BeautifulSoup as bs
import requests
import re
import sys

class Scrapping:

    def __init__(self,url):
        self.url = url
        self.data = {
            "Social Links":[],
            "Email's":[],
            "Contact":[]
            }

    def pattern_initializer(self,social_media_list:list=["facebook","linkedin","twitter","youtube","instagram"])->None:
        self.social_media_regex = re.compile("|".join(social_media_list))
        self.email_regex = re.compile("mailto:")
        self.contact_regex = re.compile("tel:")

    def get_all_href(self):
        response_web = requests.get(self.url)
        beautified_html = bs(response_web._content,"html.parser")
        all_href = beautified_html.find_all(href=True)

        return all_href

    def extract_data(self,all_href)->dict:
        for ref in all_href:
            ref_value = ref['href']
            if self.social_media_regex.search(ref_value):
                self.data["Social Links"].append(ref_value)
            elif self.email_regex.search(ref_value):
                self.data["Email's"].append(ref_value)
            elif self.contact_regex.search(ref_value):
                self.data["Contact"].append(ref_value)
        
        return self.data

if __name__ == "__main__":
    
    # getting url of website from the user input
    try:
        web_url = sys.argv[1]
    except:
        web_url = "https://ful.io"


    scrap = Scrapping(web_url)

    scrap.pattern_initializer()
    
    hrefs = scrap.get_all_href()
    
    result = scrap.extract_data(hrefs)
    for k,v in result.items():
        print(f"{k}\n{v}\n")
