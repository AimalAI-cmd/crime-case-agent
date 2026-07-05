class PromptManager:

    @staticmethod
    def research_prompt(topic):

        return f"""
Research this crime case.

Topic:

{topic}

Provide:

1. Summary
2. Timeline
3. Interesting Facts
"""