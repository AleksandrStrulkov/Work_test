import json
import random


def user_name():
    return f"Привет, выбери варианты теста:\n" \
            f"1. Промышленная безопасность.\n" \
            f"2. Охрана труда.\n" \
            f"3. Взрывные работы.\n" \
            f"4. Горное дело."


def load_test():
    """Функция загружает весь файл теста"""
    with open('test_file.json') as file:
        test_json = json.load(file)
        return test_json


def get_test_by_pk(pk):
    """Функция получает словарь с вопросами по pk"""
    questions_pk = load_test()
    for test in questions_pk:
        if pk == test["pk"]:
            return test


def work_test():
    user_input = input(f"Начинаем тест, нажми 'Enter' ")

    print(user_name())

    user_pk = int(input("Напиши номер: "))
    user_pk_input = get_test_by_pk(user_pk)

    if user_pk_input:
        user_subject = user_pk_input['title']
        # user_questions = user_pk_input['skills']
        print(f"Выбрано: {user_subject}, ответьте на вопросы данной темы.\nНажми 'Enter' чтобы перейти на следующий "
            f"вопрос. Нажми любую кнопку\nчтобы выйти из теста.")
        user_questions = user_pk_input['questions']
        random.shuffle(user_questions)
        for item in range(len(user_questions)):
            user = input("")
            if user == "":
                print(user_questions[item])
            else:
                break


if __name__ == "__main__":
    work_test()
