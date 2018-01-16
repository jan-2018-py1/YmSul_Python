# #Part 1:
def draw_stars(x):
   for i in range(0, len(x)):
        stars = ""
        for j in range(0, x[i]):
            stars += "*"
        print stars

x = [4,6,1,3,5,7,25]
draw_stars(x)

#Part 2:
def draw_stars2(x):
    for i in range(0, len(x)):
        stars = ""
        val = x[i]
        if isinstance(val, str):
            for j in range(0, len(val)):
                stars += val[0].lower()
        else:
            for k in range(0, val):
                stars += "*"
        print stars

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(x)