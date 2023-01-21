class DataStream:

    def __init__(self, value: int, k: int):
        self.count = 0
        self.value = value
        self.k_back = k

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.count = 0
            return False

        self.count += 1
        if self.count >= self.k_back:
            return True
