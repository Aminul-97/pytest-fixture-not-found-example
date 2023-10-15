def join_string(str1: str, str2: str) -> str:
    """
    Function to join two strings.
    """
    full_str = str1+str2
    return full_str

def split_string(main_str: str, dev_str: str) -> str:
    """
    Function to split two strings.
    """
    strings = main_str.split(dev_str)
    return strings

def replace_string(main_str: str, find_str: str, replace_str: str) -> str:
    """
    Function to replace specific substring from a string.
    """
    updated_str = main_str.replace(find_str, replace_str)
    return updated_str

def change_case(main_str: str)  -> str:
    """
    Function to convert string to upper and lower.
    """
    up_str = main_str.upper()
    lw_str = main_str.lower()
    return up_str, lw_str


#print(join_string("A", "B"))
#print(split_string("A-B", "-"))
#print(replace_string("ABC", "B", "-"))
#print(change_case("Abc123"))