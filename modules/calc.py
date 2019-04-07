# Module: Return Calcurate Result

import re

def calc(content = ''):
    re_var = re.compile(r'[0-9*+-\/]')
    matchobj = re_var.findall(content)

    content_removed = content
    for i in range(len(matchobj)):
        content_removed = content_removed.replace(matchobj[i], '')

    template = '''
# -*- coding: utf-8 -*-
def calc():
    return {}
    '''.format(content)

    if content_removed:
        return (False, 0)
    else:
        with open('calc_rendered.py', 'w', encoding='utf-8') as f:
            f.write(template)
        import calc_rendered as cr
        return (True, cr.calc())

if __name__ == '__main__':
    print(calc('355-6*988+356+65658'))