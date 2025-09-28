# src/nlp_bot.py
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
from utils import log_event

class NLPBot:
    """
    StrayMate AI Chatbot for the Stray Animal Feeder project.
    - Uses transformers for text generation.
    - Provides project-specific knowledge.
    - Interfaces with FeederRobot and CVModule (future integration).
    """
    def __init__(self, model_name="gpt2", max_tokens=256):
        self.model_name = model_name
        self.max_tokens = max_tokens
        log_event(f"Initializing NLPBot with model {self.model_name}")

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=0 if torch.cuda.is_available() else -1
        )
        self.intro_message = (
            "Hello! I am StrayMate, your AI assistant for the Stray Animal Feeder project. "
            "I can answer questions about myself, the robot, CV module, and feeding analytics."
        )
        log_event("NLPBot initialization complete.")

    def greet(self):
        log_event("Greet method called.")
        return self.intro_message

    def get_response(self, user_input: str):
        """
        Generates a response to the user input.
        - Uses truncation for safety.
        - Ensures project-specific context.
        """
        log_event(f"User input received: {user_input}")
        prompt = f"Project: Stray Animal Feeder\nStrayMate AI Bot knows the system and responds:\nUser: {user_input}\nStrayMate:"
        response = self.generator(
            prompt,
            max_new_tokens=self.max_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.2
        )
        log_event(f"Generated response: {response[0]['generated_text']}")
        return response[0]['generated_text']
