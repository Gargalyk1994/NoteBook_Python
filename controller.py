import view
import modul
import text

def start():
    my_nb = modul.NotesBook()
    while True:
        choice = view.main_menu()# импортируем функцию из view то есть главное меню
        match choice:
            case 1:
                my_nb.open()# pass - заглушка
                view.print_message(text.load_succes)
            case 2:
                my_nb.save()
                view.print_message(text.save_succes)
            case 3:
                nb = my_nb.load()
                view.print_nb(nb, text.load_error)
            case 4:
                note = view.input_note(text.cancel_notes)
                index_note = my_nb.add(note)
                view.print_message(text.new_note_succes(index_note))
            case 5:
                index = view.input_find(text.input_change)
                result = my_nb.find(index)
                view.print_nb(result, text.f_note(index))
            case 6:
                key_word = view.input_find(text.change_note)
                result = my_nb.find(key_word)
                if result:
                    if len(result) != 1:
                        view.print_pb(result, '')
                        current_id = view.input_find(text.input_index)
                    else:
                        current_id = result[0].get('id')
                    new_note = view.input_note(text.change_note, text.cancel_notes)
                    name = my_nb.change(new_note, current_id)
                    view.print_message(text.change_succes(name))
                else:
                    view.print_message(text.not_find)
            case 7:
                nb = my_nb.load()
                index = view.input_index(text.index_del_note, nb, text.load_error)
                name = my_nb.delete(index)
                view.print_message(text.del_note(index))
            case 8:
                break
