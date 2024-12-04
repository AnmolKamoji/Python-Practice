#for item in range (10):
 #   print(item)

# for i in range(2,6):
    #print(i)

#for i in range(6,2,-1):
    #print(i)
for i in range(2,100):
    prime = True 
    for j in range(2,i):
        if(i%j==0):
            prime = False
    if (prime == True):
            print(i)   