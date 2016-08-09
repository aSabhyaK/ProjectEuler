def list_all_prime_factors(number):
    unique_values = [];
    
    while(number % 2 == 0):
        if(2 not in unique_values):
            unique_values.append(2);

        number /= 2;
        
    flag = True;
    
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if(number % i == 0):
            flag = False;
            number /= i;
            
            if(i not in unique_values):
                unique_values.append(i);
    
    if(flag):
        unique_values.append(number);
        
    return unique_values;
        
#list_all_prime_factors(13195);
all_prime_factors = list_all_prime_factors(600851475143);
size = len(all_prime_factors);

print(all_prime_factors[size - 1]);