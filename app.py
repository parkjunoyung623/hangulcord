import re

code = open('봇', encoding = 'utf-8').read()

# ================================================================================ #
dic = {
    'str' : {
        '메시지 도착하면' : 
'''
@client.event
async def on_message(message):
''',
        '만약 메시지 전체' : 
'''
    if message.content == '%_variable_%':
''',
        '메시지 보내기' : 
'''
        await client.send_message(message.channel, '%_variable_%')
'''
    },
    're' : {
        '만약 메시지 전체' : r'만약 메시지 = (?P<content>(.*?)):',
        '메시지 보내기' : r'메시지 보내기 \((?P<content>(.*?))\)'
    }
}

# ================================================================================ #

code = code.replace('메시지 도착하면:', dic['str']['메시지 도착하면'])
code = re.sub(
    dic['re']['만약 메시지 전체'],
    dic['str']['만약 메시지 전체'].replace('%_variable_%', 
        re.compile(dic['re']['만약 메시지 전체']).search(code).group('content')
    ),
    code
)
code = re.sub(
    dic['re']['메시지 보내기'],
    dic['str']['메시지 보내기'].replace('%_variable_%', 
        re.compile(dic['re']['메시지 보내기']).search(code).group('content')
    ),
    code
)

# ================================================================================ #

native = '''
# -*- coding: utf-8 -*-
import discord

client = discord.Client()

{code}

def discord_run():
    client.run('{token}')
'''.format(code = code, token = open('key', encoding = 'utf-8').read())

with open('rendered.py', 'w', encoding = 'utf-8') as f:
    f.write(native)

import rendered
rendered.discord_run()