import classes


def start_game():
    game_setup()


def game_setup():
    classes.game.shuffle_deck()
    classes.player.cut_a_card()
    classes.opponent.cut_a_card()
    classes.game.compare_cut()
    start_hand()


def start_hand():
    while len(classes.player.hand) > 4:
        classes.player.discard_to_crib()
    while len(classes.opponent.hand) > 4:
        classes.opponent.discard_to_crib()
    classes.cycle.new_fuc()
    play_hand()


def play_hand():
    if classes.player.turn == "Yes":
        classes.player.take_turn()
    elif classes.opponent.turn == "Yes":
        classes.opponent.take_turn()


start_game()
