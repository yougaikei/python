# 获取当前目录下的 nf.config.json 文件
import os
filename = os.path.join(os.getcwd(), 'nf.config.json')
filecontent = """{
    "default": 0,
    "name": "create-file",
    "version": "1.0.0",
    "description": "create file",
    "type": "python",
    "author": "huzixuan"   
}"""

# 判断文件是否存在; true: 读取内部内容; false: 创建文件
if os.path.exists(filename):
    with open(filename, 'r') as f:
        # 获取内部 default 的值, 截至到第一个逗号
        defNum = f.read().split('"default":')[1].split(',')[0]
        # 将 default 的值转换为 int 类型
        defNum = int(defNum) + 1
        # 将 default 的值替换为 defNum 写入文件
        filecontent = filecontent.replace('0', str(defNum))
        with open(filename, 'w') as f:
            f.write(filecontent)
        # 创建文件夹: File- + defNum
        if defNum < 10:
            os.mkdir('File-0' + str(defNum))
        else:
            os.mkdir('File-' + str(defNum))
        
else:
    print('文件不存在')
    with open(filename, 'w') as f:
        f.write(filecontent)

print(filename)
# 点击任意键退出
input('Press any key to exit')