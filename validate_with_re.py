import re

# validation with Regular expression
def validate_price(value: str):

    if not re.search(r'^[0-9,]+$', value):
        raise ValueError(f'Invalid price: {value}')

validate_price('3,000')
validate_price('無料')


# the error message
"""
Traceback (most recent call last):
  File "validate_with_re.py", line 10, in <module>
    validate_price('無料')
  File "validate_with_re.py", line 7, in validate_price
    raise ValueError(f'Invalid price: {value}')
ValueError: Invalid price: 無料
"""