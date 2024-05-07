class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        M = dict()
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    M[list1[i]] = i+j
        min_index_sum = 2000
        out = []
        for word in M:
            if M[word] < min_index_sum:
                min_index_sum = M[word]
                out = []
                out += [word]
            elif M[word] == min_index_sum:
                out += [word]
        return out