'''Напишите программу, удаляющую из текста все слова, содержащие ""абв"".'''

text = "sdfsdf sdf sdf sdfsfd sdfs абв абв ываыва абв ывавыаыв"

result_text = ''.join(filter(lambda x: 'абв' not in x, text.split()))
print(result_text)