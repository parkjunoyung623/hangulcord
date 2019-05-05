dic = {
    'str' : {
        'message_recevied' : 
'''
@client.event
async def on_message(message):
    if message.content == '봇 종료':
        await message.channel.send('안녀엉!')
        print('봇 종료됨.')
        exit()
''',

        'if_message' : 'if message.content == "%_variable_%" and client.user.id != message.author.id:',
        'if_startswith' : 'if message.content.startswith("%_variable_%") and client.user.id != message.author.id:',
        'get_content' : 'modules.common.getcontent(message.content)',
        'send_message' : 'await message.channel.send("%_variable_%")',
        'send_result' : 'await message.channel.send("", embed=%_variable_%)',
        'search_naver' : 'modules.naver.request(%_variable_%)',
        'calc' : 'modules.common.get_fancy(modules.calc.calc(%_variable_%))',
        'weather' : 'modules.common.get_fancy(modules.weather.get())'
    },
    're' : {
        'if_message' : r'(?P<fullmatch>만약 메시지 = (?P<content>(.*?)):)',
        'if_startswith' : r'(?P<fullmatch>만약 메시지 시작부분 = (?P<content>(.*?)):)',
        'get_content' : r'내용 가져오기 \(\)',
        'send_message' : r'(?P<fullmatch>내용 보내기 \((?P<content>(.*?))\))',
        'send_result' : r'(?P<fullmatch>결과 내용 보내기 \((?P<content>(.*?))\))',
        'search_naver' : r'(?P<fullmatch>네이버에 검색 \((?P<content>(.*?))\))',
        'calc' : r'(?P<fullmatch>계산 \((?P<content>(.*?))\))',
        'weather' : r'날씨 검색(.*?)\(\)'
    }
}