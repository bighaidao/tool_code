import urllib,urllib2
import re
#下载 andrew moor 课件 脚本
from BeautifulSoup import BeautifulSoup
#urllib.urlretrieve(url, filename)
hosts=["http://www.cedar.buffalo.edu/~srihari/CSE574/"]

page=urllib2.urlopen("http://www.zhizhihu.com/html/y2012/4057.html");

soup=BeautifulSoup(page)
#print soup.find("ol")
soup= soup.find("div","entry")
#print soup
patter=r"<li><a href=\"(.*?)\">(.*?)</a></li>"
#for index,item in enumerate(soup):
    #print item
p=re.compile(patter)
value=p.findall(str(soup))

for match in value:
    url= match[0]
    filename=match[1]
    text=urllib2.urlopen(url);
    text=BeautifulSoup(text)
    patter=r"<h3><a href=\"(.*?)\">(.*?)</a></h3>"
    p=re.compile(patter)
    fileurl=p.findall(str(text))
    if(fileurl):
        fileurl="http://www.autonlab.org/tutorials/"+str(fileurl[0][0])
        print fileurl
        urllib.urlretrieve(fileurl, "/home/hd/"+filename+".pdf")
#match = re.match(patter, str(soup))
#if(match):
#    print match.group()
#    print match.group(1)
#    print match.group(2)
