import random

a = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]

name = input('Как Вас зовут?')

print('', 'Привет {}, я магический шар, и я знаю ответ на любой вопрос.'.format(name), "", sep='\n')

while True:
    q = input('Введите интересующий Вас вопрос:')
    if q == 'нет':
        break
    else:
        print(random.choice(a))
        print('', 'Если у вас есть вопросы еще , то задавайте, если нет то скажите "нет":', '', sep='\n')


print('', 'Возвращайтесь, если возникнут вопросы!', sep='\n')