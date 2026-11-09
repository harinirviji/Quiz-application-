import streamlit as st

st.set_page_config(
    page_title="Python Quiz Application",
    page_icon="🐍",
    layout="centered"
)

st.title("🐍 Python Quiz Application")
st.write("Test your Python programming knowledge!")

questions = [
    {
        "question": "1. Which language is Python?",
        "options": ["A. Programming language", "B. Markup language", "C. Database", "D. Operating system"],
        "answer": "A. Programming language"
    },
    {
        "question": "2. Which function is used to display output?",
        "options": ["A. input()", "B. print()", "C. display()", "D. show()"],
        "answer": "B. print()"
    },
    {
        "question": "3. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C. #"
    },
    {
        "question": "4. Which data type stores whole numbers?",
        "options": ["A. float", "B. int", "C. str", "D. list"],
        "answer": "B. int"
    },
    {
        "question": "5. Which keyword defines a function?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C. def"
    },
    {
        "question": "6. Which data type stores True or False?",
        "options": ["A. int", "B. bool", "C. str", "D. list"],
        "answer": "B. bool"
    },
    {
        "question": "7. Which operator is used for multiplication?",
        "options": ["A. +", "B. -", "C. *", "D. /"],
        "answer": "C. *"
    },
    {
        "question": "8. Which function gets input from the user?",
        "options": ["A. input()", "B. print()", "C. type()", "D. len()"],
        "answer": "A. input()"
    },
    {
        "question": "9. Which brackets are used to create a list?",
        "options": ["A. ()", "B. {}", "C. []", "D. <>"],
        "answer": "C. []"
    },
    {
        "question": "10. Which keyword is used for a decision?",
        "options": ["A. if", "B. repeat", "C. print", "D. input"],
        "answer": "A. if"
    }
]

if "submitted" not in st.session_state:
    st.session_state.submitted = False

with st.form("quiz_form"):
    answers = []

    for i, q in enumerate(questions):
        st.subheader(q["question"])
        choice = st.radio(
            "Choose your answer:",
            q["options"],
            key=f"question_{i}"
        )
        answers.append(choice)

    submitted = st.form_submit_button("Submit Quiz")

if submitted:
    score = 0

    for i, q in enumerate(questions):
        if answers[i] == q["answer"]:
            score += 1

    st.success("Quiz submitted successfully!")
    st.metric("Your Score", f"{score} / {len(questions)}")

    if score >= 8:
        st.balloons()
        st.write("Excellent work!")
    elif score >= 5:
        st.write("Good effort! Keep practising.")
    else:
        st.write("Keep learning and try again!")

    st.write("### Answer Review")

    for i, q in enumerate(questions):
        st.write(f"**{q['question']}**")
        st.write(f"Correct answer: {q['answer']}")
        st.write(f"Your answer: {answers[i]}")
