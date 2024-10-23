import pygame
import sys
import random

class PacmanGame:
    def __init__(self):
        pygame.init()
        
        # Load images for the game
        self.load_images()
        self.new_game()

        # Set the screen dimensions and title
        self.window_width = 640
        self.window_height = 480
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Pacman Game with Respawning Coins")

        # Define fonts and buttons
        self.font = pygame.font.SysFont("Arial", 24)
        self.button_font = pygame.font.SysFont("Arial", 18)
        self.restart_button = pygame.Rect(50, self.window_height - 50, 100, 30)
        self.quit_button = pygame.Rect(self.window_width - 150, self.window_height - 50, 100, 30)

        self.main_loop()

    def load_images(self):
        self.images = {
            'robot': pygame.image.load("robot.png"),
            'coin': pygame.image.load("coin.png"),
            'monster': pygame.image.load("monster.png"),
            'door': pygame.image.load("door.png")
        }

    def new_game(self):
        self.robot_position = [50, 50]  # Starting position of the robot
        self.coins = [[150, 150], [300, 100], [450, 200]]  # Positions of collectable coins
        self.monsters = [[200, 250], [400, 300]]  # Positions of monsters
        self.score = 0  # Player score
        self.game_over = False

    def main_loop(self):
        clock = pygame.time.Clock()  # Use clock to control the game frame rate
        while True:
            self.check_events()
            self.update_game()
            self.draw_window()
            clock.tick(30)  # Run at 30 frames per second (fps)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check if Restart button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.restart_button.collidepoint(event.pos):
                    self.new_game()  # Restart the game
                if self.quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

    def update_game(self):
        keys = pygame.key.get_pressed()  # Check which keys are currently being pressed

        if not self.game_over:
            if keys[pygame.K_LEFT]:
                self.robot_position[0] -= 5  # Move left
            if keys[pygame.K_RIGHT]:
                self.robot_position[0] += 5  # Move right
            if keys[pygame.K_UP]:
                self.robot_position[1] -= 5  # Move up
            if keys[pygame.K_DOWN]:
                self.robot_position[1] += 5  # Move down

        # Check if robot collected coins
        for coin in self.coins[:]:
            if pygame.Rect(self.robot_position[0], self.robot_position[1], 40, 40).colliderect(
                    pygame.Rect(coin[0], coin[1], 40, 40)):
                self.coins.remove(coin)
                self.score += 1
                # Spawn a new coin at a random location
                self.spawn_new_coin()

        # Check if robot hit a monster
        for monster in self.monsters:
            if pygame.Rect(self.robot_position[0], self.robot_position[1], 40, 40).colliderect(
                    pygame.Rect(monster[0], monster[1], 40, 40)):
                self.game_over = True

    def spawn_new_coin(self):
        # Randomly generate a new position for the coin
        new_coin_x = random.randint(0, self.window_width - 40)  # Ensure coin stays within screen width
        new_coin_y = random.randint(0, self.window_height - 40)  # Ensure coin stays within screen height
        self.coins.append([new_coin_x, new_coin_y])

    def draw_window(self):
        self.window.fill((200, 200, 200))  # Fill the screen with a light gray background

        # Draw the robot
        self.window.blit(self.images['robot'], self.robot_position)

        # Draw the coins
        for coin in self.coins:
            self.window.blit(self.images['coin'], coin)

        # Draw the monsters
        for monster in self.monsters:
            self.window.blit(self.images['monster'], monster)

        # Draw score and game status
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))  # Score in black text
        self.window.blit(score_text, (10, 10))

        if self.game_over:
            game_over_text = self.font.render("Game Over!", True, (255, 0, 0))
            self.window.blit(game_over_text, (self.window_width // 2 - 50, self.window_height // 2))

        # Draw the Restart and Quit buttons
        pygame.draw.rect(self.window, (0, 128, 0), self.restart_button)
        pygame.draw.rect(self.window, (128, 0, 0), self.quit_button)

        restart_text = self.button_font.render("Restart", True, (255, 255, 255))
        quit_text = self.button_font.render("Quit", True, (255, 255, 255))

        self.window.blit(restart_text, (self.restart_button.x + 10, self.restart_button.y + 5))
        self.window.blit(quit_text, (self.quit_button.x + 20, self.quit_button.y + 5))

        pygame.display.flip()

if __name__ == "__main__":
    PacmanGame()
