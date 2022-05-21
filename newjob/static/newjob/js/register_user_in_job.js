const register_button = document.querySelector('.register_button');
const user_id = document.querySelector(".id .user_id").innerHTML;
const job_id = document.querySelector(".id .job_id").innerHTML;


function getCookie(name) {
    var cookieValue = null;

    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');

        for (i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            };
        };
    };
    return cookieValue;
};

fetch('/registeruserinjob')
.then(response => response.json())
.then(registers => {
    registers.forEach(register => {
        if (register.user_id == user_id && register.job_id == job_id) {
            if (register.situation == "Rejected") {
                register_button.innerHTML = "You was Rejected";
                register_button.style.backgroundColor = '#0f0f2c';
                register_button.style.color = 'red';
            } else if (register.situation == "Accepted") {
                register_button.innerHTML = "You was Accepted";
                register_button.style.backgroundColor = '#0f0f2c';
                register_button.style.color = 'green';
            } else {
                register_button.innerHTML = "You're already registered";
                register_button.style.backgroundColor = '#0f0f2c';
                register_button.style.color = '#555555';
            }
            register_button.disabled = "disabled";
        };
    });
});

try{
    register_button.addEventListener('click', ()=> {
        fetch('/registeruserinjob', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                user_id: user_id,
                job_id: job_id
            })
        });

        register_button.innerHTML = "You're already registered";
        register_button.disabled = "disabled";
        register_button.style.backgroundColor = '#0f0f2c';
        register_button.style.color = '#555555';
        register_button.style.cursor = 'default';
    });
} catch (e) {}
