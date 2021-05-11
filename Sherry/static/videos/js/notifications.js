
const bell = document.getElementById('bell-counter');

let notifications = new Array();

const check_new_notification = () => {

    console.log('check');

    setTimeout(check_new_notification(), 2000)
}
