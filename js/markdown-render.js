// Dynamiskt hämta och rendera alla Markdown-filer från repo
async function init() {
  const nav = document.getElementById("nav");
  const content = document.getElementById("content");

  const owner = "ExistensialReset";
  const repo = "flowmosr";
  const branch = "main";

  // Hämta alla filer via GitHub API
  const url = `https://api.github.com/repos/${owner}/${repo}/git/trees/${branch}?recursive=1`;
  const response = await fetch(url);
  const data = await response.json();

  const mdFiles = data.tree.filter(f => f.path.endsWith(".md"));

  // Bygg navigation
  mdFiles.forEach(file => {
    const li = document.createElement("li");
    const a = document.createElement("a");
    a.href = "#";
    a.textContent = file.path.replace(/.*\//, '').replace('.md', '');
    a.dataset.md = file.path;

    a.addEventListener("click", async (e) => {
      e.preventDefault();
      const rawUrl = `https://raw.githubusercontent.com/${owner}/${repo}/${branch}/${file.path}`;
      const mdResponse = await fetch(rawUrl);
      const mdText = await mdResponse.text();
      content.innerHTML = renderMarkdown(mdText);
      window.scrollTo(0,0);
    });

    li.appendChild(a);
    nav.appendChild(li);
  });

  // Ladda README.md automatiskt på startsidan
  const readme = mdFiles.find(f => f.path.toLowerCase().endsWith("readme.md"));
  if (readme) {
    const rawUrl = `https://raw.githubusercontent.com/${owner}/${repo}/${branch}/${readme.path}`;
    const mdResponse = await fetch(rawUrl);
    const mdText = await mdResponse.text();
    content.innerHTML = renderMarkdown(mdText);
  }
}

// Enkel Markdown → HTML
function renderMarkdown(md) {
  return md
    .replace(/^### (.*$)/gim, '<h3>$1</h3>')
    .replace(/^## (.*$)/gim, '<h2>$1</h2>')
    .replace(/^# (.*$)/gim, '<h1>$1</h1>')
    .replace(/\*\*(.*)\*\*/gim, '<strong>$1</strong>')
    .replace(/\*(.*)\*/gim, '<em>$1</em>')
    .replace(/`(.*)`/gim, '<code>$1</code>')
    .replace(/\n$/gim, '<br>');
}

init();