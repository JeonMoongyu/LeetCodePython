class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def BST(left, right):
            nonlocal nums, target
            if left > right:
                return -1
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return BST(left, mid-1)
            if nums[mid] < target:
                return BST(mid+1, right)
            
        return BST(0, len(nums)-1)