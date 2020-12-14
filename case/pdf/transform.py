from PyPDF2 import PdfFileReader, PdfFileWriter

def listPages(pdf_path):
    # pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)
    # 向右旋转90度
    page_1 = pdf_reader.getPage(0).rotateClockwise(90)
    # pdf_writer.addPage(page_1)
    # 向左旋转90度
    page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
    # pdf_writer.addPage(page_2)
    # 在正常方向上添加一页
    # pdf_writer.addPage(pdf_reader.getPage(2))


pdf_path = "/Users/zifang/Downloads/现代西班牙语1.pdf"
listPages(pdf_path)


