from PyQt5.QtWidgets import QApplication , QMainWindow, QFileDialog, QDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
import sys, MainWindow, os, string, csv, subprocess

DEFAULT_STYLE = """
QProgressBar{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center
}

QProgressBar::chunk {
    background-color: lightblue;
    width: 10px;
    margin: 1px;
}
"""

class Main(QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.captchaAns = []
        self.files = []
        self.filenames = []
        self.folderPath = ""
        self.progressMax = self.progressNow = self.progressLast = 1
        self.timesMax = self.timesNow = 1
        self.hasError = False
        self.record = False
        self.defaultPath = '/Users/david/file/jupyter/simple-railway-captcha-solver/data/'
        self.extension = ['png', 'jpg', 'jpeg']
        self.progressBar.setStyleSheet(DEFAULT_STYLE)
        self.lineEditInput.setVisible(False)
        self.progressBar.setVisible(False)
        self.pushButtonSave.setVisible(False)
        self.checkBox.setVisible(False)
        self.label.setVisible(False)
        self.lineEditTimes.setVisible(False)
        self.pushButtonStart.setVisible(False)
        self.label_2.setVisible(False)
        self.pushButtonBack.setVisible(False)


    def openFile(self):
        # dialog = QFileDialog(self, '選取文件夾', '/Users/david/file/jupyter/simple-railway-captcha-solver/data/')
        # dialog.setFileMode(QFileDialog.DirectoryOnly)
        # dialog.setNameFilter('Images (*.png *.jpeg *.jpg)')
        # if dialog.exec_() == QDialog.Accepted:
        #     self.files = dialog.selectedFiles()
        #     print(self.files)

        self.folderPath = QFileDialog.getExistingDirectory(self, '選取文件夾', self.defaultPath)
        if self.folderPath:
            for root, dirs, files in os.walk(self.folderPath):
                try:
                    files.sort(key=lambda x: int(x.split('.')[0]))
                except:
                    files.sort()

                #print(files)
                for file in files:
                    filepath = os.path.join(root, file)
                    filename = file.split('.')[0]
                    ext = file.split('.')[1]
                    if ext in self.extension:
                        self.files.append(filepath)
                        self.filenames.append(filename)

            if len(self.files) > 0:
                self.lineEditFile.setText(self.folderPath)
                self.label.setVisible(True)
                self.pushButtonStart.setVisible(True)
                self.pushButtonStart.setEnabled(True)
                self.lineEditTimes.setVisible(True)
                self.lineEditTimes.setEnabled(True)
                self.lineEditTimes.setText('0')
                self.lineEditTimes.setFocus()
                recordPath = self.folderPath + '/record.txt'
                try:
                    r = open(recordPath)
                    self.progressLast = int(r.read())
                    self.checkBox.setVisible(True)
                    self.checkBox.setEnabled(True)
                    self.record = True
                    r.close()
                except:
                    self.record = False
            else:
                QMessageBox.information(self, "提示", "文件夾中沒有圖片")
                self.pushButtonStart.setEnabled(False)
                self.lineEditTimes.setEnabled(False)


    def startLabel(self):
        check = False
        try:
            self.timesMax = int(self.lineEditTimes.text()) + 1
            check = True
        except:
            check = False

        if check and self.timesMax >= 1:
            if self.record and self.checkBox.isChecked():
                self.progressNow = self.progressLast
            elif self.record and not self.checkBox.isChecked():
                cmd1 = "rm " + self.folderPath + '/record.txt'
                subprocess.Popen(cmd1.split())
                cmd2 = "rm " + self.folderPath + '/validate.csv'
                subprocess.Popen(cmd2.split())
                self.record = False
                self.progressNow = 1
            else:
                self.progressNow = 1
            self.progressMax = len(self.files)
            self.timesNow = 1
            image = QImage(self.files[self.progressNow-1])
            self.labelPic.setPixmap(QPixmap.fromImage(image))
            self.setProgressLabel()
            self.progressBar.setMaximum(self.progressMax * self.timesMax)
            self.progressBar.setValue(self.progressNow-1)
            self.pushButtonOpen.setEnabled(False)
            self.lineEditTimes.setEnabled(False)
            self.pushButtonStart.setEnabled(False)
            self.checkBox.setEnabled(False)
            self.lineEditInput.setVisible(True)
            self.lineEditInput.setEnabled(True)
            self.lineEditInput.setFocus()
            self.progressBar.setVisible(True)
            self.pushButtonSave.setVisible(True)
            self.pushButtonSave.setEnabled(True)
            self.pushButtonBack.setVisible(True)
            self.label_2.setVisible(True)
            self.setTimesLabel()
            if self.record:
                self.pushButtonBack.setEnabled(False)
        else:
            QMessageBox.information(self, "提示", "重複驗證次數至少為0或以上")


    def nextPic(self):
        check = True
        text = self.lineEditInput.text()
        for c in text:
            if c not in (string.ascii_letters + string.digits):
                check = False
                break

        if check:
            if len(text) >= 5 and len(text) <= 6:
                text = text.upper()
                if self.checkAns(text):
                    self.switch2NextPic()
                    self.progressBar.setValue(self.progressBar.value()+1)
                else:
                    s = "你輸入的跟前一次{}不同，請檢查後再送出確認的答案，答案將以這次送出的為主" \
                        "。".format(self.captchaAns[self.progressNow-1])
                    QMessageBox.information(self, "提示", s)
            else:
                QMessageBox.information(self, "提示", "驗證碼是5位或6位")
        else:
            QMessageBox.information(self, "提示", "請輸入數字或字母")


    def checkAns(self, text):
        if self.timesNow == 1:
            self.captchaAns.append(text)
            return True
        else:
            if text == self.captchaAns[self.progressNow-1]:
                return True
            elif self.hasError:
                self.hasError = False
                self.captchaAns[self.progressNow-1] = text
                return True
            else:
                self.hasError = True
                return False

    def setProgressLabel(self):
        s = '共' + str(self.progressMax) + '張，目前正處理到第' + str(self.progressNow) + '張'
        self.labelProgress.setText(s)

    def setTimesLabel(self):
        s = '共要標記' + str(self.timesMax) + '次，目前正標記到第' + str(self.timesNow) + '次'
        self.labelTimes.setText(s)

    def backPic(self):
        if self.progressNow > self.progressLast:
            self.progressNow -= 2
            self.progressBar.setValue(self.progressNow)
            self.switch2NextPic()
        else:
            QMessageBox.information(self, '提示', '無法在第一張往前...')

    def switch2NextPic(self):
        self.hasError = False
        if self.progressNow == self.progressMax:
            if self.timesNow == self.timesMax:
                if self.record:
                    cmd = "rm " + self.folderPath + '/record.txt'
                    subprocess.Popen(cmd.split())
                    self.record = False
                    self.saveTemp()
                else:
                    self.save2csv()
            else:
                self.switch2NextTimes()
        else:
            self.progressNow += 1
            self.setProgressLabel()
            image = QImage(self.files[self.progressNow-1])
            self.labelPic.setPixmap(QPixmap.fromImage(image))
            self.lineEditInput.setText("")
            self.lineEditInput.setFocus()


    def switch2NextTimes(self):
        self.timesNow += 1
        self.progressNow = 1
        image = QImage(self.files[0])
        self.labelPic.setPixmap(QPixmap.fromImage(image))
        self.setTimesLabel()
        self.setProgressLabel()
        self.lineEditInput.setText("")
        self.lineEditInput.setFocus()

    def saveTemp(self):
        if not self.record and self.progressNow == self.progressMax and self.timesNow == self.timesMax:
            self.progressNow += 1
            finish = '完成標註！'
        elif self.timesNow > 1:
            self.save2csv()
            return
        else:
            s = "還沒有完成，確定要暫時保存嗎？"
            finish = '保存成功！'
            reply = QMessageBox.information(self, '提示', s, QMessageBox.Ok | QMessageBox.Close,
                                            QMessageBox.Close)
            if reply == QMessageBox.Ok:
                saveRecordPath = self.folderPath + "/record.txt"
                with open(saveRecordPath, 'w') as r:
                    r.writelines(str(self.progressNow))
                r.close()

        saveFilePath = self.folderPath + "/validate.csv"
        saveFile = QFileDialog.getSaveFileName(self, "存檔", saveFilePath, 'CSV files (*.csv)')
        if saveFile[0]:
            with open(saveFile[0], 'a') as f:
                f_csv = csv.writer(f)
                #print(self.captchaAns)
                for i in range(0, self.progressNow - self.progressLast):
                    f_csv.writerow([self.progressLast + i, self.captchaAns[i]])
            f.close()
            QMessageBox.information(self, '提示', finish)
            self.close()

    def save2csv(self):
        saveFilePath = self.folderPath + "/validate.csv"
        saveFile = QFileDialog.getSaveFileName(self, "存檔", saveFilePath, 'CSV files (*.csv)')
        if saveFile[0]:
            with open(saveFile[0], 'w') as f:
                f_csv = csv.writer(f)
                for i in range(0, self.progressMax):
                    f_csv.writerow([i+1, self.captchaAns[i]])
            f.close()
            QMessageBox.information(self, '提示', '完成標註！')
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())