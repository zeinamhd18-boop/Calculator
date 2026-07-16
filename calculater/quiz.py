score =0
questions = {
      "what is 2+2?": "4" ,
      "what is the capital of France?" :"Paris"
         
}
for question, answer in questions.items():
    user_answer= input(question + " ")  
    if user_answer.lower() ==answer.lower(): 
        print("Correct!") 
        score +=1
    else:
         print("Wrong!") 
print(f"Game Over! Your score: {score}") 
