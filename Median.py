"""4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5."""

"""nums1 = [1,3,6]
nums2 = [2,8,9]

arr=sorted(nums1+nums2)

print(arr)

n=len(arr)

if n%2==1:
    print(float(arr[n//2]))

else:
    print((arr[n//2]+ arr[n//2 -1]) / 2.0)"""






