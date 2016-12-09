import xlrd
from datetime import date
import mysql.connector
from mysql.connector import errorcode
from PyQt5.QtWidgets import QMessageBox


def cell2str(book, cell):
    if cell.ctype == xlrd.XL_CELL_NUMBER and int(cell.value) == cell.value:
        xf = book.xf_list[cell.xf_index]
        format = book.format_map[xf.format_key]
        format_str = format.format_str
        int_str = str(int(cell.value))
        if all(x=='0' for x in format_str):
            return '0' * (len(format_str) - len(int_str)) + int_str
        else:
            return int_str
    else:
        return str(cell.value)


def add_from_sheet(str_path, main_window):
    book = xlrd.open_workbook(str_path, formatting_info=True)

    mysql_query = []

    for sheet in book.sheets():
        peng_hao = 0
        lan_hao = 0
        duan_nai_ri_qi = 0

        for row_index in range(3, sheet.nrows):
            mu_yang_hao = cell2str(book, sheet.cell(row_index, 2))
            gong_yang_hao = cell2str(book, sheet.cell(row_index, 3))
            if mu_yang_hao and gong_yang_hao and not mu_yang_hao.isspace() and not gong_yang_hao.isspace():
                try:
                    # print(sheet.name,row_index)
                    # peng_hao
                    peng_hao_tmp = cell2str(book, sheet.cell(row_index, 0))
                    if peng_hao_tmp and not peng_hao_tmp.isspace():
                        peng_hao = peng_hao_tmp
                    # lan_hao
                    lan_hao_tmp = cell2str(book, sheet.cell(row_index, 1))
                    if lan_hao_tmp and not lan_hao_tmp.isspace():
                        lan_hao = lan_hao_tmp
                    # tai_ci
                    tai_ci = cell2str(book, sheet.cell(row_index, 4))
                    # pei_zhong_ri_qi
                    pei_zhong_ri_qi = str(sheet.cell(row_index, 5).value)
                    if pei_zhong_ri_qi and not pei_zhong_ri_qi.isspace():
                        pei_zhong_ri_qi = xlrd.xldate_as_tuple(sheet.cell(row_index, 5).value, 0)
                        pei_zhong_ri_qi = date(year=pei_zhong_ri_qi[0], month=pei_zhong_ri_qi[1],
                                               day=pei_zhong_ri_qi[2])
                    # chan_gao_ri_qi
                    chan_gao_ri_qi = str(sheet.cell(row_index, 6).value)
                    if chan_gao_ri_qi and not chan_gao_ri_qi.isspace():
                        chan_gao_ri_qi = xlrd.xldate_as_tuple(sheet.cell(row_index, 6).value, 0)
                        chan_gao_ri_qi = date(year=chan_gao_ri_qi[0], month=chan_gao_ri_qi[1], day=chan_gao_ri_qi[2])
                    # chan_gao
                    chan_gao = cell2str(book, sheet.cell(row_index, 7))
                    # huo_gao
                    huo_gao = cell2str(book, sheet.cell(row_index, 8))
                    # duan_nai_ri_qi
                    duan_nai_ri_qi_tmp = str(sheet.cell(row_index, 15).value)
                    if duan_nai_ri_qi_tmp and not duan_nai_ri_qi_tmp.isspace():
                        duan_nai_ri_qi = xlrd.xldate_as_tuple(sheet.cell(row_index, 15).value, 0)
                        duan_nai_ri_qi = date(year=duan_nai_ri_qi[0], month=duan_nai_ri_qi[1], day=duan_nai_ri_qi[2])
                    # chan_gao_hao
                    chan_gao_hao = str(chan_gao_ri_qi) + mu_yang_hao + gong_yang_hao
                    # print(chan_gao_hao, peng_hao, lan_hao, mu_yang_hao, gong_yang_hao, tai_ci, pei_zhong_ri_qi,
                    #       chan_gao_ri_qi, chan_gao, huo_gao, duan_nai_ri_qi)

                    query_index = 'insert into chan_gao ('
                    query_values = ') values ('

                    if chan_gao_hao and not chan_gao_hao.isspace():
                        query_index += 'chan_gao_hao,'
                        query_values += '"' + chan_gao_hao + '",'
                    if peng_hao and not peng_hao.isspace():
                        query_index += 'peng_hao,'
                        query_values += '"' + peng_hao + '",'
                    if lan_hao and not lan_hao.isspace():
                        query_index += 'lan_hao,'
                        query_values += '"' + lan_hao + '",'
                    if mu_yang_hao and not mu_yang_hao.isspace():
                        query_index += 'mu_yang_hao,'
                        query_values += '"' + mu_yang_hao + '",'
                    if gong_yang_hao and not gong_yang_hao.isspace():
                        query_index += 'gong_yang_hao,'
                        query_values += '"' + gong_yang_hao + '",'
                    if tai_ci and not tai_ci.isspace():
                        query_index += 'tai_ci,'
                        query_values += tai_ci + ','
                    if str(pei_zhong_ri_qi) and not str(pei_zhong_ri_qi).isspace():
                        query_index += 'pei_zhong_ri_qi,'
                        query_values += '"' + str(pei_zhong_ri_qi) + '",'
                    if str(chan_gao_ri_qi) and not str(chan_gao_ri_qi).isspace():
                        query_index += 'chan_gao_ri_qi,'
                        query_values += '"' + str(chan_gao_ri_qi) + '",'
                    if chan_gao and not chan_gao.isspace():
                        query_index += 'chan_gao,'
                        query_values += chan_gao + ','
                    if huo_gao and not huo_gao.isspace():
                        query_index += 'huo_gao,'
                        query_values += huo_gao + ','
                    if str(duan_nai_ri_qi) and not str(duan_nai_ri_qi).isspace():
                        query_index += 'duan_nai_ri_qi,'
                        query_values += '"' + str(duan_nai_ri_qi) + '",'

                    query_index = query_index[:-1]
                    query_values = query_values[:-1]
                    mysql_query.append(query_index + query_values + ');')

                    for row_offset in range(0, 2):
                        for col_offset in range(0, 2):
                            if row_index + row_offset < sheet.nrows:
                                bian_hao = cell2str(book, sheet.cell(row_index + row_offset, 9 + col_offset * 3))
                                if bian_hao and not bian_hao.isspace():
                                    chu_sheng_zhong = str(sheet.cell(row_index + row_offset, 10 + col_offset * 3).value)
                                    duan_nai_zhong = str(sheet.cell(row_index + row_offset, 11 + col_offset * 3).value)
                                    # print('\t', bian_hao, chan_gao_hao, '公', chu_sheng_zhong, duan_nai_zhong)

                                    query_index = 'insert into yang ('
                                    query_values = ') values ('

                                    if bian_hao and not bian_hao.isspace():
                                        query_index += 'bian_hao,'
                                        query_values += '"' + bian_hao + '",'
                                    if chan_gao_hao and not chan_gao_hao.isspace():
                                        query_index += 'chan_gao_hao,'
                                        query_values += '"' + chan_gao_hao + '",'
                                    query_index += 'xing_bie,'
                                    if col_offset == 0:
                                        query_values += '"公",'
                                    elif col_offset == 1:
                                        query_values += '"母",'
                                    try:
                                        float(chu_sheng_zhong)
                                        query_index += 'chu_sheng_zhong,'
                                        query_values += chu_sheng_zhong + ','
                                    except:
                                        if chu_sheng_zhong and not chu_sheng_zhong.isspace():
                                            query_index += 'chu_sheng_zhong,'
                                            query_values += '-1,'
                                    try:
                                        float(duan_nai_zhong)
                                        query_index += 'duan_nai_zhong,'
                                        query_values += duan_nai_zhong + ','
                                    except:
                                        if duan_nai_zhong and not duan_nai_zhong.isspace():
                                            query_index += 'duan_nai_zhong,'
                                            query_values += '-1,'

                                    query_index = query_index[:-1]
                                    query_values = query_values[:-1]
                                    mysql_query.append(query_index + query_values + ');')
                except:
                    QMessageBox.information(main_window, '表格数据有误',
                                            '表单' + str(sheet.name) + '第' + str(row_index + 1) + '行左右存在错误')
                    return

    # print(mysql_query)
    if mysql_query:
        try:
            cnx = mysql.connector.connect(user=main_window.USER,
                                          password=main_window.PASSWD,
                                          database='pang_da_nong_ye',
                                          host='127.0.0.1')
            cursor = cnx.cursor()
            for query in mysql_query:
                try:
                    cursor.execute(query)
                    cnx.commit()
                except mysql.connector.Error as err:
                    print(query)
                    if err.errno == errorcode.ER_PARSE_ERROR:
                        QMessageBox.information(main_window, '数据库错误', '无数据输入。\n' + query)
                    elif err.errno == errorcode.ER_DUP_ENTRY:
                        QMessageBox.information(main_window, '数据库错误', '产羔号或编号重复。\n' + query)
                    elif err.errno == errorcode.ER_BAD_FIELD_ERROR:
                        QMessageBox.information(main_window, '数据库错误', '数据类型有误。\n' + query)
            cursor.close()
            cnx.close()
            QMessageBox.information(main_window, '从表格导入数据', '导入成功。')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                QMessageBox.information(main_window, '数据库错误', '登录数据库错误。')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                QMessageBox.information(main_window, '数据库错误', '数据库不存在。')
            else:
                QMessageBox.information(main_window, '数据库错误', str(err))
    else:
        QMessageBox.information(main_window, '从表格导入数据', '无数据。')