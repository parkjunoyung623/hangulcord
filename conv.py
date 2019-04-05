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