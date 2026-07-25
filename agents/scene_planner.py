import json

from models.scene import Scene
from services.ai_provider import AIProvider
from services.prompt_manager import PromptManager


class ScenePlanner:

    def __init__(self):
        self.ai = AIProvider()

    def plan(self, video):

        print("\nPlanning Documentary Scenes...\n")

        prompt = PromptManager.scene_prompt(video.script)

        ai_response = self.ai.generate(prompt)

        print("\n========== RAW SCENE RESPONSE ==========")
        print(ai_response)
        print("========================================\n")

        # Remove markdown if AI returns it
        ai_response = ai_response.replace("```json", "")
        ai_response = ai_response.replace("```", "")
        ai_response = ai_response.strip()

        print("Response Type:", type(ai_response))
        print("First 100 Characters:")
        print(repr(ai_response[:100]))

        try:
            data = json.loads(ai_response)

            print("\n✓ JSON parsed successfully.\n")

        except json.JSONDecodeError as e:

            print("\n========== JSON ERROR ==========")
            print(e)
            print("================================\n")

            raise Exception(
                "AI did not return valid JSON for Scene Planner.\n\n"
                f"JSON Error:\n{e}\n\n"
                f"Response:\n{ai_response}"
            )

        if "scenes" not in data:
            raise Exception("JSON does not contain 'scenes'.")

        video.scenes = []

        for index, item in enumerate(data["scenes"], start=1):

            try:

                scene = Scene()

                scene.number = item["number"]
                scene.narration = item["narration"]
                scene.image_prompt = item["image_prompt"]
                scene.camera = item["camera"]
                scene.duration = item["duration"]
                scene.music = item["music"]
                scene.transition = item["transition"]

                video.scenes.append(scene)

            except KeyError as e:

                raise Exception(
                    f"Scene {index} is missing key: {e}"
                )

        print(f"\n✓ Successfully created {len(video.scenes)} scenes.\n")

        return video