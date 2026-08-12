import os
import requests
import datetime
import time
import json
from openai import OpenAI

# Configurazione
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_content():
    print("Generazione articolo...")
    prompt = "Scrivi un articolo lungo (almeno 500 parole) e appassionato per un blog di cosplay. Parla di un tema specifico del cosplay (es. la creazione di armature, il trucco, le fiere, l'interpretazione). Scrivilo in italiano, in prima persona come un fan esperto e caloroso. Usa un titolo accattivante come prima riga. Non menzionare assolutamente che l'articolo o le foto sono creati da AI."
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def generate_images():
    print("Generazione immagini...")
    image_paths = []
    prompts = [
        "Professional high-quality cosplay photo, intricate detail, cinematic lighting, 8k, masterpiece, Japanese anime style.",
        "Fantasy cosplay portrait, realistic textures, moody atmosphere, professional photography, high resolution.",
        "Action cosplay shot, dynamic pose, vibrant colors, magical effects, detailed background, professional studio lighting."
    ]
    
    if not os.path.exists("images"):
        os.makedirs("images")
        
    timestamp = int(time.time())
    for i, p in enumerate(prompts):
        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=p,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            image_url = response.data[0].url
            img_data = requests.get(image_url).content
            filename = f"images/cosplay_{timestamp}_{i}.png"
            with open(filename, 'wb') as handler:
                handler.write(img_data)
            image_paths.append(filename)
            print(f"Immagine {i+1} salvata: {filename}")
        except Exception as e:
            print(f"Errore generazione immagine {i}: {e}")
            
    return image_paths

def update_script_js(content, image_paths):
    print("Aggiornamento script.js...")
    today = datetime.date.today().strftime("%d %B %Y")
    
    paragraphs = content.split('\n')
    title = paragraphs[0].strip('# ')
    body = "".join([f'<p>{p.strip()}</p>' for p in paragraphs[1:] if p.strip()])
    
    new_post = {
        "title": title,
        "date": today,
        "content": body,
        "images": image_paths
    }
    
    with open("script.js", "r") as f:
        js_content = f.read()
    
    # Cerchiamo l'inizio dell'array blogPosts
    start_marker = "const blogPosts = ["
    if start_marker in js_content:
        parts = js_content.split(start_marker)
        # Inseriamo il nuovo post all'inizio dell'array
        new_post_json = json.dumps(new_post, indent=8)
        updated_js = parts[0] + start_marker + "\n        " + new_post_json + "," + parts[1]
        
        with open("script.js", "w") as f:
            f.write(updated_js)
            
if __name__ == "__main__":
    try:
        content = generate_content()
        images = generate_images()
        if content and images:
            update_script_js(content, images)
            print("Aggiornamento completato con successo.")
        else:
            print("Errore: contenuto o immagini mancanti.")
    except Exception as e:
        print(f"Errore durante l'esecuzione: {e}")
