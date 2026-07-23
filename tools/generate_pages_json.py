import os
import json
import re
from datetime import datetime

# Root directory
ROOT_DIR = "../"  # Justera vid behov

pages = []

def extract_frontmatter_and_content(content):
    """Extraherar YAML-frontmatter och första rubriken/beskrivning"""
    frontmatter = {}
    description = ""
    title = ""
    
    # Hitta frontmatter
    fm_match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        # Enkel YAML-parsing (title, description, tags, keywords)
        for line in fm_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip().strip('"\'')
                if key == 'title':
                    title = value
                elif key == 'description':
                    description = value
                elif key in ['tags', 'keywords']:
                    frontmatter[key] = [v.strip() for v in value.split(',')] if ',' in value else [value]
    
    # Fallback: första H1 som title
    if not title:
        h1_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
        if h1_match:
            title = h1_match.group(1).strip()
    
    # Fallback description från första stycket
    if not description:
        para_match = re.search(r'^(?!#)(.+?)\n', content, re.MULTILINE)
        if para_match:
            description = para_match.group(1).strip()[:200]
    
    return {
        "title": title or "Untitled",
        "description": description,
        "frontmatter": frontmatter
    }

for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
    # Skip irrelevant folders
    if any(skip in dirpath for skip in ['.git', 'js', 'css', '.github', 'tools', 'annex']):
        continue
    
    filenames = sorted(filenames, key=lambda x: (x.lower() != 'readme.md', x.lower()))
    
    for fname in filenames:
        if fname.lower().endswith('.md'):
            full_path = os.path.join(dirpath, fname)
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                meta = extract_frontmatter_and_content(content)
                
                rel_path = os.path.relpath(full_path, ROOT_DIR).replace("\\", "/")
                
                # Generera keywords automatiskt från filnamn och title
                auto_keywords = [word.lower() for word in re.findall(r'\w+', meta['title'] + " " + rel_path)]
                
                pages.append({
                    "title": meta['title'],
                    "path": rel_path,
                    "description": meta['description'],
                    "keywords": auto_keywords + meta.get('frontmatter', {}).get('keywords', []),
                    "last_updated": datetime.now().isoformat()[:10]  # Kan förbättras med git log senare
                })
            except Exception as e:
                print(f"Error processing {fname}: {e}")

# Skriv till pages.json
with open(os.path.join(ROOT_DIR, 'pages.json'), 'w', encoding='utf-8') as f:
    json.dump({"pages": pages, "generated_at": datetime.now().isoformat()}, f, indent=2, ensure_ascii=False)

print(f"✅ Generated pages.json with {len(pages)} entries! Sökbarhet förbättrad.")