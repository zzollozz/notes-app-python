from conf import print_menu
from views import list_notes, load_file_notes, create_note, save_file_notes, read_note, update_note, delete_note


def main():
    bdnotes = load_file_notes()
    flag = True
    try:
        while flag:
            print_menu('ГЛАВНОЕ МЕНЮ ', '1: "Показать все заметки", 2: "Выбор заметки", 3: "Создать заметку"')
            res = input(">>> ")
            try:
                match int(res):
                    case 0:
                        # выход
                        print(f'"Выход" {save_file_notes(bdnotes)}')
                        break
                    case 1:
                        # показать все заметки
                        for i in list_notes(bdnotes):
                            print(i)
                    case 2:
                        # выбрать нужную заметку
                        id_note = input('Укажите номер заметки: ')
                        print(read_note(bdnotes, id_note))
                        print_menu('РЕЖИМ ЗАМЕТКИ', '1: "Редактировать", 2: "Удалить"')
                        r = int(input((f'>>> ')))
                        if r == 1:
                            print(update_note(bdnotes, id_note))
                        elif r == 2:
                            print(delete_note(bdnotes, id_note))
                        elif r == 0:
                            continue
                    case 3:
                        # создать заметку
                        print(f'РЕЖИМ СОЗДАНИЯ ЗАМЕТКИ')
                        title = input('Название: \n>>> ')
                        body = input('Текст: \n>>> ')
                        print(create_note(bdnotes, title, body))
            except ValueError:
                print("Невенрный символ ")
                continue
    except KeyboardInterrupt:
        print(f'Прервано пользователем {save_file_notes(bdnotes)}')
    except Exception as e:
        print(f'{save_file_notes(bdnotes)}')
        print(f'Ой что-то пошло не так. Ошибка: {e}')


if __name__ == '__main__':
    main()
