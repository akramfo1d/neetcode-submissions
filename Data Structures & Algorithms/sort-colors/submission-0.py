class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l,r=0,len(nums)-1
        i=0

        def swap(i,r):
            temp=nums[i]
            nums[i]=nums[r]
            nums[r]=temp

        while r>=i:
            if nums[i]==0:
                swap(l,i)
                l+=1

            elif nums[i]==2:
                swap(r,i)
                r-=1
                i-=1
            i+=1

            
        