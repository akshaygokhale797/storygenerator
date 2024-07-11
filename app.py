from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Check to see if program is reading variable
print(f"API Key: {os.getenv('OPENAI_API_KEY')}")

app = Flask(__name__)

def generate_story(prompt):
    response = openai.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to generate creative stories."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo",
        max_tokens=500
    )
    content = response.choices[0].message.content.strip()
    return content

@app.route('/', methods=['GET', 'POST'])
def home():
    story = ""
    if request.method == 'POST':
        prompt = request.form['prompt']
        story = generate_story(prompt)
    return render_template('index.html', story=story)

if __name__ == '__main__':
    app.run(debug=True)
