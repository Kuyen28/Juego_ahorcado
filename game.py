secret_word = "hola"
display_word = "_ " * len(secret_word)
user_chars = []
user_option = ""
hang_person = ['''
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
print("Bienvenido al ahorcado")
print(display_word)
print(hang_person[0])

while user_option != "3":
    print(f"Adivina esta palabra si quieres vivir\n"
          f"1. Adivinar la letra o la palabra\n"
          f"2. Resultados\n"
          f"3. Salir")
    user_option = input("Indica una opción \n")

    if(user_option == "1"):
        exit_option = False

        while not exit_option:
            print("Intenta adivinando una letra o la palabra completa")
            print("Escribe 'volver' para regresar al menú príncipal")
            user_guess = input()
            if len(user_guess) == 1:
                if(not user_guess in user_chars):
                    user_chars.append(user_guess)
                if(user_guess in secret_word):
                    print("Adivinaste una letra")
                    guess_word = ""
                    for char in secret_word:
                        if(char in user_chars):
                            guess_word += char
                        else:
                            guess_word += "_ "
                    print(guess_word)
                else:
                    print("Esa letra no está en la palabra")
                    if((user_chars) == len(hang_person)) -1:
                        print("Perdiste")
                        print(hang_person[-1])
                        exit()
                    print(hang_person[len(user_chars)])
            elif(user_guess == "volver"):
                exit_option = True
            else:
                if(user_guess == secret_word):
                    print("Ganaste")
                    exit()
                else:
                    print("Perdiste")
                    print(hang_person[-1])
    elif(user_option == "2"):
        pass
    elif(user_option == "3"):
        pass
