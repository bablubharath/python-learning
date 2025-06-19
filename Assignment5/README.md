
# Python File and List Handling Tasks

This project contains two independent Python tasks that demonstrate the use of file reading (JSON), dictionary operations, list slicing, and reversing elements with appropriate error handling.

---

## ✅ Task 1: Retrieve Student Marks from JSON File

**Description:**
- Opens a file named `data.json` that contains student names and their corresponding marks in JSON format.
- Asks the user to input a student's name.
- Retrieves and displays the corresponding marks.
- If the student’s name is not found, it gracefully handles the `KeyError` and prints "Name Not Found".

**Example `data.json` content:**
```json
{
  "Alice": 85,
  "Bob": 92,
  "Charlie": 78
}
```

**How it works:**
- Uses `json.load()` to parse the JSON file into a Python dictionary.
- Uses `input()` to get the student name from the user.
- Fetches and prints the student's marks using dictionary lookup.

---

## ✅ Task 2: List Slicing and Reversing

**Description:**
- Creates a list of numbers from 1 to 10.
- Extracts the first five elements from the list.
- Reverses the extracted elements using in-place reversal.
- Prints the original list, extracted list, and reversed list.
- Includes `try-except` block to handle `IndexError`, although slicing will not raise this error.

**Key Concepts Used:**
- List creation with `range()`
- List slicing (`my_list[:5]`)
- In-place reversal using `.reverse()`
- Error handling with `try-except`

---

## 📂 Files Required
- `data.json`: Required for Task 1. Should be in the same directory as the script.

## 🧰 Requirements
- Python 3.x
- No external libraries are required.

---

## 🔄 How to Run
Simply run the Python file containing both tasks. Each task runs independently.
