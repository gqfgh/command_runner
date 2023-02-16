import os
from urllib.parse import quote

import webview


def add_quotation_mark(string: str):
    # 如果包含单引号，用双引号包裹；反之用单引号
    if "'" in string: return f'"{string}"'
    else: return f"'{string}'"


class JSApi:
    def bp_chrome(self):
        bp = 'bp.bat'
        chrome = 'chrome'
        os.system(f'{bp} & {chrome}')

    def dirsearch(self, u):
        command = "dirsearch "
        if u != '': command += f'-u {u} '
        os.system(f'start powershell -command "{command};pause"')
        return command

    def sqlmap(self, u, r, batch, dbs, D, tables, T, columns, C, dump, random_agent, H, technique, string, sql_shell, tamper, o, current_user, level, data, skip_urlencode, shell, update, list_tampers, cookie, proxy, purge, v, m):
        global command
        command = "py310 'D:\security tool\web渗透工具\sqlmap\sqlmap.py' "

        def add_args():
            global command
            if u != '': command += f'-u {quote(u, safe="/?:=")} '
            if r != '': command += f'-r {r} '
            if batch == True: command += '--batch '
            if dbs == True: command += '--dbs '
            if D != '': command += f'-D {D} '
            if tables == True: command += '--tables '
            if T != '': command += f'-T {T} '
            if columns == True: command += '--columns '
            if C != '': command += f'-C {C} '
            if dump == True: command += '--dump '
            if random_agent == True: command += '--random-agent '
            if H != '': command += f'''-H {add_quotation_mark(H)} '''
            if technique != '': command += f'--technique {technique} '
            if string != '': command += f'--string "{string}" '
            if sql_shell == True: command += '--sql-shell '
            if tamper != '': command += f'--tamper {tamper} '
            if o == True: command += '-o '
            if current_user == True: command += '--current-user '
            if level != '': command += f'--level {level} '
            if data != '': command += f'''--data {add_quotation_mark(data)} '''
            if skip_urlencode == True: command += '--skip-urlencode '
            if shell == True: command += '--shell '
            if update == True: command += '--update '
            if list_tampers == True: command += '--list-tampers '
            if cookie != '': command += f'''--cookie {cookie} '''
            if proxy != '': command += f'''--proxy {add_quotation_mark(proxy)} '''
            if purge == True: command += '--purge '
            if v != '': command += f'-v {v} '
            if m != '': command += f'-m {m} '

        add_args()
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
