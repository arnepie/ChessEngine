import pygame.image
import Game_State
import pygame
import copy
import time

game_state = Game_State.GameState()


def draw_board():
    size = (1600, 1200)  # Width, Height
    rows, columns = 8, 8  # Board size

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


def highlight_selected_piece(selected_piece, screen):
    red = (255, 0, 0)

    for row_number, row in enumerate(game_state.board):
        for square_number, square in enumerate(row):
            if square == selected_piece:
                pygame.draw.rect(screen, red, pygame.Rect(400 + (80 * (square_number + 1)), 100 + (80 * (row_number + 1)), 80, 80))

    pygame.display.flip()  # Updating screen


def load_images():
    images = []  # Empty list for images
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bp", "wR", "wN", "wB", "wQ", "wK", "wp"]  # List of all pieces

    for piece in pieces:
        images.append(pygame.image.load("images/" + piece + ".png"))  # Adding images to list

    return images


def draw_pieces(screen, board, images):
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bp", "wR", "wN", "wB", "wQ", "wK", "wp"]  # List of all pieces

    for row in board:
        for square in row:
            if square != "---":  # Drawing images on board
                image = images[pieces.index(square[:2])]
                screen.blit(image, (487 + (row.index(square) * 80), 187 + (board.index(row) * 80)))

    pygame.display.flip()  # Updating screen


def main():
    pygame.init()
    running = True

    screen = draw_board()  # Drawing board
    images = load_images()
    time.sleep(0.01)  # Sleeping time to prevent bugs
    draw_pieces(screen, game_state.board, images)  # Drawing pieces

    player_clicks = []  # Making empty list for player clicks
    holding_a_piece = False  # Setting holding_a_piece to false
    piece_holding = None  # Setting piece_holding to None

    while running:
        for event in pygame.event.get():  # Events from pygame
            if event.type == pygame.MOUSEBUTTONDOWN:  # Clicking Event
                mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()  # Getting mouse pos
                player_clicks.append(pygame.mouse.get_pos())  # Adding mouse pos to player clicks list
                if len(player_clicks) == 1:
                    holding_a_piece = False

                    found = False
                    for row in game_state.board:
                        if found:
                            break

                        for square in row:
                            if game_state.white_to_move and square[:1] == "w":
                                piece_pos_y = 215 + (80 * game_state.board.index(row))  # Getting Y pos of piece
                                piece_pos_x = 515 + (80 * row.index(square))  # Getting X pos of piece

                                if piece_pos_x - 40 < mouse_pos_x < piece_pos_x + 40 and piece_pos_y - 40 < mouse_pos_y < piece_pos_y + 40:  # Checking if mouse pos is on square of piece
                                    piece_holding = square  # Setting piece_holding to the piece that was selected
                                    holding_a_piece = True  # Setting holding_a_piece to true
                                    valid_moves = game_state.check_valid_moves(piece_holding)
                                    for valid_move in valid_moves:
                                        print("")
                                        for row1 in valid_move:
                                            print(row1)
                                    found = True
                                    break

                            if not game_state.white_to_move and square[:1] == "b":
                                piece_pos_y = 215 + (80 * game_state.board.index(row))  # Getting Y pos of piece
                                piece_pos_x = 515 + (80 * row.index(square))  # Getting X pos of piece

                                if piece_pos_x - 40 < mouse_pos_x < piece_pos_x + 40 and piece_pos_y - 40 < mouse_pos_y < piece_pos_y + 40:  # Checking if mouse pos is on square of piece
                                    piece_holding = square  # Setting piece_holding to the piece that was selected
                                    holding_a_piece = True  # Setting holding_a_piece to true
                                    valid_moves = game_state.check_valid_moves(piece_holding)
                                    for valid_move in valid_moves:
                                        print("")
                                        for row1 in valid_move:
                                            print(row1)
                                    found = True
                                    break

                    if not holding_a_piece:
                        player_clicks = []  # If player is not holding a piece, the clicks get reset
                    else:
                        screen = draw_board()  # Drawing board
                        highlight_selected_piece(piece_holding, screen)  # Drawing highlight square
                        time.sleep(0.01)  # Sleeping time to prevent bugs
                        draw_pieces(screen, game_state.board, images)  # Drawing pieces

                if len(player_clicks) == 2:
                    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()  # Getting mouse pos

                    for row_number, row in enumerate(game_state.board):
                        for square_number, square in enumerate(row):
                            square_pos_y = 215 + (80 * row_number)
                            square_pos_x = 515 + (80 * square_number)

                            if square_pos_x - 40 < mouse_pos_x < square_pos_x + 40 and square_pos_y - 40 < mouse_pos_y < square_pos_y + 40:  # Checking on which square mouse pos is
                                row_set_index = row_number  # Defining row index of square selected
                                square_set_index = square_number  # Defining square index of square selected

                                row = game_state.board[row_set_index]  # Defining row
                                if row[square_set_index] == piece_holding:  # If player clicked the same square
                                    holding_a_piece = False
                                    player_clicks = []
                                    piece_holding = None

                                if holding_a_piece:
                                    for find_row in game_state.board:
                                        for find_square in find_row:
                                            if find_square == piece_holding:
                                                find_row[find_row.index(piece_holding)] = "---"  # Setting original square to empty
                                                set_row = game_state.board[row_set_index]  # Defining row
                                                set_row[square_set_index] = piece_holding  # Changing square selected to piece selected

                                                if len(game_state.moves) < 1:
                                                    game_state.moves.append(copy.deepcopy(game_state.board))  # Making deepcopy of board and adding it to the moves list
                                                    game_state.white_to_move = not game_state.white_to_move  # Switching color to move each turn

                                                elif game_state.board != game_state.moves[-1]:
                                                    game_state.moves.append(copy.deepcopy(game_state.board))  # Making deepcopy of board and adding it to the moves list
                                                    game_state.white_to_move = not game_state.white_to_move  # Switching color to move each turn

                    player_clicks = []  # resetting player clicks
                    holding_a_piece = False
                    screen = draw_board()  # Drawing board
                    highlight_selected_piece(None, screen)  # Drawing highlight square
                    time.sleep(0.01)  # Sleeping time to prevent bugs
                    draw_pieces(screen, game_state.board, images)  # Drawing pieces

            if event.type == pygame.KEYDOWN:  # Key down event
                if event.key == pygame.K_BACKSPACE:  # Backspace event
                    if len(game_state.moves) > 1:
                        game_state.board = copy.deepcopy(game_state.moves[-2])  # Board is set to second last move
                        game_state.moves.pop(-1)  # Last move is removed from moves list
                    else:  # If only 1 move is played, the board and the moves list is reset
                        game_state.board = [
                                            ["bR1", "bN1", "bB1", "bQ", "bK", "bB2", "bN2", "bR2"],
                                            ["bp1", "bp2", "bp3", "bp4", "bp5", "bp6", "bp7", "bp8"],
                                            ["---", "---", "---", "---", "---", "---", "---", "---"],
                                            ["---", "---", "---", "---", "---", "---", "---", "---"],
                                            ["---", "---", "---", "---", "---", "---", "---", "---"],
                                            ["---", "---", "---", "---", "---", "---", "---", "---"],
                                            ["wp1", "wp2", "wp3", "wp4", "wp5", "wp6", "wp7", "wp8"],
                                            ["wR1", "wN1", "wB1", "wQ", "wK", "wB2", "wN2", "wR2"]]
                        game_state.moves = []

                    screen = draw_board()  # Drawing board
                    time.sleep(0.01)  # Sleeping time to prevent bugs
                    draw_pieces(screen, game_state.board, images)  # Drawing pieces
                    game_state.white_to_move = not game_state.white_to_move  # Switching color to move each turn

            if event.type == pygame.QUIT:  # Quit event
                running = False


if __name__ == "__main__":
    main()
