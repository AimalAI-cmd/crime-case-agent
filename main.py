from agents.master_agent import MasterAgent
from agents.research_agent import ResearchAgent
from agents.script_writer import ScriptWriter
from utils.logger import Logger
from utils.file_manager import FileManager


def main():
    logger = Logger()

    logger.info("CrimeCase AI Studio Started")

    agent = MasterAgent()
    agent.start()

    # Research
    research_agent = ResearchAgent()
    video = research_agent.research("The Zodiac Killer")

    print("\nResearch Result:\n")
    print(video.title)
    print(video.summary)

    # Script Writing
    script_writer = ScriptWriter()
    video = script_writer.write_script(video)

    print("\nGenerated Script:\n")
    print(video.script)

    # Save Script
    FileManager.create_folder("videos/Test Project")

    FileManager.save_text(
        "videos/Test Project/script.txt",
        video.script
    )

    logger.info("Test files created successfully.")
    logger.info("Application Started Successfully")


if __name__ == "__main__":
    main()