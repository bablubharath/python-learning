try:
    my_list = list(range(1,11))
    Extracted_list = my_list[:5]
    print(f"Original List: {my_list}\nExtracted First Five Numbers: {Extracted_list}")
    reversed_list = Extracted_list
    reversed_list.reverse()
    print(f"Reversed Extracted List: {reversed_list}") 
except IndexError:
    print(f"Index Out Of Range")