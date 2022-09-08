
def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Não há o que desfazer!')
        return

    undo_aux = todo_list.pop()
    redo_list.append(undo_aux)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Não há o que desfazer!')
        return

    redo_aux = redo_list.pop()
    todo_list.append(redo_aux)


def do_add(todo, todo_list):
    todo_list.append(todo)


def show(todo_list):
    print(todo_list)


if __name__ == '__main__':
    todo_list = []
    redo_list = []


while True:
    todo = input('Digite uma tarefa ou undo, redo, ls: ')

    if todo == 'ls':
        show(todo_list)
        continue

    elif todo == 'undo':
        do_undo(todo_list, redo_list)
        continue

    elif todo == 'redo':
        do_redo(todo_list, redo_list)
        continue

    do_add(todo, todo_list)