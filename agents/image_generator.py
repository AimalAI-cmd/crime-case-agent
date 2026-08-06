import os

from services.ai_provider import AIProvider


class ImageGenerator:

    def __init__(self):

        self.ai = AIProvider()

    def generate(self, video, project):

        print("\nGenerating Scene Images...\n")

        for scene in video.scenes:

            print(f"Generating Scene {scene.number}")

            prompt = self.build_prompt(scene)

            print(prompt)

            image_name = f"scene_{scene.number}.png"

            image_path = os.path.join(
                project.images_folder,
                image_name
            )

            # Temporary placeholder
            with open(image_path, "w", encoding="utf-8") as file:
                file.write(prompt)

            print(f"Saved: {image_path}\n")

        print("✓ All image prompts generated.\n")

    def build_prompt(self, scene):

        return f"""
Netflix documentary style.

{scene.image_prompt}

Ultra realistic.

Cinematic lighting.

Highly detailed.

8K.

No text.

No watermark.

Camera:
{scene.camera}
""".strip()