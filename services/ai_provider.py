from config.settings import AI_PROVIDER, AI_MODEL


class AIProvider:

    def __init__(self):
        self.provider = AI_PROVIDER
        self.model = AI_MODEL

    def generate(self, prompt):

        print("\n========== AI Provider ==========")
        print(f"Provider : {self.provider}")
        print(f"Model    : {self.model}")
        print("=================================\n")

        print("Sending Prompt to AI...\n")
        print(prompt)

        return "This is a sample AI response."