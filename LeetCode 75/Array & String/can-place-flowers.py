class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        avail = 0
        if (len(flowerbed)) <= 2:
            return sum(flowerbed) + n <= 1
        else:
            for i, place in enumerate(flowerbed):
                if i == 0:
                    if place == 0 and flowerbed[i+1] != 1:
                        avail += 1
                        flowerbed[i] = 1
                elif i == len(flowerbed) - 1:
                    if place == 0 and flowerbed[i-1] != 1:
                        avail +=  1
                        flowerbed[i] = 1
                elif place == 0 and flowerbed[i+1] != 1 and flowerbed[i-1] != 1:
                    avail += 1
                    flowerbed[i] = 1
            return n - avail <= 0