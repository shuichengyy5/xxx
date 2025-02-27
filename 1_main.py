#202410111303
#3331592296@qq.com
#余洋
print('Hello World')
def calculate_jewels(jewels,stones):
    jewel_count=0
    for stone in stones:
        if stone in jewels:
            jewel_count+=1
    return jewel_count

input_jewels,input_stones=input("").split(',')

result=calculate_jewels(input_jewels,input_stones)

print(result)
