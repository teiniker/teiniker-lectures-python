# Directed association between classes (one-to-many)
#
#   [User]-1---*->[Mail]

class Mail():
    """Model of an email address."""

    def __init__(self, address:str)->None:
        self.address = address

    def __repr__(self)->str:
        return f"Mail('{self.address}')"

    def __str__(self)->str:
        return f"Mail: address='{self.address}'"

    def __eq__(self, other)->bool:
        return self.address == other.address


class User():
    """Model of a user having many mail addresses."""

    def __init__(self, oid:int, username:str, password:str)->None:
        self.oid = oid
        self.username = username
        self.password = password
        self.mails:list[Mail] = []

    def add_mail(self, mail:Mail)->None:
        self.mails.append(mail)

    def __repr__(self)->str:
        return f"User({self.oid}, '{self.username}', '{self.password}', {repr(self.mails)})"

    def __str__(self)->str:
        return f"User: id={self.oid}, username='{self.username}', mails={self.mails}"

    def __eq__(self, other)->bool:
        return self.oid == other.oid


if __name__ == '__main__':

    # Verify Mail
    m1 = Mail('homer.simpson@springfield.com')
    assert 'homer.simpson@springfield.com' == m1.address
    assert "Mail('homer.simpson@springfield.com')" == repr(m1)
    assert "Mail: address='homer.simpson@springfield.com'" == str(m1)

    m2 = Mail('homer.simpson@powerplant.com')
    assert m2.address ==  'homer.simpson@powerplant.com'


    # Verify User
    u = User(7, 'homer', ')jh%6Zgur5)r')
    u.add_mail(m1)
    u.add_mail(m2)

    assert 7 == u.oid
    assert 'homer' == u.username
    assert ')jh%6Zgur5)r' == u.password

    mails = u.mails
    assert 'homer.simpson@springfield.com' == mails[0].address
    assert 'homer.simpson@powerplant.com' == mails[1].address

    assert "User(7, 'homer', ')jh%6Zgur5)r', [Mail('homer.simpson@springfield.com'), "\
        "Mail('homer.simpson@powerplant.com')])" == repr(u)
    assert "User: id=7, username='homer', mails=[Mail('homer.simpson@springfield.com'), "\
        "Mail('homer.simpson@powerplant.com')]" == str(u)
