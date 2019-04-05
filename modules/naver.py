import urllib.request
import re

class req:
    query = 'content'
    target = 'https://search.naver.com/search.naver?query={}'.format(query)
    re = {
        'full' : r'<li [^>]*id="sp_blog_1"[^>]*>(?P<src>[0-9a-zA-Zㄱ-ㅣ가-힣(?=.*[!@#$%^*()\-_=+\\\|\[\]{};:\'",.  *&<>\/?\n]*)<\/li>',
        'thumb' : '',
        'title' : '',
        'content' : ''
    }

    request = urllib.request.Request(target, headers={'User-Agent': 'Mozilla/5.0'})
    content = urllib.request.urlopen(request).read().decode('utf-8')
a = re.compile(req.re['full']).search(req.content)
print(a)
