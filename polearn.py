from lesson import Lesson


def start_lesson(lesson_name):
    lesson = Lesson(lesson_name)

    lesson.start()


def choose_lesson_menu():
    while True:
        print('1. Liczba mnoga',
              '2. Stopniowanie przymiotników',
              '3. Wyjść',
              sep='\n',
              end='\n\n')

        print('[Wpisać cyfrę]')

        user_input = None

        try:
            user_input = int(input('> '))
        except ValueError:
            print('\nPowinniście wpisać cyfre!\n')

            continue

        if user_input == 1:
            start_lesson('liczba_mnoga')
        elif user_input == 2:
            start_lesson('stopniowanie')
        elif user_input == 3:
            print('Do widzenia!')

            return
        else:
            print('Mylna cyfra!\n')

            continue


if __name__ == '__main__':
    print('Zaczynaliśmy lekcję języka polskego!\n')

    choose_lesson_menu()
