from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]: # TODOO This is not working
        result= []
        self.helper(0,s,[],result)
        return result

    def helper(self,i:int,s:str,slate: List[str],result:List[List[str]]):
        if i == len(s):
            result.append(list(slate))
            return

        for end in range(i,len(s)-1):
            if self.isPalindrome(s[i:end]):
                slate.append(s[i:end])
                self.helper(i+1,s,slate,result)
                slate.pop()


    def isPalindrome(self,temp: str)->False:
        left = 0
        right = len(temp)-1
        while left < right:
            if temp[left] != temp[right]:
                return False
        return True
