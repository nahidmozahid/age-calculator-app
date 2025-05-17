document.getElementById('dobForm').addEventListener('submit', function(e) {
    const dobInput = this.elements['dob'].value;
    if (!dobInput) {
        e.preventDefault();
        alert('Please enter your date of birth!');
    }
});
