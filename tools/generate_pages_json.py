import os
import json
import re
from datetime import datetime

# ============================================================
# FLOW / M-OS-R SEARCH INDEX GENERATOR
# Version 2.0
#
# Builds a rich local search index for the entire repository.
# No external APIs. No internet connection required.
# ============================================================

# ------------------------------------------------------------
# ROOT DIRECTORY
# ------------------------------------------------------------
# The script is located in:
#
# flowmosr/
# ├── tools/
# │   └── generate_pages_json.py
# └── ...
#
# Therefore the repository root is one level above this script.
# ------------------------------------------------------------

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

OUTPUT_FILE = os.path.join(ROOT_DIR, "pages.json")


# ------------------------------------------------------------
# FOLDERS TO SKIP
# ------------------------------------------------------------

SKIP_DIRS = {
    ".git",
    ".github",
    "tools",
    "annex",
    "node_modules",
    "__pycache__",
}


# ------------------------------------------------------------
# COMMON WORDS TO REMOVE FROM KEYWORDS
# ------------------------------------------------------------

STOPWORDS = {
    # English
    "the", "and", "of", "to", "in", "for", "a", "an",
    "is", "on", "with", "from", "by", "as", "at", "or",
    "this", "that", "it", "are", "be", "not", "will",
    "can", "how", "what", "why", "when", "where",

    # Swedish
    "och", "att", "det", "som", "en", "ett", "den", "de",
    "för", "på", "av", "till", "med", "är", "inte", "om",
    "har", "kan", "ska", "ett", "denna", "detta", "hur",
    "vad", "varför", "när", "där", "från",

    # Technical noise
    "md",
    "readme",
    "document",
    "file",
    "version",
    "status",
}


# ------------------------------------------------------------
# LANGUAGE DETECTION
# ------------------------------------------------------------

SWEDISH_MARKERS = {
    "och", "att", "det", "som", "för", "inte",
    "är", "med", "en", "ett", "den", "de",
    "på", "av", "till", "har", "kan"
}

ENGLISH_MARKERS = {
    "the", "and", "that", "this", "with", "for",
    "not", "are", "from", "have", "can", "will",
    "of", "to", "in"
}


def detect_language(text):
    """
    Very simple heuristic language detection.
    Returns: sv, en, mixed, or unknown.
    """

    words = set(
        word.lower()
        for word in re.findall(r"\b[a-zA-ZåäöÅÄÖ]+\b", text)
    )

    swedish_score = len(words & SWEDISH_MARKERS)
    english_score = len(words & ENGLISH_MARKERS)

    if swedish_score == 0 and english_score == 0:
        return "unknown"

    if swedish_score > english_score * 1.5:
        return "sv"

    if english_score > swedish_score * 1.5:
        return "en"

    return "mixed"


# ------------------------------------------------------------
# FRONTMATTER
# ------------------------------------------------------------

def extract_frontmatter(content):
    """
    Extracts simple YAML-like frontmatter.

    Example:

    ---
    title: "Example"
    description: "Description"
    tags: [flow, governance]
    keywords: [lotus, rotation]
    ---
    """

    frontmatter = {}

    match = re.match(
        r"^---\s*(.*?)\s*---",
        content,
        re.DOTALL
    )

    if not match:
        return frontmatter

    fm_text = match.group(1)

    for line in fm_text.splitlines():

        if ":" not in line:
            continue

        key, value = line.split(":", 1)

        key = key.strip().lower()
        value = value.strip()

        # Remove quotation marks
        value = value.strip("\"'")

        # Handle simple arrays
        if value.startswith("[") and value.endswith("]"):

            value = value[1:-1]

            values = [
                item.strip().strip("\"'")
                for item in value.split(",")
                if item.strip()
            ]

            frontmatter[key] = values

        else:
            frontmatter[key] = value

    return frontmatter


# ------------------------------------------------------------
# TITLE EXTRACTION
# ------------------------------------------------------------

def extract_title(content, filename):

    frontmatter = extract_frontmatter(content)

    if frontmatter.get("title"):
        return frontmatter["title"]

    # First H1
    h1_match = re.search(
        r"^#\s+(.+?)\s*$",
        content,
        re.MULTILINE
    )

    if h1_match:
        return h1_match.group(1).strip()

    # Fallback to filename
    title = os.path.splitext(filename)[0]

    title = title.replace("_", " ")
    title = title.replace("-", " ")

    return title.strip()


# ------------------------------------------------------------
# HEADING EXTRACTION
# ------------------------------------------------------------

def extract_headings(content):

    headings = []

    for match in re.finditer(
        r"^(#{1,3})\s+(.+?)\s*$",
        content,
        re.MULTILINE
    ):

        level = len(match.group(1))
        text = match.group(2).strip()

        headings.append({
            "level": level,
            "text": text
        })

    return headings


# ------------------------------------------------------------
# TEXT CLEANING
# ------------------------------------------------------------

def clean_markdown(text):

    # Remove frontmatter
    text = re.sub(
        r"^---\s*.*?\s*---",
        "",
        text,
        flags=re.DOTALL
    )

    # Remove code blocks
    text = re.sub(
        r"```.*?```",
        " ",
        text,
        flags=re.DOTALL
    )

    # Remove HTML
    text = re.sub(
        r"<[^>]+>",
        " ",
        text
    )

    # Images
    text = re.sub(
        r"!\[.*?\]\(.*?\)",
        " ",
        text
    )

    # Links: keep link text
    text = re.sub(
        r"\[([^\]]+)\]\([^)]+\)",
        r"\1",
        text
    )

    # Markdown emphasis
    text = re.sub(
        r"[*_`~]",
        "",
        text
    )

    # Blockquotes
    text = re.sub(
        r"^\s*>\s?",
        "",
        text,
        flags=re.MULTILINE
    )

    # Excess whitespace
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ------------------------------------------------------------
# DESCRIPTION EXTRACTION
# ------------------------------------------------------------

def extract_description(content, title):

    frontmatter = extract_frontmatter(content)

    if frontmatter.get("description"):
        return str(frontmatter["description"])[:500]

    cleaned = clean_markdown(content)

    # Remove title if it starts the text
    if cleaned.startswith(title):
        cleaned = cleaned[len(title):].strip()

    # Try to find a meaningful sentence
    sentences = re.split(
        r"(?<=[.!?])\s+",
        cleaned
    )

    meaningful = []

    for sentence in sentences:

        sentence = sentence.strip()

        if len(sentence) < 40:
            continue

        meaningful.append(sentence)

        if len(" ".join(meaningful)) >= 300:
            break

    description = " ".join(meaningful)

    if not description:
        description = cleaned[:300]

    return description[:500]


# ------------------------------------------------------------
# TOKEN EXTRACTION
# ------------------------------------------------------------

def extract_tokens(text):

    words = re.findall(
        r"\b[a-zA-ZåäöÅÄÖ][a-zA-ZåäöÅÄÖ0-9'-]{2,}\b",
        text.lower()
    )

    tokens = []

    for word in words:

        word = word.strip("-_'")

        if not word:
            continue

        if word in STOPWORDS:
            continue

        tokens.append(word)

    return tokens


# ------------------------------------------------------------
# KEYWORD GENERATION
# ------------------------------------------------------------

def generate_keywords(title, path, headings, frontmatter, content):

    sources = []

    sources.append(title)
    sources.append(path)

    for heading in headings:
        sources.append(heading["text"])

    # Frontmatter
    for key in ["tags", "keywords"]:

        value = frontmatter.get(key, [])

        if isinstance(value, list):
            sources.extend(value)

        elif isinstance(value, str):
            sources.append(value)

    # Extract tokens
    tokens = []

    for source in sources:
        tokens.extend(extract_tokens(source))

    # Add important content terms
    content_tokens = extract_tokens(content)

    # Count frequency
    frequency = {}

    for token in content_tokens:

        frequency[token] = frequency.get(token, 0) + 1

    # Add frequent terms
    frequent_terms = [
        word
        for word, count in frequency.items()
        if count >= 3
    ]

    tokens.extend(frequent_terms)

    # Remove duplicates while preserving order
    unique = []

    seen = set()

    for token in tokens:

        if token not in seen:

            seen.add(token)
            unique.append(token)

    return unique[:100]


# ------------------------------------------------------------
# DOCUMENT LAYER
# ------------------------------------------------------------

def detect_layer(path):

    parts = path.split("/")

    if not parts:
        return "root"

    first = parts[0].lower()

    layer_map = {

        "00_core": "core",
        "01_principles": "principles",
        "02_documents": "documents",
        "03_governance": "governance",
        "04_simulations": "simulations",
        "05_anti_capture": "anti-capture",
        "06_justice": "justice",
        "07_economics": "economics",
        "08_environmental": "environmental",
        "09_implementation": "implementation",
        "10_svenska": "swedish",
        "11_flowstarterpack": "starter-pack",
        "ethos": "ethos",
        "identity": "identity",
        "guides": "guides",
        "reflections": "reflections",
        "structure_in_flow": "structure",
        "compostandgrowth": "archive"

    }

    return layer_map.get(first, first)


# ------------------------------------------------------------
# INTERNAL LINKS
# ------------------------------------------------------------

def extract_internal_links(content):

    links = []

    for match in re.finditer(
        r"\]\(([^)]+\.md(?:#[^)]*)?)\)",
        content,
        re.IGNORECASE
    ):

        link = match.group(1)

        # Remove anchors
        link = link.split("#")[0]

        links.append(link)

    return sorted(set(links))


# ------------------------------------------------------------
# SEARCH TEXT
# ------------------------------------------------------------

def build_search_text(
    title,
    path,
    description,
    headings,
    keywords,
    content
):

    heading_text = " ".join(
        heading["text"]
        for heading in headings
    )

    keyword_text = " ".join(keywords)

    return " ".join([
        title,
        path,
        description,
        heading_text,
        keyword_text,
        content
    ])


# ============================================================
# BUILD INDEX
# ============================================================

pages = []

print("🌊 Building Flow search index...")
print(f"📁 Repository: {ROOT_DIR}")
print()


for dirpath, dirnames, filenames in os.walk(ROOT_DIR):

    # Remove skipped directories from traversal
    dirnames[:] = [
        dirname
        for dirname in dirnames
        if dirname not in SKIP_DIRS
    ]

    # Sort directories
    dirnames.sort(key=str.lower)

    # Sort files
    filenames = sorted(
        filenames,
        key=lambda name: (
            name.lower() != "readme.md",
            name.lower()
        )
    )

    for filename in filenames:

        if not filename.lower().endswith(".md"):
            continue

        full_path = os.path.join(
            dirpath,
            filename
        )

        try:

            with open(
                full_path,
                "r",
                encoding="utf-8"
            ) as file:

                raw_content = file.read()

            relative_path = os.path.relpath(
                full_path,
                ROOT_DIR
            ).replace("\\", "/")

            frontmatter = extract_frontmatter(
                raw_content
            )

            title = extract_title(
                raw_content,
                filename
            )

            headings = extract_headings(
                raw_content
            )

            description = extract_description(
                raw_content,
                title
            )

            clean_content = clean_markdown(
                raw_content
            )

            keywords = generate_keywords(
                title,
                relative_path,
                headings,
                frontmatter,
                clean_content
            )

            language = detect_language(
                clean_content
            )

            internal_links = extract_internal_links(
                raw_content
            )

            search_text = build_search_text(
                title,
                relative_path,
                description,
                headings,
                keywords,
                clean_content
            )

            words = re.findall(
                r"\b[\wåäöÅÄÖ'-]+\b",
                clean_content
            )

            page = {

                "title": title,

                "path": relative_path,

                "layer": detect_layer(
                    relative_path
                ),

                "language": language,

                "description": description,

                "headings": headings,

                "keywords": keywords,

                "internal_links": internal_links,

                "word_count": len(words),

                "content": clean_content,

                "search_text": search_text,

                "last_updated": datetime.now().isoformat()[:10]

            }

            pages.append(page)

        except Exception as error:

            print(
                f"⚠️ Error processing {relative_path}: {error}"
            )


# ============================================================
# SORT
# ============================================================

pages.sort(
    key=lambda page: (
        page["layer"],
        page["path"].lower()
    )
)


# ============================================================
# WRITE INDEX
# ============================================================

output = {

    "version": "2.0",

    "generated_at": datetime.now().isoformat(),

    "document_count": len(pages),

    "layers": sorted(
        set(
            page["layer"]
            for page in pages
        )
    ),

    "pages": pages

}


with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        output,
        file,
        indent=2,
        ensure_ascii=False
    )


print()
print("✅ Flow search index generated!")
print(f"📚 Documents indexed: {len(pages)}")
print(f"🧭 Layers detected: {len(output['layers'])}")
print(f"💾 Output: {OUTPUT_FILE}")
print()
print("🌊 The archive is now searchable by:")
print("   • titles")
print("   • headings")
print("   • keywords")
print("   • descriptions")
print("   • full document content")
print("   • internal document links")
print("   • language")
print("   • Flow layer")