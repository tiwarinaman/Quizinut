$(document).ready(function () {
    $("#quiz-body").hide();
});




// const timerCtrl = (function start_timer() {
//         let time;
//         let countDownEl;
//         function updateCounter() {
//             const minutes = Math.floor(time / 60);
//             let seconds = time % 60;
//             seconds = seconds < 10 ? '0' + seconds : seconds;
//             countDownEl.innerText = `${minutes}: ${seconds}`;
//             time--;
//
//         }
//         function initTimer(duration) {
//             time = duration * 60;
//             countDownEl = document.getElementById('clock');
//             console.log('Timer Obj', countDownEl);
//             setInterval(updateCounter, 1000);
//         }
//         return {
//             init: initTimer
//         }
//     })();
//
//
