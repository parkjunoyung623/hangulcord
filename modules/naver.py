# Module: Return NAVER Search Result

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup as bs
import re

class rem:
    img = re.compile(r'src="(?P<src>.*?]*)"')
    title = re.compile(r'<a.*?>(?P<src>.*)<\/a>')
    content = re.compile(r'<dd.*?passage.*?>(?P<src>.*)<\/dd>')
    
def replace_bold(content):
    content = content.replace('<strong class="hl">', '')
    return content.replace('</strong>', '')

def request(target, rt_range = 1):
    query = target
    target = 'https://search.naver.com/search.naver?query={}'.format(urllib.parse.quote(query))

    request = urllib.request.Request(target, headers={'User-Agent': 'Mozilla/5.0'})
    req_content = urllib.request.urlopen(request).read().decode('utf-8')

    soup = {'full' : bs(req_content, 'html.parser')}
    content = soup['full'].find_all('ul', {'class' : 'type01'})

    search_result = []
    tmp = {}
    for i in range(rt_range):
        # common
        search_result += [{
            'thumbnail' : '',
            'title' : '',
            'content' : ''
        }]
        tmp = {}
        soup['obj'] = bs(str(content[i]), 'html.parser')
        tmp['content'] = soup['obj'].find('li')
        # thumbnail
        soup['obj-thumb'] = bs(str(tmp['content']), 'html.parser')
        tmp['thumb'] = str(soup['obj-thumb'].find('img', {'class' : 'thumb'}))
        if rem.img.search(tmp['thumb']) != None:
            tmp['thumb_url'] = rem.img.search(tmp['thumb']).group('src')
            search_result[i]['thumbnail'] = tmp['thumb_url']
        else:
            search_result[i]['thumbnail'] = ''
        # title
        soup['obj-title'] = bs(str(tmp['content']), 'html.parser')
        tmp['title'] = str(soup['obj-title'].find('dt', {'class' : ''}))
        tmp['title_content'] = rem.title.search(tmp['title']).group('src')
        search_result[i]['title'] = replace_bold(tmp['title_content'])
        # content
        tmp['content_native'] = rem.content.search(str(tmp['content'])).group('src')
        search_result[i]['content'] = replace_bold(tmp['content_native'])
        # result
        # print(search_result[i])
    tmp = {}
    return search_result

if __name__ == '__main__':
    print(request('Note Gulim'))