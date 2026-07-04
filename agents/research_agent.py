from models.video import Video


class ResearchAgent:

    def research(self, topic):

        print(f"Researching topic: {topic}")

        video = Video()

        video.title = topic
        video.topic = topic
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