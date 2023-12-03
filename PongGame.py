import pygame, random, time
from Entities import *

class PongGame:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.num_players = 1

    def run(self):
        # Dispatches run function based on number of players
        if self.num_players == 1:
            self.play_game(ComputerPlayer(50, HEIGHT//2), Player(WIDTH-50, HEIGHT//2, pygame.K_UP, pygame.K_DOWN))
        else:
            self.play_game(Player(50, HEIGHT//2, pygame.K_w, pygame.K_s), Player(WIDTH-50, HEIGHT//2, pygame.K_UP, pygame.K_DOWN))
        

    def play_game(self, player1: PlayerEntity, player2: PlayerEntity):
        ball = Ball()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            win_status = self.check_for_win(ball)

            if win_status != 0:
                font = pygame.font.Font(None, 74)
                text = font.render(f"Player {win_status} wins!", True, WHITE)
                text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                self.screen.blit(text, text_rect)
                pygame.display.flip()
                running = False
                time.sleep(3)
                continue

            self.screen.fill(BLACK)

            keys = pygame.key.get_pressed()

            player2.move(keys)
            player2.draw(self.screen)

            if isinstance(player1, ComputerPlayer):
                player1.move(ball)
            else:
                player1.move()
            player1.draw(self.screen)

            coll = self.check_for_collision(ball, player1, player2)

            ball.move(coll)
            ball.draw(self.screen)

            pygame.display.flip()

            self.clock.tick(FPS)
        

    def multi_player(self):
        pass

    def check_for_collision(self, ball: Ball, p1: PlayerEntity, p2: PlayerEntity) -> bool:
        """
        Checks for collisions between ball and players
        Returns:
            True for collision
            False for no collision
        """
        left_edge = ball.x - ball.radius
        right_edge = ball.x + ball.radius


        # Check for collision between ball and p1
        if left_edge <= p1.rect.right and left_edge >= p1.rect.left and ball.y <= p1.rect.bottom and ball.y >= p1.rect.top:
            return True

        # Check for collision between ball and p2
        if right_edge >= p2.rect.left and right_edge <= p2.rect.right and ball.y <= p2.rect.bottom and ball.y >= p2.rect.top:
            return True
        
        # If we get here that means no collsions
        return False

    def check_for_win(self, ball: Ball):
        """
        Checks to see if anyone won
        Returns:
            0 if no winner
            1 if Player 1 wins
            2 if Player 2 wins
        """
        left_edge = ball.x - ball.radius
        right_edge = ball.x + ball.radius

        if left_edge <= 0:
            return 2
        if right_edge >= WIDTH:
            return 1
        else:
            return 0
        