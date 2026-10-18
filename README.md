# 🔐 Password Generator | Python

## 📌 About the Project
This project is a simple **Password Generator** developed using Python as part of the CODSOFT Python Programming Internship.

It generates random passwords based on the user's preferences, allowing them to choose the password length and decide whether to include numbers and special symbols.

## ✨ Features
- **Custom Password Length:** Choose the desired length of the password.
- **Number Inclusion:** Option to include digits (0–9).
- **Symbol Inclusion:** Option to include special characters such as `@`, `#`, `$`, and `%`.
- **Custom Symbol Count:** Specify the exact number of symbols in the password.
- **Random Password Generation:** Characters are shuffled to create a randomized password.

## 🛠️ Technologies Used
- Python 3
- `random` module
- `string` module

## ⚙️ How to Run the Project

### 1. Clone the Repository
```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Directory
```bash
cd CODSOFT_1
```

### 3. Run the Python Program
```bash
python passwordgenerator.py
```

## 💻 Example Output
```text
Enter the desired password length: 12
Wanna include numbers? (yes/no): yes
Wanna include symbols? (yes/no): yes
How many symbols do you want to include? 3
Generated Password: a7@K#2m$P9xQ
```

*Note: The generated password will vary each time the program runs.*

## 📚 What I Learned
- Working with Python's built-in modules.
- Taking user input and handling conditional statements.
- Generating random characters using `random.choices()`.
- Manipulating strings and lists.
- Shuffling list elements using `random.shuffle()`.

## ⚠️ Limitations
- The program does not currently validate all user inputs.
- The number of symbols cannot exceed the requested password length.
- The program uses Python's `random` module, which is suitable for learning but not recommended for generating passwords for real-world security.

## 👨‍💻 Author
**Aditya**
