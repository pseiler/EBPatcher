# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created: Sun Mar 24 18:20:46 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(900, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/EBPatcher_Icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("color: rgb(53, 53, 53)"))
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.TopWidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.TopWidget.setFont(font)
        self.TopWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TopWidget.setAutoFillBackground(False)
        self.TopWidget.setStyleSheet(_fromUtf8("* {\n"
"    color: rgb(34, 0, 52);\n"
"    font-family: Arial;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"*:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QWidget#ApplyStep1, QWidget#ApplyStep2, QWidget#ApplyPatchDescription, QWidget#CreateStep1, QWidget#CreateStep2 {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border: 1 solid rgb(50, 50, 50);\n"
"    margin: 10;\n"
"}\n"
"\n"
"QLabel#ApplyStep1Title, QLabel#ApplyStep2Title, QLabel#CreateStep1Title, QLabel#CreateStep2Title {\n"
"    font-size: 20px;\n"
"    font-style: italic;\n"
"    font-weight: bold;\n"
"    padding: 10;\n"
"}\n"
"\n"
"QLabel#ApplyStep1Notice, QLabel#ApplyStep2Notice, QLabel#CreateStep1Notice, QLabel#CreateStep2Notice {\n"
"    color: rgb(106, 106, 106);\n"
"}"))
        self.TopWidget.setObjectName(_fromUtf8("TopWidget"))
        self.HelpButton = QtWidgets.QPushButton(self.TopWidget)
        self.HelpButton.setGeometry(QtCore.QRect(736, 50, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.HelpButton.setFont(font)
        self.HelpButton.setCheckable(False)
        self.HelpButton.setChecked(False)
        self.HelpButton.setAutoDefault(False)
        self.HelpButton.setDefault(False)
        self.HelpButton.setFlat(False)
        self.HelpButton.setObjectName(_fromUtf8("HelpButton"))
        self.Tabs = QtWidgets.QTabWidget(self.TopWidget)
        self.Tabs.setGeometry(QtCore.QRect(0, 160, 900, 440))
        self.Tabs.setStyleSheet(_fromUtf8(""))
        self.Tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.Tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Tabs.setElideMode(QtCore.Qt.ElideNone)
        self.Tabs.setDocumentMode(False)
        self.Tabs.setTabsClosable(False)
        self.Tabs.setMovable(False)
        self.Tabs.setObjectName(_fromUtf8("Tabs"))
        self.ApplyPatch = QtWidgets.QWidget()
        self.ApplyPatch.setObjectName(_fromUtf8("ApplyPatch"))
        self.ApplyStep2 = QtWidgets.QWidget(self.ApplyPatch)
        self.ApplyStep2.setEnabled(False)
        self.ApplyStep2.setGeometry(QtCore.QRect(450, 10, 450, 351))
        self.ApplyStep2.setObjectName(_fromUtf8("ApplyStep2"))
        self.ApplyStep2Title = QtWidgets.QLabel(self.ApplyStep2)
        self.ApplyStep2Title.setGeometry(QtCore.QRect(10, 10, 431, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ApplyStep2Title.setFont(font)
        self.ApplyStep2Title.setStyleSheet(_fromUtf8(""))
        self.ApplyStep2Title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ApplyStep2Title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ApplyStep2Title.setLineWidth(1)
        self.ApplyStep2Title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ApplyStep2Title.setWordWrap(True)
        self.ApplyStep2Title.setMargin(0)
        self.ApplyStep2Title.setIndent(-1)
        self.ApplyStep2Title.setOpenExternalLinks(False)
        self.ApplyStep2Title.setObjectName(_fromUtf8("ApplyStep2Title"))
        self.ApplyStep2Description = QtWidgets.QLabel(self.ApplyStep2)
        self.ApplyStep2Description.setGeometry(QtCore.QRect(20, 60, 411, 61))
        self.ApplyStep2Description.setStyleSheet(_fromUtf8(""))
        self.ApplyStep2Description.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.ApplyStep2Description.setWordWrap(True)
        self.ApplyStep2Description.setObjectName(_fromUtf8("ApplyStep2Description"))
        self.ApplyStep2Button = QtWidgets.QPushButton(self.ApplyStep2)
        self.ApplyStep2Button.setGeometry(QtCore.QRect(290, 130, 130, 40))
        self.ApplyStep2Button.setObjectName(_fromUtf8("ApplyStep2Button"))
        self.ApplyStep2Field = QtWidgets.QLineEdit(self.ApplyStep2)
        self.ApplyStep2Field.setGeometry(QtCore.QRect(30, 130, 240, 40))
        self.ApplyStep2Field.setText(_fromUtf8(""))
        self.ApplyStep2Field.setObjectName(_fromUtf8("ApplyStep2Field"))
        self.ApplyStep2Notice = QtWidgets.QLabel(self.ApplyStep2)
        self.ApplyStep2Notice.setGeometry(QtCore.QRect(20, 230, 411, 101))
        self.ApplyStep2Notice.setStyleSheet(_fromUtf8(""))
        self.ApplyStep2Notice.setText(_fromUtf8(""))
        self.ApplyStep2Notice.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.ApplyStep2Notice.setWordWrap(True)
        self.ApplyStep2Notice.setObjectName(_fromUtf8("ApplyStep2Notice"))
        self.ApplyStep2Choice = QtWidgets.QWidget(self.ApplyStep2)
        self.ApplyStep2Choice.setEnabled(False)
        self.ApplyStep2Choice.setGeometry(QtCore.QRect(300, 180, 120, 50))
        self.ApplyStep2Choice.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ApplyStep2Choice.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ApplyStep2Choice.setObjectName(_fromUtf8("ApplyStep2Choice"))
        self.ApplyStep2HeaderChoice = QtWidgets.QFormLayout(self.ApplyStep2Choice)
        self.ApplyStep2HeaderChoice.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ApplyStep2HeaderChoice.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
#        self.ApplyStep2HeaderChoice.setMargin(0)
        self.ApplyStep2HeaderChoice.setObjectName(_fromUtf8("ApplyStep2HeaderChoice"))
        self.ApplyStep2Headered = QtWidgets.QRadioButton(self.ApplyStep2Choice)
        self.ApplyStep2Headered.setObjectName(_fromUtf8("ApplyStep2Headered"))
        self.ApplyStep2HeaderChoice.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ApplyStep2Headered)
        self.ApplyStep2Unheadered = QtWidgets.QRadioButton(self.ApplyStep2Choice)
        self.ApplyStep2Unheadered.setObjectName(_fromUtf8("ApplyStep2Unheadered"))
        self.ApplyStep2HeaderChoice.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ApplyStep2Unheadered)
        self.ApplyStep2ChoiceLabel = QtWidgets.QLabel(self.ApplyStep2)
        self.ApplyStep2ChoiceLabel.setEnabled(False)
        self.ApplyStep2ChoiceLabel.setGeometry(QtCore.QRect(20, 190, 271, 31))
        self.ApplyStep2ChoiceLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ApplyStep2ChoiceLabel.setWordWrap(True)
        self.ApplyStep2ChoiceLabel.setObjectName(_fromUtf8("ApplyStep2ChoiceLabel"))
        self.ApplyStep1 = QtWidgets.QWidget(self.ApplyPatch)
        self.ApplyStep1.setGeometry(QtCore.QRect(0, 10, 450, 351))
        self.ApplyStep1.setStyleSheet(_fromUtf8(""))
        self.ApplyStep1.setObjectName(_fromUtf8("ApplyStep1"))
        self.ApplyStep1Title = QtWidgets.QLabel(self.ApplyStep1)
        self.ApplyStep1Title.setGeometry(QtCore.QRect(9, 9, 431, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ApplyStep1Title.setFont(font)
        self.ApplyStep1Title.setStyleSheet(_fromUtf8(""))
        self.ApplyStep1Title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ApplyStep1Title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ApplyStep1Title.setLineWidth(1)
        self.ApplyStep1Title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ApplyStep1Title.setWordWrap(True)
        self.ApplyStep1Title.setMargin(0)
        self.ApplyStep1Title.setIndent(-1)
        self.ApplyStep1Title.setOpenExternalLinks(False)
        self.ApplyStep1Title.setObjectName(_fromUtf8("ApplyStep1Title"))
        self.ApplyStep1Description = QtWidgets.QLabel(self.ApplyStep1)
        self.ApplyStep1Description.setGeometry(QtCore.QRect(20, 60, 411, 71))
        self.ApplyStep1Description.setStyleSheet(_fromUtf8(""))
        self.ApplyStep1Description.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.ApplyStep1Description.setWordWrap(True)
        self.ApplyStep1Description.setObjectName(_fromUtf8("ApplyStep1Description"))
        self.ApplyStep1Field = QtWidgets.QLineEdit(self.ApplyStep1)
        self.ApplyStep1Field.setGeometry(QtCore.QRect(30, 150, 240, 40))
        self.ApplyStep1Field.setReadOnly(True)
        self.ApplyStep1Field.setObjectName(_fromUtf8("ApplyStep1Field"))
        self.ApplyStep1Button = QtWidgets.QPushButton(self.ApplyStep1)
        self.ApplyStep1Button.setGeometry(QtCore.QRect(290, 150, 130, 40))
        self.ApplyStep1Button.setObjectName(_fromUtf8("ApplyStep1Button"))
        self.ApplyStep1Notice = QtWidgets.QLabel(self.ApplyStep1)
        self.ApplyStep1Notice.setGeometry(QtCore.QRect(20, 200, 411, 41))
        self.ApplyStep1Notice.setStyleSheet(_fromUtf8(""))
        self.ApplyStep1Notice.setMidLineWidth(0)
        self.ApplyStep1Notice.setText(_fromUtf8(""))
        self.ApplyStep1Notice.setAlignment(QtCore.Qt.AlignCenter)
        self.ApplyStep1Notice.setWordWrap(True)
        self.ApplyStep1Notice.setObjectName(_fromUtf8("ApplyStep1Notice"))
        self.ApplyPatchButton = QtWidgets.QPushButton(self.ApplyPatch)
        self.ApplyPatchButton.setEnabled(False)
        self.ApplyPatchButton.setGeometry(QtCore.QRect(380, 360, 141, 41))
        self.ApplyPatchButton.setFlat(False)
        self.ApplyPatchButton.setObjectName(_fromUtf8("ApplyPatchButton"))
        self.Tabs.addTab(self.ApplyPatch, _fromUtf8(""))
        self.CreatePatch = QtWidgets.QWidget()
        self.CreatePatch.setObjectName(_fromUtf8("CreatePatch"))
        self.CreatePatchButton = QtWidgets.QPushButton(self.CreatePatch)
        self.CreatePatchButton.setEnabled(False)
        self.CreatePatchButton.setGeometry(QtCore.QRect(380, 360, 141, 41))
        self.CreatePatchButton.setFlat(False)
        self.CreatePatchButton.setObjectName(_fromUtf8("CreatePatchButton"))
        self.CreateStep1 = QtWidgets.QWidget(self.CreatePatch)
        self.CreateStep1.setGeometry(QtCore.QRect(0, 10, 450, 351))
        self.CreateStep1.setStyleSheet(_fromUtf8(""))
        self.CreateStep1.setObjectName(_fromUtf8("CreateStep1"))
        self.CreateStep1Title = QtWidgets.QLabel(self.CreateStep1)
        self.CreateStep1Title.setGeometry(QtCore.QRect(9, 9, 431, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.CreateStep1Title.setFont(font)
        self.CreateStep1Title.setStyleSheet(_fromUtf8(""))
        self.CreateStep1Title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CreateStep1Title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.CreateStep1Title.setLineWidth(1)
        self.CreateStep1Title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.CreateStep1Title.setWordWrap(True)
        self.CreateStep1Title.setMargin(0)
        self.CreateStep1Title.setIndent(-1)
        self.CreateStep1Title.setOpenExternalLinks(False)
        self.CreateStep1Title.setObjectName(_fromUtf8("CreateStep1Title"))
        self.CreateStep1Description = QtWidgets.QLabel(self.CreateStep1)
        self.CreateStep1Description.setGeometry(QtCore.QRect(20, 60, 411, 71))
        self.CreateStep1Description.setStyleSheet(_fromUtf8(""))
        self.CreateStep1Description.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.CreateStep1Description.setWordWrap(True)
        self.CreateStep1Description.setObjectName(_fromUtf8("CreateStep1Description"))
        self.CreateStep1CleanField = QtWidgets.QLineEdit(self.CreateStep1)
        self.CreateStep1CleanField.setGeometry(QtCore.QRect(30, 150, 240, 40))
        self.CreateStep1CleanField.setReadOnly(True)
        self.CreateStep1CleanField.setObjectName(_fromUtf8("CreateStep1CleanField"))
        self.CreateStep1CleanButton = QtWidgets.QPushButton(self.CreateStep1)
        self.CreateStep1CleanButton.setGeometry(QtCore.QRect(290, 150, 130, 40))
        self.CreateStep1CleanButton.setObjectName(_fromUtf8("CreateStep1CleanButton"))
        self.CreateStep1Notice = QtWidgets.QLabel(self.CreateStep1)
        self.CreateStep1Notice.setGeometry(QtCore.QRect(20, 270, 411, 41))
        self.CreateStep1Notice.setStyleSheet(_fromUtf8(""))
        self.CreateStep1Notice.setMidLineWidth(0)
        self.CreateStep1Notice.setText(_fromUtf8(""))
        self.CreateStep1Notice.setAlignment(QtCore.Qt.AlignCenter)
        self.CreateStep1Notice.setWordWrap(True)
        self.CreateStep1Notice.setObjectName(_fromUtf8("CreateStep1Notice"))
        self.CreateStep1HackedField = QtWidgets.QLineEdit(self.CreateStep1)
        self.CreateStep1HackedField.setGeometry(QtCore.QRect(30, 210, 240, 40))
        self.CreateStep1HackedField.setReadOnly(True)
        self.CreateStep1HackedField.setObjectName(_fromUtf8("CreateStep1HackedField"))
        self.CreateStep1HackedButton = QtWidgets.QPushButton(self.CreateStep1)
        self.CreateStep1HackedButton.setGeometry(QtCore.QRect(290, 210, 130, 40))
        self.CreateStep1HackedButton.setObjectName(_fromUtf8("CreateStep1HackedButton"))
        self.CreateStep2 = QtWidgets.QWidget(self.CreatePatch)
        self.CreateStep2.setEnabled(False)
        self.CreateStep2.setGeometry(QtCore.QRect(450, 10, 450, 351))
        self.CreateStep2.setObjectName(_fromUtf8("CreateStep2"))
        self.CreateStep2Title = QtWidgets.QLabel(self.CreateStep2)
        self.CreateStep2Title.setGeometry(QtCore.QRect(10, 10, 431, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.CreateStep2Title.setFont(font)
        self.CreateStep2Title.setStyleSheet(_fromUtf8(""))
        self.CreateStep2Title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CreateStep2Title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.CreateStep2Title.setLineWidth(1)
        self.CreateStep2Title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.CreateStep2Title.setWordWrap(True)
        self.CreateStep2Title.setMargin(0)
        self.CreateStep2Title.setIndent(-1)
        self.CreateStep2Title.setOpenExternalLinks(False)
        self.CreateStep2Title.setObjectName(_fromUtf8("CreateStep2Title"))
        self.CreateStep2Description = QtWidgets.QLabel(self.CreateStep2)
        self.CreateStep2Description.setGeometry(QtCore.QRect(20, 60, 411, 31))
        self.CreateStep2Description.setStyleSheet(_fromUtf8(""))
        self.CreateStep2Description.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.CreateStep2Description.setWordWrap(True)
        self.CreateStep2Description.setObjectName(_fromUtf8("CreateStep2Description"))
        self.CreateStep2Button = QtWidgets.QPushButton(self.CreateStep2)
        self.CreateStep2Button.setGeometry(QtCore.QRect(290, 100, 130, 40))
        self.CreateStep2Button.setObjectName(_fromUtf8("CreateStep2Button"))
        self.CreateStep2Field = QtWidgets.QLineEdit(self.CreateStep2)
        self.CreateStep2Field.setGeometry(QtCore.QRect(30, 100, 241, 41))
        self.CreateStep2Field.setReadOnly(True)
        self.CreateStep2Field.setObjectName(_fromUtf8("CreateStep2Field"))
        self.CreateStep2PatchTitle = QtWidgets.QLineEdit(self.CreateStep2)
        self.CreateStep2PatchTitle.setGeometry(QtCore.QRect(30, 160, 221, 30))
        self.CreateStep2PatchTitle.setStyleSheet(_fromUtf8("font-size: 13px;"))
        self.CreateStep2PatchTitle.setText(_fromUtf8(""))
        self.CreateStep2PatchTitle.setObjectName(_fromUtf8("CreateStep2PatchTitle"))
        self.CreateStep2PatchDescription = QtWidgets.QPlainTextEdit(self.CreateStep2)
        self.CreateStep2PatchDescription.setGeometry(QtCore.QRect(30, 220, 390, 101))
        self.CreateStep2PatchDescription.setPlainText(_fromUtf8(""))
        self.CreateStep2PatchDescription.setObjectName(_fromUtf8("CreateStep2PatchDescription"))
        self.CreateStep2PatchAuthor = QtWidgets.QLineEdit(self.CreateStep2)
        self.CreateStep2PatchAuthor.setGeometry(QtCore.QRect(259, 160, 161, 30))
        self.CreateStep2PatchAuthor.setStyleSheet(_fromUtf8("font-size: 13px;"))
        self.CreateStep2PatchAuthor.setText(_fromUtf8(""))
        self.CreateStep2PatchAuthor.setObjectName(_fromUtf8("CreateStep2PatchAuthor"))
        self.label = QtWidgets.QLabel(self.CreateStep2)
        self.label.setGeometry(QtCore.QRect(30, 200, 171, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.Tabs.addTab(self.CreatePatch, _fromUtf8(""))
        self.HelpLabel = QtWidgets.QLabel(self.TopWidget)
        self.HelpLabel.setGeometry(QtCore.QRect(530, 100, 361, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        font.setPointSize(13)
        self.HelpLabel.setFont(font)
        self.HelpLabel.setStyleSheet(_fromUtf8("background: transparent; font-family: Segoe Print; font-size: 16px;"))
        self.HelpLabel.setTextFormat(QtCore.Qt.AutoText)
        self.HelpLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.HelpLabel.setWordWrap(True)
        self.HelpLabel.setObjectName(_fromUtf8("HelpLabel"))
        self.Logo = QtWidgets.QLabel(self.TopWidget)
        self.Logo.setGeometry(QtCore.QRect(20, 5, 446, 156))
        self.Logo.setAutoFillBackground(False)
        self.Logo.setStyleSheet(_fromUtf8("background: transparent"))
        self.Logo.setText(_fromUtf8(""))
        self.Logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/img/Logo.png")))
        self.Logo.setAlignment(QtCore.Qt.AlignCenter)
        self.Logo.setObjectName(_fromUtf8("Logo"))
        self.VersionNumber = QtWidgets.QLabel(self.TopWidget)
        self.VersionNumber.setGeometry(QtCore.QRect(467, 80, 81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.VersionNumber.setFont(font)
        self.VersionNumber.setStyleSheet(_fromUtf8("color: #001642;\n"
"font-family: \"Segoe Print\";\n"
"font-size: 38px;\n"
"font-style: italic;\n"
"font-weight: bold;"))
        self.VersionNumber.setObjectName(_fromUtf8("VersionNumber"))
        MainWindow.setCentralWidget(self.TopWidget)

        self.retranslateUi(MainWindow)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "EarthBound Patcher", None))
        self.HelpButton.setText(QtWidgets.QApplication.translate("MainWindow", "About", None))
        self.ApplyStep2Title.setText(QtWidgets.QApplication.translate("MainWindow", "Step 2 - Select your patch", None))
        self.ApplyStep2Description.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Select an <span style=\" font-weight:600;\">EBP patch</span> (recommended) or an <span style=\" font-weight:600;\">IPS patch</span> (legacy) to apply to your clean ROM.</p><p><span style=\" font-style:italic;\">Patches have the &quot;.ebp&quot; or &quot;.ips&quot; file extension.</span></p></body></html>", None))
        self.ApplyStep2Button.setText(QtWidgets.QApplication.translate("MainWindow", "Browse...", None))
        self.ApplyStep2Field.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "EBP/IPS Patch", None))
        self.ApplyStep2Headered.setText(QtWidgets.QApplication.translate("MainWindow", "Headered", None))
        self.ApplyStep2Unheadered.setText(QtWidgets.QApplication.translate("MainWindow", "Unheadered", None))
        self.ApplyStep2ChoiceLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Select the type of ROM this patch is meant for:", None))
        self.ApplyStep1Title.setText(QtWidgets.QApplication.translate("MainWindow", "Step 1 - Select your ROM", None))
        self.ApplyStep1Description.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Select a <span style=\" font-weight:600;\">clean EarthBound ROM</span> on which to apply the patch.</p><p><span style=\" font-style:italic;\">EarthBound ROMs have &quot;.sfc&quot; or &quot;.smc&quot; file extensions.</span></p></body></html>", None))
        self.ApplyStep1Field.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Clean EarthBound ROM", None))
        self.ApplyStep1Button.setText(QtWidgets.QApplication.translate("MainWindow", "Browse...", None))
        self.ApplyPatchButton.setText(QtWidgets.QApplication.translate("MainWindow", "Apply Patch!", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.ApplyPatch), QtWidgets.QApplication.translate("MainWindow", "Apply Patch", None))
        self.CreatePatchButton.setText(QtWidgets.QApplication.translate("MainWindow", "Create Patch!", None))
        self.CreateStep1Title.setText(QtWidgets.QApplication.translate("MainWindow", "Step 1 - Select your ROMs", None))
        self.CreateStep1Description.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Select a <span style=\" font-weight:600;\">clean EarthBound ROM</span>, then select another one <span style=\" font-weight:600;\">with the hack applied</span>.</p><p><span style=\" font-style:italic;\">EarthBound ROMs have &quot;.sfc&quot; or &quot;.smc&quot; file extensions.</span></p></body></html>", None))
        self.CreateStep1CleanField.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Clean EarthBound ROM", None))
        self.CreateStep1CleanButton.setText(QtWidgets.QApplication.translate("MainWindow", "Browse...", None))
        self.CreateStep1HackedField.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Hacked EarthBound ROM", None))
        self.CreateStep1HackedButton.setText(QtWidgets.QApplication.translate("MainWindow", "Browse...", None))
        self.CreateStep2Title.setText(QtWidgets.QApplication.translate("MainWindow", "Step 2 - Create your patch", None))
        self.CreateStep2Description.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Your patch will be saved in the <span style=\" font-weight:600;\">EBP</span> format. You can provide a <span style=\" font-weight:600;\">title</span>, the <span style=\" font-weight:600;\">author\'s name</span> and a <span style=\" font-weight:600;\">short description</span> for it.</p></body></html>", None))
        self.CreateStep2Button.setText(QtWidgets.QApplication.translate("MainWindow", "Browse...", None))
        self.CreateStep2Field.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Saving location", None))
        self.CreateStep2PatchTitle.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Patch title (optional)", None))
        self.CreateStep2PatchAuthor.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Author (optional)", None))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Patch description (optional):", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.CreatePatch), QtWidgets.QApplication.translate("MainWindow", "Create Patch", None))
        self.HelpLabel.setText(QtWidgets.QApplication.translate("MainWindow", "An easy-to-use EarthBound ROM patcher.", None))
        self.VersionNumber.setText(QtWidgets.QApplication.translate("MainWindow", "1.0", None))

import res_rc
