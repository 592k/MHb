# code reviewed at 11-05-2022 09:24 by.syoh5188

import random
li = [0,1,2]
n1 = 0
n2 = 0
for i in range(1000):
  ran = random.sample(li,3)
  u = ran[0]
  m = ran[1]
  if u == 2:
    n1 = n1+1
  elif u != 2 and m != 2:
    n2 = n2+1
print(n1/1000)
print(n2/1000)

# result : 0.312, 0.362 result checked!! 
