"""
PDF_kayotin_main - 一个处理PDF文件的Python程序

Author: ahjiang
Date 2023/3/30
Update：2023/4/5
"""

import PyPDF2
import kayotin_tools
from pathlib import Path


def get_files():
    while True:
        source_src = Path(input("请输入源文件夹完整路径："))
        if source_src.exists():
            break
        else:
            print("您输入的路径有误，请重新输入--->\n")
    files = source_src.glob("*.pdf")
    return files


def turn_pdf():
    """
    指定文件名和旋转角度，旋转PDF文件
    :return: 无返回值
    """
    # 指定文件名
    print("请将要翻转的pdf文件放在一个文件夹下-->\n")
    files = get_files()
    # 指定翻转的角度，顺时针
    print("""
    请选择您要旋转的角度--->\n
    例如：90 表示顺时针旋转90度--->
    """)
    point = int(input("请输入："))

    for file in files:
        try:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()
            for page_num in range(len(reader.pages)):
                current_page = reader.pages[page_num]
                current_page.rotate(point)
                writer.add_page(current_page)
            with open(f"output/fixed_{file.name}", "wb") as fixed_file:
                writer.write(fixed_file)
                print(f"已旋转{file.name},保存在output文件夹中")
        except FileNotFoundError:
            print("读取文件失败\n请确认文件是否存在，或文件名是否正确--->")
            return False
    input("请摁回车键退出，或直接关闭程序--->")


def encrypt_pdf():
    """
    对指定文件夹的所有PDF加密
    :return:无返回值
    """
    print("请将要加密的文件夹放在一个文件夹下--->\n")
    encrypt_pwd = random_pwd()

    files = get_files()
    for pdf_file in files:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_writer = PyPDF2.PdfWriter()
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])
        pdf_writer.encrypt(encrypt_pwd)
        with open(f"encrypted/已加密_{pdf_file.name}", "wb") as file:
            pdf_writer.write(file)
            print(f"{pdf_file.name}已加密,密码是：{encrypt_pwd}\n")
    input("已加密的PDF文件放在encrypted文件夹下，请妥善保存密码。\n摁回车键退出--->")


def mark_pdf():
    print("请将水印文件放在temp文件夹下,并将要加水印的pdf文件放在一个文件夹中--->\n")
    print("您可以参考temp/kayotin_temp.docx自己制作一个，然后保存为PDF--->\n")
    mark_temp = f'temp/{input("请输入水印文件名(不包含后缀)：")}.pdf'
    water_mark = PyPDF2.PdfReader(mark_temp).pages[0]

    files = get_files()
    for pdf_file in files:
        reader1 = PyPDF2.PdfReader(pdf_file)
        writer = PyPDF2.PdfWriter()
        for page_num in range(len(reader1.pages)):
            current_page = reader1.pages[page_num]
            current_page.merge_page(water_mark)
            writer.add_page(current_page)

        with open(f"output/已加水印_{pdf_file.name}", "wb") as file:
            writer.write(file)
        print(f"成功对{pdf_file.name}加了水印，保存在output中\n")
        input("请摁回车键退出，或直接关闭程序--->")


def join_pdf():
    file_join = PyPDF2.PdfMerger()
    files = get_files()
    for file in files:
        file_join.append(file)
    file_join.write("output/已合并.pdf")


def dir_check():
    paths = ["encrypted/", "output/", "temp/"]
    for path in paths:
        dir_path = Path(path)
        if dir_path.exists():
            pass
        else:
            Path.mkdir(dir_path)


def cut_file():
    pass


random_pwd = kayotin_tools.kayotin.random_password
choose_type = {
    "1": turn_pdf,
    "2": encrypt_pdf,
    "3": mark_pdf,
    "4": join_pdf,
    "5": cut_file
}


if __name__ == '__main__':
    dir_check()
    print("""
    请选择您要进行哪种操作：\n
    1：翻转PDF文件\n
    2：对PDF文件加密\n
    3：加水印\n
    4：合并PDF文件\n
    5: PDF分页
    """)
    op_num = str(input("请输入："))
    choose_type[op_num]()
