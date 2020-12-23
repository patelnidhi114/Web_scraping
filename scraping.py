import bs4
from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq

my_url = 'https://www.newegg.com/p/pl?d=graphics+card'
uclient = uReq(my_url)
page_html = uclient.read()
uclient.close()
# HTML parse using soup  cadsfccxx
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class":"item-container"})
filename = "product.csv"
f = open(filename,"w")
headers = "brand_name,product_description,shipping_info \n"
f.write(headers)
for container in containers:
    try:
        brand_name = container.div.div.a.img["title"]
    except:
        brand_name = ""
    try:
        product_description = container.div.findAll("a",{"class":"item-title"})[0].text 
    except:
        product_description = ""
    try:

        shiiping_info = container.findAll("li",{"class":"price-ship"})[0].text
    except:
        shiiping_info = ""
    # print("brand_name ",brand_name)
    # print("product_description",product_description)
    # print("shiiping_info",shiiping_info)
    f.write(brand_name + "," +product_description.replace(",","|") + "," + shiiping_info + "\n")