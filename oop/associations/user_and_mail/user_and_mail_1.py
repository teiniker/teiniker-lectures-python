# Directed association between classes (one-to-one)
#
#   [User]---1->[Mail]

class Mail():
    def __init__(self, address:str)->None:
        self.address = address

    def __repr__(self)->str:
        return f"Mail('{self.address}')"

    def __str__(self)->str:
        return f"Mail: address='{self.address}'"

    def __eq__(self, other)-> bool:
        return self.address == other.address


class User():
    """Model of a user having only one mail addresse."""

    def __init__(self, oid:int, username:str, password:str, mail:Mail)->None:
        self.oid = oid
        self.username = username
        self.password = password
        self.mail = mail

    def __repr__(self)->str:
        return f"User({self.oid}, '{self.username}', '{self.password}', {repr(self.mail)})"

    def __str__(self)->str:
        return f"User: id={self.oid}, username='{self.username}', mail='{self.mail.address}'"

    def __eq__(self, other)->bool:
        return self.oid == other.id


if __name__ == '__main__':

    # Verify Mail
    m1 = Mail('homer.simpson@springfield.com')
    assert 'homer.simpson@springfield.com' == m1.address
    assert "Mail('homer.simpson@springfield.com')" == repr(m1)
    assert "Mail: address='homer.simpson@springfield.com'" == str(m1)

    m2 = Mail('homer.simpson@springfield.com')
    assert m1 == m2


    # Verify User
    u = User(7, 'homer', ')jh%6Zgur5)r', m1)
    assert 7 == u.oid
    assert 'homer' == u.username
    assert ')jh%6Zgur5)r' == u.password
    assert 'homer.simpson@springfield.com' == u.mail.address

    assert "User(7, 'homer', ')jh%6Zgur5)r', Mail('homer.simpson@springfield.com'))" == repr(u)

    assert "User: id=7, username='homer', mail='homer.simpson@springfield.com'" == str(u)
