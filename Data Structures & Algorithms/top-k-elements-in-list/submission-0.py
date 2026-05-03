class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for number in nums:
            if number not in counter:
                counter[number] = 0
            counter[number] = counter[number] + 1

        result = sorted(counter, key = counter.get, reverse = True)[:k]

        return result