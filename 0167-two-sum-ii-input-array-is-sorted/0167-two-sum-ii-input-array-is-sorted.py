class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            n = len(numbers)
            i, j = 0, 1
            while i < n-1:
                while j < n:
                    print(i,j)
                    if numbers[i] + numbers[j] == target:
                        return [i+1, j+1]
                    elif numbers[i] + numbers[j] < target:
                        temp = numbers[j]
                        j += 1
                        while j < n-1 and temp == numbers[j]:
                            j += 1
                    else:
                        break
                temp = numbers[i]
                i += 1
                while i < n-1 and temp == numbers[i]:
                    i += 1
                j = i+1
    