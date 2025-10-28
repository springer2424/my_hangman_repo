from hangman.game import init_state,apply_guess,validate_guess,is_lost,is_won,render_display,render_summary

from hangman.io import prompt_guess,print_status,print_result
from hangman.words import choose_secret_word
from data.data import WORDS


def play(words: list[str], max_tries: int = 8) -> None:
    rand = choose_secret_word(words)
    state = init_state(rand,max_tries)
     
    while not is_lost(state) and not is_won(state):
        ch = prompt_guess()
        is_valide , msg = validate_guess(ch,state["guessed"])
        print(msg)
        if not is_valide:
            continue

        apply_guess(state,ch)
        print_status(state)
                    

    print_result(state)

                               

if __name__ == "__main__":
     play(WORDS)

