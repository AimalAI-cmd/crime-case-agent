from utils.file_manager import FileManager


class PromptManager:

    @staticmethod
    def research_prompt(topic):

        prompt = FileManager.read_text(
            "templates/research_template.txt"
        )

        return prompt.replace("{topic}", topic)

    @staticmethod
    def scene_prompt(script):

        prompt = FileManager.read_text(
            "templates/scene_template.txt"
        )

        return prompt.replace("{script}", script)