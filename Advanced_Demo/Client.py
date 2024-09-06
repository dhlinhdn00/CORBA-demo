import CORBA, Advanced_Demo

# Construct ORB
orb = CORBA.ORB_init()

# IOR String (Address)
ior = input("Enter the server IOR: ")
obj = orb.string_to_object(ior)

# Connect to QASystem
qasystem = obj._narrow(Advanced_Demo.QASystem)

# Send Question
question = input("Enter your question: ")  # Chỉ nhập câu hỏi

# Send the question to server
answer = qasystem.ask(question)

# Show the answer from server
print(f"Answer: {answer}")

orb.destroy()
