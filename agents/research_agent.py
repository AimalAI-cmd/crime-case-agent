from models.video import Video
from services.ai_provider import AIProvider
from services.prompt_manager import PromptManager


class ResearchAgent:

    def __init__(self):
        self.ai = AIProvider()

    def research(self, topic):

        print(f"Researching topic: {topic}")

        prompt = PromptManager.research_prompt(topic)

        ai_response = self.ai.generate(prompt)

        video = Video()

        video.title = topic
        video.topic = topic

        # Temporary sample data
        video.summary = "This is a sample research summary."

        video.timeline = [
            "Event 1",
            "Event 2",
            "Event 3"
        ]

        video.interesting_facts = [
            "Fact 1",
            "Fact 2"
        ]

        return video