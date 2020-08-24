from tools.TextDisplay import *
import re

def readFile(path):
    with open(path, 'r', encoding="utf-8") as fp:
        for line in fp:
            parseFile(line)

def parseFile(line):
    '''刪除字串之左側空格'''
    line = line.lstrip()

    '''從第0個位置上是<#>的話代表這行是註解'''
    if line.find("<#>") == 0:
        return 

    '''Question題號
    ^ 從第0個位置開始匹配起
    '''
    Q_match = re.match(r'^Q[\d]+:', line)
    if Q_match:
        Q_num = Q_match.group(0)[1:-1]
        Q_text = line.replace(Q_match.group(0),'')
        return (Q_num, Q_text)
    

##    if line.find("<br>") != -1:
##        line_brList = line.split("<br>")
##        line = ""
##        for string in line_brList:
##            if string != '':
##                line = line + string +'\n'
##
##    if line.find("<DIE>") != -1:
##        line_die = line.split("<DIE>")
##        pass
##
##    if line.find("<GOTO>") != -1:
##        line_goto = line.split("<GOTO>")
##        pass

    distxt(line)

##def QN(Q_num, Q_text):
##    pass

readFile(".\\data\\Question")
