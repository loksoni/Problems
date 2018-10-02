def missingNum(arr):
    misNum = 5050-int(sum(arr))
    print(misNum)

import random
a = list(range(1,101))
b = random.randint(0,100)
del a[b]
print(a)
missingNum(a)
