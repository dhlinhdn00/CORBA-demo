import CORBA
import Advanced_Demo
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import Advanced_Demo__POA

class BotSystemImpl(Advanced_Demo__POA.QASystem):
    def __init__(self):
        print("Loading model...")
        self.model_name = "bigscience/bloom-560m" # Or you want change any model in huggfing face
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name).to("cuda")
        print("Model loaded!")

    def ask(self, question):
        print(f"Received question: {question}")
        
        inputs = self.tokenizer.encode(question, return_tensors="pt").to("cuda")
        
        outputs = self.model.generate(
            inputs,
            max_length=150,  
            num_return_sequences=1,  
            no_repeat_ngram_size=3,  
            do_sample=True, 
            temperature=0.7,  
            top_k=50,  
            top_p=0.95,  
            pad_token_id=self.tokenizer.eos_token_id 
        )
        
        answer = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"Answer: {answer}")
        return answer

def main():
    try:
        orb = CORBA.ORB_init()

        obj = orb.resolve_initial_references("RootPOA")
        poa = obj  

        poaManager = poa._get_the_POAManager()

        botsystem = BotSystemImpl()
        botsystem_id = poa.activate_object(botsystem)
        botsystem_ref = poa.servant_to_reference(botsystem)

        ior = orb.object_to_string(botsystem_ref)
        print(f"Server IOR: {ior}")

        with open("ior.txt", "w") as ior_file:
            ior_file.write(ior)
            print("IOR saved to ior.txt")

        poaManager.activate()
        orb.run()

    except CORBA.Exception as ex:
        print(f"CORBA Exception: {ex}")

if __name__ == "__main__":
    main()