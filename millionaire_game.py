questions = [
    ["Who is Sharukh Khan?", "WWE Wresler","Plumber","Actor","Astronut", 3],
    ["What is the capital of France?", "Berlin", "Peris","Rome","London", 2],
    ["Which Planet is known as Red planet?", "Earth", "Venus","Mars", "Jupiter", 3],
    ["What is the largest Mammel","Whale","Blue Whale","Elephant","Giraffe",2],
    ["Who wrote'Romeo and Juliet'?","William Shakespare", "Jane Austen","Charles Dickens", "Homer", 1],
    ["What is the square root of 64 ?", "8","20","6","12",8],
    ["Which country is knowm as the land of rising Sun?","India", "South Korea","Japan", "China", 3],
    ["Who painted the mona lisa ?","Claude Monet","Pablo Picasso","Leonardo da Vinchi","Vancent van Gogh", 3],
    ["What is the fastest land animal?","Horse", "Lion","Cheetah","Elephant", 3],
    ["Which ocean is largest ? "," Indian Ocean","Pacific Ocean","Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest county in world ?", "San marino", " Vatican City","Monaco","Liechtenstein",2],
]
prizes = [100000,20000,3000000,9000000,5000000,6,7,8,9,10,11]
i = 0
for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    # check weather the answer is correct or not 
    a = int(input("Enter ypur answer. 1 for a, 2 for b, 3 for c , and 4 for d"))
    if (question[5]==a):
        print("Correct answer")
    else:
        print(f"Incorrect, the correct ans was {question[5]}")
        print("Better Luck next time!")
        break 
    print(f"You won {prizes[i]}")
    i +=1