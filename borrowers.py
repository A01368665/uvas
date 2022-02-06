j = 1
while 1:
  try:
    f = input()
  except EOFError:
    break
    #si hay en set agregalo al stack del set
    #si ya tiene stack se lo agregas al stack
    #si la letra es menor que anterior o igual, subelo al stack
    #supongamos que siempre que sea menor se puede meter a stack
    #lleva un track de los stacks
  if f == "end":
    break
  
  letters = set()
  sum = 1

  stacks = []
  for letter in f:
    flags = False
    for i in range(len(stacks)):
      if letter <= stacks[i][-1]:
        stacks[i].append(letter)
        flags = True
        break
    if not flags:
      stacks.append([letter])
    
      
   
  print(f"Case {j}: {len(stacks)}")
  j+=1


       

  