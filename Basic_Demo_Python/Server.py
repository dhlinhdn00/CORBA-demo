import sys
import CORBA, PortableServer
import Basic_Demo

class AddOperatorImpl(Basic_Demo.Add_Operator):
    def add(self, a, b):
        print(f"Server: Adding {a} and {b}")
        return a + b


def main():
    try:
        orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

        poa = orb.resolve_initial_references("RootPOA")
        rootPOA = poa._narrow(PortableServer.POA)
        poaManager = rootPOA._get_the_POAManager()
        poaManager.activate()

        add_operator_impl = AddOperatorImpl()

        objectId = rootPOA.activate_object(add_operator_impl)
        obj = rootPOA.id_to_reference(objectId)
        add_operator = obj._narrow(Basic_Demo.Add_Operator)

        ior = orb.object_to_string(add_operator)
        print(f"Server is running. IOR: {ior}")

        with open("ior.txt", "w") as ior_file:
            ior_file.write(ior)
            print("IOR saved to ior.txt")

        orb.run()
    except CORBA.Exception as ex:
        print(f"CORBA Exception: {ex}")

if __name__ == "__main__":
    main()
