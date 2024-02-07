from numb3rs import validate

def test_correct():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True

def test_wrongly_formatted():
    assert validate("127.0..") == False
    assert validate("cat") == False


def test_wrong_value():
    assert validate("128.444.3.1") == False