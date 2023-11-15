import pytest
from lib.password_checker import*

#Password >8
def test_password_checker_IppoEcho():
    password = PasswordChecker()
    assert password.check("Ippo.Echo") == True

#Password <8
def test_password_checker_Ippo():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("Ippo")
    message = str(e.value)
    assert message == "Invalid password, must be 8+ characters."
