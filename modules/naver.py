# Module: Return NAVER Search Result

import os
import sys
import urllib.request
import urllib.parse
import json

key = json.loads(open(os.path.dirname(__file__) + '/../key.json').read())

def get(search_content):
    url = 'https://openapi.naver.com/v1/search/blog?query={}'.format(urllib.parse.quote(search_content))
    request = urllib.request.Request(url)
    request.add_header('X-Naver-Client-Id', key['naver_search_client_id'])
    request.add_header('X-Naver-Client-Secret', key['naver_search_client_secret'])
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print('Error Code:' + rescode)

if __name__ == '__main__':
    get('검색')
