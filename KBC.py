ques = [
    ["From where does the Sun Rises?", "East", "West", "North", "South", 1],
    ["How many planets are there in the solar system?", "7", "8", "10", "9", 2],
    ["What Color is Rose?", "Pink", "Blue", "Red", "Yellow", 3],
    ["What color is Sky?", "Blue", "Yellow", "Pune", "Red", 1],
    ["Name of the largest river in India.", "Ganga", "Yamuna", "Bam", "Godhavari", 1],
    ["Name of the largest river in the World.", "Nile", "Amazon", "Ganga", "Yamuna", 1],
    ["Name of the largest forest in the World.", "Amazon", "Nile", "Ranpratap", "Blue", 1],
    ["Name of the Social Media Platform.", "Google Pay", "Linkdin", "Facebook", "Nike", 3],
    ["Name of the Hiring Platform.", "Google Pay", "Linkdin", "Facebook", "Nike", 2],
    ["Name of the Payment App.", "Google Pay", "Linkdin", "Facebook", "Nike", 1],
    ["Name of the Sport Company.", "Google Pay", "Linkdin", "Facebook", "Nike", 4]
]

levels = [1000, 2000, 5000, 10000, 20000, 40000, 60000, 120000, 250000, 500000, 1000000]

money = 0
for i in range(0, len(ques)):
    question = ques[i]
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(f"{ques[i][0]}")
    print(f" 1. {ques[i][1]}                       2. {ques[i][2]}")
    print(f" 3. {ques[i][3]}                       4. {ques[i][4]}")
    reply = int(input("Enter your Answer (1-4): "))
    if (reply == ques[i][-1]):
        print(f"Correct Answer, You have won Rs.{levels[i]}")
        if [i == 4]:
            money = 10000
        elif [i == 9]:
            money = 250000
        elif [i == 11]:
            money = 1000000
    else:
        print("Wrong Answer!!")
        print(f"You can take Rs.{money} home.")
        breakpoint()