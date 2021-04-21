$(document).ready(function () {
    $("#quiz-body").hide();
    $("#resultMessage").hide()
    $("#btnSubmit").hide()
});

const uiCtrl = (function uiController() {
    const domControls = {};
    const domString = {
        question: 'question',
        option1: 'option1',
        option2: 'option2',
        option3: 'option3',
        option4: 'option4',
        resultMessage: 'resultMessage',

    }

    function initUiControls() {
        domControls['question'] = document.getElementById(domString.question);
        domControls['option1'] = document.getElementById(domString.option1);
        domControls['option2'] = document.getElementById(domString.option2);
        domControls['option3'] = document.getElementById(domString.option3);
        domControls['option4'] = document.getElementById(domString.option4);
        domControls['resultMessage'] = document.getElementById(domString.resultMessage);

        domControls['resultMessage'].style.display = 'none';
    }

    function showHideAlert(alertType, isShow) {
        if (alertType == 'wrong') {
            const display = isShow ? 'block' : 'none';
            domControls['resultMessage'].style.display = display;
        } else {
            const display = isShow ? 'block' : 'none';
            domControls['resultMessage'].style.display = display;
        }
    }

    function initView(quiz) {
        initUiControls()
        populateQuiz(quiz)
    }

    function populateQuiz(quiz) {
        console.log('currentQuiz', quiz)
        domControls['question'].innerText = quiz.fields.question;
        domControls['option1'].innerText = quiz.fields.option1;
        domControls['option2'].innerText = quiz.fields.option2;
        domControls['option3'].innerText = quiz.fields.option3;
        domControls['option4'].innerText = quiz.fields.option4;
    }

    return {
        init: initView,
        currentQuiz: populateQuiz,
        showHide: showHideAlert
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
                UICtrl.init(quizList[0]);
            }
        })
    }

    function nextQuestion() {
        UICtrl.showHide('wrong', false)
        UICtrl.showHide('success', false)
        questionNumber = questionNumber < quizList.length - 1 ? questionNumber + 1 : quizList.length - 1;
        console.log('QuizList', quizList[questionNumber]);
        console.log('questionNumber', questionNumber);
        UICtrl.currentQuiz(quizList[questionNumber]);
    }

    function previousQuestion() {
        UICtrl.showHide('wrong', false)
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

    function selectedOption(selectedOption) {
        const currentQuiz = quizList[questionNumber];
        console.log('currentQuiz ', currentQuiz);
        console.log('seleccted Option ', selectedOption);
        const selectedAnswer = currentQuiz.fields[selectedOption];
        const correctAnswerNumber = currentQuiz.fields.correct_answer;
        const correctAnswer = currentQuiz.fields['option' + correctAnswerNumber];
        selectedAnswer === correctAnswer ?
            UICtrl.showHide('success', true) : UICtrl.showHide('wrong', true);
    }

    return {
        init: initUI,
        next: nextQuestion,
        previous: previousQuestion,
        chooseOption: selectedOption
    }
})(uiCtrl);


