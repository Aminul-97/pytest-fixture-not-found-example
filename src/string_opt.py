def join_string(str1: str, str2: str):
    full_str = str1+str2
    return full_str

def split_string(main_str: str, dev_str: str):
    strings = main_str.split(dev_str)
    return strings

def replace_string(main_str: str, find_str: str, replace_str: str):
    updated_str = main_str.replace(find_str, replace_str)
    return updated_str

def change_case(main_str: str):
    up_str = main_str.upper()
    lw_str = main_str.lower()
    return up_str, lw_str

#print(join_string("A", "B"))
#print(split_string("A-B", "-"))
#print(replace_string("ABC", "B", "-"))
#print(change_case("Abc123"))