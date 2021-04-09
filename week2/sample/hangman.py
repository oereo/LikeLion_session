import random

HANGMAN_SUGGESTED_WORD_START_INDEX = 1
INPUT_ATTEMPT_WORD_MESSAGE = "도전할 문자를 입력하세요! : "
INPUT_ATTEMPT_WRONG_MESSAGE = "잘못된 입력 형식입니다!"
SUCCESS_MESSAGE = "******************\nMission Complete!\n******************\n"
WRONG_MESSAGE = "단어에 포함되지 않은 문자입니다ㅠㅠ"
FAIL_MESSAGE = "게임 실패!!"

hangman_suggested_word = {
    1: "around",
    2: "complain",
    3: "improve",
    4: "sweet",
    5: "able",
    6: "arrange",
    7: "complete",
    8: "govern",
    9: "notice",
    10: "represent",
    11: "precious",
    12: "proud",
    13: "strength",
    14: "work",
    15: "complex",
    16: "claim",
    17: "flavor",
    18: "honest",
    19: "include",
    20: "order",
    21: "precise",
    22: "prove",
    23: "reputation",
    24: "stretch",
    25: "well",
    26: "above",
    27: "against",
    28: "devote",
    29: "harm",
    30: "grade",
    31: "income",
    32: "ordinary",
    33: "march",
    34: "provide",
    35: "realize", 
    36: "abroad",
    37: "before", 
    38: "compose",
    39: "gradual",
    40: "mark",
    41: "reason",
    42: "shy",
    43: "therefore",
    44: "absent",
    45: "classify",
    46: "turn",
    47: "graduate",
    48: "indeed",
    49: "original",
    50: "receive",
}

def main():
    run()

def input_attempt_word():
    input_word = input(INPUT_ATTEMPT_WORD_MESSAGE)
    return input_word

def check_input_attempt_word():
    while True:
        input_word = input_attempt_word()
        if input_word.isalpha() and len(input_word) == 1:
            break
        print(INPUT_ATTEMPT_WRONG_MESSAGE)
    
    return input_word


def printer_matched_lettering(lettering):
    print(lettering, " ", end="")

def printer_underbar():
    print("_", " ", end="")

def append_letter_attempt_word(letter, attempt_word):
    if letter not in attempt_word:
        attempt_word += letter
    return attempt_word

def compare_suggested_word(attempt_word, hangman_answer):
    is_succeedd = True
    for lettering in hangman_answer:
        if lettering in attempt_word:
            printer_matched_lettering(lettering)
        else:
            printer_underbar()
            is_succeedd = False
    
    return is_succeedd

def printer_finish_game():
    print(SUCCESS_MESSAGE)

def printer_hangman_answer_word(hangman_answer):
    print("정답 :", hangman_answer)

def printer_wrong_letter():
    print(WRONG_MESSAGE)

def printer_fail_game():
    print(FAIL_MESSAGE)

def printer_hangman(count):
    if count >= 1:
        head = "(.,.)"
    else:
        head = "     "
    if count >= 2:
        body = "|"
    else:
        body = " "
    if count >= 3:
        left_arm = "/"
    else:
        left_arm = " "
    if count >= 4:
        right_arm = "\\"
    else:
        right_arm = " "
    if count >= 5:
        left_leg = "/"
    else:
        left_leg = " "
    if count >= 6:
        right_leg = "\\"
    else:
        right_leg = " "

    print("----------")
    print("  |     ||")
    print("%s   ||" % head)
    print(" %s%s%s    ||" % (left_arm, body, right_arm))
    print("  %s     ||" % body)
    print(" %s %s    ||" % (left_leg, right_leg))
    print("        ||")
    print("     -----")

def check_letter_in_answer_word(letter, hangman_answer_word, fail_count):
    if letter not in hangman_answer_word:
        printer_wrong_letter()
        print()
        fail_count += 1
    return fail_count

def is_game_fail(fail_count):
    if fail_count >= 7:
        return True
    return False

def run():
    attempt_word = ""
    hangman_answer = get_hangman_answer_word()
    fail_count = 0

    while True:
        game_succeed = compare_suggested_word(attempt_word, hangman_answer)
        print()
        if game_succeed:
            printer_finish_game()
            printer_hangman_answer_word(hangman_answer)
            break

        letter = check_input_attempt_word()
        attempt_word = append_letter_attempt_word(letter, attempt_word)
        fail_count = check_letter_in_answer_word(letter, hangman_answer, fail_count)

        if is_game_fail(fail_count):
            printer_fail_game()
            printer_hangman_answer_word(hangman_answer)
            break

        printer_hangman(fail_count)
        
def get_hangman_word_size():
    return len(hangman_suggested_word)

def get_hangman_answer_word():
    return hangman_suggested_word[random.randint(HANGMAN_SUGGESTED_WORD_START_INDEX, get_hangman_word_size())]


if __name__ == "__main__":
    main()