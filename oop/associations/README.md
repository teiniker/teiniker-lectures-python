# Associations

In object-oriented programming (OOP), an **association** is a relationship
between two separate classes. It defines how objects of these classes are
connected to each other. Associations allow objects to communicate and
collaborate to perform tasks.

Two key properties of an association are **multiplicity** and
**directionality**:

*   **Multiplicity** defines how many objects of one class are linked to
    an object of another class (e.g., one-to-one, one-to-many).

*   **Directionality** defines how the objects are aware of each other
    (e.g., unidirectional or bidirectional).

Let's explore these concepts using the examples in this directory.


## One-to-One Directed Association

A one-to-one directed association means that one object of a class is
related to exactly one object of another class, and the relationship is
navigable in only one direction.

The owner class holds a direct reference to the owned object, but the
owned object has no knowledge of its owner.

**Example: `user_and_mail_1.py`**

In this example, a `User` has exactly one `Mail` address.

```python
class Mail():
    def __init__(self, address):
        self.address = address

class User():
    def __init__(self, oid, username, password, mail):
        self.oid = oid
        self.username = username
        self.password = password
        self.mail = mail    # ---[1]-> Holds one Mail object
```

Here, the `User` class has an attribute `mail` that holds a single `Mail`
object. You can navigate from a `User` instance to its `Mail` instance
(`user.mail`), but you cannot navigate from a `Mail` instance back to the
`User`.


## One-to-Many Directed Association

In a one-to-many directed association, one object of a class is related
to multiple objects of another class. The direction is again one-way.

This is commonly implemented by having the "one" side hold a collection
(like a list or dictionary) of objects from the "many" side.

**Example: `user_and_mail_2.py`**

Here, a `User` can have multiple `Mail` addresses.

```python
class User():
    def __init__(self, oid, username, password):
        self.oid = oid
        self.username = username
        self.password = password
        self.mails = [] # ---[*]-> Holds a list of Mail objects

    def add_mail(self, mail):
        self.mails.append(mail)
```

The `User`'s `mails` attribute is a list that can hold multiple `Mail`
objects.


## One-to-Many Bidirectional Association

A bidirectional association allows navigation in both directions. In a
one-to-many bidirectional relationship, the object on the "one" side holds
a collection of objects from the "many" side, and each object on the "many"
side holds a reference back to the single object on the "one" side.

It's crucial to correctly manage both sides of the relationship to keep them
in sync.

**Example: `user_and_mail_3.py`**

In this example, a `User` can have multiple `Mail` addresses, and each
`Mail` address knows which `User` it belongs to.

```python
class Mail():
    def __init__(self, address, user=None):
        self.address = address
        self.user = user    # ----[1]-> Holds one User object

    def set_user(self, user):
        self.user = user

class User():
    def __init__(self, oid, username, password):
        self.mails = [] # ----[*]-> Holds a list of Mail objects

    def add_mail(self, mail):
        # Set the back-reference from Mail to User
        mail.set_user(self)
        self.mails.append(mail)
```

When `user.add_mail(m1)` is called, the `User` object not only adds the `Mail`
object to its list but also sets the `user` attribute on the `Mail` object
to point back to itself. This creates the two-way link.


## References

* Eric Matthes. Python Crash Course. No Starch Press, 2016. 
    * Chapter 9: Classes



*Egon Teiniker, 2020-2026, GPL v3.0*
