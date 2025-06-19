import json
try:
    with open('data.json', 'r') as data:
        my_dict = json.load(data)
        student_name = input('Enter The Name Of Student: ')
        print(f'{student_name}\'s Marks: {my_dict[student_name]}')
except KeyError:
    print(f"Name NOt Found")