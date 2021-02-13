# Визуализация броска кубика
import random

x = random.randint(1, 6)

dices = {
    1: ' _____ \n│     │\n│  •  │\n│     │\n ‾‾‾‾‾ ',
    2: ' _____\n│   • │\n│     │\n│ •   │\n ‾‾‾‾‾',
    3: ' _____\n│   • │\n│  •  │\n│ •   │\n ‾‾‾‾‾',
    4: ' _____\n│ • • │\n│     │\n│ • • │\n ‾‾‾‾‾',
    5: ' _____\n│ • • │\n│  •  │\n│ • • │\n ‾‾‾‾‾',
    6: ' _____\n│ ••• │\n│     │\n│ ••• │\n ‾‾‾‾‾'
}

print(dices[x])