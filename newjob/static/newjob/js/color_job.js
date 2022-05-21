const job_link = document.querySelectorAll('.job_link');
const job_content = document.querySelectorAll('.job_content');

function range(start, end) {
    var ans = [];
    for (let i = start; i <= end; i++) {
        ans.push(i);
    };
    return ans;
};

for (i in range(0, job_link.length-1)) {
    if (i % 2 == 0) {
        job_content[i].style.backgroundColor = '#BA2D0B';
        job_link[i].style.color = '#F2F2F2';
    } else {
        job_content[i].style.backgroundColor = '#F2F2F2';
        job_link[i].style.color = '#04052E';
    };
};
