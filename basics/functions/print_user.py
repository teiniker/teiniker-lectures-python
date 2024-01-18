def user_to_string(username:str, password:str, group:str='user')->str:
    """Print username and passwort to the console."""
    return f'username:"{username}" password:"{password}" group:"{group}"'

def user_to_map(username:str, password:str, group:str='user')->dict[str,str]:
    """Collects a user's data in a map."""
    result = {'username':username, 'password':password, 'group':group}
    return result


if __name__ == '__main__':

    # Positional Arguments
    assert user_to_string('homer', 'Drink4DuffBeers') \
        == 'username:"homer" password:"Drink4DuffBeers" group:"user"'

    # Keyword Arguments
    assert user_to_string(password='Drink4DuffBeers', username='homer') \
        == 'username:"homer" password:"Drink4DuffBeers" group:"user"'

    # (Overide default value)
    assert user_to_string('homer', 'Drink4DuffBeers', 'admin') \
        == 'username:"homer" password:"Drink4DuffBeers" group:"admin"'

    # Map as return type
    data = user_to_map('homer', 'Drink4DuffBeers')
    assert data['username'] == 'homer'
    assert data['password'] == 'Drink4DuffBeers'
    assert data['group'] == 'user'
