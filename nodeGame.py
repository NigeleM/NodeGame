


# Graph game 
# Developed by Nigele

import itertools
import networkx as nx
import matplotlib.pyplot as plt
import graph
import os , sys
import check
import random
def game():
    status = True
    nodes = []
    end = 100
    lowEnd = -100
    highEnd = 100
    stop = 0
    answer = []
    while status:
        place = random.randint(lowEnd,highEnd)
        operator = random.choice(['+','-'])
        num = random.choice([eval(f'{end}{operator}{place}'),eval(f'{place}{operator}{end}')])
        
        #print(num)
        if end == num and len(nodes) == 0:
            continue
        elif end == num and len(nodes) > 1 and len(nodes) < 14:
            nodes.append(num)
        elif len(nodes) == 14:
            #print(nodes)
            status = False
        elif len(nodes) < 14:
            nodes.append(num)

    random.shuffle(nodes)
    print(nodes)
    start = random.choice(nodes)
    score = 0 
    print('<-------- Node --------->',start)
    with open('node.txt','w+') as file:
        file.write(str(nodes))
    graph.display(nodes)
    os.system('open graph.png')
    check.getIn()
    
    
    
    
            
        

if sys.argv[1]:
    for num in range(int(sys.argv[1])):
        game()
else:
    game()
