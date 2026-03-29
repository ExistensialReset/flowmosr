// main.js
document.addEventListener("DOMContentLoaded", async () => {
  const sidebar = document.getElementById("sidebar");
  const content = document.getElementById("content");

  // Hämta pages.json
  let pages;
  try {
    const res = await fetch("pages.json");
    pages = await res.json();
  } catch (err) {
    content.innerHTML = `<p style="color:red;">Failed to load pages.json: ${err}</p>`;
    return;
  }

  // Gruppera filer per mapp
  const folders = {};
  pages.forEach(page => {
    const pathParts = page.path.split("/");
    const folder = pathParts.length > 1 ? pathParts[0] : "root";
    if (!folders[folder]) folders[folder] = [];
    folders[folder].push(page);
  });

  // Skapa sidebar
  for (const [folder, files] of Object.entries(folders)) {
    const folderEl = document.createElement("div");
    folderEl.className = "folder";

    const folderTitle = document.createElement("div");
    folderTitle.className = "folder-title";
    folderTitle.textContent = folder === "root" ? "Home" : folder;
    folderEl.appendChild(folderTitle);

    const fileList = document.createElement("ul");
    files
      .sort((a, b) => {
        // README först
        if (a.title.toLowerCase() === "readme") return -1;
        if (b.title.toLowerCase() === "readme") return 1;
        return a.title.localeCompare(b.title);
      })
      .forEach(file => {
        const li = document.createElement("li");
        const link = document.createElement("a");
        link.href = "#";
        link.textContent = file.title;
        link.addEventListener("click", () => loadMarkdown(file.path));
        li.appendChild(link);
        fileList.appendChild(li);
      });

    folderEl.appendChild(fileList);
    sidebar.appendChild(folderEl);
  }

  // Funktion för att ladda markdown
  async function loadMarkdown(path) {
    content.innerHTML = "<p>Loading content...</p>";
    try {
      const res = await fetch(path);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const mdText = await res.text();

      // Rendera Markdown (simple)
      content.innerHTML = marked.parse(mdText);
    } catch (err) {
      content.innerHTML = `<p style="color:red;">Failed to load ${path}: ${err}</p>`;
    }
  }

  // Ladda root README först
  const rootReadme = pages.find(p => p.path.toLowerCase() === "readme.md");
  if (rootReadme) loadMarkdown(rootReadme.path);
});