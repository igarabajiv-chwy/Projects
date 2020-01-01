class MaxSizeLIst:
    def __init__(self,size):
        self.bucket = []
        self.size = size
    
    def push(self,value):
        self.bucket.append(value)
        if len(self.bucket) > self.size:
            del self.bucket[0]
    
    def get_list(self):
        return self.bucket
