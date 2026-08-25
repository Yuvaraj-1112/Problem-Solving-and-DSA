a = [5,2,6,8,9,1]
l,r = 1,5

preSum = [0]*len(a)
preSum[0] = a[0]

for i in range(1,len(a)):
    preSum[i] = preSum[i-1] + a[i]

print(preSum[r] - preSum[l-1] if l else preSum[r])