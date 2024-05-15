class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        for num1 in nums1:
            found, done = False, False
            for num2 in nums2:
                if num1 == num2:
                    found = True
                if found and not done and num1 < num2:
                    out.append(num2)
                    done = True
            if not done:
                out.append(-1)
        return out