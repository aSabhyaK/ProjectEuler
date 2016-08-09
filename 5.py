def lcm_of_two(a, b):
    max = a if a >= b else b;
    min = a if a <= b else b;
    
    for i in range(1, min + 1, 1):
        product = max * i;
        
        if(product % min == 0):
            return product;
        
    return (a * b);

def lcm_of_all(list):
    size = len(list);
    lcm_intermed = list[1];
    
    for i in range(1, size, 1):
        lcm_intermed = lcm_of_two(lcm_intermed, i);

    return lcm_intermed;
    
list = [];
upper_limit = 20;

for i in range(1, upper_limit + 1, 1):
    list.append(i);
    
print(lcm_of_all(list));