import logging
from datetime import date

import mysql.connector
import xlrd
from PyQt5.QtWidgets import QMessageBox
from mysql.connector import errorcode


def cell2str(book, cell):
    if cell.ctype == xlrd.XL_CELL_NUMBER and int(cell.value) == cell.value:
        xf = book.xf_list[cell.xf_index]
        format_str = book.format_map[xf.format_key].format_str
        int_str = str(int(cell.value))
        if all(x == "0" for x in format_str):
            return "0" * (len(format_str) - len(int_str)) + int_str
        else:
            return int_str
    else:
        return str(cell.value)


def cell2date(cell):
    value = cell.value
    date_str = str(value)
    try:
        if date_str and not date_str.isspace():
            tmp = xlrd.xldate_as_tuple(value, 0)
            return date(year=tmp[0], month=tmp[1], day=tmp[2])
        return None
    except Exception as e:
        logging.warning("Unexpected Cell: {}, Error: {}".format(cell, e))


def read_sheets(_query_list, _book):
    for sheet in _book.sheets():
        try:
            read_rows(_query_list, _book, sheet)
        except Exception as e:
            raise Exception("表单{}: {}".format(sheet.name, e))


def append_chan_gao_query(
    _query_list,
    book,
    sheet,
    row_index,
    mu_yang_hao,
    gong_yang_hao,
    peng_hao,
    lan_hao,
    duan_nai_ri_qi,
):
    tai_ci = cell2str(book, sheet.cell(row_index, 4))
    pei_zhong_ri_qi = cell2date(sheet.cell(row_index, 5))
    chan_gao_ri_qi = cell2date(sheet.cell(row_index, 6))
    chan_gao = cell2str(book, sheet.cell(row_index, 7))
    huo_gao = cell2str(book, sheet.cell(row_index, 8))
    chan_gao_hao = str(chan_gao_ri_qi) + mu_yang_hao + gong_yang_hao

    query_index = "insert into chan_gao ("
    query_values = ") values ("

    if chan_gao_hao and not chan_gao_hao.isspace():
        query_index += "chan_gao_hao,"
        query_values += '"' + chan_gao_hao + '",'
    if peng_hao and not peng_hao.isspace():
        query_index += "peng_hao,"
        query_values += '"' + peng_hao + '",'
    if lan_hao and not lan_hao.isspace():
        query_index += "lan_hao,"
        query_values += '"' + lan_hao + '",'
    if mu_yang_hao and not mu_yang_hao.isspace():
        query_index += "mu_yang_hao,"
        query_values += '"' + mu_yang_hao + '",'
    if gong_yang_hao and not gong_yang_hao.isspace():
        query_index += "gong_yang_hao,"
        query_values += '"' + gong_yang_hao + '",'
    if tai_ci and not tai_ci.isspace():
        query_index += "tai_ci,"
        query_values += tai_ci + ","
    if pei_zhong_ri_qi:
        query_index += "pei_zhong_ri_qi,"
        query_values += '"' + str(pei_zhong_ri_qi) + '",'
    if chan_gao_ri_qi:
        query_index += "chan_gao_ri_qi,"
        query_values += '"' + str(chan_gao_ri_qi) + '",'
    if chan_gao and not chan_gao.isspace():
        query_index += "chan_gao,"
        query_values += chan_gao + ","
    if huo_gao and not huo_gao.isspace():
        query_index += "huo_gao,"
        query_values += huo_gao + ","
    if duan_nai_ri_qi:
        query_index += "duan_nai_ri_qi,"
        query_values += '"' + str(duan_nai_ri_qi) + '",'

    query_index = query_index[:-1]
    query_values = query_values[:-1]
    _query_list.append(query_index + query_values + ");")

    return chan_gao_hao


def append_yang_query(
    _query_list, book, sheet, row_index, row_offset, col_offset, chan_gao_hao
):
    bian_hao = cell2str(book, sheet.cell(row_index + row_offset, 9 + col_offset * 3))
    if not bian_hao or bian_hao.isspace():
        return
    chu_sheng_zhong = str(sheet.cell(row_index + row_offset, 10 + col_offset * 3).value)
    duan_nai_zhong = str(sheet.cell(row_index + row_offset, 11 + col_offset * 3).value)

    query_index = "insert into yang ("
    query_values = ") values ("

    if bian_hao and not bian_hao.isspace():
        query_index += "bian_hao,"
        query_values += '"' + bian_hao + '",'
    if chan_gao_hao and not chan_gao_hao.isspace():
        query_index += "chan_gao_hao,"
        query_values += '"' + chan_gao_hao + '",'
    query_index += "xing_bie,"
    if col_offset == 0:
        query_values += '"公",'
    elif col_offset == 1:
        query_values += '"母",'
    try:
        float(chu_sheng_zhong)
        query_index += "chu_sheng_zhong,"
        query_values += chu_sheng_zhong + ","
    except:
        if chu_sheng_zhong and not chu_sheng_zhong.isspace():
            query_index += "chu_sheng_zhong,"
            query_values += "-1,"
    try:
        float(duan_nai_zhong)
        query_index += "duan_nai_zhong,"
        query_values += duan_nai_zhong + ","
    except:
        if duan_nai_zhong and not duan_nai_zhong.isspace():
            query_index += "duan_nai_zhong,"
            query_values += "-1,"

    query_index = query_index[:-1]
    query_values = query_values[:-1]
    _query_list.append(query_index + query_values + ");")


def read_rows(_query_list, _book, _sheet):
    # init some data may not exists every row
    peng_hao = 0
    lan_hao = 0
    duan_nai_ri_qi = None
    for row_index in range(3, _sheet.nrows):
        mu_yang_hao = cell2str(_book, _sheet.cell(row_index, 2))
        gong_yang_hao = cell2str(_book, _sheet.cell(row_index, 3))
        if (
            not mu_yang_hao
            or not gong_yang_hao
            or mu_yang_hao.isspace()
            or gong_yang_hao.isspace()
        ):
            continue
        # update peng_hao
        peng_hao_tmp = cell2str(_book, _sheet.cell(row_index, 0))
        if peng_hao_tmp and not peng_hao_tmp.isspace():
            peng_hao = peng_hao_tmp
        # update lan_hao
        lan_hao_tmp = cell2str(_book, _sheet.cell(row_index, 1))
        if lan_hao_tmp and not lan_hao_tmp.isspace():
            lan_hao = lan_hao_tmp
        # update duan_nai_ri_qi
        duan_nai_ri_qi_tmp = cell2date(_sheet.cell(row_index, 15))
        if duan_nai_ri_qi_tmp:
            duan_nai_ri_qi = duan_nai_ri_qi_tmp

        chan_gao_hao = append_chan_gao_query(
            _query_list,
            _book,
            _sheet,
            row_index,
            mu_yang_hao,
            gong_yang_hao,
            peng_hao,
            lan_hao,
            duan_nai_ri_qi,
        )
        for row_offset in range(0, 2):
            for col_offset in range(0, 2):
                if row_index + row_offset >= _sheet.nrows:
                    continue
                append_yang_query(
                    _query_list,
                    _book,
                    _sheet,
                    row_index,
                    row_offset,
                    col_offset,
                    chan_gao_hao,
                )


def save_query_list(_query_list, main_window):
    try:
        cnx = mysql.connector.connect(
            user=main_window.USER,
            password=main_window.PASSWD,
            database="pang_da_nong_ye",
            host="127.0.0.1",
        )
        cursor = cnx.cursor()
        for query in _query_list:
            try:
                cursor.execute(query)
                cnx.commit()
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_PARSE_ERROR:
                    QMessageBox.information(main_window, "数据库错误", "无数据输入。\n" + query)
                elif err.errno == errorcode.ER_DUP_ENTRY:
                    QMessageBox.information(main_window, "数据库错误", "产羔号或编号重复。\n" + query)
                elif err.errno == errorcode.ER_BAD_FIELD_ERROR:
                    QMessageBox.information(main_window, "数据库错误", "数据类型有误。\n" + query)
        cursor.close()
        cnx.close()
        QMessageBox.information(main_window, "从表格导入数据", "导入成功。")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            QMessageBox.information(main_window, "数据库错误", "登录数据库错误。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            QMessageBox.information(main_window, "数据库错误", "数据库不存在。")
        else:
            QMessageBox.information(main_window, "数据库错误", str(err))


def add_from_sheet(str_path, main_window):
    logging.info("To Read From: {}".format(str_path))
    book = xlrd.open_workbook(str_path, formatting_info=True)

    query_list = []
    try:
        read_sheets(query_list, book)
    except Exception as e:
        QMessageBox.information(main_window, "表格数据有误", str(e))
        return

    if not query_list:
        QMessageBox.information(main_window, "从表格导入数据", "无数据。")
        return

    save_query_list(query_list, main_window)
