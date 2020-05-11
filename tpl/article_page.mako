<!DOCTYPE html>
<html>

<head>
    <meta charset='UTF-8' />
    <link rel='shortcut icon' type='image/x-icon' href='/static/favicon.ico' media='screen' />
    <!--Import Google Icon Font-->
    <link href="/static/css/icons.css" rel="stylesheet" type='text/css' />
    <!--Import materialize.css-->
    <link type="text/css" rel="stylesheet" href="/static/css/materialize.css" media="screen,projection" />
    <link href="/static/css/site.css" rel="stylesheet" type='text/css' />
    <link href='/static/css/highlight.css' rel='stylesheet' type='text/css' />
    <!--Let browser know website is optimized for mobile-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>${article.majorName} - ${article.title}</title>
</head>

<body>
    <ul id="slide-out" class="sidenav sidenav-fixed">
        <li>
            <div class="user-view">
                <a href="/">${config['site_name']}</a>
            </div>
        </li>
        <li>
            <div class="divider"></div>
        </li>
        % for dir_item in dirIndex:
            <li><a class="subheader collapsible-header">${dir_item['name']}</a></li>
            % for article_item in dir_item['articles']:
                %if article_item['selected']:
                    <li class="active">
                %else:
                    <li>
                %endif
                    <a class="waves-effect" href="/note/${article_item['key']}">${article_item['title']}</a></li>
            % endfor
        % endfor
        <br /><br /><br /><br /><br />
    </ul>
    <main>
        <nav>
            <div class="nav-wrapper">
                <ul class="left">
                    <li><a href="#" data-target="slide-out"
                            class="top-nav sidenav-trigger waves-effect waves-light circle hide-on-large-only"><i
                                class="material-icons">menu</i></a></li>
                    % for major_i, major_item in enumerate(majorIndex):
                        <li><a href="/note/${major_item.firstArticle}" style="margin-left: ${(15 * (major_i == 0))}px;">${major_item.majorName}</a></li>
                    % endfor
                </ul>
                <ul id="nav-mobile" class="right hide-on-med-and-down">
                    <li><a href="${article.gitUrl}" style="margin-right: 15px">Git</a></li>
                </ul>
            </div>
        </nav>
        <div id='contentHtml' class='markdown-body'>
            ${article.contentHtml}
        </div>
    </main>

    <!--JavaScript at end of body for optimized loading-->
    <script src="/static/script/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="/static/script/materialize.js"></script>
    <script>
        $(document).ready(function () {
            $('.sidenav').sidenav();
        });
    </script>
    %if config['ga_id']:
    <script async src="https://www.googletagmanager.com/gtag/js?id=${config['ga_id']}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', '${config["ga_id"]}');
    </script>
    %endif
    <footer class="center-align" style="margin: 15px 0;">
        <span class="grey-text text-darken-2">&copy; All rights reserved.</span>
        %if config['icp_beian']:
        <a href="http://www.beian.miit.gov.cn/" class="grey-text text-darken-2">${config['icp_beian']}</a>
        %endif
    </footer>
</body>
</html>