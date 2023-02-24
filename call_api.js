var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
return new bootstrap.Tooltip(tooltipTriggerEl)
})

function dirsearch() {
    var u = dirsearch_u.value;

    pywebview.api.dirsearch(u).then((response) => {
        dirsearch_r.innerHTML = response;
    });
}

function sqlmap() {
    var u = sqlmap_u.value;
    var r = sqlmap_r.value;
    var D = sqlmap_D.value;
    var T = sqlmap_T.value;
    var C = sqlmap_C.value;
    var H = sqlmap_H.value;
    var technique = sqlmap_technique.value;
    var string = sqlmap_string.value;
    var tamper = sqlmap_tamper.value;
    var level = sqlmap_level.value;
    var data = sqlmap_data.value;
    var cookie = sqlmap_cookie.value;
    var proxy = sqlmap_proxy.value;
    var v = sqlmap_v.value;
    var m = sqlmap_m.value;
    var g = sqlmap_g.value;
    var second_url = sqlmap_second_url.value;
    var dbms = sqlmap_dbms.value;
    var threads = sqlmap_threads.value;

    var batch = sqlmap_batch.checked;
    var dbs = sqlmap_dbs.checked;
    var tables = sqlmap_tables.checked;
    var columns = sqlmap_columns.checked;
    var dump = sqlmap_dump.checked;
    var random_agent = sqlmap_random_agent.checked;
    var sql_shell = sqlmap_sql_shell.checked;
    var o = sqlmap_o.checked;
    var current_user = sqlmap_current_user.checked;
    var skip_urlencode = sqlmap_skip_urlencode.checked;
    var shell = sqlmap_shell.checked;
    var update = sqlmap_update.checked;
    var list_tampers = sqlmap_list_tampers.checked;
    var purge = sqlmap_purge.checked;
    var forms = sqlmap_forms.checked;

    pywebview.api.sqlmap(u, r, batch, dbs, D, tables, T, columns, C, dump, random_agent, H, technique, string, sql_shell, tamper, o, current_user, level, data, skip_urlencode, shell, update, list_tampers, cookie, proxy, purge, v, m, g, second_url, dbms, threads, forms).then((response) => {
        sqlmap_res.innerHTML = response;
    });
}

function flask_decode() {
    var c = flask_text.value;
    var s = flask_key.value;

    pywebview.api.flask_decode(c, s).then((response) => {
        flask_decode_res.innerHTML = response;
    });
}

function flask_encode() {
    var t = flask_text.value;
    var s = flask_key.value;

    pywebview.api.flask_encode(t, s).then((response) => {
        flask_encode_res.innerHTML = response;
    });
}
