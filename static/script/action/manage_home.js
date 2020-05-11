function do_entry() {
    $.ajax({
        url: "/mgr/me",
        method: "GET",
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        success: function (data) {
            location.assign('/static/manage/major_list.html');
        },
        error: function (resp) {
            location.assign('/static/manage/login.html');
        }
    })
}