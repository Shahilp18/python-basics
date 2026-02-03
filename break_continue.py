i = 1;

#! Break
# while(i<=10):
#     if(i%3 == 0):
#         break;
#     print(i);
#     i+=1;

#! Continue
while (i<=10):
    if(i % 3 == 0):
        i+=1
        continue
    print(i)
    i+=1
        
print("Outside loop...");