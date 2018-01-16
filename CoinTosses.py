import random

totalHeads = 0
totalTails = 0

def coinToss():
    result = ""
    flip = random.randint(0, 1)
    if flip == 0:
        result = "head"
    else:
        result = "tail"
    return result

print "Starting the program..."
for i in range(0,5000):
    toss = coinToss()
    if toss == "head":
        totalHeads += 1
    if toss == "tail":
        totalTails += 1
    print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far.".format(i, toss, totalHeads, totalTails) 
print "Ending the program, thank you!" 