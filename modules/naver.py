# Module: Return NAVER Search Result

import urllib.request
from bs4 import BeautifulSoup as bs
import re

class rem:
    img = re.compile(r'src="(?P<src>[0-9a-zA-Zㄱ-ㅣ가-힣(?=.*[!@#$%^&*();\-_=+\\\|\[\]{};:\'",.<>\/?]*)"')

class req:
    query = 'content'
    target = 'https://search.naver.com/search.naver?query={}'.format(query)

    request = urllib.request.Request(target, headers={'User-Agent': 'Mozilla/5.0'})
    content = urllib.request.urlopen(request).read().decode('utf-8')


soup = {'full' : bs(req.content, 'html.parser')}
content = soup['full'].find_all('li', {'class' : 'sh_blog_top'})

search_result = []
tmp = {}
for i in range(3):
    tmp = {}
    soup['obj'] = bs(str(content[i]), 'html.parser')
    tmp['content'] = soup['obj'].find('li')
    # thumbnail
    soup['obj-thumb'] = bs(str(tmp['content']), 'html.parser')
    tmp['thumb'] = str(soup['obj-thumb'].find('img', {'class' : 'sh_blog_thumbnail'}))
    tmp['thumb_url'] = rem.img.search(tmp['thumb']).group('src')
    # common
    # title
    # content
    # result
    search_result += {
        'thumbnail' : tmp['thumb_url'],
        'title' : '',
        'content' : ''
    }
    print(tmp['thumb_url'])
tmp = {}
