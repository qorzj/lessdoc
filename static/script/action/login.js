function submit_login() {
    $.ajax({
        url: "/public/mgr/login",
        method: "POST",
        data: {
            username: $("#username").val(),
            password: $("#password").val()
        },
        success: function (data) {
            localStorage.token = data.token;
            location.assign('/static/manage/major_list.html');
        },
        error: function (resp) {
            alert(resp.status + ": " + resp.responseText);
        }
    })
}