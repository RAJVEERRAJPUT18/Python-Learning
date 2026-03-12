print("**************WELCOME IN THE GAME KON BNEGA KROREPATI*****************\n")
   
print("READY FOR KON BNEGA KROREPATI ")

Quiz = [
    ["Who was the first President of India?",
     ["A. Jawaharlal Nehru", "B. Rajendra Prasad", "C. Indira Gandhi", "D. A.P.J. Abdul Kalam"],
     "B", 10000],

    ["Who wrote the national anthem of India?",
     ["A. Rabindranath Tagore", "B. Mahatma Gandhi", "C. Subhas Chandra Bose", "D. Bankim Chandra Chattopadhyay"],
     "A", 20000],

    ["What is the capital of Australia?",
     ["A. Sydney", "B. Canberra", "C. Melbourne", "D. Perth"],
     "B", 40000],

    ["Which planet is known as the Red Planet?",
     ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
     "C", 80000],

    ["Which is the longest river in the world?",
     ["A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"],
     "B", 160000],

    ["Which instrument is used to measure temperature?",
     ["A. Barometer", "B. Thermometer", "C. Speedometer", "D. Hygrometer"],
     "B", 320000],

      ["Who was the founder of the Maurya Empire in ancient India?",
     ["A. Ashoka", "B. Bindusara", "C. Chandragupta Maurya", "D. Bimbisara"],
     "C",640000],

    ["Which Indian scientist won the Nobel Prize in Physics in 1930?",
     ["A. C.V. Raman", "B. Homi Bhabha", "C. Vikram Sarabhai", "D. Meghnad Saha"],
     "A", 1280000],

    ["Who was the first woman governor of an Indian state?",
     ["A. Indira Gandhi", "B. Vijayalakshmi Pandit", "C. Sarojini Naidu", "D. Sucheta Kriplani"],
     "C",2500000],

    ["Where is the Pushkar Fair held annually?",
     ["A. Rajasthan", "B. Gujarat", "C. Punjab", "D. Uttar Pradesh"],
     "A", 5000000],

    ["Which Indian missile is named 'Agni'?",
     ["A. Intercontinental Ballistic Missile", "B. Anti-tank missile", "C. Submarine-launched missile", "D. Surface-to-air missile"],
     "A", 10000000],

    ["In which year was the Indian Space Research Organisation (ISRO) founded?",
     ["A. 1962", "B. 1969", "C. 1975", "D. 1984"],
     "B", 20000000],

    ["Who was the first Indian to win an individual Olympic gold medal?",
     ["A. Abhinav Bindra", "B. Leander Paes", "C. Rajyavardhan Singh Rathore", "D. Sushil Kumar"],
     "A", 30000000],

    ["Which Veda is a collection of spells and incantations?",
     ["A. Rigveda", "B. Yajurveda", "C. Samaveda", "D. Atharvaveda"],
     "D", 40000000],

    ["Who was the Viceroy of India at the time of Quit India Movement (1942)?",
     ["A. Lord Irwin", "B. Lord Mountbatten", "C. Lord Linlithgow", "D. Lord Wavell"],
     "C", 50000000],

    ["Which Indian became the President of the International Court of Justice in 1999?",
     ["A. B.R. Ambedkar", "B. R.S. Pathak", "C. Nagendra Singh", "D. Dalveer Bhandari"],
     "C", 70000000]

]
amount=0

for item in Quiz:
    question = item [0]
    option = item [1]
    answer = item [2]
    moneyamount = item [3]

    print(f"Read the question carefully or this is question for money is {moneyamount} \nQues-{question} ")
    for opt in option:
        print(opt)

    user_answer = input("Choose one option (A/B/C/D) or for quid the game to press the Q: ").upper()
    while user_answer not in ["A", "B", "C", "D","Q"]:
        print("Invalid input. Please input in A, B, C, D,.")
        user_answer = input("Try Again (A/B/C/D): ").upper()
    if user_answer== "Q" :
              
        break
    if user_answer == answer:
        print("Correct answer")
        print(f"You won the moneyamount Rs-{moneyamount}")
        
    else:
        print(f"Incorrect answer. The correct answer is {answer}")
        print("")
        break
    if(user_answer== answer and user_answer=="Q" ):
          break
print("Congratulation\n")
print(f"you take home moneyamount :{moneyamount}")
                                         
                     

            


   
       
      












