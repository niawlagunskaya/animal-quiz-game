import pygame
pygame.init()

screen_width = 700
screen_height = 500
PINK =  (222,93,131)
WHITE = (255,255,255)
ORANGE = (255,165,0)
BLUE = (65,105,225)
GREY = (169,169,169)
box_width = 200
box_height = 100
font = pygame.font.Font(None, 32) 
large_font = pygame.font.Font(None, 64)  # Larger font for final score
small_font = pygame.font.Font(None, 30)   # Smaller font for button text
question_index = 0
score = 0
boxes = []

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("animal-quiz-game")

running = True
while running:

    class Question:
        def __init__(self, text, answer_options, correct_answer):
            self.text = text
            self.correct_answer = correct_answer
            self.answer_options = answer_options
        
        def check_answer(self, user_choice):
            return int(user_choice) == int(self.correct_answer)

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           if question_index < len(quiz_questions):
               for i, (box_surface, (x, y)) in enumerate(boxes):
                   box_rect = pygame.Rect(x, y, box_width, box_height)
                   if box_rect.collidepoint(event.pos):
                       if quiz_questions[question_index].check_answer(i):
                           score += 10
                       question_index += 1
                       break
           else:
               if 100 <= event.pos[0] <= 300 and 300 <= event.pos[1] <= 400:
                   # Retake quiz button clicked
                   question_index = 0
                   score = 0
               elif 400 <= event.pos[0] <= 600 and 300 <= event.pos[1] <= 400:
                   # Quit button clicked
                   running = False

    screen.fill(WHITE)

    quiz_questions = [
        Question("Which farm animal says 'oink'?", ["Pig", "Cow", "Goat", "Duck"], 0),
        Question("What farm animal is known for its milk?", ["Cow", "Pig", "Goat", "Duck"], 0),
        Question("What animal is often used for riding?", ["Pig", "Cow", "Goat", "Horse"], 3),
        Question("What farm animal lays eggs?", ["Chicken", "Sheep", "Horse", "Duck"], 0),
        Question("Which animal is known for its wool?", ["Pig", "Cow", "Goat", "Sheep"], 3),
        Question("What animal clucks and pecks?", ["Pig", "Cow", "Goat", "Chicken"], 3),
        Question("What farm animal is often found in a pen?", ["Pig", "Cow", "Goat", "Duck"], 1),
        Question("What animal neighs and gallops?", ["Pig", "Cow", "Goat", "Horse"], 3),
        Question("What animal is known for its 'baa' sound?", ["Pig", "Cow", "Goat", "Sheep"], 3),
        Question("What farm animal says 'quack'?", ["Pig", "Cow", "Goat", "Duck"], 3),
    ]

    if question_index < len(quiz_questions):
        current_question = quiz_questions[question_index]
        text = font.render(current_question.text, True, PINK)
        text_rect = text.get_rect(center=(screen_width // 2, 75))
        screen.blit(text, text_rect)
        score_text = font.render(f"Points: {score}", True, PINK)
        score_rect = score_text.get_rect(bottomright=(screen_width - 10, screen_height - 10))
        screen.blit(score_text, score_rect)
       

        for i, option in enumerate(current_question.answer_options):
            x =  80 + (i % 2) * (screen_width // 2.5) + 25
            y = 150 + (i // 2) * (box_height + 50)
            box_surface = pygame.Surface((box_width, box_height))
            box_surface.fill(PINK)
            box_text = font.render(option, True, WHITE)
            text_rect = box_text.get_rect(center=(box_width // 2, box_height // 2))
            box_surface.blit(box_text, text_rect)
            boxes.append((box_surface, (x, y)))

        for (box_surface, (x, y)) in boxes:
            pygame.draw.rect(screen, WHITE, (x, y, box_width, box_height), 2)
            screen.blit(box_surface, (x, y))
    else:
        final_score_text = large_font.render(f"Final Score: {score}", True, ORANGE)
        final_score_rect = final_score_text.get_rect(center=(screen_width // 2, screen_height // 3))
        screen.blit(final_score_text, final_score_rect)
        
        # Draw buttons
        quit_button = pygame.Rect(400, 300, 200, 100)
        retake_button = pygame.Rect(100, 300, 200, 100)
        pygame.draw.rect(screen, GREY, quit_button)
        pygame.draw.rect(screen, BLUE, retake_button)
        retake_text = small_font.render("Retake Quiz", True, WHITE)
        quit_text = small_font.render("Quit", True, WHITE)
        retake_text_rect = retake_text.get_rect(center=retake_button.center)
        quit_text_rect = quit_text.get_rect(center=quit_button.center)
        screen.blit(quit_text, quit_text_rect)
        screen.blit(retake_text, retake_text_rect)

    pygame.display.flip()

pygame.quit()
