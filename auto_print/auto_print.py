"""
auto_print - 按时间顺序批量打印所选文件夹的pdf
需要安装 pip install pypiwin32

Author: hanayo
Date： 2024/2/5
"""

from PDF_kayotin_main import get_files
import win32print
import win32api
import time


class PrintPDF:
    def __init__(self, desc=False):
        self.files = get_files()
        self.print_name = win32print.GetDefaultPrinter()
        self.handle = win32print.OpenPrinter(self.print_name)
        if self.print_name == "":
            print("请设置默认打印机")
            return

        self.sort_file_by_time(desc)
        print(f"打印完毕，本次共打印{len(self.files)}个文件")

    def sort_file_by_time(self, desc):
        file_dict = dict()
        for file in self.files:
            file_dict[file] = file.stat().st_mtime
        res = sorted(file_dict.keys(), key=file_dict.get, reverse=desc)
        print("开始打印------")
        for r in res:
            print("正在打印：", r)
            self.print_file(r)

    def print_file(self, file):
        file = str(file)
        win32api.ShellExecute(0, "print", file, '/d:"%s"' % self.print_name, ".", 0)
        time.sleep(2)
        tasks = win32print.EnumJobs(self.handle, 0, -1, 1)
        if tasks:
            print("打印阻塞，请稍等")
        while tasks:
            time.sleep(1)
            tasks = win32print.EnumJobs(self.handle, 0, -1, 1)


if __name__ == '__main__':
    my_pdf_printer = PrintPDF()

    # # 获取默认打印机名称，例如"3009"
    # print_name = win32print.GetDefaultPrinter()
    # # 获取打印机的句柄，或者说进程
    # handle = win32print.OpenPrinter(print_name)
    # # 获取打印机当前状态
    # status = win32print.GetPrinter(handle, 2)['Status']
    # print("当前状态", status)
    # # 获取当前打印机任务
    # tasks = win32print.EnumJobs(handle, 0, -1, 1)
    # # 执行打印，注意第三个参数是字符串，如果是完整文件路径请转换成字符串
    # win32api.ShellExecute(0, "print", "FT_CN000445148884.pdf", '/d:"%s"' % print_name, ".", 0)

