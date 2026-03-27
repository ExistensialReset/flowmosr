async function init() {
  const nav = document.getElementById("nav");
  const content = document.getElementById("content");

  // Läs pages.json lokalt
  const response = await fetch("pages.json");
  const files = await response.json();

  // Bygg navigation
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
      window.scrollTo(0,0);
    });

    li.appendChild(a);
    nav.appendChild(li);
  });

  // Ladda README.md automatiskt
  const readme = files.find(f => f.title.toLowerCase() === "readme");
  if (readme) {
    const mdResponse = await fetch(readme.path);
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