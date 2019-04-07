# Module: Code Function

import random

comment = {
    'calc' : ['어.. 답은 %_s_%?', '이정돈 쉽죠, %_s_%!'],
    'calc_no' : ['제가 계산할수 없을것 같은데요?', '이건 식이 아닌것 같은데..', '글쎄요.. 전 이게 계산식인것 같진 않네요.']
}
def getcontent(content = ''):
    spltd = content.split()
    content = ''
    for i in range(len(spltd)):
        if i != 0:
            if i != 1:
                content += ' '
            content += spltd[i]
    return content

def display_calc(result):
    if result[0]:
        return random.choice(comment['calc']).replace('%_s_%', str(result[1]))
    else:
        return random.choice(comment['calc_no'])

if __name__ == '__main__':
    print(getcontent('안녕 세상아 ㅎㅎ'))