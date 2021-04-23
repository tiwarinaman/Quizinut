let questionList = [];


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function createQuiz() {
    console.log("create quiz clicked");
    csrftoken = getCookie('csrftoken');

    let data = {'questions[]': questionList.results, csrfmiddlewaretoken: csrftoken}


    // for (let i = 0; i < questionList.results.length; i++) {
    //
    //     let data = {csrfmiddlewaretoken: csrftoken, 'question': questionList.results[i].question};
    //     $.ajax({
    //         url: "/create-quiz-open-trivial/",
    //         method: "POST",
    //         data: data,
    //         success: function (data) {
    //             console.log(data);
    //         }
    //     })
    // }


    $.ajax({
        url: "/create-quiz-open-trivial/",
        method: "POST",
        data: data,
        success: function (data) {
            console.log(data);
        }
    })

}