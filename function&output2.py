def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "you didn't provide valid inputs."

    formated_f_name = f_name.title()
    foramted_l_name = l_name.title()
    return f"{formated_f_name}  {foramted_l_name}"


print(format_name(input("What is your first name? "), input("What is your last name? ")))


    
