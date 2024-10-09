import streamlit as st


def riddle():
    questions = ["What are two things you can never eat for breakfast?",
                 "What is always coming but never arrives?",
                 "What gets wetter the more it dries?",
                 "What can be broken but never held?",
                 "What word is spelled incorrectly in every single dictionary?",
                 "What is it that lives if it is fed, and dies if you give it a drink?",
                 "What never asks a question but gets answered all the time?",
                 "What goes up but never ever comes down?",
                 "What can one catch that is not thrown?",
                 "If you have one, you want to share it. But once you share it, you do not have it. What is it?",
                 "If a plane crashes on the border between the United States and Canada, where do they bury the survivors?",
                 "You spot a boat full of people but there isn’t a single person on board. How is that possible?",
                 "What has a face and two hands, but no arms or legs?",
                 "I start out tall, but the longer I stand, the shorter I grow. What am I?",
                 "Thanks to me, you can see straight through the wall. What am I?",
                 "What goes up and down, but always remains in the same place?",
                 "Everyone in the world needs it, but they usually give it without taking it. What is it?",
                 "What can you hold without touching it at all?",
                 "What has a head, a tail, but does not have a body?",
                 "I am an odd number. Take away one letter and I become even. What number am I?",
                 "What can you break by doing nothing at all?",
                 "What gets bigger the more you remove from it?",
                 "What belongs to you but is used more by other people?",
                 "What word retains the same pronunciation even after you take away four of its five letters?",
                 "What is full of holes but still holds water?",
                 "What has words, but never speaks?",
                 "What begins with an “e” and only contains one letter?",
                 "What is the end of everything?",
                 "What is black when it’s clean and white when it’s dirty?",
                 "I’m tall when I’m young, and I’m short when I’m old. What am I?"
                 ]
    options = [["A. Bread and Tea", "B. Launch and Dinner", "C. Fruits", "D. Coffee and Milk"],
               ["A. Memory", "B. Money", "C. Promises", "D. Tomorrow"],
               ["A. Towel", "B. Water", "C. Rain", "D. Weather"],
               ["A. A Dream", "B. A Promise", "C. A Lover's heart", "D. A Relationship"],
               ["A. Entertainment", "B. Communication", "C. Enthusiast", "D. Incorrectly"],
               ["A. Matches", "B. Fire", "C. Petrol", "D. Firewood"],
               ["A. Message", "B. Money", "C. Phone", "D. Question"],
               ["A. Age", "B. Space", "C. Growth", "D. Money"],
               ["A. Curse", "B. Cold", "C. Ball", "D. Rain"],
               ["A. Money", "B. Food", "C. Secret", "D. Story"],
               ["A. USA", "B. None", "C. Canada", "D. UK"],
               ["A. Dead", "B. Alive", "C. Married", "D. Buried"],
               ["A. Clock", "B. A Cripple", "C. Snake", "D. Bird"],
               ["A. Match Stick", "B. Battery %", "C. Money", "D. Candle"],
               ["A. Burglary", "B. Window", "C. Mirror", "D. Light"],
               ["A. Gravity", "B. Stock", "C. Stairs", "D. Bank Acct"],
               ["A. A Promise", "B. A secret", "C. An advise", "D. Memories"],
               ["A.Conversation", "B. Memories", "C.Money", "D.Air"],
               ["A. A Snake", "B. A Letter", "C. A Paragraph", "D. A Coin"],
               ["A. One", "B. five", "C. Eleven", "D. Seven"],
               ["A. Silence", "B. Promise", "C. Routine", "D. Trust"],
               ["A. A Space", "B. A Gap", "C. A Debt", "D. A hole"],
               ["A. Advise", "B. Name", "C. Memory", "D. Promise"],
               ["A. Five", "B. Queen", "C. Queue", "D. While"],
               ["A. A Basket", "B. A Sieve", "C. A Sponge", "D. A Bucket"],
               ["A. Manuscript", "B. Book", "C. Sign", "D. Document"],
               ["A. Entertainment", "B. English", "C. Egg", "D. Envelope"],
               ["A. Nothing", "B. G", "C. Void", "D. Vanity"],
               ["A. A Chalkboard", "B. A T-shirt", "C. A Window", "D. A cloud"],
               ["A. A Candle", "B. A Tree", "C. A Person", "D. A Mountain"]
               ]
    answers = ["B", "D", "A", "B", 'D', "B", "C", "A", "B", "C", "B", "C", "A", "D", "B", "C", "C", "A", "D", "D", "B", "D", "B", "C", "C", "B", "D", "B", "A", "A"]
    guesses = []
    question_num = 0
    score = 0

    if "user_guess" not in st.session_state:
        st.session_state.user_guess = [""] * len(questions)

    st.header("RIDDLE")
    username = st.text_input("How Can I Address You", placeholder="Andy")

    if username:
        st.subheader("WHAT IS A RIDDLE?")
        st.write(f"""A riddle is a type of puzzle or problem that is phrased in the form of a question, statement, or description, often 
        with a double or hidden meaning. The goal of a riddle is to challenge the person to figure out the answer, which may
        involve lateral thinking, clever wordplay, or interpreting the clues in an unexpected way.
    """)
        st.write("In Summary A Riddle Makes You Logical")

        user_option = st.multiselect(f"{username}, Are You Ready to test how Logical You are", ["Yes", "No"])
        if "Yes" in user_option:
            st.write(f"{username}, Enjoy Your Riddle")
            for i, question in enumerate(questions):
                st.info(f"Question{i + 1}: {question}")
                for option in options[question_num]:
                    st.write(option)
                st.session_state.user_guess[i] = st.text_input(
                    f"Your Answer:",
                    value=st.session_state.user_guess[i],
                    key=f"user {i}"
                )

                guesses.append(st.session_state.user_guess[i])
                if st.session_state.user_guess[i].strip().upper() == answers[question_num].strip().upper():
                    score += 1
                question_num += 1

            if st.button("SUBMIT"):
                st.info(f"Your Answers: {guesses}".upper())
                st.info(f"The Answers: {answers}")
                overall_score = (score / len(questions)) * 100
                st.write(f"Your Score is {overall_score:.1f}%")
                if overall_score < 30:
                    st.error(f"{username}, Your Score is too Low")
                elif overall_score >= 30 and overall_score <= 49:
                    st.warning(f"{username}, You can do Better")
                elif overall_score >= 50 and overall_score <= 69:
                    st.success(f"{username}, A Good Score")
                else:
                    st.success(f"{username}, An Amazing score")
        elif "No" in user_option:
            st.info("CHOOSE THE NEXT OPTION!")

