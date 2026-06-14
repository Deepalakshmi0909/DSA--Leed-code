left = 1
right = 22
res=[]
for num in range(left,right+1):
     temp = num
     valid=True
     while temp > 0:
            digit = temp % 10
            if digit == 0 or num % digit !=0:
                  valid =False
                  break


            temp //= 10
     if valid: 
            res.append(num)

            
        
print (res)