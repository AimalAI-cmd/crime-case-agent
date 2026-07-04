class ScriptWriter:

    def write_script(self, video):

        script = f"""
Title: {video.title}

Introduction

{video.summary}

Timeline

"""

        for event in video.timeline:
            script += f"- {event}\n"

        script += "\nInteresting Facts\n"

        for fact in video.interesting_facts:
            script += f"- {fact}\n"

        video.script = script

        return video