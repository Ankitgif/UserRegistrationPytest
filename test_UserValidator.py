import pytest
from UserValidator import UserValidator
class Test_UserValidatorTest:

    def test_givenFirstName_WhenProper_ShouldReturnTrue(self):
        validator = UserValidator()
        result = validator.validateFirstName("Ankit")
        assert result == 'matched'


    def test_givenLastName_WhenProper_ShouldReturnTrue(self):
        validator = UserValidator()
        result = validator.validateLastName("Kumar")
        assert result == 'matched'    

