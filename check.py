
import itertools
import sys
def getIn():
    line = ''
    with open('node.txt','r+') as file:
        line=file.readlines()

    nwls = list(line)
    #print('-------->>>>>',nwls)
    cap = nwls[0].replace(']','')
    cap = cap.replace('[','')
    #print(cap)
    nwls = cap.split(',')
    nwls = [int(a) for a in nwls]
    code = input(' ---: ')
    if code == 'exit':
        sys.exit(0)
    elif code == 'null':
        print('no __ solution __')
    else:
        ols = code.split(',')
        onls = [int(a) for a in ols]
        #print('onls --->',onls)
        num=len(onls)
        answer = tuple(onls)
        print(answer)
        setA = itertools.permutations(nwls,num)
        for v in setA:
            #print(v,type(v))
            if answer in v or answer == v and sum(answer) == 100 and sum(v) == 100:
                print("Answer",True)




