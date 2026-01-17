import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def review_code(code: str, language: str):
    prompt = f"""
You are a senior software engineer.

Review the following {language} code.
Focus on:
- Syntax errors
- Runtime errors
- Best practices
- Improvements

Code:
```{language}
{code}

Respond clearly in bullet points.
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.2
                }
            },
            timeout=120
        )

        data = response.json()
        return data.get("response", "No response from model.")

    except Exception as e:
        return f"Error contacting AI model: {e}"