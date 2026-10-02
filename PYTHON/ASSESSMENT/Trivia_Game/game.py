questions = [
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4" 
    },
    {
        "question": "____ is the perfect first programming language",
        "options": ["JavaScript","Java",".net","python"],
        "answer": "python"
    },
    {
        "question": "What is the primary function of the CPU in a computer?",
        "options": ["To connect to the internet","To display images on the screen","To perform arithmetic and logical operations on data","To store data permanently"],
        "answer": "To perform arithmetic and logical operations on data"
    },
    {
        "question": "What is one common challenge beginners face when learning Python?",
        "options": ["Understanding indentation and its role in Python syntax","Writing code without using any variables","Configuring Python to run on a quantum computer","Memorizing all Python libraries"],
        "answer": "Understanding indentation and its role in Python syntax" 
    },
    {
        "question": "2+10=?", 
        "options": ["12","13","34","3"],
        "answer": "12"
    }
]

for each_question in questions:
    idx=0 
    print(each_question["question"],"\n")
    for each_options in each_question["options"]:
        idx+=1
        print(f"{idx}. {each_options}")  
    chosen_option = int(input("Your answer: "))
    answer = list(each_question["options"]).index(each_question["answer"])
    if chosen_option == answer+1:
        print("Correct! 🎉")
    else:
        print("Wrong! ❌")
    print()
    