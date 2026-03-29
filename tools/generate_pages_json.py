import os
import json

# Root directory för ditt repo
ROOT_DIR = "../"  # justera beroende på var du kör scriptet

pages = []

for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
    # Hoppa över .git, js, css och .nojekyll
    if any(skip in dirpath for skip in ['.git', 'js', 'css', 'tools']):
        continue

    # Sortera filer så README kommer först
    filenames = sorted(filenames, key=lambda x: (x.lower() != 'readme.md', x.lower()))

    for fname in filenames:
        if fname.lower().endswith('.md'):
            # Skapa title från filnamn
            title = fname.replace('.md', '')
            # Skapa path relativt ROOT_DIR
            rel_path = os.path.relpath(os.path.join(dirpath, fname), ROOT_DIR).replace("\\", "/")
            pages.append({"title": title, "path": rel_path})

# Skriv till pages.json i root
with open(os.path.join(ROOT_DIR, 'pages.json'), 'w', encoding='utf-8') as f:
    json.dump(pages, f, indent=2, ensure_ascii=False)

print(f"Generated pages.json with {len(pages)} entries!")