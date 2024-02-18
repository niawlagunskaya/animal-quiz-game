
class Questions:
    def __init__(self, question_text, correct_answer, answer_options):
        self.text = question_text
        self.correct_answer = correct_answer
        self.options = answer_options
    
    def display(self, question_number):
        print(f"{question_number}. {self.text}")
        for i, option in enumerate(self.options, start=1):
            print(f"   {i}. {option}")
    
    def check_answer(self, user_choice):
        return self.options[int(user_choice)-1] == self.correct_answer

questions = [
    "What is the largest mammal?",
    "Which animal is known as the 'King of the Jungle'?",
    "What is the fastest land animal?",
    "What animal is the symbol of wisdom?",
    "What animal is known for its long neck?",
    "What is the only mammal capable of sustained flight?",
    "Which animal has the longest lifespan?",
    "What animal has the best sense of smell in the world?",
    "What is the tallest animal on Earth?",
    "What animal is a natural swimmer and can hold its breath for up to 20 minutes?",
    "What animal is known for rolling into a ball when threatened?",
    "What is the national animal of Australia?",
    "What animal has a hump on its back?",
    "What animal is often referred to as the 'Gentle Giant'?",
    "What is the largest big cat in the world?",
    "What animal is capable of changing its color to blend in with its surroundings?",
    "What animal is known for its black and white stripes?",
    "What is the only continent where giraffes live in the wild?",
    "What animal has the longest migration route of any mammal?",
    "What is the fastest marine animal?"
]
correct_answers = [
    "Blue Whale",
    "Lion",
    "Cheetah",
    "Owl",
    "Giraffe",
    "Bat",
    "Bowhead Whale",
    "Bloodhound",
    "Giraffe",
    "Hippo",
    "Armadillo",
    "Kangaroo",
    "Camel",
    "Elephant",
    "Tiger",
    "Chameleon",
    "Zebra",
    "Africa",
    "Arctic Tern",
    "Sailfish"
]
answer_options = [
    ["Elephant", "Blue Whale", "Giraffe", "Hippo"],
    ["Lion", "Tiger", "Leopard", "Elephant"],
    ["Cheetah", "Gazelle", "Ostrich", "Giraffe"],
    ["Owl", "Eagle", "Hawk", "Parrot"],
    ["Giraffe", "Elephant", "Kangaroo", "Zebra"],
    ["Bat", "Bird", "Butterfly", "Bee"],
    ["Bowhead Whale", "Tortoise", "Galapagos Giant Tortoise", "Parrot"],
    ["Bloodhound", "Wolf", "Shark", "Elephant"],
    ["Giraffe", "Elephant", "Kangaroo", "Horse"],
    ["Hippo", "Elephant", "Seal", "Penguin"],
    ["Armadillo", "Hedgehog", "Turtle", "Tortoise"],
    ["Kangaroo", "Koala", "Platypus", "Emu"],
    ["Camel", "Horse", "Cow", "Buffalo"],
    ["Elephant", "Giraffe", "Horse", "Rhinoceros"],
    ["Tiger", "Lion", "Leopard", "Jaguar"],
    ["Chameleon", "Octopus", "Cuttlefish", "Frog"],
    ["Zebra", "Tiger", "Giraffe", "Leopard"],
    ["Africa", "North America", "South America", "Asia"],
    ["Arctic Tern", "Polar Bear", "Salmon", "Monarch Butterfly"],
    ["Sailfish", "Dolphin", "Shark", "Whale"]
]
quizzes = []
score=0


for question, answer, option_list in zip(questions, correct_answers, answer_options):
    quiz = Questions(question, answer, option_list)
    quizzes.append(quiz)

for i, quiz in enumerate(quizzes, start=1):
    quiz.display(i)
    user_input = input("Your answer (enter the corresponding option number): ")
    score += 10 if quiz.check_answer(user_input) else 0
    print("Correct!\n" if quiz.check_answer(user_input) else f"Incorrect. The correct answer is: {quiz.correct_answer}\n")

print(f"Your score is {score}")


