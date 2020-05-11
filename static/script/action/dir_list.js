function do_list() {
    $.ajax({
        url: '/mgr/dir/list',
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        success: function (data) {
            var list_html = "";
            for (item of data) {
                list_html += `<div class="row">
                    <div class="col s3">
                        ${item.dirName}
                    </div>
                    <div class="col">
                        ${item.majorName}
                    </div>
                    <div class="col">
                        ${item.position}
                    </div>
                    <div class="col">
                        <a href='/static/manage/dir_edit.html?dirId=${item.dirId}'>
                            <i class="material-icons">edit</i>
                        </a>
                        &nbsp; &nbsp;
                        <a href='javascript:void(0)' onclick='do_delete(${item.dirId})'>
                            <i class="material-icons">delete</i>
                        </a>
                    </div>
                </div>\n`;
            }
            $('#dir_list').html(list_html);
        }
    })
}

function do_delete(dirId) {
    $.ajax({
        url: '/mgr/dir/' + dirId,
        method: 'DELETE',
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        success: function (data) {
            location.reload();
        }
    })
}