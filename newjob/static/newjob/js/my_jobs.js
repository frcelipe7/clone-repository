const user_id = document.querySelector(".id .user_id").innerHTML;
const job_id = document.querySelector(".id .job_id").innerHTML;


fetch('/registeruserinjob')
.then(response => response.json())
.then(registers => {
    registers.forEach(register => {
        const isThisUser = register.user_id == user_id;
        if (isThisUser) {
            const content_job = document.createElement('div');
            content_job.className = `div_${register.job_id} content_job`;
            content_job.id = register.job_id;

            const jobs_content = document.querySelector('.jobs_content');
            jobs_content.append(content_job);
        };
    });
});

fetch('/usershired/api')
.then(response => response.json())
.then(registers => {
    registers.forEach(register => {
        const isThisUser = register.user_id == user_id;
        if (isThisUser) {
            const content_job = document.createElement('div');
            content_job.className = `div_${register.job_id} content_job`;
            content_job.id = register.job_id;

            const jobs_content = document.querySelector('.closed_jobs_content');
            jobs_content.append(content_job);
        };
    });
});

function changeInnerHTML() {
    this.innerHTML = 'See more';
};

function openedJobs() {
    const allInfoJobs = document.querySelectorAll('.content_job');

    fetch('/jobinfo')
    .then(response => response.json())
    .then(jobsJson => {
        allInfoJobs.forEach(jobInfo => {
            jobsJson.forEach(jobJson => {
                if (jobJson.id == jobInfo.id) {
                    const content_job = document.querySelector(`.div_${jobInfo.id}`);

                    const img_job = document.createElement('img');
                    img_job.className = `img ${jobInfo.id}`;
                    img_job.src = `/static/newjob/media/${jobJson.image}`;
                    img_job.alt = "image_job";

                    content_job.append(img_job);

                    const title_job = document.createElement('strong');
                    title_job.className = 'title_job'
                    title_job.innerHTML = jobJson.title;
        
                    content_job.append(title_job);

                    const link = document.createElement('a');
                    link.href = `job/view/id=${jobInfo.id}`;
                    link.className = 'link';

                    fetch('/registeruserinjob')
                    .then(response => response.json())
                    .then(registers => {
                        registers.forEach(register => {
                            if (register.user_id == user_id && register.job_id == jobInfo.id) {
                                const registerSituation = document.createElement('div');
                                registerSituation.innerHTML = register.situation;
                                registerSituation.className = 'register_situation';
                                if (String(register.situation) == 'Accepted') {
                                    link.style.color = 'green';
                                } else if (String(register.situation) == "Rejected") {
                                    link.style.color = 'red';
                                } else {
                                    link.style.color = 'black';
                                }

                                registerSituation.addEventListener("mouseover", changeInnerHTML);
                                registerSituation.addEventListener("mouseout", () => {
                                    registerSituation.innerHTML = register.situation;
                                });

                                link.append(registerSituation);
                    
                                content_job.append(link);
                            };
                        });
                    });
                };
            });
        });
    });
};

function closedJobs() {
    const allInfoJobs = document.querySelectorAll('.content_job');

    fetch('/closejob/api')
    .then(response => response.json())
    .then(jobsJson => {
        allInfoJobs.forEach(jobInfo => {
            jobsJson.forEach(jobJson => {
                if (jobJson.id == jobInfo.id) {
                    const content_job = document.querySelector(`.div_${jobInfo.id}`);

                    const img_job = document.createElement('img');
                    img_job.className = `img ${jobInfo.id}`;
                    img_job.src = `/static/newjob/media/${jobJson.image}`;
                    img_job.alt = "image_job";

                    content_job.append(img_job);

                    const title_job = document.createElement('strong');
                    title_job.className = 'title_job'
                    title_job.innerHTML = jobJson.title;
        
                    content_job.append(title_job);

                    const link = document.createElement('a');
                    link.href = `closed_job/view/id=${jobInfo.id}`;
                    link.className = 'link';

                    fetch('/usershired/api')
                    .then(response => response.json())
                    .then(registers => {
                        registers.forEach(register => {
                            if (register.user_id == user_id && register.job_id == jobInfo.id) {
                                const registerSituation = document.createElement('div');
                                registerSituation.innerHTML = register.situation;
                                registerSituation.innerHTML = "Accepted";
                                registerSituation.className = 'register_situation';
                                link.style.color = 'green';

                                registerSituation.addEventListener("mouseover", changeInnerHTML);
                                registerSituation.addEventListener("mouseout", () => {
                                    registerSituation.innerHTML = "Accepted";
                                });

                                link.append(registerSituation);

                                content_job.append(link);
                            };
                        });
                    });
                };
            });
        });
    });
};


document.addEventListener('DOMContentLoaded', () => {
    setTimeout(openedJobs, 100);
    setTimeout(closedJobs, 100);
});
