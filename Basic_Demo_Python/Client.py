import sys
from omniORB import CORBA
import Basic_Demo

def main():
    try:
        orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

        ior = input("Enter IOR: ")

        obj = orb.string_to_object(ior)

        add_operator = obj._narrow(Basic_Demo.Add_Operator)

        if add_operator is None:
            print("Failed to narrow object reference.")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = add_operator.add(num1, num2)
        print(f"Result of {num1} + {num2}: {result}")

        orb.destroy()

    except CORBA.Exception as ex:
        print(f"CORBA Exception: {ex}")

if __name__ == "__main__":
    main()
