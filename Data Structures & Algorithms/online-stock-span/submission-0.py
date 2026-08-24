class StockSpanner:

    def __init__(self):
        self.stock = []
        self.span_length = 0

    def next(self, price: int) -> int:
        self.stock.append(price)
        self.span_length += 1
        span = 0
        for i in range(self.span_length-1,-1,-1):
            if price >= self.stock[i]:
                span+=1
            else:
                return span
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)