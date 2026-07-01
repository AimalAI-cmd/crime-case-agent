import logging
import os


class Logger:
    def __init__(self, log_file="logs/crime_case_agent.log"):
        os.makedirs("logs", exist_ok=True)

        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )

        self.logger = logging.getLogger("CrimeCaseAI")

    def info(self, message):
        self.logger.info(message)
        print(f"[INFO] {message}")

    def error(self, message):
        self.logger.error(message)
        print(f"[ERROR] {message}")