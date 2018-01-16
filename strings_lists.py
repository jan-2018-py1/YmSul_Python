words = "It's Thanksgiving day. It's my birthday, too!"
print words.find("day")
new_words = words.replace("day", " month")
print new_words 
# that was Find and Replace
x = [2,54,-2,7,12,98]
print min(x)
print max(x)
# that was Min and Max
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[7]
print [x[0], x[7]]
# that was First and Last
A = [19,2,54,-2,7,12,98,32,10,-3,6]
print sorted([19,2,54,-2,7,12,98,32,10,-3,6])
A = [-3,-2,2,6,7,10,12,19,32,54,98]
B = A[:len(A)/2]
C = A[len(A)/2:]
print [B, C]