import json
import requests

from config.settings import (
    AI_PROVIDER,
    AI_MODEL,
    OPENROUTER_API_KEY
)


class AIProvider:

    def __init__(self):
        self.provider = AI_PROVIDER
        self.model = AI_MODEL

    def generate(self, prompt):

        print("\n========== AI Provider ==========")
        print(f"Provider : {self.provider}")
        print(f"Model    : {self.model}")
        print("=================================\n")

        if not OPENROUTER_API_KEY:
            raise Exception("OpenRouter API Key not found.")

        print("Connecting to OpenRouter...\n")

        print("========== FINAL PROMPT ==========")
        print(prompt)
        print("==================================\n")

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "CrimeCase AI Studio"
        }

        data = {
            "model": self.model,
            "temperature": 0,
            "max_tokens": 1500,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Always follow the user's instructions exactly. "
                        "Return ONLY valid JSON. "
                        "Never use markdown. "
                        "Never use code blocks."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        try:

            print("Sending POST request...")

            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )

            print("POST request completed.")
            print(f"HTTP Status Code: {response.status_code}")

            try:
                result = response.json()
            except ValueError:
                raise Exception(
                    f"Server did not return JSON.\n\n"
                    f"Response:\n{response.text}"
                )

            print("\n========== API Response ==========")
            print(result)
            print("==================================\n")

            if response.status_code != 200:
                raise Exception(
                    f"HTTP {response.status_code}\n\n{result}"
                )

            if "error" in result:
                raise Exception(result["error"]["message"])

            if "choices" not in result:
                raise Exception(
                    f"Unexpected API response:\n{result}"
                )

            content = result["choices"][0]["message"]["content"]

            print("\n========== RAW AI CONTENT ==========")
            print(content)
            print("====================================\n")

            # Remove markdown if present
            content = content.replace("```json", "")
            content = content.replace("```", "")
            content = content.strip()

            # Extract JSON if extra text exists
            start = content.find("{")
            end = content.rfind("}")

            if start != -1 and end != -1:
                content = content[start:end + 1]

            # Validate JSON before returning
            json.loads(content)

            return content

        except json.JSONDecodeError as e:
            raise Exception(
                f"AI returned invalid JSON.\n\n"
                f"JSON Error: {e}\n\n"
                f"Response:\n{content}"
            )

        except requests.exceptions.Timeout:
            raise Exception(
                "OpenRouter request timed out after 30 seconds."
            )

        except requests.exceptions.ConnectionError:
            raise Exception(
                "Could not connect to OpenRouter."
            )

        except requests.exceptions.RequestException as e:
            raise Exception(f"Network Error: {e}")

        except Exception as e:
            raise Exception(str(e))