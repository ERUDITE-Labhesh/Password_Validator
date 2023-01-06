# THIS IS THE SOURCE CODE FOR PASSWORD VALIDATOR
# THE PASSWORD VALIDATORS ARE RESPONSIBLE FOR DETERMINING WHETHER
# A PROPOSED PASSWORD IS ACCEPTABLE FOR USE AND COULD INCLUDE CHECKS

# IMPORTED CSV HEADER FILE
import csv


# THE PATH OF CSV FILE WHERE COOMON PASSWORD IS SAVED
csv_file_path = r"C:\Users\Labhesh\Desktop\Python\Common_password.csv"


# THIS FUNCTION CONTAINS INSTRUCTIONS TO DISPLAY FOR PASSWORD VALIDATOR
def instructions():
    print("WELCOME TO PASSWORD VALIDATOR")
    print("----------------------------\
INSTRUCTIONS-----------------------------\n")
    print("1: PASSWORD LENGTH SHOULD BE OF MINIMUM 12 CHARACTER ")
    print("2: PASSWORD LENGTH SHOULD NOT BE GREATER THAN 20 CHARACTER")
    print("3: PASSWORD MUST CONSIST OF UPPER-CASE CHARACTER [A-Z] ")
    print("4: PASSWORD MUST CONSIST OF LOWER-CASE CHARACTER [a-z]")
    print("5: PASSWORD MUST CONSIST OF NUMBER [0-9] ")
    print("6: PASSWORD MUST CONSIST OF SPECIAL\
CHARACTER - !, @, #, $, %, ^, &, *, (, ), _, -, ~ ")
    print("7: PASSWORD SHOULD START WITH EITHER ANY SPECIAL\
CHARACTER OR WITH 2 DIGIT'S NUMBER")
    print("8: PASSWORD SHOULD CONTAIN ATLEAST\
3 UPPER-CASE CHARACTER AND 3 LOWER-CASE CHARACTER")
    print("9: PASSWORD SHOULD CONTAIN ATLEAST\
3 SPECIAL CHARACTER")
    print("10: PASSWORD SHOULD NOT CONTAIN 5 SAME\
CHARACTER\ OR NUMBER CONSECUTIVELY ")
    print("11: PASSWORD SHOULD NOT HAVE USERNAME\
INTO IT AT ANY POSITION")
    print("12: PASSWORD SHOULD NOT CONTAIN 3 \
SAME SPECIAL CHARACTER'S CONSECUTIVELY")

# CALLING INSTRUCTION FUNCTION
instructions()


# MAIN FUNCTION OF PASSWORD VALIDATOR
def password_validator_main(user_name, user_pass):

    return_checklen = check_length(user_pass)
    if return_checklen is False:
        user_newpass = get_password()
        password_validator_main(user_name, user_newpass)
    else:
        print(" THE LENGTH OF PASSWORD IS STATISFIED !!  ")
        return_checkupper = check_uppercase(user_pass)

        if return_checkupper is False:
            print("PASSWORD INVALID, THE PASSWORD SHOULD CONTAIN\
OF ATLEAST MINIMUM 3 UPPER-CASE CHARACTER [A-Z] ")
            user_newpass = get_password()
            password_validator_main(user_name, user_newpass)
        else:
            print(" THE PASSWORD PASSED UPPER-CASE CONDITION !! ")
            return_checklower = check_lowercase(user_pass)

            if return_checklower is False:
                print("PASSWORD INVALID, THE PASSWORD SHOULD\
CONTAIN OF ATLEAST 3 LOWER-CASE CHARACTER [a-z] ")
                user_newpass = get_password()
                password_validator_main(user_name, user_newpass)
            else:
                print(" THE PASSWORD PASSED LOWER-CASE CONDITION !! ")
                return_checknumber = check_numbers(user_pass)

                if return_checknumber is False:
                    print("PASSWORD INVALID, THE PASSWORD\
SHOULD CONSIST OF NUMBER [0-9]")
                    user_newpass = get_password()
                    password_validator_main(user_name, user_newpass)
                else:
                    print(" THE PASSWORD PASSED NUMBER CONDITION !! ")
                    return_checkspecial = check_specialchar(user_pass)

                    if return_checkspecial is False:
                        print("PASSWORD INVALID, PASSWORD SHOULD CONTAIN\
OF ATLEAST 3 SPECIAL CHARACTER - !, @, #, $, %, ^, &, *, (, ), _, -, ~ ")
                        user_newpass = get_password()
                        password_validator_main(user_name, user_newpass)
                    else:
                        print(" THE PASSWORD PASSED SPECIAL\
CHARACTER CONDITION !! ")
                        return_checkstart = check_start(user_pass)

                        if return_checkstart is False:
                            print("PASSWORD SHOULD START WITH EITHER ANY\
SPECIAL CHARACTER OR WITH 2 DIGIT'S NUMBER")
                            user_newpass = get_password()
                            password_validator_main(user_name, user_newpass)
                        else:
                            print(" THE PASSWORD PASSED THE START CONDITION")
                            return_checkuser = check_username(user_name, user_pass)

                            if return_checkuser is False:
                                print("PASSWORD INVALID, PASSWORD SHOULD NOT \
HAVE USERNAME INTO IT AT ANY POSITION")
                                user_newpass = get_password()
                                password_validator_main(user_name, user_newpass)
                            else:
                                print(" THE PASSWORD PASSED AS IT DOES'NT\
 INCLUDE USERNAME IN IT ")
                                return_checkconsi = check_consi(user_pass)

                                if return_checkconsi is False:
                                    print("PASSWORD INVALID, PASSWORD CONTAINS\
MORE THAN 5 SAME CHARACTER OR NUMBER CONSECUTIVELY ")
                                    user_newpass = get_password()
                                    password_validator_main(user_name, user_newpass)
                                else:
                                    print(" THE PASSWORD PASSED AS IT DOES'NT \
INCLUDE CONSECUTIVELY SPECIAL CHARACTER IN IT")
                                    return_checkconsi_special = check_consi_special(user_pass)

                                    if return_checkconsi_special is False:
                                        print("PASSWORD INVALID, PASSWORD CONTAINS \
MORE THAN 3 SAME SPECIAL CHARACTER CONSECUTIVELY ")
                                        user_newpass = get_password()
                                        password_validator_main(user_name, user_newpass)
                                    else:
                                        print(" THE PASSWORD PASSED AS IT DOES'NT HAVE USERNAME \
INTO PASSWORD AT ANY POSITION")
                                        return_checkcommon = check_csv(user_pass, csv_file_path)

                                        if return_checkcommon is True:
                                            print("PASSWORD INVALID, PASSWORD IS MOST COMMON")
                                            user_newpass = get_password()
                                            password_validator_main(user_name, user_newpass)
                                        else:
                                            print(" ")
                                            print("-------PASSWORD VALIDATED, THE GIVEN \
PASSWORD STATISFY ALL ABOVE CONDITION, HENCE IT IS STRONG PASSWORD ---------")
                                            print("FINAL VALIDATED PASSWORD: \n>> {}".format(user_pass))


# TO CHECK THE LENGTH OF PASSWORD
def check_length(user_pass):
    if len(user_pass) < 12:
        print("INVALID PASSWORD, THE PASSWORD SHOULD\
CONTAIN MINIMUM 12 CHARACTER IN IT ! ")
        return False
    elif len(user_pass) > 20:
        print("INVALID PASSWORD, THE PASSWORD SHOULD\
NOT CONTAIN MORE THAN 20 CHARACTER IN IT ! ")
        return False
    else:
        return True


# TO CHECK PASSWORD CONSIST OF UPPER-CASE [A-Z]
def check_uppercase(user_pass):
    count_upper = 0
    for i in user_pass:
        if ord(i) >= 65 and ord(i) <= 90:
            count_upper = count_upper + 1
        else:
            continue
    if count_upper < 3:
        return False
    else:
        return True


# TO CHECK PASSWORD CONSIST OF LOWER-CASE [a-z]
def check_lowercase(user_pass):
    count_lower = 0
    for i in user_pass:
        if ord(i) >= 97 and ord(i) <= 122:
            count_lower = count_lower + 1
        else:
            continue
    if count_lower < 3:
        return False
    else:
        return True


# TO CHECK PASSWORD CONSIST OF NUMBER IN RANGE [0-9]
def check_numbers(user_pass):
    count_number = 0
    numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in user_pass:
        if i in numbers_list:
            count_number = count_number + 1
        else:
            continue
    if count_number <= 0:
        return False
    else:
        return True


# TO CHECK PASSWORD CONSIST OF SPECIAL CHARACTER
def check_specialchar(user_pass):
    count_special = 0
    special_chars = ["!", "@", "#", "$", "%",
                     "^", "&", "*", "(", ")",
                     "_", "-", "~"]
    for i in user_pass:
        if i in special_chars:
            count_special = count_special + 1
        else:
            continue
    if count_special < 3:
        return False
    else:
        return True


# TO CHECK PASSWORD SHOULD START WITH EITHER
# ANY SPECIAL CHARACTER OR WITH 2 DIGIT'S NUMBER
def check_start(user_name):
    special_chars = ["!", "@", "#", "$",
                     "%", "^", "&", "*",
                     "(", ")", "_", "-", "~"]
    numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if user_name[0] in special_chars:
        return True
    elif (user_name[0] and user_name[1]) in numbers_list:
        return True
    else:
        return False


# TO CHECK SHOULD NOT CONTAIN 5 SAME CHARACTER OR NUMBER CONSECUTIVELY
def check_consi(user_pass):
    MAX_COUNT = 5
    for i in range(0, len(user_pass)):
        current_count = 1
        for j in range(i+1, len(user_pass)):
            if user_pass[i] != user_pass[j]:
                break
            else:
                current_count = current_count + 1

        if current_count >= 5:
            return False
    else:
        return True


# TO CHECK PASSWORD NOT CONTAIN 3 SAME SPECIAL CHARACTER'S CONSECUTIVELY
def check_consi_special(user_pass):
    MAX_COUNT_SPECIAL = 3
    for i in range(0, len(user_pass)):
        current_count = 1
        for j in range(i+1, len(user_pass)):
            if user_pass[i] != user_pass[j]:
                break
            else:
                current_count = current_count + 1

        if current_count >= 3:
            return False
    else:
        return True


# TO CHECK WHEATHER PASSWORD CONTAINS USERNAME IN IT
def check_username(user_name, user_pass):
    if user_name in user_pass:
        return False
    else:
        return True


# TO CHECK WHEATHER THE GIVEN PASSWORD IS GLOBALLY COMMON
def check_csv(user_pass, csv_file_path):
    with open(csv_file_path, 'r') as file:
        FOUND = False
        reader = csv.reader(file)

        for password in reader:
            if password[0] == user_pass:
                FOUND = True
                break
            else:
                continue
    return FOUND


# TO GET PASSWORD FROM USER AS INPUT
def get_password():
    print("-----------------------------------\
----------------------------------")
    user_pass = input("ENTER THE PASSWORD: \n >>")
    return user_pass


# TO GET USERNAME FROM USER AS INPUT
def get_username():
    user_name = input("ENTER THE USERNAME: \n >>")
    return user_name

def sample_function(): 
    print("This is the function wrote by Labhesh")
    print("This is Second Line")


def sample_function_1(): 
    print("Hello World")
    print("2nd line of thi functions")

print("This is my Work")

# DRIVER'S CODE
if __name__ == "__main__":
    print("---------------------------------------------------------------------")
    user_input = input("DO YOU WANT TO USE PASSWORD VALIDATOR (Y/N) : \n>>")
    if user_input.upper() == "Y":
        user_name = get_username()
        user_pass = get_password()
        password_validator_main(user_name, user_pass)
    elif user_input.upper() == "N":
        print("THANK YOU !!! ")
    else:
        print("INVALID INPUT, PLEASE CHOOSE Y OR N TO USE PASSWORD VALIDATOR")

    def function_1(num1, num2): # Labhesh's New Task 
        return num1+num2 
    
    def function_2(num1, num2): # Alexs New Task 
        return num1+num2 
    
    
    
