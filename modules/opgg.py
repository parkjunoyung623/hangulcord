# Module: Return OP.GG Search Result

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup as bs
import re

re_dict = {
    'profile_image' : re.compile(r'<img class="ProfileImage" src="(?P<profileimg>.*?)"\/>'),
    'lastupdate' : re.compile(r'<span class=.*?>(?P<datetime>.*?)<\/span>'),
    'tierrank' : re.compile(r'>(?P<tierrank>.*?)<'),
    'tiermedal' : re.compile(r'"(?P<tiermedal>\/\/opgg-static\.akamaized\.net\/images\/medals.*?)"')
}

def set_protocol(url):
    if url[0] == '/':
        return 'https:' + url

def get(username):
    target = 'https://www.op.gg/summoner/userName={}'.format(urllib.parse.quote(username))
    request = urllib.request.Request(target, headers={'User-Agent': 'Mozilla/5.0'})
    req_content = urllib.request.urlopen(request).read().decode('utf-8')

    result = {'__init__' : 'op.gg-lol', 'username' : username}

    if 'SummonerNotFoundLayout' in req_content:
        result['queryok'] = False
        return result

    soup = bs(req_content, 'html.parser')
    element = {
        'profile' : str(soup.find_all('div', {'class' : 'Header'})[0]),
        'lastupdate' : str(soup.find_all('div', {'class' : 'LastUpdate'})[0]),
        'solorank' : str(soup.find_all('div', {'class' : 'TierRank'})[0].decode_contents()),
        'solomedal' : str(soup.find_all('div', {'class' : 'TierBox'})[0])
    }

    result['profile_image'] = set_protocol(re_dict['profile_image'].search(element['profile']).group('profileimg'))
    result['lastupdate'] = re_dict['lastupdate'].search(element['lastupdate']).group('datetime')
    result['tierrank'] = (element['solorank'].replace('\t', '')).replace('\n', '')
    result['tiermedal'] = set_protocol(re_dict['tiermedal'].search(element['solomedal']).group('tiermedal'))
    result['queryok'] = True

    return result

if __name__ == '__main__':
    print(str(get('잘못된소환사명')))