

def quiz_logic():
#     await ctx.send("Choose a pun, 1 or 2")

        
        

#         await ctx.send("My favorite drink? Purr-secco")
#         time.sleep(2)
#         await ctx.send("What do you call an alligator in a vest?")
#         time.sleep(2)
#         await ctx.send("AN INVESTIGATOR!!")
    #print("choose a pun, 1 or 2")
        
    input_choice = int(input("Choose a pun, 1 or 2 \n"))
    

    if input_choice == 1:
        print("My favorite drink? Purr-secco")
    elif input_choice == 2:
        print("What do you call an alligator in a vest?....AN INVESTIGATOR!!")
    else:
        print(input_choice)



quiz_logic()
