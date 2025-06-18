try:
    with open('my_file.txt', 'r+') as new:
        for line in new:
            print(line.strip())
except FileNotFoundError:
    print(f"Error: The file was not found")