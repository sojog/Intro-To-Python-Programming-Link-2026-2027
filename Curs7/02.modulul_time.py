import time

nums = [1,2,3]
for i in range(len(nums)):
    nums.insert(i,i+1)
    print(nums)
    time.sleep(4)
