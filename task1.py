"""
===================   TASK 1   ====================
* Name: Can String Be Float
*
* Write a function `can_string_be_float` that will
* check whether the passed string value can be
* converted to float. If the string value can be
* successfully converted to float, function should
* return `True` otherwise it should return `False`.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

#da li string moze da se konvertuje u broj
def  moze_li_u_float(string_broj):
    if not isinstance(string_broj,str):
        return False

    dozvoljeni_karakteri = ['0','1','2','3','4','5','6','7','8','9','.','-']

    for karakter in string_broj:
        if karakter not in dozvoljeni_karakteri:
           return False

    return True

print(moze_li_u_float("5"))