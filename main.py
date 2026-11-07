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

def main():
    while True:
        show_menu()
        choice = read_number("선택 : ", 1, 5)

        if choice == 5:
            print("게임을 종료합니다.")
            break
        print(f"{choice}번 기능은 아직 준비 중입니다.")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n 입력이 중단되어 게임을 종료합니다.")

    