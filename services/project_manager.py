import os

from utils.file_manager import FileManager


class ProjectManager:

    def __init__(self, project_name):

        self.project_name = project_name

        self.base_folder = os.path.join(
            "projects",
            project_name
        )

        self.images_folder = os.path.join(
            self.base_folder,
            "images"
        )

        self.audio_folder = os.path.join(
            self.base_folder,
            "audio"
        )

        self.clips_folder = os.path.join(
            self.base_folder,
            "clips"
        )

        self.subtitle_folder = os.path.join(
            self.base_folder,
            "subtitles"
        )

        self.cache_folder = os.path.join(
            self.base_folder,
            "cache"
        )


        # Project files

        self.research_file = os.path.join(
            self.base_folder,
            "research.json"
        )

        self.script_file = os.path.join(
            self.base_folder,
            "script.txt"
        )

        self.scenes_file = os.path.join(
            self.base_folder,
            "scenes.json"
        )

        self.state_file = os.path.join(
            self.base_folder,
            "state.json"
        )


    def create_project(self):

        folders = [
            self.base_folder,
            self.images_folder,
            self.audio_folder,
            self.clips_folder,
            self.subtitle_folder,
            self.cache_folder
        ]

        for folder in folders:
            FileManager.create_folder(folder)


    def show_paths(self):

        print("\n========== PROJECT ==========")
        print("Name:", self.project_name)

        print("\nBase:")
        print(self.base_folder)

        print("\nResearch:")
        print(self.research_file)

        print("\nScript:")
        print(self.script_file)

        print("\nScenes:")
        print(self.scenes_file)

        print("\nImages:")
        print(self.images_folder)

        print("\nAudio:")
        print(self.audio_folder)

        print("\nClips:")
        print(self.clips_folder)

        print("\nSubtitles:")
        print(self.subtitle_folder)

        print("\nCache:")
        print(self.cache_folder)

        print("=============================\n")