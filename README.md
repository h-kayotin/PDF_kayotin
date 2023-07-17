# PDF_kayotin
对pdf进行处理，加密、翻转、加水印、合并。

### Start

工作中总是遇到很多需要处理PDF的情况，比如加密、翻转，等等。

虽然大多数情况某些pdf的软件就可以做到，比如foxreader。

但是还是试着用python做一个多合一的工具

目前有以下功能，运行主程序即可， 

注意选择的是文件夹，会对该文件夹所有pdf文件执行操作。

    1：翻转PDF文件
    2：对PDF文件加密
    3：加水印
    4：合并PDF文件
    5：PDF文件分页

需要以下依赖库
```python
pip install PyPDF2
pip install pathlib
````

可以直接下载Releases版本运行