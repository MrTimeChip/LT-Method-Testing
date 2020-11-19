def note_case(case_name, anom_count):
    if anom_count != 0:
        make_note(f'Для {case_name} найдено {anom_count} аномалий.')
    else:
        make_note(f'Для {case_name} не найдено аномалий.')


def note_method_name(method_name):
    make_note(f'---{method_name}{"-" * 10}')


def make_note(text):
    with open('notes.txt', 'a') as f:
        f.write(f'{text}\n')
