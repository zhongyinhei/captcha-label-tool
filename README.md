# captcha-label-tool
基於PyQt5的验证码标注工具

## Introduction(简介)
![image](./img/main.png)
这是一个简单的验证码标注工具，在需要手动大量标注验证码是比较方便，而且比较不容易出错。

完成后会在当前目录创建```validate.csv```文件，每一个row是一笔验证码，其中第一个column是图片的文件名，第二个column是该图片标注的验证码。

暂时存档功能，会在当前目录创建```record.json```文件，记录当前标注的位置，以及已经标注好了的csv文件。下次继续标注时，可以选择继续完成上次未完成的标注任务。在需要标注大量的验证码时，可以分多次完成任务。

如果当前目录存在已经标记完了的```validate.csv```文件，可以选择重复验证选项，对已标注的验证码进行验证。（一般标注完一次，没人会想重复标注第二次吧XD）这个功能一般是让其他人去使用。

|Name|Description|
|:-:|:-:|
|MainWindow.ui|使用QtDesigner制作的图形化界面|
|MainWindow.py|MainWindow.ui转换的python文件|
|main.py|程序入口，负责所有逻辑部分|
|dist|打包的App文件，可在任何macos系统上执行|

## Dependencies(环境依赖)
|Name|Version|
|:-:|:-:|
|macOS|10.14.2|
|python|3.6.6|
|pyqt5|5.11.2|
|pyInstaller|3.4|

## Running(运行)
转换ui文件到python文件
```pyuic5 MainWindow.ui -o MainWindow.py```

启动
```python main.py```

## APP Bundle(打包成APP)
使用pyInstaller工具进行打包

第一步
```pyinstaller --windowed --clean --noconfirm --onefile main.py```

第二步
```pyinstaller --windowed --clean --noconfirm --onefile main.spec```

打包的时候遇到的一些问题：
1. 我的程序是在Anaconda下开发的，但是如果在此环境下进行pyInstaller打包，会出现PyQt库的依赖问题，与Anaconda下的PyQt库出现冲突。所以后来是在另外的python3.6环境下进行打包的。
2. pyInstaller暂时还不支援python3.7
3. ~~出现```ModuleNotFoundError: No module named 'PyQt5.sip'```这个问题，加上```--hidden-import PyQt5.sip```可以解決。~~
4. 更新完到macOS 10.14.2，重新编译运行时，结果出现下面这个问题
> FileNotFoundError: Tcl data directory "/var/folders/vh/td8y99_d3x591mmjsfr1klm80000gp/T/_MEIHjYohe/tcl" not found.
[20078] Failed to execute script pyi_rth__tkinter

这个问题，在第一步编译时手动加上对应的binary库可以解决。即，

> pyinstaller --windowed --clean --noconfirm --onefile --add-binary="/System/Library/Frameworks/Tk.framework/Tk":"tk" --add-binary="/System/Library/Frameworks/Tcl.framework/Tcl":"tcl" main.py
