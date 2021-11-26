#Codigo para resolver o problema Love Triangle no codeForces, https://codeforces.com/contest/939/problem/A
#Foi usado uma implementação do algoritmo Depth First Search com algumas modificações

quant = int(input())
lista = [int(x) for x in input().split()]

#Implementação de um algoritmo parecido com o depth first search usando iteração
def planesLove(graph, v): 
    stack = [v]
    trilha = [] 
    w = 0
    while len(stack) > 0:
        v = stack.pop()
        trilha.append(v)
        w = graph[v]
        if w not in trilha:
            stack.append(w)
        else:
            comeco = trilha.index(w)
            if len(trilha) - comeco == 3:
                return True
            else:
                return False
            
graph = {}
for i in range(quant):
    graph[i + 1] = lista[i]


#Executa o algoritmo. 
#Ele é executado de forma que se testa todos os pontos de partida.
listaverdade = []
for i in range(len(lista)):
    if planesLove(graph, i + 1):
        listaverdade.append(1)
    else:
        listaverdade.append(0)

if 1 in listaverdade:
    print('YES')
else:
    print('NO')


