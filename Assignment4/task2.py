try:
    with open('read_write.txt', 'w') as first:
        initial_text = input('Enter The Initial Text To FIle: ')
        write_file = first.write(initial_text + '\n')
    with open('read_write.txt', 'a') as second:
        append_text = input('Enter The Second Line Text: ')
        append_file = second.write(append_text + '\n')
    with open('read_write.txt', 'r') as new:
        for line in new:
            print(line.strip())
except FileNotFoundError:
    print(f"The Required FIle Is NOt Present")