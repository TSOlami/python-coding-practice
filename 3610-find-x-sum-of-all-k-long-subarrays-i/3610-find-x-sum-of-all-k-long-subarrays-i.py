class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # First get the lenght of the answer array (n - k + 1)
        n = len(nums)
        len_ans = n - k + 1
        answer = []
        # For the lenght of the answer array, try to get each answer item value
        for i in range(len_ans):
            subarr = nums[i:i + k]
            # Look for duplicates in the subarray
            count = {}
            for j in subarr:
                if j in count:
                    count[j] += 1
                else:
                    count[j] = 1
            # Get the x keys with the highest count
            top_x = sorted(count.keys(), key=lambda v: (-count[v], -v))[:x]

            # Keep only the top x nums in the sub array
            # Sum the duplicates and add it to the answer array
            total = sum(num for num in subarr if num in top_x)
            answer.append(total)

        # Return the answer array
        return answer
