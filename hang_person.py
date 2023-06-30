word_to_guess = "cumbias"
guess_word = ""
user_option = ""
user_chars = []
display_word = "_ " * len(word_to_guess)

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
print("Bienvenido al ahorcadito")

print(hang_person[-0])
while user_option != "3":
    print("Adivina esta palabra si quieres vivir\n")
    print(display_word)
    print("1. Adivinar palabra")
    print("2. Resultados")
    print("3. Salir")

    user_option = input("Indíca una opción\n")

    if user_option == "1":
        exit_game = False
        while not exit_game:
            print("Intenta adivinando una letra o la palabra completa\n")
            print("Escribe 'salir' para volver al menú princípal")
            user_guess = input()
            guess_word = ""

            # Si el usuario ingresó una letra
            if len(user_guess) == 1:
                # Si es una letra nueva, se agrega al listado de letras intentadas
                if not user_guess in user_chars:
                    user_chars.append(user_guess)

                if(user_guess in word_to_guess):
                    print("Adivinaste una letra")
                    for char in word_to_guess:
                        if char in user_chars:
                            guess_word += char
                        else:
                            guess_word += "_ "
                    print(guess_word)
                else:
                    print("Esa letra no está en la palabra")
                    print(hang_person[len(user_chars)])
        # Si el usuario quiere volver al menú princípal
            elif (user_guess == "Salir"):
                exit_game = True
        # El usuario intentó una palabra
            else:
                # Si la palabra del usuario es la misma
                if(user_guess == word_to_guess):
                    print("¡Ganaste!")
                    exit(1)
                else:
                    print("No no no")
                    print("¡Perdiste y te quemarás!")
                    print(hang_person[-1])
                    exit(1)
    elif user_option == "2":
        print(f"Has intentado las siguientes letras: {user_chars}")
    elif user_option == "3":
        print("Chaucito")