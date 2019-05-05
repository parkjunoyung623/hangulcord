import urllib.request
import urllib.parse
from bs4 import BeautifulSoup as bs
import re

target = 'https://search.naver.com/search.naver?query={}'.format(urllib.parse.quote('날씨'))
re_dict = {
    'degree' : re.compile(r'<span class="todaytemp">(?P<temp>.*?)<\/span>'),
    'minmax' : re.compile(r'<span class="merge">.*?<span class="min">.*?<span class="num">(?P<min>.*?)<\/span>.*?˚.*?<\/span>.*?<span class="slash">.*?\/.*?<\/span>.*?<span class="max">.*?<span class="num">(?P<max>.*?)<\/span>.*?˚.*?<\/span>.*?<\/span>'),
    'subgre' : re.compile(r'<div class="sub_info">.*?<div class="detail_box">.*?<dl class="indicator">.*?<dt>.*?<a.*?미세먼지<\/a><\/dt>.*?<dd class="lv(?P<dust_lv>.*?)">.*?<span class="num">(?P<dust>.*?)<\/span>(?P<dust_kor>.*?)<span class="ico"><\/span><\/dd>.*?<dt>.*?<a.*?초미세먼지<\/a>.*?<\/dt>.*?<dd class="lv(?P<smalldust_lv>.*?)">.*?<span class="num">(?P<smalldust>.*?)<\/span>(?P<smalldust_kor>.*?)<span class="ico">.*?<\/span>.*?<\/dd>.*?<dt>.*?<a.*?오존지수<\/a>.*?<\/dt>.*?<dd class="lv(?P<ozon_lv>.*?)">.*?<span class="num">(?P<ozon>.*?)<\/span>(?P<ozon_kor>.*?)<span class="ico">.*?<\/span>.*?<\/dd>.*?<\/dl>.*?<\/div>.*?<\/div>')
}
request = urllib.request.Request(target, headers={'User-Agent': 'Mozilla/5.0'})

def get():
    req_content = urllib.request.urlopen(request).read().decode('utf-8')

    soup = bs(req_content, 'html.parser')
    content = str(soup.find_all('div', {'class' : 'today_area'})[0])

    result = {'__init__' : 'weather', 'degree' : {}, 'detail' : {'dust' : {}, 'smalldust' : {}, 'ozon' : {}}}
    result['degree']['now'] = re_dict['degree'].search(content).group('temp')
    result['degree']['sub'] = re_dict['minmax'].search(content)
    result['degree']['max'] = result['degree']['sub'].group('max')
    result['degree']['min'] = result['degree']['sub'].group('min')
    result['degree']['sub'] = 0
    result['detail']['nat'] = re_dict['subgre'].search(content)
    result['detail']['dust']['degree'] = result['detail']['nat'].group('dust')
    result['detail']['dust']['evel'] = result['detail']['nat'].group('dust_kor')
    result['detail']['dust']['level'] = int(result['detail']['nat'].group('dust_lv'))
    result['detail']['smalldust']['degree'] = result['detail']['nat'].group('smalldust')
    result['detail']['smalldust']['evel'] = result['detail']['nat'].group('smalldust_kor')
    result['detail']['smalldust']['level'] = int(result['detail']['nat'].group('smalldust_lv'))
    result['detail']['ozon']['degree'] = result['detail']['nat'].group('ozon')
    result['detail']['ozon']['evel'] = result['detail']['nat'].group('ozon_kor')
    result['detail']['ozon']['level'] = int(result['detail']['nat'].group('ozon_lv'))
    result['detail']['nat'] = 0

    return result

if __name__ == '__main__':
    get()