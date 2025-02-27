#202410111303
#3331592296@qq.com
#余洋
def calculate_sum(nums):
    while len(nums)>1:
        new_nums=[(nums[i] + nums[i+1]) % 10 for i in range(len(nums)-1)]
        nums=new_nums
    return nums[0]

input_nums=input("")
nums=list(map(int,input_nums.split(',')))

result=calculate_sum(nums)

print(result)
