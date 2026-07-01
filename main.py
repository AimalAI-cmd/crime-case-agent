from agents.master_agent import MasterAgent
from utils.logger import Logger


def main():
    logger = Logger()

    logger.info("CrimeCase AI Studio Started")

    agent = MasterAgent()
    agent.start()

    logger.info("Application Started Successfully")


if __name__ == "__main__":
    main()