from resistor import Resistor

if __name__ == '__main__':

    # Verify implementation

    try:
        r1 = Resistor(1000, -1)
        #...
    except ValueError as ex:
        print(f"Resistor object can't be created: {ex}")
    else:
        print("No exception thrown.")


    try:
        r1 = Resistor(-1000, 2)
        #...
    except ValueError as ex:
        print(f"Resistor object can't be created: {ex}")
    finally:
        print("Do some clean-up.")
