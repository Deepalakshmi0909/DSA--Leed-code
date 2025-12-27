# My brute force solution to sort an array of 0s, 1s and 2s
class Solution(object):
    def sortColors(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(arr)
        i=0
        for j in range (len(arr)-1,-1,-1):
                if len(arr) < 3:
                    while i < j:
                         if arr[i] > arr[j]:
                            arr[i],arr[j] = arr[j],arr[i]
                            j-=1

                
                elif len(arr) > 3:
                    while i < j:
                        if arr[i] > arr[j]:
                            arr[i],arr[j] = arr[j], arr[i] 
                            i+=1
                            j-=1
                        elif arr[i] < arr[j]:
                            i+=1
        
             
                
        return arr
obj=Solution()
print(obj.sortColors([2,0,2,1,1,0]))

# optimized solution :

class solution():
    def sortColors(self,arr):
        left=0
        right=len(arr)-1
        i=0
        while i<=right:
            if arr[i]==0:
                arr[i],arr[left]=arr[left],arr[i]
                left+=1
                i+=1
            elif arr[i]==2:
                arr[i],arr[right]=arr[right],arr[i]
                right-=1
            else:
                i+=1
        return arr
obj=solution()
print(obj.sortColors([2,0,1]))