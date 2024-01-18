class User():
    pass

class UserTable():
    pass


if __name__ == '__main__':

    # Verify implementations
    bart1 = User(1, 'bart', 'EatMyShorts!')
    bart2 = User(1, 'bart', '#Kig%/5gT54$§')
    assert bart1 == bart2
    assert "User: id=1, username='bart'" == str(bart1)

    homer = User(3, 'homer', 'MoreDuff4Me!')
    marge = User(7, 'marge', 'Kh7gT.9/8#gH')

    table = UserTable()
    table.insert(homer)
    table.insert(marge)

    assert 'marge' == table.find_by_id(7).username
    assert 'homer' == table.find_by_id(3).username
    assert 2 == len(table.find_all())
