# _*_ coding: utf-8 _*_
# @Time : 2020/12/31 9:44 
# @Author : 廖郡 
# @Version：V 0.1
# @File : get_excel.py
# @desc : 获取接口测试有效接口
import os

import xlrd


class TestCaseData:
    # 所有的excel测试用例集
    _excel_cases = None

    @classmethod
    def getExcelCases(cls):
        """
        获取excel文件中的测试用例集合
        :return:
        """
        if cls._excel_cases is None:
            cls._excel_cases = cls.paarseExcelCaseData()

        return cls._excel_cases

    @classmethod
    def paarseExcelCaseData(cls):
        """
        加载测试用例数据
        :return:
        """
        url = 'E://python_work//V1.0.1//test_case/test_case.xlsx'
        wb = xlrd.open_workbook(url)  # 打开excel
        sh = wb.sheet_by_name("user_login")  # 按工作簿名定位工作表
        datas = []
        for i in range(1, sh.nrows):
            data = dict(zip(sh.row_values(0), sh.row_values(i)))
            datas.append(data)
        return datas


if __name__ == '__main__':
    print(os.getcwd())
    excel_datas = TestCaseData.getExcelCases()
    print(excel_datas)
