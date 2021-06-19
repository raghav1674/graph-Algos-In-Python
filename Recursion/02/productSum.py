# nice one 
# O(n): time complexity 
# O(d): space depth 
def product_sum(arr,multiplier=1):
        
        _sum = 0 
        for element in arr:
                if type(element) is list:
                        _sum+=product_sum(element,multiplier+1)
                else:
                        _sum+=element 
        return _sum * multiplier

print(product_sum([5,2,[7,-1],3,[6,[-13,8],4]]))