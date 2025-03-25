class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        if not arr:
            return 0
        
        max_ending_here = arr[0]
        min_ending_here = arr[0]
        max_so_far = arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] < 0:
                max_ending_here, min_ending_here = min_ending_here, max_ending_here
            
            max_ending_here = max(arr[i], max_ending_here * arr[i])
            min_ending_here = min(arr[i], min_ending_here * arr[i])
            
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far