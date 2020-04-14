import re
class UserValidator:
    

    def validateFirstName(self, fname):
        FIRST_NAME_PATTERN = '^[A-Z]{1}[a-z]{2,}$'
        check = re.match(FIRST_NAME_PATTERN, fname)
        if check:
            return 'matched'
        else:
            return 'unmatched'    
