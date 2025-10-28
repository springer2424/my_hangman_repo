def init_state(secret: str, max_tries: int) -> dict:
    state = {
        "secret":secret,
        "display":list(len(secret)*"_"),
        "guessed": set(),
        "wrong_guesses": 0,
        "max_tries": max_tries 
    }
    return state

     



def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if ch in guessed:
        return (False,"Letter already used")
    elif len(ch) != 1:
        return (False,"Only one letter allowed")
    return (True,"valid")

def apply_guess(state: dict, ch: str) -> bool:
    state["guessed"].add(ch)
    if ch in state["secret"]:
        for i,leter in enumerate(state["secret"]):
            if leter == ch:
                state["display"][i] = leter
        return True
    else:
        state["wrong_guesses"] += 1
        return False



def is_won(state: dict) -> bool:
    if set(state["secret"]).issubset(state["display"]):
        return True
    else:
        return False




def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] >= state["max_tries"]:
        return True
    else:
        return False    

def render_display(state: dict) -> str:
    return state["display"]

def render_summary(state: dict) -> str:
    summary = (f"the secret word is {state["secret"]} and you guessed {" ".join(state["display"])}")
    return summary 



