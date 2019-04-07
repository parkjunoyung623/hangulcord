dic = {
    'str' : {
        'message_recevied' : 
'''
@client.event
async def on_message(message):
''',

        'if_message' : 
'''
    if message.content == '%_variable_%':
''',
        'send_message' : 
'''
        await client.send_message(message.channel, '%_variable_%')
'''

    },
    're' : {
        'if_message' : r'만약 메시지 = (?P<content>(.*?)):',
        'send_message' : r'메시지 보내기 \((?P<content>(.*?))\)'
    }
}

# message_recevied      메시지 도착하면
# if_message            만약 메시지 전체
# send_message          메시지 보내기