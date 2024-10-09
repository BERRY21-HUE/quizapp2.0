import streamlit as st


def greek():
    questions_2 = ["Who is the Greek God of the Underworld?",
                   "What effect did Medusa's gaze have on people?",
                   "Prometheus faced eternal punishment for stealing what from the gods?",
                   "What was the only thing left in Pandora’s jar?",
                   "Which of these mighty warriors was dipped in the River Styx as a baby, making him nearly invulnerable?",
                   "What monstrous creature resides in the center of the Labyrinth?",
                   "Icarus, using wings designed by his father, died because of what?",
                   "Used to help the Argonauts overcome the Sirens, Orpheus’s superhuman skills are in what field?",
                   "Zeus’s father, Cronus, did which of the following to his children?",
                   "Who stared at his own reflection until he died?",
                   "Zeus assumed the form of what animal to seduce the Spartan queen Leda?",
                   "Which of these was one of the 12 Labors of Hercules?",
                   "Best known as the god of the sea, Poseidon was also god of which of these?",
                   "Which musical instrument did Apollo play?",
                   "How many labors did Hercules complete?",
                   "Where was Hades born?",
                   "Who was the mother of Hades, Zeus, and Poseidon?",
                   "Which two gods are twins?",
                   "Who shot the arrow that struck Achilles in his heel?",
                   "What is the name for the part of the Underworld where the majority of ordinary souls were sent to live after their death?",
                   "Who cut off Medusa’s head?",
                   "Scylla was a sea monster with how many heads?",
                   "What was King Midas cursed with because of his greed?",
                   "According to Greek mythology, who was the first mortal woman?",
                   "What is the name of the father of Zeus?",
                   "What is the name of the three-headed dog referred to as the Hound of Hades?",
                   "Which Greek hero was called ‘tamer of horses’?",
                   "Which Greek hunter has a constellation named after him?",
                   "What is Ares the God of?",
                   "Finally, which of the following is NOT a Greek mythology retelling?"
                   ]
    options_2 = [["A. Poseidon", "B. Hades", "C. Zeus", "D. Apollo"],
                 ["A. It gave them Incredible Strength", "B. It Accelerated there aging", "C. It Made them fall in love", "D. It Turned them to stone"],
                 ["A. The Wheel", "B. Fire", "C. Wine", "D. Bronze"],
                 ["A. Disease", "B. Poverty", "C. Hope", "D. War"],
                 ["A. Jason", "B. Achilles", "C. Odysseus", "D. Hercules"],
                 ["A. Minotaur", "B. Medusa", "C. Sphinx", "D. Centaur"],
                 ["A. He became trapped in a cloud", "B. He was attacked by harpies", "C. He was mistaken for a bird by a hunter", "D. He flew too close to the Sun"],
                 ["A. Rowing", "B. Wrestling", "C. Archery", "D. Music"],
                 ["A. Ate them alive", "B. Weaned them on wolf’s milk", "C. Trained them for combat", "D. Abandoned them on a desert island"],
                 ["A. Sisyphus", "B. King Midas", "C. Hermaphroditus", "D. Narcissus"],
                 ["A. Ram", "B. Swan", "C. Dragon", "D. Snake"],
                 ["A. Massaging Hermes’ feet", "B. Plucking the wings of Pegasus", "C. Stealing a girdle from Hippolyte", "D. Trimming Zeus’s beard"],
                 ["A. Earthquakes", "B. Fire", "C. The sky", "D. Love"],
                 ["A. Flute", "B. Piano", "C. Syrinx", "D. Lyre"],
                 ["A. 13", "B. 10", "C. 12", "D. 9"],
                 ["A. Crete", "B. Mount Olympus", "C. Sicily", "D. Rhodes"],
                 ["A. Rhea", "B. Phoebe", "C. Tethys", "D. Theai"],
                 ["A. Ares and Artemis", "B. Apollo and Artemis", "C. Aphrodite and Apollo", "D. Ares and Aphrodite"],
                 ["A. Rhea", "B. Helios", "C. Eros", "D. Paris"],
                 ["A. Hell fire", "B. Paradise", "C. Asphodel Meadows", "D. The Labrynth"],
                 ["A. Perseus", "B. Poseidon", "C. Pan", "D. Persephone"],
                 ["A. 2", "B. 3", "C. 5", "D. 6"],
                 ["A. Famine", "B. Betrayer among his Subordinate", "C. Everything he touched turned to gold", "D. Unable to Reproduce"],
                 ["A. Helen of Troy", "B. Pandora", "C. Hermione", "D. Europa"],
                 ["A. Kronos", "B. Hades", "C. Apollo", "D. Oceanus"],
                 ["A. Medusa", "B. Ragnarok", "C. Cerberus", "D. Chimera"],
                 ["A. Jason", "B. Hercules", "C. Orpheus", "D. Hector"],
                 ["A. Theseus", "B. Orion", "C. Meleager", "D. Atalanta"],
                 ["A. Sun", "B. Music", "C. War", "D. Fire"],
                 ["A. A touch Of Darkness", "B. Lore", "C. The Palace of Illusions", "D. Neon Gods"]
                 ]
    answers_2 = ["B", "D", "B", "C", "B", "A", "D", 'D', "A", "D", "B", "C", "A", "D", "C", "A", "A", "B", "D", "C", "A", "D", "C", "B", "A", "C", "D", "B", "C", "C"]
    guesses_2 = []
    questions_num_2 = 0
    score_2 = 0

    if "user_guess" not in st.session_state:
        st.session_state.user_guess = [""] * len(questions_2)

    st.header("GREEK MYTHOLOGY")
    user_name = st.text_input("How Can I address You", placeholder="Smith")
    if user_name:
        st.subheader("WHAT IS GREEK MYTHOLOGY?")
        st.write("Greek mythology is a body of myths and stories originating from ancient Greece that explain the origins "
                 "of the world, the lives and adventures of gods, goddesses, heroes, and mythological creatures."
                 " These myths were a vital part of ancient Greek religion and culture, offering explanations for natural"
                 " phenomena, human behavior, and the world’s mysteries.")
        user_option_3 = st.multiselect(f"{user_name}, Do You want to test how good you are in Myths", ["Yes", "No"])
        if "Yes" in user_option_3:
            st.write(f"{user_name}, Enjoy Your Quiz")
            for i, question in enumerate(questions_2):
                st.info(f"Question {i + 1}: {question}")
                for opt in options_2[questions_num_2]:
                    st.write(opt)

                st.session_state.user_guess[i] = st.text_input(
                    "Your Answer:",
                    value=st.session_state.user_guess[i],
                    key=f"user_{i}"
                    )

                guesses_2.append(st.session_state.user_guess[i])
                if st.session_state.user_guess[i].strip().upper() == answers_2[questions_num_2].strip().upper():
                    score_2 += 1
                questions_num_2 += 1

            if st.button("SUBMIT"):
                st.info(f"Your Answers: {guesses_2}".upper())
                st.info(f"The Answers: {answers_2}")
                overall_score = (score_2 / len(questions_2)) * 100
                st.write(f"Your Score is {overall_score:.1f}%")
                if overall_score < 30:
                    st.error(f"{user_name}, Your Score is too Low")
                elif overall_score >= 30 and overall_score <= 49:
                    st.warning(f"{user_name}, You can do Better")
                elif overall_score >= 50 and overall_score <= 69:
                    st.success(f"{user_name}, A Good Score")
                else:
                    st.success(f"{user_name}, An Amazing Score")
        elif "No" in user_option_3:
            st.info("CHOOSE THE NEXT OPTION!")

