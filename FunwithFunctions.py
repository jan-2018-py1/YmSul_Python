# #Odd/Even:
def OddEven(num):
    i = 0
    for i in range(0,num):
        if i % 2 == 0:
            print "Number is {}. This is an even number.".format(i)
        else:
            print "Number is {}. This is an odd number.".format(i)
        i += 1    
OddEven(2000)

# #Multiply:
def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b

#Hacker Challenge:
def layered_multiples(arr):
    new_array = []
    for y in arr: 
        ones = []
        for z in range(0,y):
            ones.append(1)
        new_array.append(ones)   
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x

