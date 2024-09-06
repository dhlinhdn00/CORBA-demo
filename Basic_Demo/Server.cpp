#include <iostream>
#include "Basic_Demo.hh"
#include <omniORB4/CORBA.h>
#include <omniORB4/poa.h>  

class AddOperatorImpl : public POA_Basic_Demo::Add_Operator {
public:
    virtual float add(float a, float b) override {
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

        // Tạo đối tượng AddOperatorImpl
        AddOperatorImpl* addOperatorImpl = new AddOperatorImpl();

        // Kích hoạt AddOperatorImpl trong POA
        PortableServer::ObjectId_var id = rootPOA->activate_object(addOperatorImpl);
        CORBA::Object_var obj = rootPOA->id_to_reference(id);
        Basic_Demo::Add_Operator_var add_operator = Basic_Demo::Add_Operator::_narrow(obj);

        // In ra IOR của Add_Operator
        CORBA::String_var ior = orb->object_to_string(add_operator);
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
