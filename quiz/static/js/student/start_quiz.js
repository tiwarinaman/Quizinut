$(document).ready(function () {
    $("#quiz-body").hide();
});

const uiCtrl = (function uiController(){

    const domString =  {
        btnNext: 'btn_next',
        btnPrev: 'btn_prev'
    }

    function setUiControls(quiz) {
        let nextButton = document.getElementById(domString.btnNext);
        nextButton.innerText = quiz.next();
    }

    function initView() {
        setUiControls()
    }
    function populateQuiz(quiz) {
        console.log('currentQuiz', quiz)
    }

    return {
        init: initView,
        currentQuiz: populateQuiz
    }

})();

const quizCtrl = (function quizHandler(UICtrl) {
    let time;
    let countDownEl;
    let quizList = [];
    let questionNumber = 0;

    function fetchQuiz(api_id) {
        $.ajax({
            url: "/get-questions/" + api_id,
            method: "GET",
            success: function (data) {
                console.log(data);
                quizList = data;
                // UICtrl.init();
            }
        })
    }

    function nextQuestion() {
        questionNumber = questionNumber < quizList.length ? questionNumber + 1 : quizList.length - 1;
        console.log('QuizList', quizList[questionNumber]);
        console.log('questionNumber', questionNumber);
        UICtrl.currentQuiz(quizList[questionNumber]);
    }

    function previousQuestion() {
        questionNumber = questionNumber > 0 ? questionNumber - 1 : 0;
        console.log('Pre_QuizList', quizList[questionNumber]);
        console.log('Prev_questionNumber', questionNumber);
        UICtrl.currentQuiz(quizList[questionNumber]);
    }

    function updateCounter() {
        const minutes = Math.floor(time / 60);
        let seconds = time % 60;
        seconds = seconds < 10 ? '0' + seconds : seconds;
        countDownEl.innerText = `${minutes}: ${seconds}`;
        time--;

    }

    function initTimer(duration) {
        time = duration * 60;
        countDownEl = document.getElementById('clock');
        console.log('Timer Obj', countDownEl);
        setInterval(updateCounter, 1000);
    }

    function initUI(quizId) {
        $("#start-button").hide();
        $("#quiz-body").show();
        fetchQuiz(quizId);
    }

    return {
        init: initUI,
        next: nextQuestion,
        previous: previousQuestion
    }
})(uiCtrl);


