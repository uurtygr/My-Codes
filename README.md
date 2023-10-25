# Credit Card Validation

This program checks the validity of a credit card number entered by the user using the Luhn algorithm. It takes into account the type and length of the credit card number and prints the result on the screen.

## How to Use

1. Run the program.
2. Enter your credit card number in the console.
3. The program checks the input and prints the result on the screen.

## Card Types

- 16-digit card numbers are Visa or MasterCard.
- 15-digit card numbers are American Express. The program considers another card type when the card number doesn't start with "34" or "37."

## Requirements

- Python 3.x

## Installation

1. Clone this repository or download it as a ZIP file.
2. If you don't have Python installed, [download and install Python](https://www.python.org/downloads/).
3. Open the program in a text editor or run it in your preferred Python IDE.

## Credit Card Number Input

- Enter a credit card number that contains only digits.
- A valid card number should be either 16 or 15 digits long.

## Running the Program

Run the program in the command line or in your preferred Python IDE:

```bash
python credit_card_validation.py
