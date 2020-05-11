function do_list() {
    $.ajax({
        url: '/mgr/article/list',
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        success: function (data) {
            var list_html = "";
            for (item of data) {
                list_html += `<div class="row">
                    <div class="col s3">
                        ${item.title}
                    </div>
                    <div class="col">
                        ${item.articleKey}
                    </div>
                    <div class="col">
                        ${item.majorName} / ${item.dirName}
                    </div>
                    <div class="col">
                        ${item.posInDir}
                    </div>
                    <div class="col">
                        <a href='/static/manage/article_edit.html?articleId=${item.articleId}'>
                            <i class="material-icons">edit</i>
                        </a>
                        &nbsp; &nbsp;
                        <a href='javascript:void(0)' onclick='do_delete(${item.articleId})'>
                            <i class="material-icons">delete</i>
                        </a>
                    </div>
                </div>\n`;
            }
            $('#article_list').html(list_html);
        }
    })
}

function do_delete(articleId) {
    $.ajax({
        url: '/mgr/article/' + articleId,
        method: 'DELETE',
        headers: {
            'Authorization': 'Bearer ' + localStorage.token
        },
        success: function (data) {
            location.reload();
        }
    })
}