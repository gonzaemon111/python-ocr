from PIL import Image
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
print(tools)
print(type(tools))
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
print(tool)

txt = tool.image_to_string( # ここでOCRの対象や言語，オプションを指定する
    Image.open('test.png'),
    lang='eng',
    builder=pyocr.builders.TextBuilder()
)
print(txt)

