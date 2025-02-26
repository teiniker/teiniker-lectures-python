# Bidirectional association between classes (one-to-many)
#
#   [User]-[1]---[*]-[Mail]

class Mail():
    """Model of an email address."""

    def __init__(self, address, user=None):
        self.address = address
        self.user = user    # ----[1]->[User]

    def set_user(self, user):
        self.user = user


class User():
    """Model of a user having many mail addresses."""

    def __init__(self, oid, username, password):
        self.oid = oid
        self.username = username
        self.password = password
        self.mails = [] # ----[*]->[Mail]

    def add_mail(self, mail):
        mail.set_user(self)
        self.mails.append(mail)


if __name__ == '__main__':

    # Verify Mail
    m1 = Mail('homer.simpson@springfield.com')
    assert 'homer.simpson@springfield.com' == m1.address

    m2 = Mail('homer.simpson@powerplant.com')
    assert m2.address ==  'homer.simpson@powerplant.com'


    # Verify User
    u = User(7, 'homer', ')jh%6Zgur5)r')
    u.add_mail(m1)
    m1.set_user(u)

    u.add_mail(m2)
    m2.set_user(u)

    assert 7 == u.oid
    assert 'homer' == u.username
    assert ')jh%6Zgur5)r' == u.password

    mails = u.mails
    assert 'homer.simpson@springfield.com' == mails[0].address
    assert 'homer.simpson@powerplant.com' == mails[1].address

    assert 7 == mails[0].user.oid
    assert 7 == mails[1].user.oid
