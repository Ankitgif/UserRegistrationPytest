import re
class UserValidator:
    
    global NAME_PATTERN
    global EMAIL_PATTERN
    NAME_PATTERN = '^[A-Z]{1}[a-z]{2,}$'
    EMAIL_PATTERN = "^[a-z]{3,}([._+\-][a-z0-9]*)?[@]{1}[a-z]{2,}[.]{1}[a-z]{2,4}(\.[a-z]{2})?$"
    

    def validateFirstName(self, fname):
        check = re.match(NAME_PATTERN, fname)
        if check:
            return 'matched'
        else:
            return 'unmatched'


    def validateLastName(self, lname):
        check = re.match(NAME_PATTERN, lname)
        if check:
            return 'matched'
        else:
            return 'unmatched' 

    def validateEmail(self, email):
        check = re.match(EMAIL_PATTERN, email)
        if check:
            return 'matched'
        else:
            return 'unmatched' 


    def validateMobileNumber(self, number):
        MOBILE_PATTERN = "^[0-9]{2}[ :space: ][0-9]{10}"
        check = re.match(MOBILE_PATTERN, number)
        if check:
            return 'matched'
        else:
            return 'unmatched' 

    def validatePassWord(self, password):
        PASSWORD_PATTERN = "^(?=.*?[A-Z])(?=.*?[0-9])(?=.*[@$!%*#?&]).{8,}"
        check = re.match(PASSWORD_PATTERN, password)
        if check:
            return 'matched'
        else:
            return 'unmatched'   

    def validateEmailParam(self,name):
        check = re.match(EMAIL_PATTERN, name)
        if check:
            return True
        else:
            return False



               
