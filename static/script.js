document.querySelector('.email').addEventListener('input', function () {
    this.style.boxShadow = this.value.length > 0 
        ? '0 0 8px #7efff5' 
        : 'none';
});
document.querySelector('form').addEventListener('submit', function (e) {
    const emailField = document.querySelector('.email');
    if (!emailField.value.includes('@')) {
        e.preventDefault();
        alert("ksj");
    }
});
