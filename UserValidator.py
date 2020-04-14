import re
class UserValidator:
    
    global NAME_PATTERN
    NAME_PATTERN = '^[A-Z]{1}[a-z]{2,}$'

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


               
