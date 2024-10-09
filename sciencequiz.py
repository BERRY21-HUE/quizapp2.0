import streamlit as st


def science():
    questions_1 = ["What does DNA stand for?",
                   "How many bones are in the human body?",
                   "What is the hardest natural substance on Earth?",
                   "Humans and chimpanzees share roughly how much DNA?",
                   "Roughly how long does it take for the sun's light to reach Earth?",
                   "What is the biggest planet in our solar system?",
                   "What is a material that will not carry an electrical charge called?",
                   "What is the only even prime number?",
                   "Sound travels faster in air than in water?",
                   "Which of the world's oceans in the deepest?",
                   "Where in the human body can the smallest bone be found?",
                   "What does USB stand for?",
                   "What is the heaviest organ in the human body?",
                   "What is the rarest blood type in humans?",
                   "In which year was Pluto reclassified as a Dwarf Planet?",
                   "What is the biggest animal in the world?",
                   "How many states of matter are there?",
                   "What is measured using an Anemometer?",
                   "In the computer acronym USB, what does the 'B' stand for?",
                   "Jaguars are native to which continent?",
                   "Which is the fourth planet from the Sun?",
                   "Optics is the studying of what?",
                   "Which scientist in 1774 discovered oxygen?",
                   "In the human body what protein helps to form both fingernails and hair?",
                   "In computing what do the letters HDMI represent?",
                   "What is the condition Myopia more commonly known as?",
                   "What was founded by Jimmy Wales in 2001?",
                   "In medical terms what is BMI?",
                   "Who invented the television?",
                   "What is emitted from a plant during the process of transpiration?"
    ]
    options_1 = [["A. Dynamic New Algorithm", "B. Digital Nervous Array", "C. Deoxyribonucleic acid", "D. Data Never Ages"],
                 ["A. 150", "B. 206", "C. 50", "D. 200"],
                 ["A. Gold", "B. Iron", "C. Silver", "D. Diamond"],
                 ["A. 98%", "B. 20%", "C. 0%", "D. 50%"],
                 ["A. 8 minutes", "B. 8 seconds", "C. 8 hours", "D. 8 days"],
                 ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
                 ["A. Vacuum", "B. Air", "C. Rubber", "D. Insulator"],
                 ["A. 5", "B. 2", "C. 1", "D. 0"],
                 ["A. True", "B. False", "C. True and False", "D. None of the above"],
                 ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"],
                 ["A. The Head", "B. The Nose", "C. The Eyes", "D. The Ear"],
                 ["A. Universal Serial Bus", "B. Unlimited Storage Bridge", "C. Ultra Speed Bridge", "D. Universal Socket Battery"],
                 ["A. The Kidney", "B. The Heart", "C. The Liver", "D. The Private Part"],
                 ["A. O positive", "B. AB negative", "C. A positive", "D. B negative"],
                 ["A. 2010", "B. 1997", "C. 1899", "D. 2006"],
                 ["A. Fin Whale", "B. Humpback Whale", "C. African Elephant", "D. The Antarctic blue whale"],
                 ["A. 4", "B. 2", "C. 5", "D. 1"],
                 ["A. Air Pressure", "B. Temperature", "C. Wind Speed", "D. Humidity"],
                 ["A. Bios", "B. Boot", "C. Byte", "D. Bus"],
                 ["A. Asia", "B. America", "C. Africa", "D. Europe"],
                 ["A. Mars", "B. Venus", "C. Earth", "D. Mecury"],
                 ["A. Light", "B. Eyes", "C. Glass", "D. Matter"],
                 ["A. Isaac Newton", "B. Carl Wilhelm Scheele", "C. Antonie Lavoisier", "D. Joseph Priestley"],
                 ["A. Tubulin", "B. Actin", "C. Keratin", "D. Elastin"],
                 ["A. High-Definition Markup Interface", "B. High-Definition Multimedia Interface", "C. Hyper-Digital Media Interface", "D. High-Definition Media Interconnect"],
                 ["A. Deaf and Dumb", "B. Short-sightedness", "C. Dry Eye Syndrome", "D. Far-sightedness"],
                 ["A. Chrome", "B. Television", "C. Youtube", "D. Wikipedia"],
                 ["A. Business Model Innovation", "B. Broadcast Media interface", "C. Body Mass Index", "D. Baptist Missionary Institute"],
                 ["A. Jimmy Wales", "B. Alaxandar Graham Bell", "C. Elon Musk", "D. John Logie Baird"],
                 ["A. Water", "B. Soil", "C. Branches", "D. Root"]
                 ]
    answers_1 = ["C", "B", "D", "A", "A", "B", "D", "B", "B", "C", "D", "A", "C", "B", "D", "D", "A", "C", "D", "B", "A", "A", "D", "C", "B", "B", "D", "C", "D", "A"]
    guesses_1 = []
    question_num1 = 0
    score_1 = 0

    if "user_guess" not in st.session_state:
        st.session_state.user_guess = [""] * len(questions_1)

    st.header("SCIENCE & NATURE")
    user_name_2 = st.text_input("How Can I Address You", placeholder="John")
    if user_name_2:
        st.subheader("WHAT IS SCIENCE & NATURE?")
        st.write("SCIENCE")
        st.write("Science is a systematic way of exploring, understanding, and explaining the universe. It involves the "
                 "observation, experimentation, and analysis of natural phenomena, aiming to develop knowledge based on facts"
                 " and evidence. The goal of science is to discover laws and principles that govern how things work, predict"
                 " future outcomes, and improve human life through technological advances.")
        st.write("NATURE")
        st.write("Nature refers to the physical world and everything in it that is not human-made. It encompasses all living"
                 " organisms (plants, animals, microorganisms), the environment (air, water, soil), and natural forces (gravity,"
                 " weather patterns, geological processes).")
        user_menu = st.multiselect(f"{user_name_2}, Do You Want to Test How Smart You Are?", ["Yes", "No"])
        if "Yes" in user_menu:
            st.write(f"{user_name_2}, Enjoy Your Quiz")
            for i, quest in enumerate(questions_1):
                st.info(f"Question {i + 1}: {quest}")
                for opt in options_1[question_num1]:
                    st.write(opt)
                st.session_state.user_guess[i] = st.text_input(
                    "Your Answer:",
                    value=st.session_state.user_guess[i],
                    key=f"user{i}"
                )

                guesses_1.append(st.session_state.user_guess[i])
                if st.session_state.user_guess[i].strip().upper() == answers_1[question_num1].strip().upper():
                    score_1 += 1
                question_num1 += 1

            if st.button("SUBMIT"):
                st.info(f"Your Answers: {guesses_1}".upper())
                st.info(f"The Answers: {answers_1}")
                overall_score = (score_1 / len(questions_1)) * 100
                st.write(f"Your Score is {overall_score:.1f}%")
                if overall_score < 30:
                    st.error(f"{user_name_2}, Your Score is too Low")
                elif overall_score >= 30 and overall_score <= 49:
                    st.warning(f"{user_name_2}, You can do Better")
                elif overall_score >= 50 and overall_score <= 69:
                    st.success(f"{user_name_2}, A Good Score")
                else:
                    st.success(f"{user_name_2}, An Amazing Score")
        elif "No" in user_menu:
            st.info("CHOOSE THE NEXT OPTION!")

