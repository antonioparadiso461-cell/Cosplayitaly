import os
import requests
import datetime
from openai import OpenAI

# Configurazione
REPO_OWNER = "antoniodarkv890-ai"
REPO_NAME = "Cosplayitaly890"

client = OpenAI()

def generate_content():
    prompt = "Scrivi un articolo lungo e appassionato per un blog di cosplay. Parla delle ultime tendenze, della dedizione dei fan e della bellezza dei costumi. Scrivilo in italiano, in prima persona come un fan esperto. Non menzionare che l'articolo o le foto sono creati da AI."
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def update_script_js(content, image_paths):
    today = datetime.date.today().strftime("%d %B %Y")
    images_html = "".join([f'<img src="{path}" alt="Cosplay">' for path in image_paths])
    
    new_post_html = f"""
        <article>
            <h2>{content.split('\\n')[0]}</h2>
            <p><strong>Data:</strong> {today}</p>
            {content.replace('\\n', '<p>')}
            <div class="cosplay-gallery">
                {images_html}
            </div>
        </article>
    """
    
    with open("script.js", "r") as f:
        lines = f.readlines()
    
    # Inserisce il nuovo post all'inizio
    for i, line in enumerate(lines):
        if 'const firstPost = `' in line:
            lines.insert(i, f"    const newPost = `{new_post_html}`;\n")
            break
            
    for i, line in enumerate(lines):
        if 'postsContainer.innerHTML = firstPost;' in line:
            lines[i] = line.replace('firstPost', 'newPost + firstPost')
            break
            
    with open("script.js", "w") as f:
        f.writelines(lines)

# Nota: In un ambiente GitHub Action reale, le immagini verrebbero generate via API
# e salvate nella cartella images/. Questo script è un template per l'Action.
