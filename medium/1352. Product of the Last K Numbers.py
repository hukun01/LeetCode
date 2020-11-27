# 1352. Product of the Last K Numbers
class ProductOfNumbers:
    '''
    Prefix product.
    If we record the products in an array, where array[i] is the product of
    all numbers in data[1:i] inclusive, then we can get the product of
    data[a:b] by products[b] // products[a - 1]. Except that there's a 0 in
    the middle that causes products[a-1] to be 0.
    If there's a zero, we know that all numbers before it will have product as
    0 when we compute the product from the last k numbers, so we can just drop
    all prefix products when we see 0. If k is greater than the size of
    products, we know it covers some range that contains 0, so return 0,
    otherwise the prefix product approach works.
    Time: O(1) for each operation.
    Space: O(k) where k is the min between number of non-zero numbers, and
    number of last numbers required.
    '''
    def __init__(self):
        self.data = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.data = [1]
        else:
            self.data.append(self.data[-1] * num)
        

    def getProduct(self, k: int) -> int:
        if len(self.data) < k + 1:
            return 0
        
        return self.data[-1] // self.data[- (k + 1)]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)