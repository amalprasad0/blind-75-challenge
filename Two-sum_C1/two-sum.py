class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        numSet={}
        for i in range(len(nums)):
            if(target-nums[i] in numSet):
                res.append(i)
                res.append(numSet[target-nums[i]])
                numSet.pop(target-nums[i])
            else:
                numSet[nums[i]]=i
        return res


# TC=> O(n)  and SC => O(n)