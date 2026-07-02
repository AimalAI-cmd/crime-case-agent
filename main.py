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

    # Research Agent
    research_agent = ResearchAgent()
    research = research_agent.research("The Zodiac Killer")

    print("\nResearch Result:\n")
    print(research)

    # Script Writer
    script_writer = ScriptWriter()
    script = script_writer.write_script(research)

    print("\nGenerated Script:\n")
    print(script)

    # Save Script
    FileManager.create_folder("videos/Test Project")

    FileManager.save_text(
    "videos/Test Project/script.txt",
    script
)
    

    logger.info("Test files created successfully.")
    logger.info("Application Started Successfully")


if __name__ == "__main__":
    main()