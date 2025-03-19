import xml.etree.ElementTree as et

user_id = 1
username = 'homer'
password = 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8='
mail_id = 2
email_address = 'homer.simpson@springfield.com'

# Create a user tree
user_elem = et.Element('user', id=str(user_id))

username_elem = et.SubElement(user_elem, 'username')
username_elem.text = username

password_elem = et.SubElement(user_elem, 'password')
password_elem.text = password

mails_elem = et.SubElement(user_elem, 'mails')
mail_elem = et.SubElement(mails_elem, 'mail', id=str(mail_id))
address_elem = et.SubElement(mail_elem, 'address')
address_elem.text = email_address

# Create an ElementTree object
tree = et.ElementTree(user_elem)

# Write to XML file
with open("other_user.xml", "wb") as file:
    tree.write(file, encoding='utf-8', xml_declaration=True)
