import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Typing Speed Test")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 48)

# Set up game variables
word_list = ["apple", "banana", "cherry", "grape", "orange", "strawberry", "watermelon"]
current_word = ""
player_input = ""
start_time = None

def generate_word():
    return random.choice(word_list)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                player_input = player_input[:-1]
            elif event.key == pygame.K_RETURN:
                if player_input == current_word:
                    player_input = ""
                    current_word = generate_word()
            else:
                player_input += event.unicode

    display.fill(WHITE)
    
    if start_time is None:
        start_time = time.time()

    word_text = font.render(current_word, True, BLACK)
    input_text = font.render(player_input, True, BLACK)

    display.blit(word_text, (width // 2 - word_text.get_width() // 2, height // 2 - 50))
    display.blit(input_text, (width // 2 - input_text.get_width() // 2, height // 2 + 50))

    pygame.display.flip()

    if current_word == player_input:
        elapsed_time = time.time() - start_time
        words_per_second = len(player_input) / elapsed_time
        result_text = font.render(f"Words per second: {words_per_second:.1f}", True, BLACK)
        display.blit(result_text, (width // 2 - result_text.get_width() // 2, height // 2 + 150))
        pygame.display.flip()
        pygame.time.delay(3000)  # Display result for 3 seconds
        start_time = None
        current_word = generate_word()
        player_input = ""

pygame.quit()
