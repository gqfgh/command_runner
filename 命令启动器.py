import os
from urllib.parse import quote

import webview


def add_quotation_mark(string: str) -> str:
    # 如果包含单引号，用双引号包裹；反之用单引号
    if "'" in string: return f'"{string}"'
    else: return f"'{string}'"


class JSApi:
    def bp_chrome(self):
        bp = 'bp.bat'
        chrome = 'chrome'
        os.system(f'{bp} & {chrome}')

    def dirsearch(self, u: str) -> str:
        command = "dirsearch "
        if u != '': command += f'-u {u} '
        os.system(f'start powershell -command "{command};pause"')
        return command

    def sqlmap(self, u, r, batch, dbs, D, tables, T, columns, C, dump, random_agent, H, technique, string, sql_shell, tamper, o, current_user, level, data, skip_urlencode, shell, update, list_tampers, cookie, proxy, purge, v, m, g, second_url, dbms, threads, forms):
        command = "py310 'D:\security tool\web渗透工具\sqlmap\sqlmap.py' "

        maps = {
            '-u': u, '-r': r, '--batch': batch, '--dbs': dbs, '-D': D, '--tables': tables,
            '--columns': columns, '-T': T, '-C': C, '--dump': dump, '--random-agent': random_agent,
            '-H': H, '--technique': technique, '--string': string, '--sql-shell': sql_shell,
            '--tamper': tamper, '-o': o, '--current-user': current_user, '--level': level,
            '--data': data, '--skip-urlencode': skip_urlencode, '--shell': shell, '--update': update,
            '--list-tampers': list_tampers, '--cookie': cookie, '--proxy': proxy, '--purge': purge,
            '-v': v, '-m': m, '-g': g, '--second-url': second_url, '--dbms': dbms, 
            '--threads': threads, '--forms': forms
        }
        for key, value in maps.items():
            match value:
                case False | '':
                    pass
                # 没有值的参数，布尔型
                case True:
                    command += f'{key} '
                # 有值的参数，字符串
                case value:
                    if not value.isdigit():
                        value = add_quotation_mark(value)
                    command += f"""{key} {value} """
        os.system(f'start powershell -command "{command};pause"')
        return command

    def flask_decode(self, c, s):
        command = r"py310 'D:/security tool/web渗透工具/flask-session-cookie-manager/flask_session_cookie_manager3.py' decode "
        if c != '': command += f'-c {c} '
        if s != '': command += f'-s {s} '
        os.system(f'start powershell -command "{command};pause"')
        return command

    def flask_encode(self, t, s):
        command = r"py310 'D:\security tool\web渗透工具\flask-session-cookie-manager\flask_session_cookie_manager3.py' encode "
        if t != '': command += f'-t "{t}" '
        if s != '': command += f'-s {s} '
        os.system(f'start powershell -command "{command};pause"')
        return command


window = webview.create_window(
    title='命令启动器',
    url='gui.html',
    js_api=JSApi(),
    text_select=1,  # 文本可选择
    zoomable=True,  # 开启缩放
    min_size=(1900, 1000)
)

if __name__ == '__main__':
    webview.start(debug=False)
