"""
===================   TASK 2   ====================
* Name: Convert Kilometers To Miles
*
* Write a script that will convert kilometers to
* miles. Script should ask user for input and check
* if user input is valid. If not, the script should
* quit immediately with appropriate message.
*
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Note: You may use `can_string_be_float` function
* from previous task to validate user input.
===================================================
"""

def can_string_be_float(user_value):

    dozvoljeni_karakteri = ['0','1','2','3','4','5','6','7','8','9','.','-']

    for ch in user_value:

        if ch not in dozvoljeni_karakteri:
            return False

        broj_tacaka = 0

        for ch in user_value:
            if ch == '.':
                broj_tacaka = broj_tacaka + 1

        if broj_tacaka > 1:
            return False

        broj_minusa = 0

        for ch in user_value:
            if ch=='-':
                broj_minusa = broj_minusa + 1

        if broj_minusa > 1:
            return False

        if broj_minusa == 1:
            if user_value[0] != '-':
                return False

    return True

def main():

    user_value= (input("Unesite duzinu u kilometrima: "))

    if can_string_be_float(user_value):
        print("Duzina u miljama je: ", float(user_value) * 0.6214)
    else:
        print("Unijeli ste pogresan podatak!")

main()