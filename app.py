import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API with the loaded API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini."""
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

# Update photo name here to match your actual file
files = [
  upload_to_gemini("santa.png", mime_type="image/png"),  # Updated to "santa.png"
]

chat_session = model.start_chat(
  history=[{
    "role": "user",
    "parts": [
      files[0],
      "You are Santa Claus, write a letter back for this kid.",
    ],
  }]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)
