import random


class Mistake:

    def __init__(self, question, answer, user_answer):
        self.question = question

        self.answer = answer

        self.user_answer = user_answer

    def __str__(self):
        return 'Pytanie: {} Odpowiedź: {} Wasz odpowiedź: {}'\
            .format(self.question, self.answer, self.user_answer)


class Lesson:

    def __init__(self, lesson_name: str):
        self.lesson_name = lesson_name

        self.lesson_materials = self.__get_lesson_materials()

        self.mistakes = []

    def __get_lesson_materials(self) -> dict:
        materials = dict()

        materials_file_name = 'lessons/{}.txt'.format(self.lesson_name)

        with open(materials_file_name, 'r') as materials_file:
            for line in materials_file:
                (left_value, right_value) = line.split('-')

                left_value = left_value.strip()

                right_value = right_value.strip()

                materials[left_value] = right_value

        return materials

    def start(self):
        lesson_materials_keys = list(self.lesson_materials.keys())

        word_number = 1

        while True:
            question_value = random.choice(lesson_materials_keys)

            answer_value = self.lesson_materials[question_value]

            user_answer = input('{}. {} = '
                                .format(word_number, question_value)).strip()

            if user_answer == 'exit':
                break

            if user_answer == answer_value:
                print('\tPoprawnie!')
            else:
                print('\tPomyłka! Prawidłowy odpowiedź: {}'
                      .format(answer_value))

                mistake = Mistake(question_value, answer_value, user_answer)

                self.mistakes.append(mistake)

            word_number += 1

        self.mistakes_output()

    def mistakes_output(self):
        if len(self.mistakes) == 0:
            print('Wy nie zrobiliście ani jednej pomyłki!\n')

            return

        print('\nPomyłki:')
        for i, mistake in enumerate(self.mistakes):
            print('\t{}. {}'.format(i, mistake))
        else:
            print('\n')
