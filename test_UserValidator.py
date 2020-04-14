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

    def test_givenEmail_WhenProper_ShouldReturnTrue(self):
        validator = UserValidator()
        result = validator.validateEmail("abc@yahoo.com")
        assert result == 'matched' 

    def test_givenMobileNumber_WhenProper_ShouldReturnTrue(self):
        validator = UserValidator()
        result = validator.validateMobileNumber("91 8877150686")
        assert result == 'matched'            

