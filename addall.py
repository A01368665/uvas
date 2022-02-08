
import heapq as pq
while 1:
    try:
        s = int(input())
    except EOFError:
        break
    if s == 0:
        break
    pri = []
    entr = [int(x) for x in input().split()]
    for value in entr:
        pq.heappush(pri,value)
    costo = 0
    
    while pri:

        if len(pri) == 1:
            break
        ant = pq.heappop(pri)
        dos = pq.heappop(pri)
        
        costo+=ant+dos
        ant = ant+dos
        pq.heappush(pri,ant)
    print(costo)

        