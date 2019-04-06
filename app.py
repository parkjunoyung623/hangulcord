import re
from conv.py import *

code = open('봇', encoding = 'utf-8').read()

# ================================================================================ #


code = code.replace('메시지 도착하면:', dic['str']['message_recevied'])
code = re.sub(
    dic['re']['if_message'],
    dic['str']['if_message'].replace('%_variable_%', re.compile(dic['re']['if_message']).search(code).group('content')),
    code
)
code = re.sub(
    dic['re']['send_message'],
    dic['str']['send_message'].replace('%_variable_%', re.compile(dic['re']['send_message']).search(code).group('content')),
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