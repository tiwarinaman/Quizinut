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
        btnSubmit: 'btnSubmit',
        btnNext: 'btnNext',

    }

    function initUiControls() {
        domControls['question'] = document.getElementById(domString.question);
        domControls['btnNext'] = document.getElementById(domString.btnNext);
        domControls['btnSubmit'] = document.getElementById(domString.btnSubmit);
        domControls['resultMessage'] = document.getElementById(domString.resultMessage);
        domControls['tickIconTag'] = '<div class="icon tick"><i class="fas fa-check"></i></div>';
        domControls['crossIconTag'] = '<div class="icon cross"><i class="fas fa-times"></i></div>';
        domControls['optionList'] = document.querySelector(".option_list");
        domControls['time_line'] = document.querySelector("header .time_line");
        domControls['timeText'] = document.querySelector(".timer .time_left_txt");
        domControls['timeCount'] = document.querySelector(".timer .timer_sec");
    }

    function initView(quiz) {
        initUiControls()
        populateQuiz(quiz, 1)
    }

    function populateQuiz(quiz, queNum) {
        console.log('currentQuiz', quiz)
        domControls['question'].innerText = quiz.fields.question;
        //creating a new span and div tag for question and option and passing the value using array index
        let que_tag = '<span>' + queNum + ". " + quiz.fields.question + '</span>';
        let option_tag = '<div class="option-container"><span>' + quiz.fields.option1 + '</span></div>'
            + '<div class="option-container"><span>' + quiz.fields.option2 + '</span></div>'
            + '<div class="option-container"><span>' + quiz.fields.option3 + '</span></div>'
            + '<div class="option-container"><span>' + quiz.fields.option4 + '</span></div>';
        domControls['question'].innerHTML = que_tag; //adding new span tag inside que_tag
        domControls['optionList'].innerHTML = option_tag; //adding new div tag inside option_tag

        const option = domControls['optionList'].querySelectorAll(".option-container");

        // set onclick attribute to all available options
        for (let i = 0; i < option.length; i++) {
            option[i].setAttribute("onclick", "quizCtrl.chooseOption(this)");
        }
    }

    function correctAnswer(selectedOption) {
        const allOptions = domControls['optionList'].children.length; //getting all option items
        selectedOption.classList.add("correct"); //adding green color to correct selected option
        selectedOption.insertAdjacentHTML("beforeend", domControls['tickIconTag']); //adding tick icon to correct selected option
        console.log("Correct Answer");
        for (let i = 0; i < allOptions; i++) {
            domControls['optionList'].children[i].classList.add("disabled"); //once user select an option then disabled all options
        }
    }

    function inCorrectAnswer(selectedOption, correctAnswerNumber) {
        const allOptions = domControls['optionList'].children.length; //getting all option items
        selectedOption.classList.add("incorrect"); //adding green color to correct selected option
        selectedOption.insertAdjacentHTML("beforeend", domControls['crossIconTag']); //adding tick icon to correct selected option
        console.log("Wrong Answer");
        //show the correct answer & once user select an option then disabled all options
        for (let i = 0; i < allOptions; i++) {
            domControls['optionList'].children[i].classList.add("disabled");
            if (i == correctAnswerNumber - 1) {
                domControls['optionList'].children[i].classList.add("correct"); //adding green color to correct selected option
                domControls['optionList'].children[i].insertAdjacentHTML("beforeend", domControls['tickIconTag']);
            }
        }

    }

    return {
        init: initView,
        currentQuiz: populateQuiz,
        correct: correctAnswer,
        inCorrect: inCorrectAnswer,
        domControls: domControls
    }

})();

const quizCtrl = (function quizHandler(UICtrl) {
    let time, counter;
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
        clearInterval(counter); //clear counter
        startTimer(15);
        questionNumber = questionNumber < quizList.length - 1 ? questionNumber + 1 : quizList.length - 1;
        if (questionNumber === quizList.length - 1) {
            UICtrl.domControls['btnNext'].style.display = 'none';
            UICtrl.domControls['btnSubmit'].style.display = 'block';
            UICtrl.currentQuiz(quizList[questionNumber], questionNumber + 1);
        } else {
            UICtrl.domControls['btnSubmit'].style.display = 'none'
            UICtrl.currentQuiz(quizList[questionNumber], questionNumber + 1);
        }
        console.log('QuizList', quizList[questionNumber]);
        console.log('questionNumber', questionNumber);
    }

    function previousQuestion() {
        clearInterval(counter); //clear counter
        startTimer(15);
        questionNumber = questionNumber > 0 ? questionNumber - 1 : 0;
        console.log('Pre_QuizList', quizList[questionNumber]);
        console.log('Prev_questionNumber', questionNumber);
        UICtrl.currentQuiz(quizList[questionNumber], questionNumber + 1);
    }

    function initUI(quizId) {
        $("#start-button").hide();
        $("#quiz-body").show();
        fetchQuiz(quizId);
        startTimer(15); //calling startTimer function
        startTimerLine(0); //calling startTimerLine function
    }

    function startTimer(duration) {
        counter = setInterval(handleTimer, 1000);

        function handleTimer() {
            UICtrl.domControls['timeCount'].textContent = duration;
            duration -= 1;//decrement timer value
            if (duration < 9) {
                const withZero = '0' + UICtrl.domControls['timeCount'].textContent;
                UICtrl.domControls['timeCount'].textContent = withZero;
            }
            if (duration < 0) {
                clearInterval(counter); //clear counter
                UICtrl.domControls['timeText'].textContent = "Time Off";
                const allOptions = UICtrl.domControls['optionList'].children.length; //getting all option items
                let correctAns = quizList[questionNumber].fields.correct_answer;
                const currentQuiz = quizList[questionNumber];
                const correctAnswer = currentQuiz.fields['option' + correctAns];
                for (let i = 0; i < allOptions; i++) {
                    if (UICtrl.domControls['optionList'].children[i].textContent === correctAnswer) {
                        UICtrl.domControls['optionList'].children[i].classList.add("correct"); //adding green color to correct selected option
                        UICtrl.domControls['optionList'].children[i].insertAdjacentHTML("beforeend", UICtrl.domControls['tickIconTag']);
                    }
                }
                for (let i = 0; i < allOptions; i++) {
                    UICtrl.domControls['optionList'].children[i].classList.add("disabled"); //once user select an option then disabled all options
                }
            }
        }
    }

    function startTimerLine(duration) {
    }

    function selectedOption(selectedOption) {
        clearInterval(counter); //clear counter
        const currentQuiz = quizList[questionNumber];
        console.log('currentQuiz ', currentQuiz);
        const selectedAnswer = selectedOption.textContent;
        const correctAnswerNumber = currentQuiz.fields.correct_answer;
        const correctAnswer = currentQuiz.fields['option' + correctAnswerNumber];
        if (selectedAnswer === correctAnswer) {
            UICtrl.correct(selectedOption, correctAnswerNumber);
        } else {
            UICtrl.inCorrect(selectedOption, correctAnswerNumber);
        }
    }


    return {
        init: initUI,
        next: nextQuestion,
        previous: previousQuestion,
        chooseOption: selectedOption
    }
})(uiCtrl);


