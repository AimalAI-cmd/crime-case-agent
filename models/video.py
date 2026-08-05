import json


class Video:

    def __init__(self, project=None):

        # Project reference
        self.project = project


        # Basic Information
        self.title = ""
        self.topic = ""


        # Research Data
        self.summary = ""
        self.timeline = []
        self.interesting_facts = []


        # Generated Content
        self.script = ""

        self.scenes = []


        # Media Assets

        self.images = []

        self.audio = ""

        self.music = ""

        self.subtitles = ""

        self.clips = []

        self.thumbnail = ""

        self.final_video = ""



        # Pipeline State

        self.status = {

            "research": "pending",

            "script": "pending",

            "scenes": "pending",

            "images": "pending",

            "audio": "pending",

            "video": "pending",

            "upload": "pending"

        }



    def update_status(self, step, value):

        if step in self.status:

            self.status[step] = value



    def to_dict(self):

        return {

            "title": self.title,

            "topic": self.topic,

            "summary": self.summary,

            "timeline": self.timeline,

            "interesting_facts": self.interesting_facts,

            "script": self.script,

            "status": self.status

        }



    def save_json(self, path):

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.to_dict(),
                file,
                indent=4,
                ensure_ascii=False
            )