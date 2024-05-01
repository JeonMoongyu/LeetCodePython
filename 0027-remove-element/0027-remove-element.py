class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] == val:
                print("val", left, right, end=" ")
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                print("not val", left, right, end=" ")
                left += 1
            print(nums)
        return left