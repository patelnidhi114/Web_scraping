import bs4
from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq

my_url = 'https://www.newegg.com/p/pl?d=graphics+card'
uclient = uReq(my_url)
page_html = uclient.read()
uclient.close()
# HTML parse using soup  cadsfccxx
page_soup = soup(page_html,"html.parser")
container = page_soup.findAll("div",{"class":"item-container"})