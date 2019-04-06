import urllib.request
from bs4 import BeautifulSoup as bs
import re

class rem:
    img = r'src="(?P<src>[0-9a-zA-Zㄱ-ㅣ가-힣(?=.*[!@#$%^*()\-_=+\\\|\[\]{};:\'",.<>\/?]*)"'

class req:
    query = 'content'
    target = 'https://search.naver.com/search.naver?query={}'.format(query)

    request = urllib.request.Request(target, headers={'User-Agent': 'Mozilla/5.0'})
    content = urllib.request.urlopen(request).read().decode('utf-8')


soup = {'full' : bs(req.content, 'html.parser')}
content = soup['full'].find_all('li', {'class' : 'sh_blog_top'})

tmp = {}
for i in range(len(content)):
    print(content[i])
    bs(content[i], 'html.parser')
    #soup['obj'] = bs(content[i], 'html.parser')
    #tmp['content'] = soup.find('li')
    #soup['obj-thumb'] = bs(tmp['content'], 'html.parser')
    #tmp['thumb'] = soup.find('img', {'class' : 'sh_blog_thumbnail'})
    #tmp['re'] = re.compile(img)
    #tmp['res-thumb'] = tmp['re'].group('src')
    #print(tmp['res-thumb'])
tmp = {}
