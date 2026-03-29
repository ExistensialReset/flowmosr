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

    // Ladda första sidan automatiskt
    if (pages.length > 0) {
      loadPage(pages[0].path);
    }
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