import random

questions_hard = ["What is the name of the main antagonist ?", "how many difficulties are there for each boss ?",
                  "What is the name of the hardest boss difficulty ?", " Does ragnarok have explorer notes ?",
                  "Does genesis part 2 have explorer notes ?", "At what level can you make Tranquilizer Dart’s ?",
                  "How many metal ingots does a Tranquilizer Dart cost in total (including the rifle ammo) ?",
                  "Can wyverns carry 2 creatures at once ?", "How many hexagons do 20 pieces of crystal cost ?",
                  "Coes the chem bench require a generator to power it ?"]
answers_hard = ["rockwell", "3", "alpha", "no", "yes", "62", "3", "no", "230", "yes"]

i = len(questions_hard)
while i > 0:
    num_of_questions = len(questions_hard) - 1
    question_num = random.randint(0, num_of_questions)
    print(questions_hard[question_num])
    print(answers_hard[question_num])
    questions_hard.remove(questions_hard[question_num])
    answers_hard.remove(answers_hard[question_num])
    i -= 1
