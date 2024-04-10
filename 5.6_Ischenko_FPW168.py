board = list(range(1, 10))


def game_field():
    '''выводим игровое поле'''
    for i in range(3):
        print('|', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('_' * 13)

def gamer_move(index, char):
    '''выполняем ход'''
    if (index < 1 or index > 9 or board[index - 1] in ('X', 'O')):
        return False
    board[index - 1] = char
    return True

def check_win():
    '''проверка победы'''
    win = False
    win_comb = (
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    )
    for n in win_comb:
        if (board[n[0]] == board[n[1]] and board[n[1]] == board[n[2]]):
            win = board[n[0]]
    return win

def main_func():
    '''основная, вывывает ф-ции по очереди'''
    #текущий игрок
    player = 'X'
    #номер шага
    step = 1
    game_field()

    while (step <= 9) and (check_win() == False):
        index = input(f'Ходит игрок {player}. Укажите номер поля (0 - выход): ')
        if (int(index) == 0):
            break

        # если получилось сделать ход
        if (gamer_move(int(index), player)):
            print('Ход выполнен!')

            if (player == 'X'):
                player = '0'
            else:
                player = 'X'

            game_field()
            step += 1
        else:
            print("Неверный номер! Повторите!")

    if step == 10:
        print('Игра окончена. Ничья!')
    else:
        print(f'Выйграл {check_win()}')

print('Добро пожаловать в игру "Крестики-нолики!" :)')
main_func()