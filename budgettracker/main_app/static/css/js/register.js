document.addEventListener("DOMContentLoaded", function () {
    const usernameField = document.querySelector('#usernameField');
    const feedBackArea = document.querySelector('.invalid_feedback');
    const passwordField = document.querySelector('#passwordField');
    const showPasswordToggle = document.querySelector('.position-absolute');


    if (!usernameField || !feedBackArea|| !passwordField || !showPasswordToggle) {
        console.warn("Missing elements, please check your HTML.");
        return;
    }

    usernameField.addEventListener("keyup", (e) => {
        const usernameVal = e.target.value;

        usernameField.classList.remove('is-invalid');
        feedBackArea.style.display = 'none';

        if (usernameVal.length > 0) {
            fetch('/authentication/validate-username', {
                method: "POST",
                body: JSON.stringify({ username: usernameVal }),
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"), // Required in Django!
                }
            })
                .then((res) => {
                    console.log('Response status:', res.status); // Log the response status
                    return res.json();
                })
                .then((data) => {
                    console.log('Response data:', data);
           
                if (data.username_error) {
                    usernameField.classList.add('is-invalid');
                    feedBackArea.style.display = 'block';
                    feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
                }
            })
            .catch((error) => {
                console.error('Error:', error);

        });
    }
})
showPasswordToggle.addEventListener('click', () => {
    const type = passwordField.type === 'password' ? 'text' : 'password';
    passwordField.type = type;
    showPasswordToggle.textContent = type === 'password' ? 'Show' : 'Hide';
});

// CSRF token helper function
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
});
