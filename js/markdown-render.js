// main.js

fetch('pages.json')
  .then(res => res.json())
  .then(pages => {
    const sidebar = document.getElementById('sidebar');
    if (!sidebar) return;

    // Skapa ett objekt som grupperar efter folder
    const tree = {};

    pages.forEach(page => {
      const parts = page.path.split('/');
      if (parts.length === 2) { // folder/file.md
        const folder = parts[0];
        if (!tree[folder]) tree[folder] = [];
        tree[folder].push(page);
      } else if (parts.length > 2) { // nested
        let current = tree;
        for (let i = 0; i < parts.length - 1; i++) {
          if (!current[parts[i]]) current[parts[i]] = {};
          current = current[parts[i]];
        }
        if (!current._files) current._files = [];
        current._files.push({ title: parts[parts.length-1].replace(/\.md$/, ''), path: page.path });
      }
    });

    function createList(obj, parent) {
      const ul = document.createElement('ul');
      for (const key of Object.keys(obj)) {
        if (key === '_files') {
          obj._files.forEach(f => {
            const li = document.createElement('li');
            const a = document.createElement('a');
            a.href = f.path;
            a.textContent = f.title;
            li.appendChild(a);
            ul.appendChild(li);
          });
          continue;
        }
        const li = document.createElement('li');
        const span = document.createElement('span');
        span.textContent = key;
        li.appendChild(span);
        li.appendChild(createList(obj[key], li));
        ul.appendChild(li);
      }
      return ul;
    }

    sidebar.appendChild(createList(tree));
  })
  .catch(err => {
    console.error('Failed to load pages.json', err);
  });