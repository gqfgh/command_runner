import os

import webview


def add_quotation_mark(string: str) -> str:
    '''如果包含单引号，用双引号包裹；反之用单引号'''
    if "'" in string:
        return f'"{string}"'
    else:
        return f"'{string}'"


def add_args(maps: dict) -> str:
    args = ''
    for key, value in maps.items():
        match value:
            case False | '':
                pass
            case True:  # true 直接加 key
                args += f'{key} '
            case value:  # 非空字符串需要处理引号
                if not value.isdigit():  # 数字不加引号
                    value = add_quotation_mark(value)
                args += f'''{key} {value} '''
    return args


def run_command(command: str) -> None:
    os.system(f'start powershell -command "{command};pause"')


class JSApi:
    def bp_chrome(self):
        bp = 'bp.pyw'
        chrome = 'chrome'
        os.system(f'{bp} & {chrome}')

    def dirsearch(self, u: str, e: str) -> str:
        command = "dirsearch "
        maps = {
            '-u': u, '-e': e
        }
        command += add_args(maps)
        # 指定默认字典
        command += '-w D:/安全工具/web渗透工具/字典/web目录.txt'
        run_command(command)
        return command

    def sqlmap(self, u, r, batch: bool, dbs, D, tables, T, columns, C, dump, random_agent, H, technique, string, sql_shell, tamper, o, current_user, level, data, skip_urlencode, shell, update, list_tampers, cookie, proxy, purge, v, m, g, second_url, dbms, threads, forms, alert, is_dba) -> str:
        command = 'python D:/安全工具/web渗透工具/sqlmap/sqlmap.py '
        maps = {
            '-u': u, '-r': r, '--batch': batch, '--dbs': dbs, '-D': D, '--tables': tables,
            '--columns': columns, '-T': T, '-C': C, '--dump': dump, '--random-agent': random_agent,
            '-H': H, '--technique': technique, '--string': string, '--sql-shell': sql_shell,
            '--tamper': tamper, '-o': o, '--current-user': current_user, '--level': level,
            '--data': data, '--skip-urlencode': skip_urlencode, '--shell': shell, '--update': update,
            '--list-tampers': list_tampers, '--cookie': cookie, '--proxy': proxy, '--purge': purge,
            '-v': v, '-m': m, '-g': g, '--second-url': second_url, '--dbms': dbms,
            '--threads': threads, '--forms': forms, '--alert': alert, '--is-dba': is_dba
        }
        command += add_args(maps)
        run_command(command)
        return command

    def flask_decode(self, c: str, s: str) -> str:
        command = 'python D:/安全工具/web渗透工具/flask-session-cookie-manager/flask_session_cookie_manager3.py decode '
        maps = {
            '-c': c, '-s': s
        }
        command += add_args(maps)
        run_command(command)
        return command

    def flask_encode(self, t: str, s: str) -> str:
        command = "python D:/安全工具/web渗透工具/flask-session-cookie-manager/flask_session_cookie_manager3.py encode "
        maps = {
            '-t': t, '-s': s
        }
        command += add_args(maps)
        run_command(command)
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
