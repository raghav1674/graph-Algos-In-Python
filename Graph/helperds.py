class MinHeap:

    def __init__(self):

        self.arr = []

    def put(self, data):

        
        
        index = len(self.arr)
        parent_index = (index - 1)//2
        temp = data
        

        while parent_index >= 0 and temp < self.arr[parent_index]:

            self.arr.insert(index,self.arr[parent_index])
            index = parent_index
            parent_index = (index - 1)//2

        self.arr.insert(index,temp)

        def get(self):
                
                # number To return
                num = self.arr.pop(0)
                
                # last element to whom we need to replace
                temp = self.arr[len(self.arr)-1]

                
                index  = 0 
                
                left = 1
                
                right =2 
                
                
                # while left > 
                
                
mypq = MinHeap()
mypq.put(10)
# mypq.put(2)
# mypq.put(200)
mypq.put(-1)

print(mypq.__dict__)

                
                

