function do_create() {
    $.ajax({
        url: '/mgr/dir',
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        data: {
            dirName: $('#dirName').val(),
            majorId: $('#majorId').val(),
            position: $('#position').val()
        },
        success: function (data) {
            location.assign('/static/manage/dir_list.html');
        }
    });
}

function do_edit() {
    $.ajax({
        url: '/mgr/dir',
        method: 'PUT',
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        data: {
            dirId: $('#dirId').val(),
            dirName: $('#dirName').val(),
            majorId: $('#majorId').val(),
            position: $('#position').val()
        },
        success: function (data) {
            alert("保存成功");
        }
    });
}

function do_detail() {
    $.ajax({
        url: '/mgr/major/list',
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        success: function (data) {
            var majorIdHtml = "";
            for (item of data) {
                majorIdHtml += `<option value="${item.majorId}">${item.majorName}</option>\n`;
            }
            $('#majorId').html(majorIdHtml);
            $('select').formSelect();  //refresh <select>
            if (location.search === '') {
                $('#btn-area').html(`<a href='javascript:void(0)' onclick='do_create()'
                       class='weui-btn weui-btn_mini weui-btn_default'>提交新增</a>`);
                return;
            }
            $.ajax(({
                url: '/mgr/dir/detail' + location.search,
                headers: {
                    'Authorization': 'Bearer ' + localStorage.token
                },
                success: function (data) {
                    $('#dirId').val(data.dirId);
                    $('#dirName').val(data.dirName);
                    $('#majorId').val(data.majorId);
                    $('#position').val(data.position);
                    $('#btn-area').html(`<a href='javascript:void(0)' onclick='do_edit()'
                       class='weui-btn weui-btn_mini weui-btn_default'>提交修改</a>`);
                    $('select').formSelect();
                },
                error: function (resp) {
                    alert(resp.status + ": " + resp.responseText);
                }
            }))
        }
    });
}