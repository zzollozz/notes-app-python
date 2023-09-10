import json
import os
import datetime

from conf import print_menu


def save_file_notes(data_notes):
    """
    Запись заметок в файл
    :param data_notes:
    :return:
    """
    with open('db_notes.json', 'w') as file:
        json.dump(data_notes, file, indent=4, ensure_ascii=False)
        return f'Заметки сохранены'

def load_file_notes():
    """
    Загрузка имеющихся заметок
    :return:
    """
    if os.path.isfile('db_notes.json'):
        with open('db_notes.json') as file:
            return json.load(file)
    else:
        return {}

def list_notes(bdnotes):
    """
    Просмотр всех заметок
    :param bdnotes:
    :return:
    """
    if not bdnotes:
        return f'Заметок нет'
    else:
        return list(map(lambda note: f'{note[0]}: {note[1].get("title")}', bdnotes.items()))

def create_note(bdnotes, title, body):
    print()
    temp_note = {'title': title,
                 'body': body,
                 'data/time': datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")}

    bdnotes[len(bdnotes) + 1] = temp_note
    save_file_notes(bdnotes)
    return f'Заметка создана'

def read_note(bdnotes, id_note):

    return f"Название: {bdnotes[id_note]['title']}\nТекст: {bdnotes[id_note]['body']}\nДата/Время создания (изменения): {bdnotes[id_note]['date/time']}"

def update_note(bdnotes, id_note):
    flag = True
    while flag:
        print_menu('РЕЖИМ РЕДАКТИРОВАНИЯ', '1: "Редактирование Названия" 2: "Редактирование текста"')
        numbers = input('>>> ')
        match int(numbers):
            case 0:
                flag = False
            case 1:
                bdnotes[id_note]['title'] = input('Новое название\n >>> ')
                bdnotes[id_note]['date/time'] = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
            case 2:
                bdnotes[id_note]['body'] = input('Ведите текст\n >>> ')
                bdnotes[id_note]['date/time'] = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    return f'Выход из режима редактирования заметки'

def delete_note(bdnotes, id_note):
    del bdnotes[id_note]
    return f'Заметка удалена'
