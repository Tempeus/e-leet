class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total_gain = 0
        gain_list = [0]
        for height in gain:
            total_gain += height
            gain_list.append(total_gain)
        
        return max(gain_list)