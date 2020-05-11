function do_list() {
    $.ajax({
        url: '/mgr/major/list',
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        success: function (data) {
            var list_html = "";
            for (item of data) {
                list_html += `<div class="row">
                    <div class="col s3">
                        ${item.majorName}
                    </div>
                    <div class="col">
                        <a href="${item.gitUrl}">
                            <i class="material-icons">code</i>
                        </a>
                    </div>
                    <div class="col">
                        ${item.position}
                    </div>
                    <div class="col">
                        <a href='/static/manage/major_edit.html?majorId=${item.majorId}'>
                            <i class="material-icons">edit</i>
                        </a>
                        &nbsp; &nbsp;
                        <a href='javascript:void(0)' onclick='do_delete(${item.majorId})'>
                            <i class="material-icons">delete</i>
                        </a>
                    </div>
                </div>\n`;
            }
            $('#major_list').html(list_html);
        }
    })
}

function do_delete(majorId) {
    $.ajax({
        url: '/mgr/major/' + majorId,
        method: 'DELETE',
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        success: function (data) {
            location.reload();
        }
    })
}