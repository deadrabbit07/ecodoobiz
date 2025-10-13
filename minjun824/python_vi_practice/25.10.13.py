import os
import datetime

class Todo:
    def __init__(self, title, due_date):
        # 할 일 제목
        self.title = title
        # 마감일
        self.due_date = due_date
        # 완료 여부 (기본값: False)
        self.is_done = False

    def mark_done(self):
        self.is_done = True
    def __str__(self):
        status = "✅ 완료" if self.is_done else "🕓 미완료"
        return f"{self.title} (마감일: {self.due_date}, 상태: {status})"

# 할 일 목록을 관리하는 전체 프로그램의 핵심 클래심
class TodoApp:
    def __init__(self, filename="todos.txt"):
        self.filename = filename
        self.todos = []
        self.load_todos()

    def add_todo(self):
        title = input("할 일 제목을 입력하세요: ")
        due_date = input("마감일을 입력하세요 (YYYY-MM-DD): ")
        
        new_todo = Todo(title, due_date)
        self.todos.append(new_todo)
        print("새 할 일이 추가되었습니다.")

    def list_todos(self):
        if not self.todos:
            print("등록된 할 일이 없습니다.")
            return
        print("\n==== 현재 할 일 목록 ====")
        for idx, todo in enumerate(self.todos, start=1):
            print(f"{idx}. {todo}")
        
    def mark_done(self):
        self.list_todos()
        try: 
            num = int(input("완료 처리할 번호를 입력하세요: "))
            self.todos[num - 1].mark_done()
            print("🎉 완료 처리되었습니다!")
        except (ValueError, IndexError):
            print("⚠️ 잘못된 번호입니다.")
        
    def delete_todo(self):
        self.list_todos()
        try:
            num = int(input("삭제할 번호를 입력하세요: "))
            deleted = self.todos.pop(num - 1)
            print(f"'{deleted.title}' 항목이 삭제되었습니다.")
        except (ValueError, IndexError):
            print("⚠️ 잘못된 번호입니다.")

    def save_tools(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            for todo in self.todos:
                line = f"{todo.title}|{todo.due_date}|{int(todo.is_done)}\n"
                f.write(line)
        print("할 일 목록이 저장되었습니다.")

    def load_todos(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                title, due_date, done_str = line.strip().split("|")
                todo = Todo(title, due_date)
                todo.is_done = done_str == "True"
                self.todos.append(todo)

def main():
    app = TodoApp()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. 할 일 추가")
        print("2. 할 일 목록 보기")
        print("3. 완료 처리")
        print("4. 삭제")
        print("5. 저장 및 종료")

        choice = input("메뉴를 선택하세요:  ")

        if choice == "1":
            app.add_todo()
        elif choice == "2":
            app.list_todos()
        elif choice == "3":
            app.mark_done()
        elif choice == "4":
            app.delete_todo()
        elif choice == "5":
            app.save_todos()
            print("👋 프로그램을 종료합니다.")
            break
        else:
            print("⚠️ 잘못된 입력입니다. 다시 선택해주세요.")
if __name__ == "__main__":
    main()