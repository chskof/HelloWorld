import myModule      # 导入模块 红线报错原因:目录下import其他模块，会出现No model named ...的报错，但实际可以运行 这是因为PyCharm不会将当前文件目录自动加入source_path


myModule.myPrint("TestImport!")