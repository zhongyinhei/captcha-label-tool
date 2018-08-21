# captcha-label-tool
基於PyQt5的驗證碼標註工具

## Introduction(簡介)
![image](./img/captcha-label-tool.png)
這是一個簡單的驗證碼標註工具，在需要手動大量標註驗證碼時還蠻方便的，而且比較不容易出錯。

使用時先打開存放驗證碼的目錄，然後設定重複驗證次數，即可開始標記。

完成後會在當前目錄創建```*.csv```文件，每一個row是一筆驗證碼，其中第一個column是圖片的檔名，第二個column是標註的驗證碼。

重複驗證次數如果設為1次，在第一次輸入完所有答案後，會要求重複輸入第2次答案。如果跟前一次輸入不同會提示，要求檢查後輸入確認的答案，這樣可以盡量避免標註錯誤的答案。

暫時存檔功能，會在當前目錄創建```record.txt```，紀錄當前標註的位置，以及當前已經標註答案的csv文件。下次要繼續標註時，會讓你選擇是否繼續完成上次未完成的標註。在需要標註大量的驗證碼時，可以分多次完成任務。

|Name|Description|
|----|----|
|MainWindow.ui|使用QtDesigner製作的圖形化介面|
|MainWindow.py|MainWindow.ui轉換的python文件|
|main.py|程序入口，負責所有邏輯部分|
|dist|打包的App文件，可在任何macos系統上執行|

## Dependencies(環境依賴)
|Name|Version|
|----|----|
|python|3.6.6|
|pyqt5|5.11.2|
|pyInstaller|3.3.1|

## Running(運行)
轉換ui文件到python文件
```pyuic5 MainWindow.ui -o MainWindow.py```

啟動
```python main.py```

## APP Bundle(打包成APP)
使用pyInstaller工具進行打包

第一步
```pyinstaller --windowed --clean --noconfirm --hidden-import PyQt5.sip --onefile main.py```

第二步
```pyinstaller --windowed --clean --noconfirm --onefile main.spec```

打包的時候遇到的一些問題：
1. 我的程序是在Anaconda下開發的，但是如果在此環境下進行pyInstaller打包，會出現PyQt庫的依賴問題，與Anaconda下的PyQt庫出現衝突。所以後來是在另外的python3.6環境進行打包的。
2. pyInstaller暫時還不支援python3.7
3. 出現```ModuleNotFoundError: No module named 'PyQt5.sip'```這個問題，Google一下發現加上```--hidden-import PyQt5.sip```可以解決。
