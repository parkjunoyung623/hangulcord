# Module: Return NAVER Search Result

import os
import sys
import urllib.request
import urllib.parse
import json

try:
    key = json.loads(open(os.path.dirname(__file__) + '/../key.json').read())
except:
    pass

def get(search_content):
    url = 'https://openapi.naver.com/v1/search/blog?query={}'.format(urllib.parse.quote(search_content))
    request = urllib.request.Request(url)
    request.add_header('X-Naver-Client-Id', key['naver_search_client_id'])
    request.add_header('X-Naver-Client-Secret', key['naver_search_client_secret'])
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        result = response.read().decode('utf-8')
        result['__init__'] = 'naver'
        result['status'] = 200
        print(result)
    else:
        result['__init__'] = 'naver'
        result['status'] = 0
        print('Error Code:' + rescode)

if __name__ == '__main__':
    key = json.loads(open('key.json').read())
    get('검색')