class Edge:
        
        def __init__(self,src,dest,weight):
                
                self.src = src 
                self.dest = dest 
                self.weight = weight
        def __repr__(self):
        	return "( "+str(self.src)+" , "+str(self.dest)+" , "+str(self.weight)+" )"
 
                


class NodeIterator:
    
    def __init__(self,current):
        
        self.current = current 
    
    def __next__(self):
        
        if self.current is not None:
            
            cur = self.current.data 
            
            self.current = self.current.next 
            
            return cur 
        else:
            
            raise StopIteration()
            
    def __iter__(self):
        return self 

class Node:
        
        def __init__(self,data):
                
                self.next = None 
                self.data = data
        def __repr__(self): 
            str_repr=""
            temp = self
            while temp.next is not None:
                	str_repr += "[ "+str(temp.data+1)+" | "+str(hex(id(temp)))+" ]" +" -> "
                	temp = temp.next
            if temp:
                str_repr += "[ "+str(temp.data+1)+" | "+str(hex(id(temp)))+" ]" +" -> "
            str_repr += "None"																																																																																																																																																																																																																											
            return str_repr 
            
        def __iter__(self):
            
            return NodeIterator(self)