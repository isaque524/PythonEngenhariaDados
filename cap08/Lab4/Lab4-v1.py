# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

import random
from os import system, name

def limparTela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letrasErradas = []
        self.letrasCertas = []

    def guess(self, letra):
        if letra in self.palavra and letra not in self.letrasCertas:
            self.letrasCertas.append(letra)
        elif letra not in self.palavra and letra not in self.letrasErradas:
            self.letrasErradas.append(letra)
        else:
            return False
        return True
    
    def hangman_over(self):
        return self.hangman_won() or (len(self.letrasErradas) == 6)
    
    def hangman_won(self):
        if '_' not in self.hide_palavra():
            return True
        return False

    def hide_palavra(self):
        rtn = ''
        for letra in self.palavra:
            if letra not in self.letrasCertas:
                rtn += '_'
            else:
                rtn += letra
        return rtn

    def print_game_status(self):
        print(board[len(self.letrasErradas)])
        print('\nPalavra: ' + self.hide_palavra())
        print('\nLetras erradas: ', end='')
        for letra in self.letrasErradas:
            print(letra, end=' ')
        print()
        print('\nLetras corretas: ', end='')
        for letra in self.letrasCertas:
            print(letra, end=' ')
        print()

def rand_palavra():
    palavras = ['computador', 'python', 'programacao', 'jogos', 'teclado', 'mouse', 'monitor', 'notebook', 'celular', 'internet', 'tecnologia']
    palavra = random.choice(palavras)
    return palavra

def main():
    limparTela()
    game = Hangman(rand_palavra())
    while not game.hangman_over():
        game.print_game_status()
        letra = input('\nDigite uma letra: ')
        game.guess(letra)

    game.print_game_status()

    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.palavra)

if __name__ == "__main__":
    main()
