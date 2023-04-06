"""
PDF_kayotin_main - 一个处理PDF文件的Python程序

Author: ahjiang
Date 2023/3/30
Update：2023/4/5
"""

import PyPDF2
from PyPDF2 import PaperSize
from PyPDF2 import PageObject
import kayotin_tools
from pathlib import Path


def turn_pdf():
    """
    指定文件名和旋转角度，旋转PDF文件
    :return: 无返回值
    """
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
    """
    对指定文件夹的所有PDF加密
    :return:无返回值
    """
    print("请将要加密的文件夹放在resources文件夹下--->\n")
    encrypt_pwd = random_pwd()
    src_folder = Path("resources/")

    files = list(src_folder.glob("*"))
    for pdf_file in files:
        pdf_reader = PyPDF2.PdfReader(f"resources/{pdf_file.name}")
        pdf_writer = PyPDF2.PdfWriter()
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])
        pdf_writer.encrypt(encrypt_pwd)
        with open(f"encrypted/已加密_{pdf_file.name}", "wb") as file:
            pdf_writer.write(file)
            print(f"{pdf_file.name}已加密,随机密码是：{encrypt_pwd}\n")
    input("已加密的PDF文件放在encrypted文件夹下，\n请摁回车键退出--->")


def mark_pdf():
    print("请将水印文件放在temp文件夹下,并将要加水印的pdf文件放在resources文件夹中--->\n")
    print("您可以参考resources/kayotin_temp.docx自己制作一个，然后保存为PDF--->\n")
    mark_temp = f'temp/{input("请输入水印文件名(不包含后缀)：")}.pdf'
    water_mark = PyPDF2.PdfReader(mark_temp).pages[0]

    src_folder = Path("resources/")
    files = list(src_folder.glob("*"))
    for pdf_file in files:
        reader1 = PyPDF2.PdfReader(f"resources/{pdf_file.name}")
        writer = PyPDF2.PdfWriter()
        for page_num in range(len(reader1.pages)):
            current_page = reader1.pages[page_num]
            current_page.merge_page(water_mark)
            writer.add_page(current_page)

        with open(f"output/已加水印_{pdf_file.name}", "wb") as file:
            writer.write(file)
        print(f"成功对{pdf_file.name}加了水印，保存在output中")


def join_pdf():
    pass


random_pwd = kayotin_tools.kayotin.random_password
choose_type = {
    "1": turn_pdf,
    "2": encrypt_pdf,
    "3": mark_pdf,
    "4": join_pdf
}


if __name__ == '__main__':
    print("""
    请选择您要进行哪种操作：\n
    1：翻转PDF文件\n
    2：对PDF文件加密\n
    3：加水印\n
    """)
    op_num = str(input("请输入："))
    choose_type[op_num]()







