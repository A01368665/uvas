import heapq as hq
from sys import stdin

a = stdin.read().splitlines()

b = []

i = 0
while 1:
    reading = a[i]
    i+=1
    
    if reading == "#":
        break
    parts = reading.split()
   #aqui metes el tiempo luego metes las partes 1 y dos
    hq.heappush(b, (int(parts[2]), [int(parts[1]), int(parts[2])]))
    

k = int(a[i])

#el caso especial del cero no respeta nada, entonces
#para handlear el cero, lo que se hace es
#en ves de pushearle el valor + 0 le pusheas el valor + 1
#que hace que el cero valga casi lo mismo?
for m in range(k):
    value = hq.heappop(b)
    print(value[1][0])
    if value[0] == 0:
        hq.heappush(b, (value[0]+1,[value[1][0],1 ] ))
  
    else:
        hq.heappush(b, (value[0]+value[1][1],[value[1][0],value[1][1] ] ))
    


    

