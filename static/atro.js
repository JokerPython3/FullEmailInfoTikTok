document.querySelectorAll('pre').forEach(item => {
    item.addEventListener('click', () => {
        navigator.clipboard.writeText(item.innerText).then(() => {
            alert("done copy ");
        });
    });
});
