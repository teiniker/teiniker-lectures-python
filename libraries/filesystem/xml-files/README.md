# XML Files

**XML (eXtensible Markup Language)** is a flexible, text-based markup language 
designed to store and transport data in a structured, human-readable, and 
machine-readable format.

## Structure of an XML File

An XML file has a hierarchical, tree-like structure defined by nested tags. 
It consists of the following main elements:

* **Declaration**: (optional) Specifies XML version and character encoding.
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  ```

* **Root Element**: Every XML document has exactly one root element containing all other elements.
  ```xml
  <books>
    <!-- All content goes here -->
  </books>
  ```

* **Elements**: Defined using tags (`<element>`). Elements can contain:
  - **Nested elements** (child elements)
  - **Text content**
  - **Attributes**

  ```xml
  <book id="1">
      <title>XML Guide</title>
      <author>John Doe</author>
  </book>
  ```

* **Attributes**: Extra information about elements, provided in key-value pairs within the opening tag.
  ```xml
  <book id="1" genre="Education" />
  ```

* **Comments**: Ignored by the parser, used for human readability.
  ```xml
  <!-- This is a comment -->
  ```

## XML Syntax Rules
* XML is case-sensitive.
* Elements must have matching opening and closing tags, or self-closing tags (`<element />`).
* Tags cannot overlap; proper nesting is required.
* Attribute values must be enclosed in quotes (single `'` or double `"` quotes).

## Example XML Documents
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<user id="1">
    <username>homer</username>
    <password>Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=</password>
    <mails>
        <mail id="2">
            <address>homer.simpson@springfield.com</address>
        </mail>
    </mails>
</user>
```

## Common Use Cases
* Data transfer between different applications or services.
* Configuration files.
* Web services (SOAP protocol).
* Document formats (e.g., Microsoft Office documents like `.docx` and `.xlsx`).


## xml.etree.ElementTree (ElementTree)

### Read XML Files

_Example:_ Read an XML file called `user.xml` 

```Python
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
```

* `et.fromstring(xml_data)` takes a string containing XML (`xml_data`) 
  and parses it into an `Element` object named `root`.
  This `root` object is the starting point to access all elements in your XML document.

* `root.get('id')` extracts the value of the attribute `id` from the `<user>` element.

* `root.findtext('username')` searches the direct child element named `<username>` 
  under `<user>` and returns its text content.
  Similarly, `password` extracts the `<password>` element's text.

* `root.find('mails/mail'`) searches for a nested element `<mail>` under `<mails>`. 
  It retrieves the first `<mail>` element found inside `<mails>`. 
  If found, `mail_element` is not `None`, and the attribute `id` is extracted.  

* `root.findtext('mails/mail/address')` searches for the `<address>` element nested 
  inside `<mail>`. It returns the text content of the `<address>` element.


### Write XML Files

_Example:_ Write an XML file from given user data

```Python
import xml.etree.ElementTree as et

# User data
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
```

* `user_elem = et.Element('user', id=str(user_id))` creates the root XML 
  element `<user>` and sets its attribute `id`.

* `username_elem = et.SubElement(user_elem, 'username')` 
  and `username_elem.text = username`
  adds a child `<username>` element under `<user>`.

* `password_elem = et.SubElement(user_elem, 'password')`
  and `password_elem.text = password` adds a child `<password>` element 
  under `<user>` and assigns it the provided password text.
  
* `mails_elem = et.SubElement(user_elem, 'mails')` adds a child `<mails>` 
  element under `<user>` to hold mail information.  

* `mail_elem = et.SubElement(mails_elem, 'mail', id=str(mail_id))` adds 
  a nested child `<mail>` element under `<mails>` and sets its attribute `id`.

* `address_elem = et.SubElement(mail_elem, 'address')` and 
  `address_elem.text = email_address` adds another nested child `<address>` 
  under `<mail>` to store the user's email address text.  

* `tree = et.ElementTree(user_elem)` creates an `ElementTree` 
  object from the root XML element `user_elem`.
  `ElementTree` objects can easily be written to XML files.

* `tree.write(file, encoding='utf-8', xml_declaration=True)`
  Writes the XML content into this file with `UTF-8` encoding and includes 
  an XML declaration at the top `<?xml version='1.0' encoding='utf-8'?>`.


## References

* [Real Python: A Roadmap to XML Parsers in Python](https://realpython.com/python-xml-parser/)


*Egon Teiniker, 2020-2025, GPL v3.0*