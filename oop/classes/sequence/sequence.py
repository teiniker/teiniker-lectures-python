class IntegerSequence():
    _value = 0   # class variable

    @classmethod
    def init_value(cls, value):
        cls._value = value

    @classmethod
    def next_value(cls):
        cls._value += 1
        return cls._value


if __name__ == '__main__':

    # Verify implementations

    IntegerSequence.init_value(0)

    assert 1 == IntegerSequence.next_value()
    assert 2 == IntegerSequence.next_value()
    assert 3 == IntegerSequence.next_value()
