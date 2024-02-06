"""
combin_for_print - 

Author: hanayo
Date： 2024/2/6
"""

from PDF_kayotin_main import get_files
import PyPDF2


class CombinPrint:
    def __init__(self, desc=False):
        self.files = get_files()
        self.counts = 0
        self.sort_file_by_time(desc)
        self.check_files()
        self.merger_files()

    def sort_file_by_time(self, desc):
        file_dict = dict()
        for file in self.files:
            file_dict[file] = file.stat().st_mtime
        self.files = sorted(file_dict.keys(), key=file_dict.get, reverse=desc)

    def check_files(self, size=2):
        """检查文件，如果是奇数页，就补足一页空白页"""
        for file in self.files:
            reader = PyPDF2.PdfReader(file)
            if len(reader.pages) % size:
                writer = PyPDF2.PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)
                writer.add_blank_page()
                with open(file, mode='wb') as new_file:
                    writer.write(new_file)

    def merger_files(self):
        """合并到一个pdf中"""
        file_join = PyPDF2.PdfMerger()
        for file in self.files:
            file_join.append(file)
            self.counts += 1
        file_join.write("已合并.pdf")
        print("pdf文件合并已完成---")
        print(f"本次共合并{self.counts}个pdf文件^ ^")


if __name__ == '__main__':
    CombinPrint()
