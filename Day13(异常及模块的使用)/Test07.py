"""
自定义模块的发布，安装
    1.发布安装自定义的包、模块到系统目录

        创建要发布的包(包中包含对应的模块)

        在统一目录中创建setup.py模块
        setup.py文件中的内容

    2. 找到文件所在位置，执行以下两个命令
        构建模块
            python setup.py build

            使用DOS命令
        打包
            python setup.py sdist

        解压生成的压缩包

        进入解压后的文件夹

        执行
        python setup.py install

"""