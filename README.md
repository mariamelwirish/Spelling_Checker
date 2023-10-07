# Project Title
This project is a simple application that checks the spelling of the inputted word.

## Description
This is a simple GUI application that checks the spelling of the inputted word. Its mechanism and test cases are as follows:
1. If there is a _**correct word**_, the application just says it is `correct`.
2. If there is an **_incorrect word_**, the application corrects and displays the `corrected word`.
3. A _**random word**_ that doesn’t exist, the program will raise a `“Not found”` message.
4. If there is _**no input**_ (one word) the program asks to input a word.
5. If there is _**more than one word**_, the program raises an `error` not to add more than one word.
6. If there is a _**space after the word**_, it is considered as there is nothing and the word is `correct`.
7. If there is more than one **_space before the word_**, the application raises an `error` not to add spaces before words.

## Dependencies
* You need to have `pyspellchecker`, `textblob`, `re` libraries installed.

## Executing program
Run the program, test the cases, and have fun ^^.
