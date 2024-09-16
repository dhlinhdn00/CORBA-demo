#include <iostream>
#include "Basic_Demo.hh"
#include <omniORB4/CORBA.h>

int main(int argc, char** argv) {
    try {
        CORBA::ORB_var orb = CORBA::ORB_init(argc, argv);

        std::string ior;
        std::cout << "Enter IOR: ";
        std::cin >> ior;

        CORBA::Object_var obj = orb->string_to_object(ior.c_str());

        Basic_Demo::Add_Operator_var add_operator = Basic_Demo::Add_Operator::_narrow(obj);

        if (!CORBA::is_nil(add_operator)) {
            float num1, num2;
            std::cout << "Enter first number: ";
            std::cin >> num1;
            std::cout << "Enter second number: ";
            std::cin >> num2;

            float result = add_operator->add(num1, num2);
            std::cout << "Result of " << num1 << " + " << num2 << ": " << result << std::endl;
        } else {
            std::cerr << "Failed to narrow object reference." << std::endl;
        }

        orb->destroy();
    }
    catch (CORBA::Exception& e) {
        std::cerr << "CORBA Exception: " << e._name() << std::endl;
        return 1;
    }

    return 0;
}
