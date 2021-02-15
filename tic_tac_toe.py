# Рандомная генерация поля крестиков-ноликов 3х3 и проверка победителя
import random

row_top =    ['', '', '']
row_middle = ['', '', '']
row_bottom = ['', '', '']

grid = [row_top, row_middle, row_bottom]

def generateGrid(): # Генерация и вывод сетки

    for top in range(3): # Генерация верхней строки
        x_or_o = random.randint(0,1) # Генерация крестика или нолика
        value = ''
        if x_or_o == 0:
            value = 'O'
        elif x_or_o == 1:
            value = 'X'

        row_top[top] = value;
        
    for middle in range(3): # Генерация средней строки
        x_or_o = random.randint(0,1) # Генерация крестика или нолика
        value = ''
        if x_or_o == 0:
            value = 'O'
        elif x_or_o == 1:
            value = 'X'

        row_middle[middle] = value;

    for bottom in range(3): # Генерация нижней строки
        x_or_o = random.randint(0,1) # Генерация крестика или нолика
        value = ''
        if x_or_o == 0:
            value = 'O'
        elif x_or_o == 1:
            value = 'X'

        row_bottom[bottom] = value;
    
    print(grid[0]) # Вывод топ
    print(grid[1]) # Вывод миддл
    print(grid[2]) # Вывод боттом


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