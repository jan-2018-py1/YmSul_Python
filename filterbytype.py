y = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
print isinstance(y, int) 
print isinstance(y, str)
print isinstance(y, list)
if isinstance(y, int) is True:
    if y >= 100:
        print "That's a big number!"
    else:
        print "That's a small number." 
elif isinstance(y, str) is True:
    if len(y) >= 50:
        print "Long sentence."
    else:
        print "Short sentence."
elif isinstance(y, list) is True:
    if len(y) >= 10:
        print "Big list!"
    else:
        print "Short list."  

# # Integer
# i = 355
# if i >= 100:
#     print "That's a big number!"
# elif i < 100:
#     print "That's a small number."

# # String
# star = "I am a string named Star. Oh happy day! Today was a stressful day. I CAN and I WILL learn python. My ultimate goal is to be data scientist. It is currently 9:39 PM on January 9th, 2018. I wonder why my secondary antibody didn't work. I confirmed that I used goat anti-mouse because that's what is written on the aliquot tube, then why didn't it work with my mouse monoclonal primary antibodies. Strange things... or should I say stranger things? haha."
# if len(star) >= 50:
#     print "Long sentence."
# else:
#     print "Short sentence."

# # List
# groceries = ['apple','orange','avocado','cheese','milk','bread','tomato']
# if len(groceries) >= 10:
#     print "Big list!"
# else:
#     print "Short list."