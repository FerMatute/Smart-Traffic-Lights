import numpy as np

num = np.arange(100)
total = np.arange(10)


for i in num:
    if len(total) == 10:
        print("full")
        total[:9] = total[1:]
        total[9] = i
        
    else:
        total[i] = i

print(total)