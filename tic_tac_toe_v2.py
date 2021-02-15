# Рандомная генерация поля крестиков-ноликов 3х3 и проверка победителя
# Вывод сетки через string
import random

row_top =    ['', '', '']
row_middle = ['', '', '']
row_bottom = ['', '', '']

grid = [row_top, row_middle, row_bottom]

top_string =    ' 0  1  2'
middle_string = ' 0  1  2'
bottom_string = ' 0  1  2'

def generateGrid(): # Генерация и вывод сетки

    for top in range(3): # Генерация верхней строки
        x_or_o = random.randint(0,1) # Генерация крестика или нолика
        value = ''
        if x_or_o == 0:
            value = 'O'
        elif x_or_o == 1:
            value = 'X'

        row_top[top] = value
    top_string = row_top[0] + ' ' + row_top[1] + ' ' + row_top[2]

    for middle in range(3): # Генерация средней строки
        x_or_o = random.randint(0,1) # Генерация крестика или нолика
        value = ''
        if x_or_o == 0:
            value = 'O'
        elif x_or_o == 1:
            value = 'X'

        row_middle[middle] = value
    middle_string = row_middle[0] + ' ' + row_middle[1] + ' ' + row_middle[2]
        

    for bottom in range(3): # Генерация нижней строки
        x_or_o = random.randint(0,1) # Генерация крестика или нолика
        value = ''
        if x_or_o == 0:
            value = 'O'
        elif x_or_o == 1:
            value = 'X'

        row_bottom[bottom] = value
    bottom_string = row_bottom[0] + ' ' + row_bottom[1] + ' ' + row_bottom[2]
    
    print(top_string)
    print(middle_string)
    print(bottom_string)


def whoIsTheWinner(): # Определитель выигрышных ходов
    """       grid[*][0]      grid[*][1]       grid[*][2]
    grid[0]        ·               ·                ·
    grid[1]        ·               ·                ·
    grid[2]        ·               ·                ·
    """
    N_x = 0 # Кол-во выигрышей крестика
    # Крестики по горизонтали
    if grid[0][0] == grid[0][1] == grid[0][2] == 'X':
        N_x+=1
    if grid[1][0] == grid[1][1] == grid[1][2] == 'X':
        N_x+=1
    if grid[2][0] == grid[2][1] == grid[2][2] == 'X':
        N_x+=1
    
    # Крестики по вертикали
    if grid[0][0] == grid[1][0] == grid[2][0] == 'X':
        N_x+=1
    if grid[0][1] == grid[1][1] == grid[2][1] == 'X':
        N_x+=1
    if grid[0][2] == grid[1][2] == grid[2][2] == 'X':
        N_x+=1
    
    # Крестики по диагонали
    if grid[0][0] == grid[1][1] == grid[2][2] == 'X':
        N_x+=1
    if grid[0][2] == grid[1][1] == grid[2][0] == 'X':
        N_x+=1

    N_o = 0 # Кол-во выигрышей нолика
    # Нолики по горизонтали
    if grid[0][0] == grid[0][1] == grid[0][2] == 'O':
        N_o+=1
    if grid[1][0] == grid[1][1] == grid[1][2] == 'O':
        N_o+=1
    if grid[2][0] == grid[2][1] == grid[2][2] == 'O':
        N_o+=1
    
    # Нолики по вертикали
    if grid[0][0] == grid[1][0] == grid[2][0] == 'O':
        N_o+=1
    if grid[0][1] == grid[1][1] == grid[2][1] == 'O':
        N_o+=1
    if grid[0][2] == grid[1][2] == grid[2][2] == 'O':
        N_o+=1
    
    # Нолики по диагонали
    if grid[0][0] == grid[1][1] == grid[2][2] == 'O':
        N_o+=1
    if grid[0][2] == grid[1][1] == grid[2][0] == 'O':
        N_o+=1
    
    
    if N_x != 0:
        print('Крестик: ', N_x)
    if N_o != 0:
        print('Нолик: ', N_o)
    if N_x == N_o == 0:
        print('Ничья')

generateGrid()
whoIsTheWinner()