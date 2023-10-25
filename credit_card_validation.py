"""

This program checks the credit card's validation

"""


def luhn_checksum(card_number):
    """
    It checks the authenticity of the credit card number according to the Luhn algorithm.

    Parameters:
    - card_number (str): Credit card number.
    Returns:
    - bool: True if the card is correct, False otherwise.
    """
    
    digits = [int(d) for d in card_number]  # Card number is converted to the list.
    digits.reverse()

    total = 0
    for i, digit in enumerate(digits):  
        if i % 2 == 1:           # Multiplying odd numbers by 2
            digit *= 2
            if digit > 9:        # If results of multiplying are higher than 9, it should be subtracted 9.
                digit -= 9
        total += digit

    return total % 10 == 0       # Checks if sum is equal to multiples of 10.      


        
def validate_card(card_number):
    
    """
    Checks the validity of the credit card number according to its length and prints the result on the screen.
    Parameters:
    - card_number (str): Credit card number
    """


   
    if len(card_number) == 16:
            card_type = "Visa/MasterCard"
    elif len(card_number) == 15:
            card_type = "American Express"
            card_number = "0" + card_number  #Since American Express cards have 15 digits, we add 0 to the beginning.
    else:
        return
    
        
        
    if luhn_checksum(card_number):
        print(f"The credit card you entered is a valid {card_type} card.")
    else:
        print("The credit card you entered is not valid.")

# 
while True:
    card_number = input("Enter your credit card number: ")

    # Check the validity of the entered value
    if card_number.isdigit() and (len(card_number) == 16 or (len(card_number) == 15)):
        break
    elif not card_number.isdigit():
        print("Please only use digits")
    else:
        print("Invalid entry. Please enter a correct credit card number.")
        
        
# Verify the card number and print the result on the screen
validate_card(card_number)
