nums = [3,3]
min=nums[0]
max=0

for i in nums:
    if i < min:
        min =i
        
    elif i > max:
        max=i
    


if max%min==0:
        print(min)

else:
        print(1)  

    
  
