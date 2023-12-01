import text

def main_menu() -> int: # главное меню
    print(text.main_menu)
    while True:
        choice = input(text.choice_input)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)

def print_message(message: str): # ф-ия печатает текст выделением === сверху и снизу
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message)+'\n')

def print_nb(nb: list[dict[str, str]], error: str):
    if nb:
        print('\n' + '=' * 75)
        for i, note in enumerate(nb, 1):
            print(f'{note.get("id"):>3}. {note.get("text_note"):<30}')
        print('=' * 75 +'\n')
    else:
        print_message(error)

def input_note(cancel: str) -> dict: # принимает строки две и возвращает словарь
    note = {}
    for key, value in text.input_note.items():
        data = input(value)
        if data:
            note[key] = data
        else:
            print_message(cancel)
    return note

def input_index(message: str, nb: list, error: str) -> int:# удаление по индексу(номеру) контакта
    print_nb(nb, error)
    while True:
        index = input(message)
        if index.isdigit() and 0 < int(index) < len(nb) + 1:
            return int(index)
        
# def input_find(pb: dict, message: str, try_again: str):
#     for key, value in pb:
#         if pb.keys == input(message):
#             print(message)
#         else:
#             print_message(try_again)

def input_find(message) -> str:
    return input(message)
           