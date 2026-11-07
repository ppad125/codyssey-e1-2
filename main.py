class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self, number):
        print(f"[문제 {number}]")
        print(self.question)
        print()
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")
        print()

    def is_correct(self, user_answer):
        return self.answer == user_answer

def create_default_quizzes():
    return [
        Quiz("우사기의 제초 자격증 등급은?", ["1급", "2급", "3급", "5급"], 2),
        Quiz("헌책방에서 돈을 내지 않고 그냥 가려고 했던 캐릭터는?", ["모몽가", "시사", "카니", "치이카와"], 1),
        Quiz("하치와레가 존경하는 캐릭터는?", ["모몽가", "갑옷씨", "랏코", "꿀맛맨"], 3),
        Quiz("쿠리만쥬가 가지고 있는 자격증은?", ["먹방 자격증", "요리 자격증", "제과 자격증", "주류 자격증"], 4),
        Quiz("도토리로 디제잉 하는 캐릭터는?", ["우사기", "모몽가", "쿠리만쥬", "파자마 파티즈"], 1),
    ]

    

def show_menu():
    print("=" * 40)
    print(" 치이카와 퀴즈 게임 ")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)

def read_number(prompt, min_value, max_value):
    while True:
        text = input(prompt).strip()

        if text == "":
            print("입력값이 없습니다. 다시 입력해주세요.")
            continue

        try:
            number = int(text)
        except ValueError:
            print(f"잘못된 입력입니다. {min_value}- {max_value} 사이의 숫자를 입력해주세요.")
            continue

        if min_value <= number <= max_value:
            return number
        
        print(f"잘못된 입력입니다. {min_value}- {max_value} 사이의 숫자를 입력해주세요.")

def play_quiz(quizzes):
    if not quizzes:
        print("퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
        return

    print(f"퀴즈를 시작합니다! (총 {len(quizzes)}문제)")
    correct_count = 0

    for number, quiz in enumerate(quizzes, start=1):
        print("-" * 40)
        quiz.display(number)
        user_answer = read_number("정답을 선택하세요 (1-4): ", 1, 4)

        if quiz.is_correct(user_answer):
            print("정답입니다!")
            correct_count += 1
        else:
            print(f"틀렸습니다. 정답은 {quiz.answer}번입니다.")

    score  = correct_count * 100 // len(quizzes)
    print("-" * 40)
    print(f"퀴즈가 끝났습니다! 총 {len(quizzes)}문제 중 {correct_count}문제를 맞히셨습니다. 점수: {score}점")
    print("-" * 40)



def main():
    quizzes = create_default_quizzes()

    while True:
        show_menu()
        choice = read_number("선택 : ", 1, 5)

        if choice == 1:
            play_quiz(quizzes)
        elif choice == 5:
            print("게임을 종료합니다.")
            break
        else:
            print(f"{choice}번 기능은 아직 준비 중입니다.")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n 입력이 중단되어 게임을 종료합니다.")

    