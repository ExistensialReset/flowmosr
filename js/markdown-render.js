// Enkel Markdown-render i browser
document.querySelectorAll('nav a').forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    const mdFile = e.target.dataset.md;

    fetch(mdFile)
      .then(response => response.text())
      .then(md => {
        // Enkel konvertering: rubriker och stycken
        let html = md
          .replace(/^# (.*$)/gim, '<h1>$1</h1>')
          .replace(/^## (.*$)/gim, '<h2>$1</h2>')
          .replace(/^### (.*$)/gim, '<h3>$1</h3>')
          .replace(/\*\*(.*)\*\*/gim, '<strong>$1</strong>')
          .replace(/\*(.*)\*/gim, '<em>$1</em>')
          .replace(/\n$/gim, '<br>');

        document.getElementById('content').innerHTML = html;
      });
  });
});