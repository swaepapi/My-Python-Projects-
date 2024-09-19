# utils

def is_valid_amount(amount_str):
    """Checks if the input string is a valid float for amount."""
    try:
        float(amount_str)
        return True
    except ValueError:
        return False
