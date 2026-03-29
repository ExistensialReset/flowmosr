
fetch('./pages.json')
  .then(res => res.json())
  .then(pages => {
    // Ta bort "./" i path
    pages.forEach(p => {
      if (p.path.startsWith("./")) p.path = p.path.slice(2);
    });

    sidebar.innerHTML = "";

    folderOrder.forEach(folder => {
      const folderDiv = document.createElement("div");
      folderDiv.className = "folder";

      const folderTitle = document.createElement("h3");
      folderTitle.textContent = folder;
      folderDiv.appendChild(folderTitle);

      const fileList = document.createElement("ul");
      fileList.className = "file-list";

      const files = pages.filter(p => p.path.startsWith(folder + "/"));

      files.forEach(file => {
        const li = document.createElement("li");
        const link = document.createElement("a");
        link.href = "#";
        link.textContent = file.title;

        link.onclick = (e) => {
          e.preventDefault();
          loadPage(file.path);
        };

        li.appendChild(link);
        fileList.appendChild(li);
      });

      folderDiv.appendChild(fileList);
      sidebar.appendChild(folderDiv);
    });

    // Ladda root README.md först om den finns
    fetch('README.md')
      .then(res => {
        if (res.ok) return res.text();
        else throw new Error("No root README.md");
      })
      .then(md => content.innerHTML = marked.parse(md))
      .catch(() => {
        // Om ingen root README, ladda första filen i första mappen
        const firstFolderFiles = pages.filter(p => p.path.startsWith(folderOrder[0] + "/"));
        if (firstFolderFiles.length > 0) loadPage(firstFolderFiles[0].path);
      });
  });
const folderOrder = [
  "00_core",
  "01_principles",
  "02_documents",
  "03_governance",
  "04_simulations",
  "05_facilitators",
  "06_justice",
  "07_technology",
  "08_environmental",
  "09_economics",
  "10_svenska"
];

const sidebar = document.getElementById("sidebar");
const content = document.getElementById("content");

// Ladda alla sidor
fetch('./pages.json')
  .then(res => res.json())
  .then(pages => {
    // Ta bort "./" i path
    pages.forEach(p => {
      if (p.path.startsWith("./")) p.path = p.path.slice(2);
    });

    sidebar.innerHTML = "";

    folderOrder.forEach(folder => {
      const folderDiv = document.createElement("div");
      folderDiv.innerHTML = `<h3>${folder}</h3>`;

      const files = pages.filter(p => p.path.startsWith(folder + "/"));

      files.forEach(file => {
        const link = document.createElement("a");
        link.href = "#";
        link.textContent = file.title;

        link.onclick = (e) => {
          e.preventDefault();
          loadPage(file.path);
        };

        folderDiv.appendChild(link);
      });

      sidebar.appendChild(folderDiv);
    });

    // Ladda första sidan i första foldern
    const firstFolderFiles = pages.filter(p => p.path.startsWith(folderOrder[0] + "/"));
    if (firstFolderFiles.length > 0) loadPage(firstFolderFiles[0].path);
  });

function loadPage(path) {
  fetch(path)
    .then(res => res.text())
    .then(md => {
      content.innerHTML = marked.parse(md);
    })
    .catch(() => {
      content.innerHTML = "❌ Could not load file: " + path;
    });
}