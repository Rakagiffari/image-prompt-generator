PROMPT_STYLES = {
    "Detailed": """
Create a highly detailed image generation prompt based on the image.

Describe:
- main subject
- physical appearance
- clothing
- pose
- facial expression
- environment
- background
- composition
- camera angle
- lighting
- colors
- visual style
- important visual details

The generated prompt should be suitable for modern AI image generators.
Do not invent major visual elements that are not visible in the image.
""",

    "Photorealistic": """
Analyze the image and create a photorealistic image generation prompt.

Focus on:
- realistic subject appearance
- clothing
- pose
- environment
- natural lighting
- camera angle
- lens characteristics
- depth of field
- composition
- realistic textures

Preserve the visual information from the original image.
""",

    "Cinematic": """
Analyze the image and transform it into a cinematic image generation prompt.

Focus on:
- cinematic composition
- subject
- pose
- environment
- lighting
- color atmosphere
- camera angle
- lens
- depth of field
- dramatic visual details

Keep the main visual characteristics of the original image.
""",

    "Simple": """
Describe the image clearly and convert it into a concise AI image generation prompt.

Focus only on the most important visible elements.
"""
}


def build_instruction(style):
    return PROMPT_STYLES.get(
        style,
        PROMPT_STYLES["Detailed"]
    )
