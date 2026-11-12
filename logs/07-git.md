# 07. Git 작업 기록

## 커밋 그래프 (`git log --oneline --graph`, 작성 시점)
```text
* 43e8391 Docs: 설계 이유, JSON 한계, 백업·복구, Git 작업 방식, 변경 가이드 추가
* 76135c7 Feat: 저장 파일 자동 백업과 손상 파일 보관 기능 추가
* 6f630f1 Docs: git log 그래프 스크린샷 추가
* f06f8b1 Docs: 실행 화면 스크린샷 추가 및 README 실행 화면 섹션 작성
* 2659b1f Chore: state.json 데이터 정리 (테스트 문제 제거, 작가 문제 추가)
* 652a04c Docs: README에 clone/pull 실습 기록 추가
* 11135d8 Docs: README 제목 추가 (clone 저장소에서 작업)
* 8526891 Docs: README 제목과 프로젝트 개요 추가
* 33072aa Docs: README 작성 (개요, 실행 방법, 기능, 파일 구조, 데이터 설명)
* 9d4eb7d Feat: state.json 저장/불러오기 구현
* dbb28f1 게임 기능을 QuizGame 클래스로 분리
* 3e57c11 Feat: 최고 점수 확인 및 갱신 기능 구현
* ea4739a Feat: 퀴즈 목록 기능 구현
* d428481 Feat: 퀴즈 추가 기능 구현 (입력 검증 포함)
*   d49ea49 Merge: 퀴즈 풀기 기능 병합
|\  
| * 82af12d Feat: 퀴즈 풀기 기능 구현 (채점, 결과 출력)
|/  
* 723aba6 Feat: 치이카와 퀴즈 5개 작성
* 1b714e8 Feat: Quiz 클래스 구현 (문제 출려그 정답 확인)
* bda008c Feat: 메뉴 출력과 입력 예외 처리 구현
* 176b351 Chore: 프로젝트 초기 설정
```

## 브랜치 생성과 병합 (`git reflog` 발췌, 원래 폴더 `e1-2`)
```text
723aba6 HEAD@{2026-11-07 13:10:06 +0900}: checkout: moving from main to feature/play-quiz
723aba6 HEAD@{2026-11-07 13:44:35 +0900}: checkout: moving from feature/play-quiz to main
d49ea49 HEAD@{2026-11-07 13:44:39 +0900}: merge feature/play-quiz: Merge made by the 'ort' strategy.
```

- `git checkout -b feature/play-quiz`로 브랜치를 만들고, 퀴즈 풀기 기능을 커밋(`82af12d`)한 뒤
- `git checkout main` → `git merge --no-ff feature/play-quiz`로 병합 커밋 `d49ea49`를 만들었습니다.

## clone과 pull 실습 (`git reflog` 발췌)
**복사본 폴더 `e1-2-clone`**
```text
8526891 HEAD@{2026-11-12 14:17:27 +0900}: clone: from github.com:ppad125/codyssey-e1-2.git
11135d8 HEAD@{2026-11-12 16:07:08 +0900}: pull: Fast-forward
652a04c HEAD@{2026-11-12 16:07:15 +0900}: commit: Docs: README에 clone/pull 실습 기록 추가
```

**원래 폴더 `e1-2`**
```text
652a04c HEAD@{2026-11-12 16:07:35 +0900}: pull: Fast-forward
```

복사본 폴더에서 README에 한 섹션을 추가해 commit/push(`652a04c`)하고, 원래 폴더에서 `git pull`로 같은 커밋을 받아왔습니다.

> 참고: `11135d8`은 메시지에 "clone 저장소에서 작업"이라고 적었지만, 실수로 원래 폴더에서 만든 커밋입니다. 실제 clone 실습 커밋은 `652a04c`입니다.

## Git 기초 명령어 7종 사용 기록
| 명령 | 사용한 곳 |
|---|---|
| `init` | `git init -b main`으로 저장소 생성 |
| `add` | 기능마다 `git add main.py` 등으로 스테이징 |
| `commit` | 기능 단위 커밋 (`Feat`/`Refactor`/`Docs`/`Chore`) |
| `push` | `git push -u origin main` 후 커밋마다 push |
| `checkout` | `feature/play-quiz` 브랜치 생성·이동, `main` 복귀 |
| `clone` | `e1-2-clone` 폴더로 복제 |
| `pull` | `e1-2-clone`과 `e1-2`에서 각각 `git pull` |
