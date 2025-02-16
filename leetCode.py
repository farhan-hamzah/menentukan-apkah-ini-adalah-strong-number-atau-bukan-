import math
nums = int(input())
hasil = 0
num = nums
while nums > 0:
    c = nums%10
    hasil += math.factorial(c)
    nums = nums//10
if hasil ==  num:
    print(True)
else:
    print(False)