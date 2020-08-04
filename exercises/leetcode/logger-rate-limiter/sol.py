class Logger:

    def __init__(self):
        self.printedTime = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.printedTime:
            self.printedTime[message] = timestamp
            return True
        
        if timestamp - self.printedTime[message] >= 10:
            self.printedTime[message] = timestamp
            return True

        return False
        

logger = Logger()

# logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo") # true; 

# logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar") # true;

# logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo") # false;

# logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar") # false;

# logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo") # false;

# logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo") # true;