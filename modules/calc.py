def calc(variable):
    result = {'__init__' : 'calculate', 'variable' : variable}

    try:
        result['value'] = eval(variable)
        result['calced'] = True
    except SyntaxError:
        result['calced'] = False
        result['display'] = '이건.. 문제가 있는 식인것 같은데요?'
    except NameError:
        result['calced'] = False
        result['display'] = '이건 식이 아니잖아요.'
    except:
        result['calced'] = False
        result['display'] = '자꾸 이상한거 계산하려고 하지마세요.'
    return result