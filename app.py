import re
import json
from conv import *

code = open('봇', encoding = 'utf-8').read()

# ================================================================================ #


code = code.replace('메시지 도착하면:', dic['str']['message_recevied'])

find = re.compile(dic['re']['if_message']).findall(code)
for find_obj in find:
    code = code.replace(
        find_obj[0], dic['str']['if_message'].replace(
            '%_variable_%', 
            re.compile(dic['re']['if_message']).search(code).group('content')
            )
        )

find = re.compile(dic['re']['if_startswith']).findall(code)
for find_obj in find:
    code = code.replace(
        find_obj[0], dic['str']['if_startswith'].replace(
            '%_variable_%', 
            re.compile(dic['re']['if_startswith']).search(code).group('content')
            )
        )

find = re.compile(dic['re']['calc']).findall(code)
for find_obj in find:
    code = code.replace(
        find_obj[0], dic['str']['calc'].replace(
            '%_variable_%', 
            re.compile(dic['re']['calc']).search(code).group('content')
            )
        )

find = re.compile(dic['re']['opgg']).findall(code)
for find_obj in find:
    code = code.replace(
        find_obj[0], dic['str']['opgg'].replace(
            '%_variable_%', 
            re.compile(dic['re']['opgg']).search(code).group('content')
            )
        )


find = re.compile(dic['re']['search_naver']).findall(code)
for find_obj in find:
    code = code.replace(
        find_obj[0], dic['str']['search_naver'].replace(
            '%_variable_%', 
            re.compile(dic['re']['search_naver']).search(code).group('content')
            )
        )


find = re.compile(dic['re']['send_result']).findall(code)
for find_obj in find:
    search = re.compile(dic['re']['send_result']).search(code)
    if search != None:
        code = code.replace(
            find_obj[0], dic['str']['send_result'].replace(
                '%_variable_%', 
                re.compile(dic['re']['send_result']).search(code).group('content')
                )
            )

find = re.compile(dic['re']['send_message']).findall(code)
for find_obj in find:
    code = code.replace(
        find_obj[0], dic['str']['send_message'].replace(
            '%_variable_%', 
            re.compile(dic['re']['send_message']).search(code).group('content')
            )
        )


code = re.sub(
    dic['re']['get_content'],
    dic['str']['get_content'],
    code
)

code = re.sub(
    dic['re']['weather'],
    dic['str']['weather'],
    code
)
# ================================================================================ #

native = '''
# -*- coding: utf-8 -*-
import discord
import modules.common
import modules.naver
import modules.weather
import modules.calc
import modules.opgg

client = discord.Client()

@client.event
async def on_ready():
    print('봇 시작됨.')
    print('봇 이름: ' + client.user.name)
    print('봇 아이디: ' + str(client.user.id))
    print('------')
    await client.change_presence(activity=discord.Game(name='안녕하세요!'))

{code}

def discord_run():
    client.run('{token}')

if __name__ == '__main__':
    discord_run()
'''.format(code = code, token = json.loads(open('key.json', encoding='utf-8').read())['discord_bot_token']
)

with open('rendered.py', 'w', encoding = 'utf-8') as f:
    f.write(native)

import rendered
rendered.discord_run()
