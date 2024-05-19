class Solution:
    def capitalizeTitle(self, title: str) -> str:
        arr = title.split()
        
        def Upper(c):
            if 'a' <= c and c <= 'z':
                return chr(ord(c) - ord('a') + ord('A'))
            return c
        
        def Lower(c):
            if 'A' <= c and c <= 'Z':
                return chr(ord(c) - ord('A') + ord('a'))
            return c
        
        def capitalize(word):
            out = Upper(word[0]) if len(word) > 2 else Lower(word[0])
            for c in word[1:]:
                out += Lower(c)
            return out
        
        arr = [ capitalize(word) for word in arr ]
        return ' '.join(arr)
            
                