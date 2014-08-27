import mysql.connector
from mysql.connector import errorcode
from PyQt5.QtWidgets import *


def avg_CHU_SHENG_DUAN_NAI_ZHONG(QWidget):
    text, ok = QInputDialog.getText(QWidget, '出生重，断奶重平均值', '请输入棚号：', QLineEdit.Normal)

    if ok and text and not text.isspace():
        try:
            cnx = mysql.connector.connect(user='root', database='test')
            cursor = cnx.cursor()
            cursor.execute(
                'select chu_sheng_zhong,duan_nai_zhong from yang where chan_gao_hao in ' +
                '(select chan_gao_hao from chan_gao where peng_hao="' + text + '");')

            avg = cursor.fetchall()
            # print(avg)

            cursor.close()
            cnx.close()

            CHU_SHENG_ZHONG = []
            DUAN_NAI_ZHONG = []
            for avg_item in avg:
                if avg_item[0] and avg_item[0] > 0:
                    CHU_SHENG_ZHONG.append(avg_item[0])
                if avg_item[1] and avg_item[1] > 0:
                    DUAN_NAI_ZHONG.append(avg_item[1])

            QMessageBox.information(QWidget, '出生重，断奶重平均值',
                                    u'出生重平均：{0:.2f}（{1:d}只）\n断奶重平均：{2:.2f}（{3:d}只）'.format(
                                        sum(CHU_SHENG_ZHONG) / len(CHU_SHENG_ZHONG),
                                        len(CHU_SHENG_ZHONG),
                                        sum(DUAN_NAI_ZHONG) / len(DUAN_NAI_ZHONG),
                                        len(DUAN_NAI_ZHONG)))

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                QMessageBox.information(QWidget, '数据库错误', '登录数据库错误。')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                QMessageBox.information(QWidget, '数据库错误', '数据库不存在。')
            elif err.errno == errorcode.ER_NO_SUCH_TABLE:
                QMessageBox.information(QWidget, '数据库错误', '表单不存在。')
            else:
                QMessageBox.information(QWidget, '数据库错误', str(err))
    else:
        if ok:
            QMessageBox.information(QWidget, '输入错误', '无棚号输入。')