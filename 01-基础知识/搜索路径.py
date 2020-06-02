""" 
1. 设置PYTHONPATH环境变量
2. 添加.pth文件
3. 通过sys.path设置路径
4. 如果使用PyCharm，可以直接设置搜索路径 
"""
import sys
sys.path.append('/MyStudio/video_demo/csdn_python1/src/01-基础知识/modules')
import working

print(working.greet('Bill'))