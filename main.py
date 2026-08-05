from agents.master_agent import MasterAgent
from agents.research_agent import ResearchAgent
from agents.script_writer import ScriptWriter
from agents.scene_planner import ScenePlanner

from services.project_manager import ProjectManager

from utils.logger import Logger
from utils.file_manager import FileManager

import json
import traceback


def main():

    logger = Logger()

    logger.info("CrimeCase AI Studio Started")

    agent = MasterAgent()
    agent.start()


    try:

        # ==================================================
        # Project Initialization
        # ==================================================

        project = ProjectManager(
            "The_Zodiac_Killer"
        )

        project.create_project()


        print("\nProject Ready:")
        print(project.base_folder)


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
        # Save Script
        # ==================================================

        FileManager.save_text(
            project.script_file,
            video.script
        )



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
        # Save Scenes JSON
        # ==================================================

        scenes_data = []


        for scene in video.scenes:

            scenes_data.append({

                "number": scene.number,

                "narration": scene.narration,

                "image_prompt": scene.image_prompt,

                "camera": scene.camera,

                "duration": scene.duration,

                "music": scene.music,

                "transition": scene.transition

            })


        with open(
            project.scenes_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                {
                    "scenes": scenes_data
                },
                file,
                indent=4,
                ensure_ascii=False
            )



        # ==================================================
        # Create Initial State
        # ==================================================

        state = {

            "project": project.project_name,

            "status": "scene_planning_completed",

            "completed_steps": [

                "research",

                "script",

                "scene_planning"

            ]

        }


        with open(
            project.state_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                state,
                file,
                indent=4
            )



        logger.info(
            "Project files created successfully."
        )

        logger.info(
            "Application Started Successfully"
        )

        print("\n================================")
        print("PROJECT PIPELINE COMPLETED")
        print("================================\n")


    except Exception as e:


        print("\n========== FULL ERROR ==========\n")

        traceback.print_exc()

        print("\n===============================\n")

        logger.error(str(e))



if __name__ == "__main__":

    main()