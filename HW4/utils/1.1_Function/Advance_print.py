"""
Advanced printing with 3 non-obligatory arguments:
Printing starts with "start". Default - empty;
max_line - maximum length when printing. If more than maximum, start with a new line;
in_file - print in file or not.
"""


def adv_print(*args, start='', max_line=0, in_file=False):
    result = str(start)
    text = ''
    for item in args:
        result += str(item)

    if max_line > 0 and len(result) > max_line:
        for item in range(0, len(result), max_line):
            text += result[item:item + max_line] + '\n'
        result = text

    if in_file:
        print(result)
        with open('result.txt', 'w', encoding='utf8') as file:
            print(result, file=file)
    else:
        print(result)


text_data = str('Здесь мы пишем что угодно, чтобы проверить длину строки. '
                'Если она больше 79 символов (PEP8 says: Limit all'
                ' lines to a maximum of 79 characters. The limits are'
                ' chosen to avoid wrapping in editors with the window'
                ' width set to 80, то она должна перенестись на следующую строчку')

adv_print(text_data, start="start ", max_line=79, in_file=True)
