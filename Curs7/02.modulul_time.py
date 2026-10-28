import time

nums = [1,2,3]

for i in range(len(nums)):
    nums.insert(i,i+1)
    print(nums)
    # Modulul sleep oprește functionarea programului pentru un anumit numar de secunde
    time.sleep(4)
