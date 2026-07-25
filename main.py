from agents.master_agent import MasterAgent
from agents.research_agent import ResearchAgent
from agents.script_writer import ScriptWriter
from agents.scene_planner import ScenePlanner

from utils.logger import Logger
from utils.file_manager import FileManager

import traceback


def main():

    logger = Logger()

    logger.info("CrimeCase AI Studio Started")

    agent = MasterAgent()
    agent.start()

    try:

        # ==================================================
        # Research
        # ==================================================

        research_agent = ResearchAgent()

        video = research_agent.research(
            "The Zodiac Killer"
        )

        print("\n========== RESEARCH RESULT ==========\n")

        print(video.title)
        print()
        print(video.summary)

        # ==================================================
        # Script Writing
        # ==================================================

        script_writer = ScriptWriter()

        video = script_writer.write_script(video)

        print("\n========== GENERATED SCRIPT ==========\n")

        print(video.script)

        # ==================================================
        # Scene Planning
        # ==================================================

        scene_planner = ScenePlanner()

        video = scene_planner.plan(video)

        print("\n========== GENERATED SCENES ==========\n")

        for scene in video.scenes:

            print(f"Scene {scene.number}")

            print("\nNarration:")
            print(scene.narration)

            print("\nImage Prompt:")
            print(scene.image_prompt)

            print(f"\nCamera      : {scene.camera}")
            print(f"Duration    : {scene.duration}")
            print(f"Music       : {scene.music}")
            print(f"Transition  : {scene.transition}")

            print("-" * 60)

        # ==================================================
        # Save Files
        # ==================================================

        FileManager.create_folder("videos/Test Project")

        FileManager.save_text(
            "videos/Test Project/script.txt",
            video.script
        )

        logger.info("Test files created successfully.")
        logger.info("Application Started Successfully")

    except Exception as e:

        print("\n========== FULL ERROR ==========\n")

        traceback.print_exc()

        print("\n===============================\n")

        logger.error(str(e))


if __name__ == "__main__":
    main()