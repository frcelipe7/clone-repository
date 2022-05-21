const register_yes = document.querySelector('.yes');
const register_not = document.querySelector('.not_yet');
const question = document.querySelector('.question');

register_yes.addEventListener('click', () => {
    window.location.href = 'profile/user/edit';
});
register_not.addEventListener('click', () => {
    question.innerHTML = 'Ok. Bye!'
    question.classList = 'question bye'
});