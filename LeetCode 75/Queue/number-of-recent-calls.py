class RecentCounter:
    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        total = 0
        self.queue.append(t)
        for i in range(len(self.queue) - 1, -1, -1):
            if self.queue[i] >= t-3000:
                total += 1
            else:
                break
            
        return total