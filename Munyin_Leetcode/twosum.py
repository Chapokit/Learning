
def twoSum(nums, target):
        
    done = False
    n = len(nums)
    output = []
    while done == False:
        for i in range(n):
            if done:
                break
            for j in range(i+1, n):
                if i == j:
                    pass
                sum = nums[i]+nums[j]
                if sum == target:
                    output.append(i)
                    output.append(j)
                    done = True
    print(output)

twoSum([3,2,4],6)