file = open('text.txt', 'r')

char_count = 0
word_count = 0
line_count = 1
prev_char = None

while True:
    # read by character
    char = file.read(1)
    if not char:
        break
    elif char.isalpha():
        char_count += 1
    elif char == ' ':
        word_count += 1
    elif char == '\n' and prev_char == None:
        line_count += 1
    elif char == '\n':
        if prev_char == '\n':
            line_count += 1
        else:
            line_count += 1
            word_count += 1
    prev_char = char

print(f'Char count: {char_count}')
print(f'Word count: {word_count}')
print(f'Line count: {line_count}')

file.close()