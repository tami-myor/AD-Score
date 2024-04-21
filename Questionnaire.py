class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "What is the baby's gender?\n(a) Male\n(b) Female\n\n",
    "Do you live in an urban enviorment? \n(a) Yes \n(b) No \n\n",
    "Is the baby due during Autumn? \n(a) Yes \n(b) No \n\n",
    "Does anyone in the household smoke? \n(a) Yes \n(b) No \n\n",
    "What is your social economic status? \n(a) Medium-High \n(b) Medium-Low \n\n",

    "Parents Information: \n\nDoes the baby's mother have or use to have an atopic condition? \n(a) Yes \n(b) No \n\n",
    "Does the baby's father have or use to have an atopic condition? \n(a) Yes \n(b) No \n\n",
    "Does any of the biological parents have or use to have an Atopic Dematitis? \n(a) Yes \n(b) No \n\n",
    "Did the baby's mother consume antibiotics during pregnancy? \n(a) Yes \n(b) No \n\n",

    "Siblings Information: \n\nIs the baby a first born? \n(a) Yes \n(b) No \n\n",
    "How many siblings have an atopic condition? \n(a) one or more \n(b) Non  \n\n",
    "Does at least one of the siblings have Atopic Dermatitis? \n(a) Yes \n(b) No \n\n"
]



questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "a"),

    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "a"),

    Question(question_prompts[9], "a"),
    Question(question_prompts[10], "a"),
    Question(question_prompts[11], "a")
]


def score_cat (score):
    res = []
    if score <=0.35 :
      res = "Low Risk"
    elif score <= 0.5:
      res = "Medium Risk"
    else:
      res = "High Risk"
    return res


def run_quest(question):
    score = 0
    oneplus = "a"
    if input(question[0].prompt) == oneplus:
            score += 4
    if input(question[1].prompt) == oneplus:
            score += 4
    if input(question[2].prompt) == oneplus:
            score += 2
    if input(question[3].prompt) == oneplus:
            score += 2
    if input(question[4].prompt) == oneplus:
            score += 8
    if input(question[5].prompt) == oneplus:
            score += 2.5
    if input(question[6].prompt) == oneplus:
            score += 2.5    
    if input(question[7].prompt) == oneplus:
            score += 5
    if input(question[8].prompt) == oneplus:
            score += 1.5
    if input(question[9].prompt) == oneplus:
            score += 6
    if input(question[10].prompt) == oneplus:
            score += 4
    if input(question[11].prompt) == oneplus:
            score += 10
    calc_score = (score/49) + 0.1        
    final_score = score_cat(calc_score)                                                                                         
    print ("The baby's AD risk category: " + final_score) 


# Run the questionnaire, fill the answers and get the baby's AD risk score:
run_quest(questions)

