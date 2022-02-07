import heapq as pq
"""

• ‘green and blue died’ if both races died in the same round
• ‘green wins’ if the green army won the Deadly War, followed by one line for each surviving
soldier (in descending order)
• ‘blue wins’ if the blue army won the Deadly War, followed by one line for each surviving soldier
(in descending order)

"""

while 1:
    try:
        t = int(input())
    except EOFError:
        break
    for smth in range(t):
        dd =input()

        B, SG, SB = [int(x) for x in dd.split()]

        SGset = []
        SBset = []
        for i in range(SG):
            valor = int(input())
            #para que sea key value
            pq.heappush(SGset, -valor)
        for i in range(SB):
            valor = int(input())
            pq.heappush(SBset,-valor)
        
        while SGset and SBset:
            surv1 =[]
            surv2 = []
            for i in range(B):
                if not (SGset and SBset):
                    break
                un=-pq.heappop(SGset)
                dos = -pq.heappop(SBset)
                cual = un - dos
                otro = dos - un
               
                
                if cual > 0:
                    surv1.append(cual)
                if otro > 0:
                    surv2.append(otro)
            for val in surv1:
                pq.heappush(SGset, -val)
            for val in surv2:
                pq.heappush(SBset, -val)
            
        if len(SGset) == len(SBset):
            print('green and blue died')
        elif len(SGset) > len(SBset):
            print('green wins')
            for w in range(len(SGset)):
                print(-pq.heappop(SGset))
        else:
            print('blue wins')
            for x in range(len(SBset)):
                print(-pq.heappop(SBset))
        if smth != t-1:
            print()

            