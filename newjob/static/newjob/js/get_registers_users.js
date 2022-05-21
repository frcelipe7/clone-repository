document.addEventListener('DOMContentLoaded', () => {
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
    const job_id = document.querySelector(".id .job_id").innerHTML;
    const registered_users = document.querySelector('.content_enterprise .registered_users');
    const see_more_content = document.querySelector(".see_more_content");

    function reject_acept(user_id, job_id, situation) {
        fetch('/registeruserinjob')
        .then(response => response.json())
        .then(registers_jobs => {
            registers_jobs.forEach(register_job => {
                if (register_job.user_id == user_id && register_job.job_id == job_id) {
                    fetch('/registeruserinjob', {
                        method: 'PUT',
                        headers: {
                            'X-CSRFToken': getCookie('csrftoken'),
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            user_id: user_id,
                            job_id: job_id,
                            situation: situation
                        })
                    });
                };
            });
        });
        
    }

    fetch('/registeruserinjob')
    .then(response => response.json())
    .then(registers => {
        registers.forEach(register => {
            if (parseInt(register.job_id) == parseInt(job_id)) {
                const user_img = document.createElement('img');
                user_img.className = `img ${register.id}`;
                user_img.alt = 'User Image';

                const user_username = document.createElement('strong');
                user_username.id = `${register.user_id}`;

                fetch(`/user/id=${register.user_id}/get`)
                .then(response => response.json())
                .then(user => {
                    user_username.innerHTML = user.username;
                    user_img.src = `/static/newjob/media/${user.image}`;
                });

                const content_img_name = document.createElement('div');
                content_img_name.className = 'content_img_name';
                content_img_name.append(user_img, user_username);

                const button_accept = document.createElement('button');
                button_accept.type = "submit";
                button_accept.innerHTML = 'Accept';
                button_accept.className = `accept id_accept_${register.user_id}`;
                button_accept.id = register.user_id;
                button_accept.addEventListener('click', () => {
                    reject_acept(register.user_id, register.job_id, "Accepted");
                });

                const button_reject = document.createElement('button');
                button_reject.type = "submit";
                button_reject.innerHTML = 'Reject';
                button_reject.className = `reject id_reject_${register.user_id}`;
                button_reject.id = register.user_id;
                button_reject.addEventListener('click', () => {
                    reject_acept(register.user_id, register.job_id, "Rejected");
                });

                const button_see_more = document.createElement('div');
                button_see_more.innerHTML = "See more";
                button_see_more.className = 'button_see_more';
                button_see_more.id = register.user_id;
                button_see_more.addEventListener('click', () => {

                    function fetch_user(user_id) {
                        fetch(`/user/id=${user_id}/get`)
                        .then(response => response.json())
                        .then(user => {
                            if (user.id) {
                                const user_description = document.createElement('div');
                                user_description.className = 'user_description'
                                user_description.innerHTML = `
                                <div class="img_and_name">
                                    <img src="/../static/newjob/media/${user.image}" alt="User Image">
                                    <h4 class="username">${user.first_name} ${user.last_name}</h4>
                                </div>
                                <p class="username">Username: ${user.username}</p>
                                <p class="email">Email: ${user.email}</p>
                                <p class="experience">${user.experience}</p>
                                `;

                                see_user.append(user_description);

                            } else {
                                fetch_user(register.user_id);
                            };
                        });
                    };
    

                    const see_user = document.createElement('div');
                    see_user.className = "see_user";

                    see_more_content.style.display = 'flex';
                    see_more_content.style.position = 'fixed';

                    const button_close = document.createElement('div');
                    button_close.className = 'button_close';
                    button_close.innerHTML = `
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-circle" viewBox="0 0 16 16">
                                <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                                <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>
                            </svg>
                        `;
                    button_close.addEventListener('click', () => {
                        see_more_content.style.display = 'none';
                        see_more_content.style.position = 'none';
                        see_user.remove();
                    });

                    see_user.append(button_close);
                    see_more_content.append(see_user);

                    fetch_user(register.user_id);

                });

                

                const div_buttons = document.createElement('div');
                div_buttons.className = 'div_buttons';
                div_buttons.id = register.user_id;
                div_buttons.append(button_accept, button_reject, button_see_more);

                button_reject.addEventListener('click', () => {
                    button_accept.remove()
                    button_reject.remove()

                    const situation_div = document.createElement('p');
                    situation_div.className = 'situation_div';
                    situation_div.innerHTML = `User Rejected`;
                    situation_div.style.color = 'red';


                    div_buttons.append(situation_div);
                });

                button_accept.addEventListener('click', () => {
                    button_accept.remove()
                    button_reject.remove()

                    const situation_div = document.createElement('p');
                    situation_div.innerHTML = `User Accepted`;
                    situation_div.className = 'situation_div';
                    situation_div.style.color = 'green';

                    div_buttons.append(situation_div);
                });

                const content_user = document.createElement('div');
                content_user.className = 'content_user';
                content_user.id = register.user_id;
                content_user.append(content_img_name, div_buttons);
                registered_users.append(content_user);
            };
        });
    });

    setTimeout(() => {
        const DivButtons = document.querySelectorAll('.div_buttons');
            
        fetch('/registeruserinjob')
        .then(response => response.json())
        .then(registers => {
            registers.forEach(register => {
                if (parseInt(job_id) == parseInt(register.job_id)) {
                    DivButtons.forEach(div => {
                        if (parseInt(div.id) == parseInt(register.user_id)) {
                            const button_reject = document.querySelector(`.content_user .div_buttons .id_reject_${register.user_id}`);
                            const button_accept = document.querySelector(`.content_user .div_buttons .id_accept_${register.user_id}`);

                            if (register.situation != "Under analysis") {
                                button_accept.remove()
                                button_reject.remove()

                                const situation_div = document.createElement('p');
                                situation_div.innerHTML = `User ${register.situation}`;
                                situation_div.className = 'situation_div';
                                if (register.situation == "Accepted") {situation_div.style.color = 'green';} else {situation_div.style.color = 'red'}

                                div.append(situation_div);
                            }
                        }
                    })
                }
            })
        })
    }, 500);
});
