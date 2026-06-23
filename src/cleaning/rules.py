"""
Reusable cleaning functions.
"""

def replace_negative_one(value):
    """
    Convert sentinel -1 values to None.
    """

    if value == -1:
        return None
    
    return value

def clean_string(value):
    """
    Trime whitespcae.
    """

    if value is None:
        return None
    
    value = str(value)

    value = value.strip()

    if value == "":
        return None
    
    return value