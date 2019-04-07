# Module: Code Function

def getcontent(content = ''):
    spltd = content.split()
    content = ''
    for i in range(len(spltd)):
        if i != 0:
            if i != 1:
                content += ' '
            content += spltd[i]
    return content

if __name__ == '__main__':
    print(getcontent('안녕 세상아 ㅎㅎ'))