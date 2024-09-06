import CORBA, Advanced_Demo
from transformers import pipeline
import omniORB
import PortableServer
import Advanced_Demo__POA  # Import đúng module chứa class servant

# Kế thừa từ Advanced_Demo__POA.QASystem, class servant được tạo ra từ IDL
class QASystemImpl(Advanced_Demo__POA.QASystem):
    def __init__(self):
        print("Loading model...")
        # Sử dụng mô hình BERT truyền thống với độ chính xác cao hơn
        self.qa_model = pipeline(
            "question-answering", 
            model="bert-large-uncased-whole-word-masking-finetuned-squad", 
            device=0,
            max_answer_len=128  # Set giới hạn độ dài câu trả lời là 128 token
        )
        print("Model loaded!")

    def ask(self, question):
        print(f"Received question: {question}")
        
        # Cố định context cụ thể và chi tiết hơn
        context = """
        I am an intelligent assistant trained to answer questions across various topics including science, 
        technology, history, and general knowledge. Feel free to ask me anything, and I will try to help 
        you with the best of my abilities.
        
        For example, I can explain scientific concepts, historical events, or provide summaries of complex ideas.
        """
        
        # Sử dụng mô hình QA để trả lời dựa trên context cố định và câu hỏi từ client
        response = self.qa_model(question=question, context=context)
        answer = response['answer']
        print(f"Answer: {answer}")
        return answer

# Khởi tạo ORB và lấy đối tượng POA
orb = CORBA.ORB_init()

# Lấy POA từ RootPOA, không cần narrow nữa
obj = orb.resolve_initial_references("RootPOA")
poa = obj  # Không cần gọi _narrow vì obj đã là PortableServer.POA

# Khởi tạo POAManager
poaManager = poa._get_the_POAManager()

# Đăng ký đối tượng servant (QASystemImpl)
qasystem = QASystemImpl()
qasystem_id = poa.activate_object(qasystem)
qasystem_ref = poa.servant_to_reference(qasystem)

# Chuyển đối tượng thành chuỗi IOR để client sử dụng
ior = orb.object_to_string(qasystem_ref)
print(f"Server IOR: {ior}")

# Kích hoạt POA và bắt đầu chạy server
poaManager.activate()
orb.run()
