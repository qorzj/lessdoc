function do_create() {
    $.ajax({
        url: '/mgr/article',
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        data: {
            articleKey: $('#articleKey').val(),
            title: $('#title').val(),
            dirId: $('#dirId').val(),
            posInDir: $('#posInDir').val(),
            contentMd: $('#contentMd').val()
        },
        success: function (data) {
            location.assign('/static/manage/article_list.html');
        }
    });
}

function do_edit() {
    $.ajax({
        url: '/mgr/article',
        method: 'PUT',
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        data: {
            articleId: $('#articleId').val(),
            articleKey: $('#articleKey').val(),
            title: $('#title').val(),
            dirId: $('#dirId').val(),
            posInDir: $('#posInDir').val(),
            contentMd: $('#contentMd').val()
        },
        success: function (data) {
            alert("保存成功");
        }
    });
}

function do_detail() {
    $.ajax({
        url: '/mgr/dir/list',
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        success: function (data) {
            var dirIdHtml = "";
            for (item of data) {
                dirIdHtml += `<option value="${item.dirId}">${item.majorName} / ${item.dirName}</option>\n`;
            }
            $('#dirId').html(dirIdHtml);
            $('select').formSelect();  //refresh <select>
            if (location.search === '') {
                $('#btn-area').html(`<a href='javascript:void(0)' onclick='do_create()'
                       class='weui-btn weui-btn_mini weui-btn_default'>提交新增</a>`);
                return;
            }
            $.ajax(({
                url: '/mgr/article/detail' + location.search,
                headers: {
                    'Authorization': 'Bearer ' + localStorage.token
                },
                success: function (data) {
                    $('#articleId').val(data.articleId);
                    $('#articleKey').val(data.articleKey);
                    $('#title').val(data.title);
                    $('#dirId').val(data.dirId);
                    $('#posInDir').val(data.posInDir);
                    $('#contentMd').val(data.contentMd);
                    $('#contentHtml').html(data.contentHtml);
                    $('#btn-area').html(`<a href='javascript:void(0)' onclick='do_edit()'
                       class='weui-btn weui-btn_mini weui-btn_default'>提交修改</a>`);
                    $('select').formSelect();
                    M.textareaAutoResize($('#contentMd'));
                },
                error: function (resp) {
                    alert(resp.status + ": " + resp.responseText);
                }
            }))
        }
    });
}

function do_preview() {
    $.ajax({
        url: '/public/article/preview',
        method: 'PUT',
        data: {
            contentMd: $('#contentMd').val()
        },
        success: function (data) {
            $('#contentHtml').html(data.contentHtml)
        },
        error: function (resp) {
            alert(resp.status + ": " + resp.responseText);
        }
    })
}