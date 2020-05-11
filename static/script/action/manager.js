function do_logout() {
    $.ajax({
        url: "/mgr/logout",
        method: "POST",
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        success: function (data) {
            localStorage.token = '';
            location.assign('/manage');
        },
        error: function (resp) {
            alert(resp.status + ": " + resp.responseText);
        }
    })
}