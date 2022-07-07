tot_score=0
n_total=0
repeat =1
easy_set={
    "What color is sky?":"blue",
    "What color is grass?":"green",
    "What color is ocean":"blue"
}
medium_set = {
    "How Many States in America?":"50",
    "How Many Cars are Manufactured each Year?":"12000",
    "How Many Days in a Year?":"365"
}
hard_set = {
    "How tall is the tallest Man":"2.3m",
    "Who Gifted the Liberty Tower to the US":"france",
    "whats 10+10?":"20"
}

name=(input("Welcome to My Quizzing Game!\nPlease Specify Your name:")).strip().capitalize()
while repeat ==1:
    difficulty=int(input(f"Hello {name}.Please Choose a Difficulty From the following:\n"
                         "(1)-Easy\n"
                         "(2)-Medium\n"
                         "(3)-Hard\n"
                            "Difficulty Level:"))
    while difficulty !=1 and difficulty !=2 and difficulty !=3:
        difficulty = int(input(f"Invalid Option!Please Enter the Equivalent number of Difficulty\n"
                               "(1)-Easy\n"
                               "(2)-Medium\n"
                               "(3)-Hard\n"
                               "Difficulty Level:"))
    if difficulty == 1:
        print("Welcome to the easy Question Section.\nEach Question has 1 Mark.")
        easy_score=0
        i,j=1,1
        ne = int(input("Choose nb of Questions (Max 3): "))
        while ne!=1 and ne!=2 and ne!=3:
            ne = input("Please Choose a valid Number (1=>3): ")
        n_total += ne
        for question in easy_set.keys(): #Problem was Here <====
            if j > ne:
                break
            else:
                print(f"Question {i}:\n{question}")
                j+=1
                i+=1
                ans=(input("Your answer: ")).strip().lower()
                if ans == easy_set[question]:
                    print("You are Correct!")
                    easy_score+=1
                else:
                    print("Wrong Answer!")
        tot_score+=easy_score
        print(f"You Scored {easy_score}/{ne}.")
        repeat=int(input("Would you like to play more?:\n(1)-Yes\n(2)-No\nOption:"))
        while repeat!=1 and repeat !=2:
            repeat = int(input("Please Choose a Valid Number:\n(1)-Yes\n(2)-No\nOption:"))
    elif difficulty == 2:
        print("Welcome to the Medium Question Section!Each Question has 2 Marks.")
        nm = int(input("Choose the Number of Questions (Max=3):"))
        while nm!=1 and nm!=2 and nm!=3:
            n=int(input("Please Choose a Valid Number (1=>3): "))
        n_total += nm*2
        i, j=1 ,1
        medium_score=0
        for question in medium_set.keys():
            if j>nm:
                break
            else:
               j+=1
               print(f"Question {i}:\n{question}")
               i += 1
               ans=input("Your Answer: ").strip().lower()
               if ans == medium_set[question]:
                   print("You are Correct!")
                   medium_score+=2
               else:
                   print("You are Wrong!")
        tot_score += medium_score
        print(f"You Score {medium_score}/{nm*2}.")
        repeat = int(input("Would you like to play more?:\n(1)-Yes\n(2)-No\nOption:"))
        while repeat != 1 and repeat != 2:
            repeat = int(input("Please Choose a Valid Number:\n(1)-Yes\n(2)-No\nOption:"))
    elif difficulty ==3:
        print("Welcome to the hardest Set of Questions!Each Question has 3 Marks.")
        nh = int(input("How Many Questions Would You Like (Max = 3): "))
        while nh !=1 and nh!=2 and nh!=3:
            print("Please Enter a Valid Number (1=>3): ")
        n_total+=nh*3
        i ,j =1 ,1
        hard_score=0
        for question in hard_set:
            if j > nh:
                break
            else:
                j +=1
                print(f"Question {i}:\n{question}")
                i+=1
                ans = (input("Your Answer: ")).strip().lower()
                if ans == hard_set[question]:
                    print("You are Correct!")
                    hard_score+=3
                else:
                    print("You are Wrong!")
        print(f"You scored {hard_score}/{nh*3}.")
        tot_score+=hard_score
        repeat = int(input("Would you like to play more?:\n(1)-Yes\n(2)-No\nOption:"))
        while repeat != 1 and repeat != 2:
            repeat = int(input("Please Choose a Valid Number:\n(1)-Yes\n(2)-No\nOption:"))
print(f"Thanks for Playing!\nYou Scored {tot_score}/{n_total} which is {(tot_score/n_total)*100}%")
print("You Nailed it!" if tot_score/n_total==1 else "You Did Great!" if tot_score/n_total>=0.7 else "You Did good!" if tot_score/n_total>=0.5 else "Better Luck Next Time!")

