// Dynamiskt läs in alla Markdown-filer i repo och skapa navigation
async function init() {
  const nav = document.getElementById("nav");
  const content = document.getElementById("content");

  // Dynamiskt generera lista med alla .md-filer
  // Här använder vi en "index.json" som listar alla Markdown-filer (automatiskt uppdaterad)
  const response = await fetch("index.json");
  const files = await response.json();

  files.forEach(file => {
    const li = document.createElement("li");
    const a = document.createElement("a");
    a.href = "#";
    a.textContent = file.title;
    a.dataset.md = file.path;
    a.addEventListener("click", async (e) => {
      e.preventDefault();
      const mdResponse = await fetch(file.path);
      const mdText = await mdResponse.text();
      content.innerHTML = renderMarkdown(mdText);
    });
    li.appendChild(a);
    nav.appendChild(li);
  });
}

// Enkel Markdown → HTML funktion
function renderMarkdown(md) {
  let html = md
    .replace(/^### (.*$)/gim, '<h3>$1</h3>')
    .replace(/^## (.*$)/gim, '<h2>$1</h2>')
    .replace(/^# (.*$)/gim, '<h1>$1</h1>')
    .replace(/\*\*(.*)\*\*/gim, '<strong>$1</strong>')
    .replace(/\*(.*)\*/gim, '<em>$1</em>')
    .replace(/\n$/gim, '<br>');
  return html;
}

init();