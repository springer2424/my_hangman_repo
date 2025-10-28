from hangman.game import render_display,render_summary,is_won,is_lost



def prompt_guess() -> str:
    ch = input("plise gess a leter: ")
    return ch

def print_status(state: dict) -> None:
    print(" ".join(render_display(state)))
    print(state["guessed"])
    print(8 - state["wrong_guesses"])

def print_result(state: dict) -> None:
    if is_won(state):
        print("harrrrryyyyyy you won")
        print(render_summary(state))
    elif is_lost(state):
        print("hahahahaha you lost")
        print(render_summary(state))    