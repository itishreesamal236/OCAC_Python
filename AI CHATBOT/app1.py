import chainlit as cl
import google.generativeai as genai
import os

# Set up Google API Key
os.environ['GOOGLE_API_KEY'] = 'AIzaSyChQlDgvAFkfA8GKV4j1kcgLHrJZjnR31w'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Function to generate content using the GenerativeModel
def generate_story(prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text

@cl.on_message
async def on_message(message):
    prompt = message.content  # Correct way to access the text content of the message
    if prompt:
        result = generate_story(prompt)
        await cl.Message(content=result).send()
    else:
        await cl.Message(content="Please enter a prompt before generating.").send()

if __name__ == "__main__":
    cl.run()