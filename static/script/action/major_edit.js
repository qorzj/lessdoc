function do_create() {
    $.ajax({
        url: '/mgr/major',
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        data: {
            majorName: $('#majorName').val(),
            gitUrl: $('#gitUrl').val(),
            position: $('#position').val()
        },
        success: function (data) {
            location.assign('/static/manage/major_list.html');
        }
    });
}

function do_edit() {
    $.ajax({
        url: '/mgr/major',
        method: 'PUT',
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        data: {
            majorId: $('#majorId').val(),
            majorName: $('#majorName').val(),
            gitUrl: $('#gitUrl').val(),
            position: $('#position').val()
        },
        success: function (data) {
            alert("保存成功");
        }
    });
}

function do_detail() {
    if (location.search === '') {
        $('#btn-area').html(`<a href='javascript:void(0)' onclick='do_create()'
               class='weui-btn weui-btn_mini weui-btn_default'>提交新增</a>`);
        return;
    }
    $.ajax(({
        url: '/mgr/major/detail' + location.search,
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        success: function (data) {
            $('#majorId').val(data.majorId);
            $('#majorName').val(data.majorName);
            $('#gitUrl').val(data.gitUrl);
            $('#position').val(data.position);
            $('#btn-area').html(`<a href='javascript:void(0)' onclick='do_edit()'
               class='weui-btn weui-btn_mini weui-btn_default'>提交修改</a>`);
        },
        error: function (resp) {
            alert(resp.status + ": " + resp.responseText);
        }
    }))
}