# PASSWORD VALIDATOR

THIS REPOSITORY CONSIST OF SOURCE CODE OF PASSWORD VALIDATOR IN PYTHON LANGUAGE AND CSV FILE OF MOST COMMON PASSWORD  

## REQUIREMENTS:

To Run the Source Code of Password Validator you would need Python3 Installed onto your Computer.

## INSTALLATION OF PYTHON 3:

STEP 1 : Visit the link [Python Link] (https://www.python.org/downloads) and Select the Version above 
         Python 3.0 and above

STEP 2 :  Download Python Executable Installer 

STEP 3 : Run Executable Installer

STEP 4 :  Verify Python Was Installed On Windows

***Note: if above steps are not clear please visit below link for more information***
(https://phoenixnap.com/kb/how-to-install-python-3-windows)

## INFORMATION ABOUT PASSWORD VALIDATOR

Password Validators are responsible for determining whether a proposed password is acceptable for use and could include checks like ensuring it meets minimum length requirements, that it has an appropriate range of characters, or that it is not in the history.

The password policy for a user specifies the set of password validators that should be used whenever that user provides a new password. In order to activate a password validator, the corresponding configuration entry must be enabled, and the DN of that entry should be included in the password-validator attribute of the password policy in which you want that validator active. All password validator configuration entries must contain the password-validator structural objectclass.

## PASSWORD VALIDATION SCENARIOS/ ACCEPTANCE CRITERIA

The Below Scenarios are to Validate the Password  

**1) PASSWORD LENGTH SHOULD BE OF MINIMUM 12 CHARACTER**

**2) PASSWORD LENGTH SHOULD NOT BE GREATER THAN 20 CHARACTER**

**3) PASSWORD MUST CONSIST OF UPPER-CASE CHARACTER'S [A-Z]**

**4) PASSWORD MUST CONSIST OF LOWER-CASE CHARACTER'S [a-z]**

**5) PASSWORD MUST CONSIST OF NUMBER [0-9]**

**6) PASSWORD MUST CONSIST OF SPECIAL CHARACTERS - !, @, #, $, %, ^, &, *, (, ), _, -, ~,***

**7) PASSWORD SHOULD START WITH EITHER ANY SPECIAL CHARACTER OR WITH 2 DIGIT'S NUMBER**

**8) PASSWORD SHOULD CONTAIN ATLEAST 3 UPPER-CASE CHARACTER'S AND 3 LOWER-CASE CHARACTER'S**

**9) PASSWORD SHOULD CONTAIN ATLEAST 3 SPECIAL CHARACTER**

**10) PASSWORD SHOULD NOT CONTAIN 5 SAME CHARACTER'S OR NUMBER CONSECUTIVELY**

**11) PASSWORD SHOULD NOT CONTAIN 3 SAME SPECIAL CHARACTER'S CONSECUTIVELY**

**12) PASSWORD SHOULD NOT HAVE USERNAME INTO IT AT ANY POSITION**

***The Password will get Validated only and only if every scenario is Passed, Hence it will be one of the Strong Validated Passwords after satisfying the above criteria***

## FUNCTIONS PRESENT IN SOURCE CODE
```
1) instructions()
2) get_password()
3) get_username()
4) password_validator_main()
5) check_length()
6) check_uppercase()
7) check_lowercase()
8) check_numbers()
9) check_specialchar()
10) check_start()
11) check_username()
12) check_consi()
13) check_consi_special()
14) check_csv()
```

## FUNCTION DESCRIPTION

***Note:***

***user_pass is the Password given by user to validate.***

***user_name is the Username given by user.*** 

---------------------------------------------------------------------------------------------------
***1) instructions() :***
This Function does not takes any formal parameters, The Functionality of instrunction() is to generally display the Instructions of Password Validator, This function consist of print Statement and does not return any value. 

***2) get_password():***
This Function does not take any formal parameter, The Functionality of get_password() is to take the Passowrd from user using input() function in and This Function returns the user_pass the return type of user_pass is string.

***3) get_username():***
This Function does not take any formal parameter, The Functionality of get_username() is to take the Username from user using input() function in and This Function returns the user_name, the return type of user_name is string.

***4) password_validator_main(user_name, user_pass):***
This Function take two formal parameter such as user_name, user_pass of string data-type, This Function is the main function of the password Validator, This function consist of Decision Statements i.e cluster of if and else statements in it  to call other function according to there functionality.

***5) check_length(user_pass):***
This Function takes one formal parameter user_password of string data-type , The Functionality of check_length() is to check the length of user's password wheather it statisfy the criteria of 
***PASSWORD LENGTH SHOULD BE OF MINIMUM 12 CHARACTER*** and ***PASSWORD LENGTH SHOULD NOT BE GREATER THAN 20 CHARACTER*** , The function Return boolean value True or False depending criteria, if criteria gets statisfy the function returns True or else return False.

***6) check_uppercase(user_pass):***
This Function takes one formal parameter user_password of string data-type, The Functionality of check_uppercase() is to check presence of the upper-case characters [A-Z] in password and also to check the count of upper_case character as password should consist atleast 3 upper-case character. This function has return-type boolean True or False value. if criteria gets statisfy the function returns True or else return False.
  
***7) check_lowercase(user-pass):***
This Function takes one formal parameter user_password of string data-type, The Functionality of check_lowercase() is to check presence of the lower-case characters [a-z] in password and also to check the count of lower_case character as password should consist atleast 3 lower-case character. This function has return-type boolean True or False value. if criteria gets statisfy the function returns True or else return False 

***8) check_numbers(user_pass):***
This Function takes one formal parameter user_password of string data-type, The Functionality of check_numbers() is to check presence of the numbers [0-9] in password. This function has return-type boolean True or False value. if criteria gets statisfy the function returns True or else return False  

***9) check_specialchar(user_pass):***
This Function takes one formal parameter user_password of string data-type, The Functionality of check_specailchar() is to check presence of the special characters that are in password and also count the special character present in password, as passowrd should consist atleast 3 special scharacter in it  This function has return-type boolean True or False value. if criteria gets statisfy the function returns True or else return False   


***11) check_start(user_name):***
This Function takes one formal parameter user_name of string data-type, The Functionality of check_start() is to chec kwhether the password starts from 1 special character or 2 digit's number 
This function has return-type boolean True or False value. if criteria gets statisfy the function returns True or else return False 

***12) check_username(user_name, user_pass):***
This Function takes two formal parameter user_password and user_nameof string data-type, The Functionality of check_username() is to check whether password contains username in it , if Passowrd consist of username in it this function will return Flase or else it will return True. 

***13) check_consi(user_pass):***
This Function takes one formal parameter user_password of string data-type, The Functionality of check_consi() is to check the whether there are 5 same consecutively character or number in password,
This function has return-type boolean True or False value. if criteria gets statisfy the function returns True or else return False 

***14) check_consi_special(user_pass):***
This Function takes one formal parameter user_password of string data-type, The The Functionality of check_consi_special() is to check the whether there are 3 same consecutively special character in password, This function has return-type boolean True or False value. if criteria gets statisfy the function returns True or else return False   

***15) check_csv(user_pass):***
This Function takes one formal parameter user_password of string data-type, The Functionality of check_csv is to check whether the password is most common or not , The csv file will consist of most common password combination, this function will parse the csv and return the result as True or False  function has return-type boolean True or False value. if criteria gets statisfy the function returns True or else return False.  

## SOURCE CODE EXPLANATION:
The source code consist of functions and used functional programming with Decision making statements in it, also the code consist of Parsing / reading concept of CSV file (Comma Separated Values ) file using csv python module.

## EXTRA PYTHON MODULES USED IN SOURCE CODE:
**1) CSV module**

Imported csv module, to parse or for Reading and Writing CSV Files using Python programming.
* CSV module Installation link and Documentaion link (https://pypi.org/project/python-csv)

## RESOUCRCE

* Python (https://www.python.org/doc)
* Python Tutorial (https://www.tutorialspoint.com/python/index.html)
* CSV File Tutorial (https://www.programiz.com/python-programming/csv)
-----------------------------------------------------------------------------------------------------
**CREATED BY LABHESH LALKA**

**SOFTWARE ENGINEER - CONSULTADD** 
**TEAM ERUDITE**
