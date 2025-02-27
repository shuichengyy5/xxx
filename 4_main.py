#202410111303
#3331592296@qq.com
#余洋
def arrange_device(bank):
    m=len(bank)
    n=len(bank[0])
    laser=0
  
    for i in range(m):
        devices_i = [j for j in range(n) if bank[i][j] == '1']
        
        for k in range(i + 1, m):
            devices_k = [j for j in range(n) if bank[k][j] == '1']
            
            if devices_i and devices_k:
                valid_device = True
                
                for l in range(i + 1, k):
                    
                    if any(bank[l][j] == '1' for j in range(n)):
                        valid_device = False
                        break
                
                if valid_device:
                    laser += len(devices_i) * len(devices_k)
    
    return laser

input_bank=input("").split(",")
result=arrange_device(input_bank)
print(result)
