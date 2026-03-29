async function loadPages() {
  try {
    const res = await fetch('pages.json');
    const pages = await res.json();

    const sidebar = document.getElementById('sidebar');
    const content = document.getElementById('content');

    function createSidebar(pages) {
      let html = '';
      const folders = {};

      pages.forEach(p => {
        const folder = p.path.split('/')[0];
        if (!folders[folder]) folders[folder] = [];
        folders[folder].push(p);
      });

      for (const folder of Object.keys(folders).sort()) {
        html += `<div class="folder">${folder}</div><ul>`;
        folders[folder].sort((a,b)=>a.title.localeCompare(b.title)).forEach(file => {
          html += `<li><a href="#" data-path="${file.path}">${file.title}</a></li>`;
        });
        html += `</ul>`;
      }

      sidebar.innerHTML = html;

      // Add click events
      sidebar.querySelectorAll('a').forEach(a => {
        a.addEventListener('click', async e => {
          e.preventDefault();
          const mdPath = a.getAttribute('data-path');
          const mdRes = await fetch(mdPath);
          const mdText = await mdRes.text();
          content.innerHTML = `<pre>${mdText}</pre>`; // Simple render, kan bytas mot markdown parser
        });
      });
    }

    createSidebar(pages);

    // Load root README.md by default
    const readmeRes = await fetch('README.md');
    const readmeText = await readmeRes.text();
    content.innerHTML = `<pre>${readmeText}</pre>`;
    
  } catch(err) {
    console.error("Failed to load pages:", err);
    document.getElementById('content').innerText = "Failed to load content.";
  }
}

loadPages();