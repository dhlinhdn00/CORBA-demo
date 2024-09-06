#include <iostream>
#include "Calculator.hh"
#include <omniORB4/CORBA.h>

int main(int argc, char** argv) {
    try {
        // Khởi tạo ORB
        CORBA::ORB_var orb = CORBA::ORB_init(argc, argv);

        // Nhập IOR từ người dùng
        std::string ior;
        std::cout << "Enter IOR: ";
        std::cin >> ior;

        // Chuyển IOR thành đối tượng CORBA
        CORBA::Object_var obj = orb->string_to_object(ior.c_str());

        // Hẹp đối tượng về giao diện Calculator
        Demo::Calculator_var calculator = Demo::Calculator::_narrow(obj);

        if (!CORBA::is_nil(calculator)) {
            // Yêu cầu người dùng nhập hai số
            float num1, num2;
            std::cout << "Enter first number: ";
            std::cin >> num1;
            std::cout << "Enter second number: ";
            std::cin >> num2;

            // Gọi phương thức add từ xa
            float result = calculator->add(num1, num2);
            std::cout << "Result of " << num1 << " + " << num2 << ": " << result << std::endl;
        } else {
            std::cerr << "Failed to narrow object reference." << std::endl;
        }

        // Hủy ORB
        orb->destroy();
    }
    catch (CORBA::Exception& e) {
        std::cerr << "CORBA Exception: " << e._name() << std::endl;
        return 1;
    }

    return 0;
}
