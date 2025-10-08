# this programme to guess the num between 0(inclusive) and 100(not inclusive)
# User input ==> just Enters(too small or too high) and according to this input, the programme guess

low = 0
high = 50

print("please think of a number between", low, "and", high)

for i in range(low, high):
    mid = (low + high) // 2
    
    # print("low is:", low,"mid is:", mid,"high is:", high) #this line for teting purpose
    print("is your secret number:", mid)
    
    user_input = input(str(mid) +" is lower than my secret num(l),\n" + str(mid) +" is higher than my secret num(h)\n,correct num(c): ")

    if user_input == 'c':
        print("Done with true guess")
        break
    elif user_input == 'l':
        low = mid
    elif user_input == 'h':
        high = mid
    else:
        print("sorry, i don't understand your input")
        break
    

    
