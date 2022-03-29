def hangman(word):
    wrong = 0 #отслеживает кол-во неправ. букв
    stages = ["",
              "_______        ",
              "|              ",
              "|      |       ",
              "|      0       ",
              "|     /|\      ",
              "|     / \      ",
              "|              ",
              "|              ",
              ]
    rletters = list(word) #список  букв загад. слова
    board = ["__"] * len(word)
    win = False
    print('Добро пожаловать на казнь')

    while wrong < len(stages) - 1:
        print('\n')
        char = input('Enter a char: ')
        if char in rletters:
            cind = rletters.index(char) #индекс правильной буквы слова
            board[cind] = char
            if rletters.count(char) > 1:
                for char in rletters:
                    symbol = rletters.index(char,rletters.index(char),len(char))
            rletters[cind] = '$'
        else:
            wrong += 1
        print((' '.join(board)))#строка с результатом угадывания
        e = wrong + 1
        print('\n'.join(stages[0:e])) 
        if '__' not in board: #условие победы
            print('You win! Word was: ')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('You loose! The word was: {}.'.format(word))
            
hangman('representative')
