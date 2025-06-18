# File Handling Tasks in Python

This project contains two simple file handling tasks using Python. Each task demonstrates basic operations such as reading, writing, and appending to text files while handling possible errors gracefully.

---

## ✅ Task 1: Reading from a File

- **File Name:** `my_file.txt`
- **Operation:** 
  - Attempts to open the file in read (`r+`) mode.
  - Reads and prints each line from the file, removing any trailing newline characters.
- **Error Handling:**
  - If the file does not exist, it catches a `FileNotFoundError` and displays a friendly error message.

---

## ✅ Task 2: Writing, Appending, and Reading from a File

- **File Name:** `read_write.txt`
- **Operations:**
  1. **Writing:**
     - Takes input from the user and writes it as the first line to the file (overwriting any existing content).
  2. **Appending:**
     - Prompts the user again and appends the second input to the file.
  3. **Reading:**
     - Reads and prints all lines from the updated file.
- **Error Handling:**
  - If for any reason the file can't be accessed or written to, it catches a `FileNotFoundError` and displays an appropriate message.

---

## 💡 Usage

To run either task, simply execute the Python script containing the corresponding code block. The program will guide you through any required inputs.

---

## 🔧 Requirements

- Python 3.x
- No additional libraries are required.

---

## 📂 Files Used

- `my_file.txt` – Used for reading in Task 1.
- `read_write.txt` – Used for writing, appending, and reading in Task 2.

---

## 🛡️ Notes

- Make sure the file `my_file.txt` exists in the same directory when running Task 1, or you will get a file-not-found error.
- Task 2 will create or overwrite `read_write.txt` as needed.

---
