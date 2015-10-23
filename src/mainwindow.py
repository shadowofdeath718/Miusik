# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(565, 470)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Triangular)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.mainMenu = QtGui.QHBoxLayout()
        self.mainMenu.setObjectName(_fromUtf8("mainMenu"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.mainMenu.addItem(spacerItem)
        self.musicMenuButton = QtGui.QPushButton(self.centralwidget)
        self.musicMenuButton.setEnabled(True)
        self.musicMenuButton.setFlat(False)
        self.musicMenuButton.setObjectName(_fromUtf8("musicMenuButton"))
        self.mainMenu.addWidget(self.musicMenuButton)
        self.radioMenuButton = QtGui.QPushButton(self.centralwidget)
        self.radioMenuButton.setObjectName(_fromUtf8("radioMenuButton"))
        self.mainMenu.addWidget(self.radioMenuButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.mainMenu.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.mainMenu)
        self.lineUnderMainMenu = QtGui.QFrame(self.centralwidget)
        self.lineUnderMainMenu.setFrameShape(QtGui.QFrame.HLine)
        self.lineUnderMainMenu.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineUnderMainMenu.setObjectName(_fromUtf8("lineUnderMainMenu"))
        self.verticalLayout_2.addWidget(self.lineUnderMainMenu)
        self.toolBar = QtGui.QHBoxLayout()
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        spacerItem2 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.toolBar.addItem(spacerItem2)
        self.openFolderButton = QtGui.QToolButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/open_folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openFolderButton.setIcon(icon)
        self.openFolderButton.setObjectName(_fromUtf8("openFolderButton"))
        self.toolBar.addWidget(self.openFolderButton)
        self.addFileButton = QtGui.QToolButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/add_file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addFileButton.setIcon(icon1)
        self.addFileButton.setObjectName(_fromUtf8("addFileButton"))
        self.toolBar.addWidget(self.addFileButton)
        self.savePlaylistButton = QtGui.QToolButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.savePlaylistButton.setIcon(icon2)
        self.savePlaylistButton.setObjectName(_fromUtf8("savePlaylistButton"))
        self.toolBar.addWidget(self.savePlaylistButton)
        self.loadPlaylistButton = QtGui.QToolButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/load.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadPlaylistButton.setIcon(icon3)
        self.loadPlaylistButton.setObjectName(_fromUtf8("loadPlaylistButton"))
        self.toolBar.addWidget(self.loadPlaylistButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.toolBar.addItem(spacerItem3)
        self.settingButton = QtGui.QToolButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/setting.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingButton.setIcon(icon4)
        self.settingButton.setObjectName(_fromUtf8("settingButton"))
        self.toolBar.addWidget(self.settingButton)
        self.infoButton = QtGui.QToolButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infoButton.setIcon(icon5)
        self.infoButton.setObjectName(_fromUtf8("infoButton"))
        self.toolBar.addWidget(self.infoButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.toolBar.addItem(spacerItem4)
        self.lineEditSearch = QtGui.QLineEdit(self.centralwidget)
        self.lineEditSearch.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditSearch.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEditSearch.setText(_fromUtf8(""))
        self.lineEditSearch.setObjectName(_fromUtf8("lineEditSearch"))
        self.toolBar.addWidget(self.lineEditSearch)
        spacerItem5 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.toolBar.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.toolBar)
        self.mainArea = QtGui.QVBoxLayout()
        self.mainArea.setObjectName(_fromUtf8("mainArea"))
        self.mainInterface = QtGui.QHBoxLayout()
        self.mainInterface.setObjectName(_fromUtf8("mainInterface"))
        self.playlistsTabWidget = QtGui.QTabWidget(self.centralwidget)
        self.playlistsTabWidget.setEnabled(True)
        self.playlistsTabWidget.setStyleSheet(_fromUtf8("QTabWidget::pane {\n"
"    border-top: 1px solid #c4c4c4;\n"
"    top:-1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px;\n"
"}"))
        self.playlistsTabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.playlistsTabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.playlistsTabWidget.setUsesScrollButtons(True)
        self.playlistsTabWidget.setTabsClosable(True)
        self.playlistsTabWidget.setMovable(True)
        self.playlistsTabWidget.setObjectName(_fromUtf8("playlistsTabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget = QtGui.QTableWidget(self.tab)
        self.tableWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.playlistsTabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.playlistsTabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.mainInterface.addWidget(self.playlistsTabWidget)
        self.artistInfo = QtGui.QWidget(self.centralwidget)
        self.artistInfo.setObjectName(_fromUtf8("artistInfo"))
        self.mainInterface.addWidget(self.artistInfo)
        self.lyricsView = QtGui.QWidget(self.centralwidget)
        self.lyricsView.setObjectName(_fromUtf8("lyricsView"))
        self.mainInterface.addWidget(self.lyricsView)
        self.mainArea.addLayout(self.mainInterface)
        self.chooseLayoutButtons = QtGui.QHBoxLayout()
        self.chooseLayoutButtons.setObjectName(_fromUtf8("chooseLayoutButtons"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.chooseLayoutButtons.addItem(spacerItem6)
        self.playlistChooseButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playlistChooseButton.sizePolicy().hasHeightForWidth())
        self.playlistChooseButton.setSizePolicy(sizePolicy)
        self.playlistChooseButton.setMinimumSize(QtCore.QSize(30, 25))
        self.playlistChooseButton.setMaximumSize(QtCore.QSize(30, 25))
        self.playlistChooseButton.setDefault(False)
        self.playlistChooseButton.setFlat(False)
        self.playlistChooseButton.setObjectName(_fromUtf8("playlistChooseButton"))
        self.chooseLayoutButtons.addWidget(self.playlistChooseButton)
        self.lyricsChooseButton = QtGui.QPushButton(self.centralwidget)
        self.lyricsChooseButton.setMinimumSize(QtCore.QSize(30, 25))
        self.lyricsChooseButton.setMaximumSize(QtCore.QSize(30, 25))
        self.lyricsChooseButton.setObjectName(_fromUtf8("lyricsChooseButton"))
        self.chooseLayoutButtons.addWidget(self.lyricsChooseButton)
        self.artistInfoChooseButton = QtGui.QPushButton(self.centralwidget)
        self.artistInfoChooseButton.setMinimumSize(QtCore.QSize(30, 25))
        self.artistInfoChooseButton.setMaximumSize(QtCore.QSize(30, 25))
        self.artistInfoChooseButton.setObjectName(_fromUtf8("artistInfoChooseButton"))
        self.chooseLayoutButtons.addWidget(self.artistInfoChooseButton)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.chooseLayoutButtons.addItem(spacerItem7)
        self.mainArea.addLayout(self.chooseLayoutButtons)
        self.verticalLayout_2.addLayout(self.mainArea)
        self.lineUnderMainArea = QtGui.QFrame(self.centralwidget)
        self.lineUnderMainArea.setFrameShape(QtGui.QFrame.HLine)
        self.lineUnderMainArea.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineUnderMainArea.setObjectName(_fromUtf8("lineUnderMainArea"))
        self.verticalLayout_2.addWidget(self.lineUnderMainArea)
        self.controlArea = QtGui.QHBoxLayout()
        self.controlArea.setObjectName(_fromUtf8("controlArea"))
        spacerItem8 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.controlArea.addItem(spacerItem8)
        self.mainControl = QtGui.QVBoxLayout()
        self.mainControl.setObjectName(_fromUtf8("mainControl"))
        self.controlButton = QtGui.QHBoxLayout()
        self.controlButton.setObjectName(_fromUtf8("controlButton"))
        self.musicControlButtons = QtGui.QHBoxLayout()
        self.musicControlButtons.setObjectName(_fromUtf8("musicControlButtons"))
        self.previous = QtGui.QToolButton(self.centralwidget)
        self.previous.setMaximumSize(QtCore.QSize(25, 25))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous.setIcon(icon6)
        self.previous.setIconSize(QtCore.QSize(22, 22))
        self.previous.setObjectName(_fromUtf8("previous"))
        self.musicControlButtons.addWidget(self.previous)
        self.playToggle = QtGui.QToolButton(self.centralwidget)
        self.playToggle.setMinimumSize(QtCore.QSize(50, 50))
        self.playToggle.setMaximumSize(QtCore.QSize(50, 50))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playToggle.setIcon(icon7)
        self.playToggle.setIconSize(QtCore.QSize(48, 48))
        self.playToggle.setObjectName(_fromUtf8("playToggle"))
        self.musicControlButtons.addWidget(self.playToggle)
        self.stop = QtGui.QToolButton(self.centralwidget)
        self.stop.setMinimumSize(QtCore.QSize(34, 34))
        self.stop.setMaximumSize(QtCore.QSize(34, 34))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon8)
        self.stop.setIconSize(QtCore.QSize(32, 32))
        self.stop.setObjectName(_fromUtf8("stop"))
        self.musicControlButtons.addWidget(self.stop)
        self.next = QtGui.QToolButton(self.centralwidget)
        self.next.setMinimumSize(QtCore.QSize(25, 25))
        self.next.setMaximumSize(QtCore.QSize(25, 25))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next.setIcon(icon9)
        self.next.setIconSize(QtCore.QSize(22, 22))
        self.next.setObjectName(_fromUtf8("next"))
        self.musicControlButtons.addWidget(self.next)
        self.volume = QtGui.QToolButton(self.centralwidget)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/volume.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.volume.setIcon(icon10)
        self.volume.setObjectName(_fromUtf8("volume"))
        self.musicControlButtons.addWidget(self.volume)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.musicControlButtons.addItem(spacerItem9)
        self.controlButton.addLayout(self.musicControlButtons)
        self.playingSongInfo = QtGui.QVBoxLayout()
        self.playingSongInfo.setObjectName(_fromUtf8("playingSongInfo"))
        self.PlayingSong = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PlayingSong.setFont(font)
        self.PlayingSong.setObjectName(_fromUtf8("PlayingSong"))
        self.playingSongInfo.addWidget(self.PlayingSong)
        self.Artist = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(12)
        self.Artist.setFont(font)
        self.Artist.setObjectName(_fromUtf8("Artist"))
        self.playingSongInfo.addWidget(self.Artist)
        self.controlButton.addLayout(self.playingSongInfo)
        self.mainControl.addLayout(self.controlButton)
        self.sliderArea = QtGui.QHBoxLayout()
        self.sliderArea.setObjectName(_fromUtf8("sliderArea"))
        self.duration = QtGui.QLabel(self.centralwidget)
        self.duration.setObjectName(_fromUtf8("duration"))
        self.sliderArea.addWidget(self.duration)
        self.seekSlider = phonon.Phonon.SeekSlider(self.centralwidget)
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.sliderArea.addWidget(self.seekSlider)
        self.position = QtGui.QLabel(self.centralwidget)
        self.position.setObjectName(_fromUtf8("position"))
        self.sliderArea.addWidget(self.position)
        self.mainControl.addLayout(self.sliderArea)
        self.controlArea.addLayout(self.mainControl)
        spacerItem10 = QtGui.QSpacerItem(12, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.controlArea.addItem(spacerItem10)
        self.AlbumArt = QtGui.QLabel(self.centralwidget)
        self.AlbumArt.setMinimumSize(QtCore.QSize(100, 100))
        self.AlbumArt.setMaximumSize(QtCore.QSize(100, 100))
        self.AlbumArt.setText(_fromUtf8(""))
        self.AlbumArt.setPixmap(QtGui.QPixmap(_fromUtf8("AlbumArtExample/Take me to your heart.jpg")))
        self.AlbumArt.setScaledContents(True)
        self.AlbumArt.setObjectName(_fromUtf8("AlbumArt"))
        self.controlArea.addWidget(self.AlbumArt)
        spacerItem11 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.controlArea.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.controlArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.playlistsTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.musicMenuButton.setText(_translate("MainWindow", "MUSIC", None))
        self.radioMenuButton.setText(_translate("MainWindow", "RADIO", None))
        self.openFolderButton.setText(_translate("MainWindow", "Open Folder", None))
        self.addFileButton.setText(_translate("MainWindow", "Open Files", None))
        self.savePlaylistButton.setText(_translate("MainWindow", "Save Playlist", None))
        self.loadPlaylistButton.setText(_translate("MainWindow", "Load Playlist", None))
        self.settingButton.setText(_translate("MainWindow", "Setting", None))
        self.infoButton.setText(_translate("MainWindow", "...", None))
        self.lineEditSearch.setPlaceholderText(_translate("MainWindow", "Search", None))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Artist", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Album", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Length", None))
        self.playlistsTabWidget.setTabText(self.playlistsTabWidget.indexOf(self.tab), _translate("MainWindow", "Playlist 1", None))
        self.playlistsTabWidget.setTabText(self.playlistsTabWidget.indexOf(self.tab_2), _translate("MainWindow", "Playlist 2", None))
        self.playlistChooseButton.setText(_translate("MainWindow", "1", None))
        self.lyricsChooseButton.setText(_translate("MainWindow", "2", None))
        self.artistInfoChooseButton.setText(_translate("MainWindow", "3", None))
        self.previous.setText(_translate("MainWindow", "...", None))
        self.playToggle.setText(_translate("MainWindow", "...", None))
        self.stop.setText(_translate("MainWindow", "...", None))
        self.next.setText(_translate("MainWindow", "...", None))
        self.volume.setText(_translate("MainWindow", "...", None))
        self.PlayingSong.setText(_translate("MainWindow", "Take me to your heart", None))
        self.Artist.setText(_translate("MainWindow", "Michael Learn To Rock", None))
        self.duration.setText(_translate("MainWindow", "0:00", None))
        self.position.setText(_translate("MainWindow", "3:57", None))

from PyQt4 import phonon
import resources_rc
