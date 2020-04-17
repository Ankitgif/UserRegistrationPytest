import pytest
from UserValidator import UserValidator

testdata = [
   ["abc@yahoo.com", True],
   ["abc-100@yahoo.com", True],
   ["abc.100@yahoo.com", True],
   ["abc111@abc.com", True],
   ["abc-100@abc.net", True],
   ["abc.100@abc.com.au", True],
   ["abc@1.com", True],
   ["abc@gmail.com.com", True],
   ["abc+100@gmail.com", True],
   ["abc", False],
   ["abc@.com.my", False],
   ["abc123@gmail.a", False],
   ["abc123@.com", False],
   ["abc123@.com.com", False],
   [".abc@abc.com", False],
   ["abc()*@gmail.com", False],
   ["abc@%*.com", False],
   ["abc..2002@gmail.com", False],
   ["abc.@gmail.com", False],
   ["abc@abc@gmail.com", False],
   ["abc@gmail.com.1a", False],
   ["abc@gmail.com.aa.au", False]
]

@pytest.mark.parametrize("name,expected",testdata)
def test_email_Validator(name,expected):
    validator = UserValidator()
    result = validator.validateEmailParam(name)
    assert result == expected
