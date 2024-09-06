#include <iostream>
#include "Calculator.hh"
#include <omniORB4/CORBA.h>
#include <omniORB4/poa.h>  // Sử dụng POA.h cho quản lý POA

// Triển khai lớp Calculator
class CalculatorImpl : public POA_Demo::Calculator {
public:
    virtual float add(float a, float b) {
        std::cout << "Server: Adding " << a << " and " << b << std::endl;
        return a + b;
    }
};

int main(int argc, char** argv) {
    try {
        // Khởi tạo ORB
        CORBA::ORB_var orb = CORBA::ORB_init(argc, argv);

        // Lấy RootPOA và kích hoạt POA Manager
        CORBA::Object_var poaObj = orb->resolve_initial_references("RootPOA");
        PortableServer::POA_var rootPOA = PortableServer::POA::_narrow(poaObj);
        PortableServer::POAManager_var poaManager = rootPOA->the_POAManager();
        poaManager->activate();

        // Tạo đối tượng CalculatorImpl
        CalculatorImpl* calculatorImpl = new CalculatorImpl();

        // Kích hoạt CalculatorImpl trong POA
        PortableServer::ObjectId_var id = rootPOA->activate_object(calculatorImpl);
        CORBA::Object_var obj = rootPOA->id_to_reference(id);
        Demo::Calculator_var calculator = Demo::Calculator::_narrow(obj);

        // In ra IOR của Calculator
        CORBA::String_var ior = orb->object_to_string(calculator);
        std::cout << "Server is running. IOR: " << ior << std::endl;

        // Chạy ORB
        orb->run();
    }
    catch (CORBA::Exception& e) {
        std::cerr << "CORBA Exception: " << e._name() << std::endl;
        return 1;
    }

    return 0;
}
