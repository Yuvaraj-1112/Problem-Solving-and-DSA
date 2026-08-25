'''
arr = [2,1,5,1,3,2]
 k = 3 
 
 Answer = 9
 explanation : 5 + 1 + 3 = 9  '''

def max_num_subarray(arr, k):
   window_sum = sum(arr[:k])
   ans = window_sum

   for i in range(k,len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        ans = max(ans, window_sum)

   print(ans)

arr = [2,1,5,1,3,2]
k = 3

max_num_subarray(arr,k)
