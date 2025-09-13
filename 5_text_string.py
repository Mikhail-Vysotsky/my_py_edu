import string

# 1) Написать с заглавной буквы слово, которое начинается с буквы m:
song = """When an ell grabs your arm,
And it causes great harm,
That's - a moray!"""

wind_word = ' m'
m_word = song.find(wind_word)+1
_1_result = song[m_word:].strip(string.punctuation).title()

print(_1_result)


# 2) Вывести на экран все вопросы из списка и правильные ответы в виде
# Q: вопрос
# A: ответ

questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
    "An exploding sheep.",
    "No, i'm a frayed knot.",
    "'Pop!' goes the weasel."
]

print('Q: ', questions[0],'\n'
      'A: ', answers[1])
print('Q: ', questions[1],'\n'
      'A: ', answers[2])
print('Q: ', questions[2],'\n'
      'A: ', answers[0])


# 3) Вывести на экран стихотворение, используя стиль форматирования. 
# Подставить в него строки: 'roast beef', 'ham', 'head', 'clam'
poetry = """
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s
"""
poetry_words = ('roast beef', 'ham', 'head', 'clam')
print(poetry % poetry_words)

# 4) Написать письмо с использованием нового стиля форматирования. Сохранить предложенную
# строку в переменную letter (понадобится в следующем упражнении)

template = """
Dear {salutation} {name},

Thank you for your letter. Wa are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be uset in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send your another {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.
Sincerely,
{spokesman}
{job_title}
"""
temp_dict = {
    'salutation': 'mr.',
    'name': 'Bond',
    'product': 'pSeven',
    'verbed': 'seen',
    'room': 'cabinet #7',
    'animals': 'cat',
    'amount': '14',
    'percent': '95',
    'spokesman': 'Mikhail Vysotskiy',
    'job_title': 'Engineer'
             }
letter = template.format(**temp_dict)
print(letter)
