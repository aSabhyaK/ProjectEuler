array = [];
array.insert(0, 1);
array.insert(1, 1);

upper_limit = 4000000;
sum_even = 0;
i = 2;

while(True):
    array.insert(i, array[i - 1] + array[i - 2]);
    current_number = array[i];
    
    if(current_number % 2 == 0):
        sum_even += current_number;

    if(current_number > upper_limit):
        break;
        
    i += 1;

"""        
for number in array:
    print(number);
""" 
print(sum_even);