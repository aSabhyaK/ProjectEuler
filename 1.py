sum = 0;
for i in range(1, 101, 1):
    if(i % 3 == 0 or i % 5 == 0):
        #print(str(i) + "; ", end = '');
        sum += i;
        
print(sum);