"""
PDF_kayotin_main - 一个处理PDF文件的Python程序

Author: ahjiang
Date 2023/3/30
"""

import PyPDF2
from PyPDF2 import PaperSize
from PyPDF2 import PageObject
import kayotin_tools


def turn_pdf():
    # 指定文件名
    print("请将pdf文件放在resources文件夹下-->\n")
    filename = str(input("请输入文件名,不包括文件类型："))

    # 指定翻转的角度，顺时针
    print("""
    请选择您要旋转的角度--->\n
    例如：90 表示顺时针旋转90度--->
    """)
    point = int(input("请输入："))
    try:
        reader = PyPDF2.PdfReader(f"resources/{filename}.pdf")
        writer = PyPDF2.PdfWriter()
        for page_num in range(len(reader.pages)):
            current_page = reader.pages[page_num]
            current_page.rotate(point)
            writer.add_page(current_page)
        with open(f"output/{filename}_fixed.pdf", "wb") as file:
            writer.write(file)
    except FileNotFoundError:
        print("读取文件失败\n请确认文件是否存在，或文件名是否正确--->")
        return False


def encrypt_pdf():
    pass


def mark_pdf():
    pass


random_pwd = kayotin_tools.kayotin.random_password
choose_type = {
    "1": turn_pdf,
    "2": encrypt_pdf,
    "3": mark_pdf
}


if __name__ == '__main__':
    # print("""
    # 请选择您要进行哪种操作：\n
    # 1：翻转PDF文件\n
    # 2：对PDF文件加密\n
    # 3：加水印\n
    # """)
    # op_num = input("请输入：")
    turn_pdf()




