/* Funzione che tronca il nome del file se troppo lungo*/
function truncateFilename(name, maxLength) {
    if (name.length <= maxLength) return name;

    const extIndex = name.lastIndexOf(".");
    if (extIndex === -1) {
        return name.slice(0, maxLength - 1) + "…";
    }

    const ext = name.slice(extIndex);
    const base = name.slice(0, maxLength - ext.length - 1);

    return base + "…" + ext;
}

/* Rimuove il formato di input dal menu */
document.querySelectorAll('input[type="file"]').forEach(input => {
    input.addEventListener('change', () => {
        const file = input.files[0];
        if (!file) return;

        const ext = file.name.split('.').pop().toLowerCase();
        const form = input.closest('form');
        const select = form.querySelector('.format-select');

        if (select) {
            Array.from(select.options).forEach(opt => {
                if (opt.value.toLowerCase() === ext || opt.text.toLowerCase() === ext) {
                    opt.style.display = 'none';
                    if (opt.selected) select.selectedIndex = 0;
                } else {
                    opt.style.display = 'block';
                }
            });
        }
    });
});

/* Drag & drop file */
document.querySelectorAll('.file-drop').forEach(drop => {
    const input = drop.querySelector('input[type="file"]');
    const span = drop.querySelector('span');

    function updateFileName() {
        if (input.files.length > 0) {
            const file = input.files[0];
            const accept = input.accept.split(',').map(a => a.trim());
            const ext = file.name.split('.').pop().toLowerCase();
            let valid = false;

            // controlla i tipi MIME generici video/*, image/* e le estensioni .pdf
            for (let a of accept) {
                if (a.endsWith('/*')) {
                    const typePrefix = a.split('/')[0];
                    if (file.type.startsWith(typePrefix + '/')) valid = true;
                } else if (a.startsWith('.')) {
                    if (ext === a.slice(1).toLowerCase()) valid = true;
                } else {
                    if (file.type === a) valid = true;
                }
            }

            if (!valid) {
                alert(`Tipo file non valido per questa sezione!\nHai selezionato: ${file.name}`);
                input.value = '';
                span.textContent = 'Trascina il file qui o clicca per selezionarlo';
                span.style.color = '#aaa';
                return false;
            }

            span.textContent = truncateFilename(file.name, 28);
            span.title = file.name;
            span.style.color = '#fff';
            return true;
        } else {
            span.textContent = 'Trascina il file qui o clicca per selezionarlo';
            span.style.color = '#aaa';
            return false;
        }
    }

    // dragover / dragleave per evidenziare il box
    drop.addEventListener('dragover', (e) => {
        e.preventDefault();
        drop.classList.add('dragover');
    });

    drop.addEventListener('dragleave', () => drop.classList.remove('dragover'));

    drop.addEventListener('drop', (e) => {
        e.preventDefault();
        drop.classList.remove('dragover');
        if (e.dataTransfer.files.length > 0) {
            const dt = new DataTransfer();
            dt.items.add(e.dataTransfer.files[0]);
            input.files = dt.files;

            if (!updateFileName()) return; // file non valido
            input.dispatchEvent(new Event('change')); // aggiorna menu a tendina
        }
    });

    input.addEventListener('change', updateFileName);

    // intercetta submit del form per sicurezza
    const form = input.closest('form');
    form.addEventListener('submit', (e) => {
        if (!updateFileName()) {
            e.preventDefault(); // blocca submit se file non valido
        }
    });
});

/* Funzione che mostra lo spinner */
document.querySelectorAll('.form').forEach(form => {
    form.addEventListener('submit', (e) => {
        e.preventDefault();

        // Mostra spinner
        const spinner = document.getElementById('loading-spinner');
        spinner.style.display = 'flex';

        const formData = new FormData(form);
        const action = form.getAttribute('action');

        const xhr = new XMLHttpRequest();
        xhr.open('POST', action, true);

        xhr.onreadystatechange = () => {
            if (xhr.readyState === 4) {
                spinner.style.display = 'none'; // nascondi spinner

                if (xhr.status === 200) {
                    const blob = new Blob([xhr.response], {type: xhr.getResponseHeader('Content-Type')});
                    const url = URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    const filename = xhr.getResponseHeader('Content-Disposition')?.split('filename=')[1] || 'file_output';
                    a.download = filename.replace(/"/g, '');
                    a.click();
                    URL.revokeObjectURL(url);
                } else {
                    alert('Errore nella conversione!');
                }
            }
        };

        xhr.responseType = 'blob';
        xhr.send(formData);
    });
});
