class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber <= 26:
            return chr( columnNumber + ord('A') - 1 )
        return self.convertToTitle((columnNumber-1)//26) + self.convertToTitle((columnNumber-1)%26 + 1)
            