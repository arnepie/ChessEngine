import pygame.image
import Game_State
import pygame

game_state = Game_State.GameState()


def draw_board():
    pygame.init()

    size = (1600, 1200)  # Width, Height
    rows, columns = 8, 8  # Changeable board size

    first_color = gray = 128, 128, 128  # RGB color code
    second_color = white = 255, 255, 255  # RGB color code

    screen = pygame.display.set_mode(size)  # Make screen
    pygame.display.set_caption("Chess")  # Set caption of screen

    pos_y = 100  # Starting Y position
    for i in range(rows):
        first_color = gray if first_color == white else white  # Switching colors each row
        second_color = gray if second_color == white else white  # Switching colors each row
        pos_y += 80
        pos_x = 400  # Starting X position
        for j in range(int(columns / 2)):
            pos_x += 80
            pygame.draw.rect(screen, first_color, pygame.Rect(pos_x, pos_y, 80, 80))
            pos_x += 80
            pygame.draw.rect(screen, second_color, pygame.Rect(pos_x, pos_y, 80, 80))

    pygame.display.flip()  # Updating screen

    return screen  # Returning screen for future use


def draw_pieces(screen, board):
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bp", "wR", "wN", "wB", "wQ", "wK", "wp"]  # List of all pieces
    images = []  # Empty list for images

    for piece in pieces:
        images.append(pygame.image.load("images/" + piece + ".png"))  # Adding images to list

    for row in board:
        for square in row:
            if square != "---":  # Drawing images on board
                image = images[pieces.index(square[:2])]
                screen.blit(image, (487 + (row.index(square) * 80), 187 + (board.index(row) * 80)))

    pygame.display.flip()  # Updating screen


def main():
    running = True

    screen = draw_board()
    draw_pieces(screen, game_state.board)

    while running:
        for event in pygame.event.get():  # Events from pygame
            if event.type == pygame.QUIT:  # Quit event
                running = False


if __name__ == "__main__":
    main()
