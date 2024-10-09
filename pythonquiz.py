import streamlit as st


def python():
    questions_4 = ["Who developed Python Programming Language?",
                   "What is a correct syntax to output 'Hello World' in Python?",
                   "How do you insert COMMENTS in Python code?",
                   "The 'in' operator is used to check if a value exists within an iterable object container such as a list." 
                    "Evaluate to 'True' if it finds a variable in the specified sequence and 'False' otherwise.",
                   "Which one is NOT a legal variable name?",
                   "Which type of Programming does Python support?",
                   "What does pip stand for python?",
                   "Which of the following functions is a built-in function in python?",
                   "Which of the following is the use of id() function in python?",
                   "Which of the following is not a core data type in Python programming?",
                   "Which of these is the definition for packages in Python?",
                   "Which one of the following is not a keyword in Python language?",
                   "Which module in the python standard library parses options received from the command line?",
                   "What arithmetic operators cannot be used with strings in Python?",
                   "To add a new element to a list we use which Python command?",
                   "Which one of the following is the use of function in python?",
                   "What is the maximum possible length of an identifier in Python?",
                   "What are the two main types of functions in Python?",
                   "Which of the following is a Python tuple?",
                   "What is output of print(math.pow(3, 2))?",
                   "Which of the following commands will create a list?",
                   "Which of these about a dictionary is false?",
                   "Which of the following is not a declaration of the dictionary?",
                   "Which of the following isn’t true about dictionary keys?",
                   "Which operator is overloaded by __invert__()?",
                   "To open a file c:\scores.txt for reading, we use?",
                   "How many keyword arguments can be passed to a function in a single function call?",
                   "Which operator has higher precedence in the following list?",
                   "Which of the following cannot be a Python variable name?",
                   "Which of the following is not a Python Data Type?"
                   ]
    options_4 = [["A. Wick van Rossum", "B. Rasmus Lerdorf", "C. Guido van Rossum", "D. Niene Stom"],
                 ["A. print('Hello World')", "B. echo('Hello World');", "C. p('Hello World')", "D. echo'Hello World'"],
                 ["A. /*This is a comment*/", "B. //This is a comment", "C. #This is a comment", "D. Comment'This is a comment'"],
                 ["A. True", "B. False", "C. Only the 'in' is True", "D. Only the 'in' is False"],
                 ["A. _myvar", "B. Myvar", "C. my-var", "D. my_var"],
                 ["A. Object-oriented programming", "B. Structured programming", "C. Functional programming", "D. All of the mentioned"],
                 ["A. Pip Installs Python", "B. Pip Installs Packages", "C. Preferred Installer Program", "D. All of the mentioned"],
                 ["A. factorial()", "B. print()", "C. seed()", "D. sqrt()"],
                 ["A. Every object doesn’t have a unique id", "B. Id returns the identity of the object", "C. All of the mentioned", "D. None of the mentioned"],
                 ["A. Tuples", "B. Lists", "C. Class", "D. Dictionary"],
                 ["A. A set of main modules", "B. A folder of python modules", "C. A number of files containing Python definitions and statements", "D. A set of programs making use of Python modules"],
                 ["A. pass", "B. eval", "C. assert", "D. nonlocal"],
                 ["A. getarg", "B. getopt", "C. main", "D. os"],
                 ["A. *", "B. -", "C. +", "D. All of the Above"],
                 ["A. list1.addEnd(5)", "B. list1.addLast(5)", "C. list1.append(5)", "D. list1.add(5)"],
                 ["A. Functions don’t provide better modularity for your application", "B. You can’t also create your own functions", "C. Functions are reusable pieces of programs", "D. All of the mentioned"],
                 ["A. 79 characters", "B. 31 characters", "C. 63 characters", "D. None of the mentioned"],
                 ["A. System function & User function", "B. Custom function & Built-in function", "C. Built-in function & User defined function", "D. User function & Custom function"],
                 ["A. {1, 2, 3}", "B. {}", "C. [1, 2, 3]", "D. (1, 2, 3)"],
                 ["A. 9.0", "B. 0", "C. 9", "D. None of the Above"],
                 ["A. list1 = list()", "B. list1 = []", "C. list1 = list([1, 2, 3])", "D. All of the mentioned"],
                 ["A. The values of a dictionary can be accessed using keys", "B. The keys of a dictionary can be accessed using values", "C. Dictionaries aren’t ordered", "D. Dictionaries are mutable"],
                 ["A. {1: ‘A’, 2: ‘B’}", "B. dict([[1,”A”],[2,”B”]])", "C. {1,”A”,2”B”}", "D. {}"],
                 ["A. More than one key isn’t allowed", "B. Keys must be immutable", "C. Keys must be integers", "D. When duplicate keys encountered, the last assignment wins"],
                 ["A. !", "B. ~", "C. ^", "D. -"],
                 ["A. infile = open(“c:\scores.txt”, “r”)", "B. infile = open(“c:\\scores.txt”, “r”)", "C. infile = open(file = “c:\scores.txt”, “r”)", "D. infile = open(file = “c:\\scores.txt”, “r”)"],
                 ["A. zero", "B. one", "C. zero or more", "D. one or more"],
                 ["A. % (Modulus)", "B. & (BitWise AND)",  "C. ** (Exponent)", "D. > (Comparison)"],
                 ["A. int_1", "B. true", "C. var-2", "D. name3"],
                 ["A. int", "B. string", "C. set", "D. char"]
                 ]
    answers_4 = ["C", "A", "C", "A", "D", "D", "C", "B", "B", "C", "B", "B", "B", "B", "C", "C", "D", "C", "D", "A", 'D', "B", "C", "C", "B", 'B', "C", "C", "C", "D"]
    guesses_4 = []
    questions_num_4 = 0
    score_4 = 0

    if "user_input" not in st.session_state:
        st.session_state.user_input = [""] * len(questions_4)

    st.header("PYTHON")
    username_4 = st.text_input("How Can I Address You?", placeholder="kate")
    if username_4:
        st.subheader("WHAT IS PYTHON?")
        st.write("Python is a high-level, interpreted programming language known for its simplicity and readability."
                 " It was created by Guido van Rossum and first released in 1991. Python emphasizes code readability "
                 "with its clean syntax and indentation, making it easier to write and maintain code. It is used for "
                 "a wide variety of applications, including web development, data analysis, artificial intelligence, "
                 "machine learning, automation, and scientific computing.")
        user_option_4 = st.multiselect("Do You Want test how Smart You are", ["Yes", "No"])
        if "Yes" in user_option_4:
            st.write(f"Enjoy Your Quiz, {username_4}")
            for i, q in enumerate(questions_4):
                st.info(f"Question {i + 1}: {q}")
                for o in options_4[questions_num_4]:
                    st.write(o)

                st.session_state.user_input[i] = st.text_input(
                    f"Your Answer:",
                    value=st.session_state.user_input[i],
                    key=f"user + {i}"
                )

                guesses_4.append(st.session_state.user_input[i])
                if st.session_state.user_input[i].strip().upper() == answers_4[questions_num_4].strip().upper():
                    score_4 += 1
                questions_num_4 += 1

            if st.button("SUBMIT"):
                st.info(f"Your Answers: {guesses_4}".upper())
                st.info(f"The Answers: {answers_4}")
                overall_score = (score_4 / len(questions_4)) * 100
                st.write(f"Your Score is {overall_score:.1f}%")
                if overall_score <= 29:
                    st.error(f"{username_4}, Your Score is too Low")
                elif overall_score >= 30 and overall_score <= 49:
                    st.warning(f"{username_4}, You can do Better")
                elif overall_score >= 50 and overall_score <= 69:
                    st.success(f"{username_4}, A Good Score")
                else:
                    st.success(f"{username_4}, An Amazing Score")

        elif "No" in user_option_4:
            st.info("CHOOSE THE NEXT OPTION!")

