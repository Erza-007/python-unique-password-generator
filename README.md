# python-unique-password-generator

# Password Generator

A simple and secure password generator built using Python.

This project focuses on the problems faced by the users to generate strong passwords with a custom length.  
It ensures that each password contains uppercase letters, lowercase letters, digits, and special characters.

---

##  Features

- User-defined password length
- Minimum length validation (at least 4 characters)
- Includes:
  -  Uppercase letters
  -  Lowercase letters
  -  Numbers
  -  Special characters
- Randomized and shuffled output
- Input validation for numeric values

---

##  Technologies Used

- Python 3
- `random` module
- `string` module

---

## How It Works

1. The program asks the user to enter the desired password length.
2. It validates the input:
   - Ensures the value is numeric
   - Ensures the length is at least 4
3. It generates a password containing at least:
   - One uppercase letter
   - One lowercase letter
   - One digit
   - One special character
4. The remaining characters are filled randomly.
5. The password is shuffled for security.
6. Final secure password is displayed.

---

## How To Run

1. Download or clone this repository.
2. Open the project folder in your terminal.
3. Run:


python password.py
