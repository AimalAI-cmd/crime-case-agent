from config.settings import PROJECT_NAME, VERSION


class MasterAgent:
    def __init__(self):
        self.project_name = PROJECT_NAME
        self.version = VERSION

    def start(self):
        print("=" * 50)
        print(f"{self.project_name} v{self.version}")
        print("Master Agent Started Successfully!")
        print("=" * 50)