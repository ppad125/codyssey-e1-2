import json
from pathlib import Path

STATE_FILE = Path(__file__).parent / "state.json"


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

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

def create_default_quizzes():
    return [
        Quiz("우사기의 제초 자격증 등급은?", ["1급", "2급", "3급", "5급"], 2),
        Quiz("헌책방에서 돈을 내지 않고 그냥 가려고 했던 캐릭터는?", ["모몽가", "시사", "카니", "치이카와"], 1),
        Quiz("하치와레가 존경하는 캐릭터는?", ["모몽가", "갑옷씨", "랏코", "꿀맛맨"], 3),
        Quiz("쿠리만쥬가 가지고 있는 자격증은?", ["먹방 자격증", "요리 자격증", "제과 자격증", "주류 자격증"], 4),
        Quiz("도토리로 디제잉 하는 캐릭터는?", ["우사기", "모몽가", "쿠리만쥬", "파자마 파티즈"], 1),
    ]

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


def read_text(prompt):
    while True:
        text = input(prompt).strip()

        if text == "":
            print("입력값이 없습니다. 다시 입력해주세요.")
            continue
        return text

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = None
        self.load_state()

    def load_state(self):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            quizzes = []
            for item in data["quizzes"]:
                quizzes.append(Quiz(item["question"], item["choices"], item["answer"]))

            self.quizzes = quizzes
            self.best_score = data["best_score"]
            print(f"저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개)")
        except FileNotFoundError:
            print("저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
            self.quizzes = create_default_quizzes()
            self.best_score = None
        except (ValueError, KeyError, TypeError):
            print("데이터 파일이 손상되어 기본 퀴즈로 복구합니다.")
            self.quizzes = create_default_quizzes()
            self.best_score = None

    def save_state(self):
        quiz_list = []
        for quiz in self.quizzes:
            quiz_list.append(quiz.to_dict())

        data = {
            "quizzes": quiz_list,
            "best_score": self.best_score,
        }

        try:
            with open(STATE_FILE, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except OSError:
            print("데이터를 저장하지 못했습니다.")

    def show_menu(self):
        print("=" * 40)
        print(" 치이카와 퀴즈 게임 ")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def play_quiz(self):
        if not self.quizzes:
            print("퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        print(f"퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        correct_count = 0

        for number, quiz in enumerate(self.quizzes, start=1):
            print("-" * 40)
            quiz.display(number)
            user_answer = read_number("정답을 선택하세요 (1-4): ", 1, 4)

            if quiz.is_correct(user_answer):
                print("정답입니다!")
                correct_count += 1
            else:
                print(f"틀렸습니다. 정답은 {quiz.answer}번입니다.")

        score = correct_count * 100 // len(self.quizzes)
        print("-" * 40)
        print(f"퀴즈가 끝났습니다! 총 {len(self.quizzes)}문제 중 {correct_count}문제를 맞히셨습니다. 점수: {score}점")
        print("-" * 40)
        self.update_best_score(score)

    def update_best_score(self, score):
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print(f"최고 점수가 갱신되었습니다! 현재 최고 점수: {self.best_score}점")
            self.save_state()

    def add_quiz(self):
        print("퀴즈를 추가합니다.")
        question = read_text("문제를 입력하세요: ")

        choices = []
        for i in range(4):
            choice = read_text(f"{i + 1}번 선택지를 입력하세요: ")
            choices.append(choice)

        answer = read_number("정답 번호를 입력하세요 (1-4): ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_state()
        print("퀴즈가 추가되었습니다.")

    def list_quizzes(self):
        if not self.quizzes:
            print("퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
            return

        print(f"총 {len(self.quizzes)}개의 퀴즈가 있습니다.")
        print("-" * 40)

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")

        print("-" * 40)

    def show_score(self):
        if self.best_score is None:
            print("점수를 확인할 수 없습니다. 먼저 퀴즈를 풀어주세요.")
            return

        print(f"최고 점수: {self.best_score}점")

    def run(self):
        while True:
            self.show_menu()
            choice = read_number("선택 : ", 1, 5)

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                self.save_state()
                print("게임을 종료합니다.")
                break

def main():
    game = QuizGame()

    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 저장 후 게임을 종료합니다.")
        game.save_state()


if __name__ == "__main__":
    main()

    