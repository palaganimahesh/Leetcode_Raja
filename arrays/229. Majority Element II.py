from typing import List


class Solution:#space complexity O(1)
    def majorityElement(self, nums: List[int]) -> List[int]:
        # First pass: find potential candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Second pass: verify the candidates actually appear more than n/3 times
        result = []
        n = len(nums)
        if nums.count(candidate1) > n // 3:
            result.append(candidate1)
        if candidate2 != candidate1 and nums.count(candidate2) > n // 3:
            result.append(candidate2)

        return result
class Solution_Using_MAP:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
         k = n//3

        """
        nums_freq = Counter(nums)#. O(n)
        k = (len(nums)//3)+1
        return [key for key,val in nums_freq.items() if val >=k ] #O(k)
