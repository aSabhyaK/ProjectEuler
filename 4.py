#pass the string representation here
def check_if_palindrome(number):
    size = len(number);
    
    if(size == 1):
        return True;
        
    mid = int(size / 2) if size % 2 == 0 else int(size / 2) + 1;
        
    for i in range(0, mid, 1):
        if(number[i] != number[size - i - 1]):
            return False;
            
    return True;
    
array = [];
#906609; 993 * 913
count = 0;

for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        final_number = i * j;
        
        if(check_if_palindrome(str(final_number))):
            array.append(final_number);
            count += 1;

array.sort();
print(array[count - 1]);