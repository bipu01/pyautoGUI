# gemini_analyzer.py

import google.generativeai as genai
import asyncio
import json
import base64
from typing import Optional, Union
from pathlib import Path


async def analyze_image_data(
        api_key: str,
        image_path: str,
        prompt: str = None
) -> Optional[dict]:

    """Analyzes image data using Gemini Vision API"""
    try:
        # Configure Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-pro")

        image_path = Path(image_path)

        image_file = genai.upload_file(str(image_path))

        # Use provided prompt or default
        if prompt is None:
            prompt = """I have provided you with image with the resolution of the image. the resolution of display is width=1680, height=1050 You just give me the position of comment button in the terms of x and y direction in json format in px like {
            "comment_button_position": {
            "x": 1400,          "y": 1000
            }
            }. Do not give any other response."""

        # Make API call
        response = await asyncio.to_thread(
            model.generate_content, [image_file, prompt]
        )

        # Parse response
        try:
            return json.loads(response.text)
        except json.JSONDecodeError:
            print("Failed to parse JSON response:", response.text)
            return None

    except Exception as e:
        print(f"Error analyzing image: {str(e)}")
        return None


# Example usage in this file (if run directly)
async def main(image_path:str, api_key: str, prompt: str = None) -> Optional[dict]:
    """Main function that can be called from other files"""
    return await analyze_image_data(api_key, image_path, prompt)


if __name__ == "__main__":
    # This code only runs if the file is run directly
    print("This module is meant to be imported")