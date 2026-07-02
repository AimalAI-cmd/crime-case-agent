class ScriptWriter:

    def write_script(self, research):

        title = research["title"]
        summary = research["summary"]

        script = f"""
Title: {title}

Introduction

{summary}

Timeline

"""

        for event in research["timeline"]:
            script += f"- {event}\n"

        script += "\nInteresting Facts\n"

        for fact in research["interesting_facts"]:
            script += f"- {fact}\n"

        return script