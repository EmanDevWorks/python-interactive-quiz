def ask_question(question, correct_answer, score):
    print(question)
    user_answer = input().strip().lower()

    if user_answer == correct_answer.lower():
        print("Your answer is correct")
        return score + 1
    else:
        print(f"Not correct! The correct answer is {correct_answer}.")
        return score

def main():
    print("Hello, welcome to the general knowledge quiz. Please check your spelling before submitting")

    score = 0

    # Question 1
    score = ask_question("Q1. What is the capital city of Japan?", "Tokyo", score)

    # Question 2
    score = ask_question("Q2. How many states are in the US?", "50", score)

    # Question 3
    score = ask_question("Q3. What is the largest planet in our solar system?", "Jupiter", score)

    # Question 4
    score = ask_question("Q4. Which ocean is the largest on Earth?", "Pacific Ocean", score)

    # Question 5
    score = ask_question("Q5. What is the main gas responsible for the greenhouse effect on Earth?", "CO2", score)

    # Question 6
    score = ask_question("Q6. What is the chemical symbol for gold?", "Au", score)

    # Question 7
    score = ask_question("Q7. Which country is known as the Land of the Rising Sun?", "Japan", score)

    # Question 8
    score = ask_question("Q8. What is the capital city of the United States?", "Washington D.C.", score)

    # Question 9
    score = ask_question('Q9. Who is known as the "Father of Modern Physics"?', "Albert Einstein", score)

    # Question 10
    score = ask_question("Q10. What is the largest organ in the human body?", "Skin", score)

    print(f"You finished the quiz and your score is {score} out of 10")

    if score >= 9:
        print("Congratulations! Your general knowledge is excellent!")
    elif score >= 6:
        print("Well done! Your general knowledge is decent.")
    else:
        print("Keep learning. Your general knowledge needs improvement.")

if __name__ == "__main__":
    main()
