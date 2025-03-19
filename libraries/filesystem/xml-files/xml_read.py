import xml.etree.ElementTree as et

# Open and parse XML from the file
with open('user.xml', 'r', encoding='utf-8') as file:
    xml_data = file.read()

# Parse XML data
root = et.fromstring(xml_data)

# Extract values
user_id = root.get('id')
username = root.findtext('username')
password = root.findtext('password')
mail_element = root.find('mails/mail')
if mail_element is not None:
    mail_id = mail_element.get('id')
else:
    mail_id = None
email_address = root.findtext('mails/mail/address')

# Assertions to validate the parsed XML data
assert '1' == user_id
assert 'homer' == username
assert 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=' == password
assert '2' == mail_id
assert 'homer.simpson@springfield.com' == email_address
