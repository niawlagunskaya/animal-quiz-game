
class Question:
    def __init__(self, question_text, answer_options, correct_answer):
        self.text = question_text
        self.correct_answer = correct_answer
        self.answer_options = answer_options
    
    def display(self, question_number):
        print(f"{question_number}. {self.text}")
        for i, option in enumerate(self.answer_options, start=1):
            print(f"   {i}. {option}")
    
    def check_answer(self, user_choice):
        return int(user_choice)-1 == self.correct_answer

score=0

quiz_questions = [
    Question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippo"], 1),
    Question("Which animal is known as the 'King of the Jungle'?", ["Lion", "Tiger", "Leopard", "Elephant"], 0),
    Question("What is the fastest land animal?", ["Gazelle", "Ostrich", "Cheetah", "Giraffe"], 2),
    Question("What animal is the symbol of wisdom?", ["Eagle", "Owl", "Hawk", "Parrot"], 1),
    Question("What animal is known for its long neck?", ["Giraffe", "Elephant", "Kangaroo", "Zebra"], 0),
    Question("What is the only mammal capable of sustained flight?", ["Bat", "Bird", "Butterfly", "Bee"], 0),
    Question("Which animal has the longest lifespan?", ["Tortoise", "Galapagos Giant Tortoise", "Bowhead Whale", "Parrot"], 2),
    Question("What animal has the best sense of smell in the world?", ["Wolf", "Shark", "Elephant", "Bloodhound"], 3),
    Question("What is the tallest animal on Earth?", ["Elephant", "Giraffe", "Kangaroo", "Horse"], 1),
    Question("What animal is a natural swimmer and can hold its breath for up to 20 minutes?", ["Hippo", "Elephant", "Seal", "Penguin"], 0),
    Question("What animal is known for rolling into a ball when threatened?", ["Armadillo", "Hedgehog", "Turtle", "Tortoise"], 0),
    Question("What is the national animal of Australia?", ["Koala", "Platypus", "Emu", "Kangaroo"], 3),
    Question("What animal has a hump on its back?", ["Horse", "Camel", "Cow", "Buffalo"], 1),
    Question("What animal is often referred to as the 'Gentle Giant'?", ["Giraffe", "Horse", "Elephant", "Rhinoceros"], 2),
    Question("What is the largest big cat in the world?", ["Tiger", "Lion", "Leopard", "Jaguar"], 0),
    Question("What animal is capable of changing its color to blend in with its surroundings?", ["Octopus", "Cuttlefish", "Frog", "Chameleon"], 3),
    Question("What animal is known for its black and white stripes?", ["Tiger", "Zebra", "Giraffe", "Leopard"], 1),
    Question("What is the only continent where giraffes live in the wild?", ["North America", "South America", "Africa",  "Asia"], 2),
    Question("What animal has the longest migration route of any mammal?", ["Arctic Tern", "Polar Bear", "Salmon", "Monarch Butterfly"], 0),
    Question("What is the fastest marine animal?", ["Dolphin", "Shark", "Whale", "Sailfish"], 3)
]

for i, quiz in enumerate(quiz_questions, start=1):
    quiz.display(i)
    user_input = input("Your answer (enter the corresponding option number): ")
    score += 10 if quiz.check_answer(user_input) else 0
    print("Correct!\n" if quiz.check_answer(user_input) else f"Incorrect. The correct answer is: {quiz.answer_options[quiz.correct_answer]}\n")

print(f"Your score is {score}")
 