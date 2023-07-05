from ui_interface import *
from Custom_Widgets.Widgets import *

from datetime import datetime
import sys

settings = QSettings()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.startup()

        self.definition_local_variables()
        
        loadJsonStyle(self, self.ui) 

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.showMaximized()
        self.show()

        self.ui.settingBtn.clicked.connect(self.menuButtonsClickEvent)
        self.ui.homeBtn.clicked.connect(self.menuButtonsClickEvent)
        self.ui.logBtn.clicked.connect(self.menuButtonsClickEvent)
        
        self.ui.item1Btn.clicked.connect(self.changeSettingPagesEvent)
        self.ui.item2Btn.clicked.connect(self.changeSettingPagesEvent)
        self.ui.item3Btn.clicked.connect(self.changeSettingPagesEvent)
        self.ui.item4Btn.clicked.connect(self.changeSettingPagesEvent)
        self.ui.item5Btn.clicked.connect(self.changeSettingPagesEvent)

        self.ui.playPauseBtn.clicked.connect(self.playPauseBtnClickedEvent)
        self.ui.loginBtn.clicked.connect(self.login_to_setting)

        self.ui.customizePosBtn.clicked.connect(self.robotPositionsChangePageEvent)
        self.ui.backToViewPositionsSettingBtn.clicked.connect(self.robotPositionsChangePageEvent)
        
        self.ui.customizeTakePosBtn.clicked.connect(self.goToSettingPositionPage)
        self.ui.customizeWaitPosBtn.clicked.connect(self.goToSettingPositionPage)
        self.ui.customizeCollPathPosBtn.clicked.connect(self.goToSettingPositionPage)
        self.ui.customizeFirstTilePosBtn.clicked.connect(self.goToSettingPositionPage)
        self.ui.backToMenuPositionsBtn.clicked.connect(self.backToMenuCustomizePositions)
        
        self.ui.chineseLangBtn.clicked.connect(self.changeLanguageEvent)
        self.ui.englishLangBtn.clicked.connect(self.changeLanguageEvent)
        self.ui.persianLangBtn.clicked.connect(self.changeLanguageEvent)
        
        self.ui.num0Btn.clicked.connect(self.keyboardLoginSettingEvent)
        self.ui.num1Btn.clicked.connect(self.keyboardLoginSettingEvent)
        self.ui.num2Btn.clicked.connect(self.keyboardLoginSettingEvent)
        self.ui.num3Btn.clicked.connect(self.keyboardLoginSettingEvent)
        self.ui.num4Btn.clicked.connect(self.keyboardLoginSettingEvent)
        self.ui.num5Btn.clicked.connect(self.keyboardLoginSettingEvent)
        self.ui.num6Btn.clicked.connect(self.keyboardLoginSettingEvent)
        self.ui.num7Btn.clicked.connect(self.keyboardLoginSettingEvent)
        self.ui.num8Btn.clicked.connect(self.keyboardLoginSettingEvent)
        self.ui.num9Btn.clicked.connect(self.keyboardLoginSettingEvent)
        self.ui.backspaceBtn.clicked.connect(self.keyboardLoginSettingEvent)

        self.ui.jointsManControlBtn.clicked.connect(self.change_manual_control_menu_handler)
        self.ui.endeffectorManControlBtn.clicked.connect(self.change_manual_control_menu_handler)
    
        self.ui.joint1MinusBtn.clicked.connect(self.manual_joint_controller_event_handler)
        self.ui.joint1PlusBtn.clicked.connect(self.manual_joint_controller_event_handler)
        self.ui.joint2MinusBtn.clicked.connect(self.manual_joint_controller_event_handler)
        self.ui.joint2PlusBtn.clicked.connect(self.manual_joint_controller_event_handler)
        self.ui.joint3MinusBtn.clicked.connect(self.manual_joint_controller_event_handler)
        self.ui.joint3PlusBtn.clicked.connect(self.manual_joint_controller_event_handler)
        self.ui.joint4MinusBtn.clicked.connect(self.manual_joint_controller_event_handler)
        self.ui.joint4PlusBtn.clicked.connect(self.manual_joint_controller_event_handler)
        self.ui.joint5MinusBtn.clicked.connect(self.manual_joint_controller_event_handler)
        self.ui.joint5PlusBtn.clicked.connect(self.manual_joint_controller_event_handler)
        self.ui.joint6MinusBtn.clicked.connect(self.manual_joint_controller_event_handler)
        self.ui.joint6PlusBtn.clicked.connect(self.manual_joint_controller_event_handler)
        
        self.ui.railMinusBtn.clicked.connect(self.update_rail_position)
        self.ui.railPlusBtn.clicked.connect(self.update_rail_position)
        
        self.ui.previusMenuCumstomPosBtn.clicked.connect(self.change_position_menu_event)
        self.ui.nextMenuCumstomPosBtn.clicked.connect(self.change_position_menu_event)
    
    def change_position_menu_event(self):
        
        past_label_txt = self.ui.titleCountLabel.text()
        
        if self.sender() == self.ui.previusMenuCumstomPosBtn:
            new_label_txt = past_label_txt.replace(past_label_txt[-1],\
            str(int(past_label_txt[-1])-1))
            
            if int(new_label_txt[-1]) == 1:
                self.ui.previusMenuCumstomPosBtn.setVisible(False)
            
            self.ui.titleCountLabel.setText(new_label_txt)
            self.ui.nextMenuCumstomPosBtn.setVisible(True)
        
        if self.sender() == self.ui.nextMenuCumstomPosBtn:
            
            new_label_txt = past_label_txt.replace(past_label_txt[-1],\
            str(int(past_label_txt[-1])+1))


            if int(new_label_txt[-1]) == self.max_custom_position_setting_page:
                self.ui.nextMenuCumstomPosBtn.setVisible(False)

            self.ui.titleCountLabel.setText(new_label_txt)
            self.ui.previusMenuCumstomPosBtn.setVisible(True)
            


    def update_rail_position(self):
        
        past_rail_pos = self.ui.railPosLabel.text()
        
        if self.sender() == self.ui.railMinusBtn:
            new_rail_pos = int(past_rail_pos) - 1
        
        if self.sender() == self.ui.railPlusBtn:
            new_rail_pos = int(past_rail_pos) + 1    

        self.ui.railPosLabel.setText(str(new_rail_pos))
    
    def manual_joint_controller_event_handler(self):
        
        if self.sender() == self.ui.joint1MinusBtn:
           past_degree = int(self.ui.degreeJoint1Label.text().replace("°", ""))-1
           self.ui.degreeJoint1Label.setText(f"{past_degree}°")
        
        if self.sender() == self.ui.joint1PlusBtn:
           past_degree = int(self.ui.degreeJoint1Label.text().replace("°", ""))+1
           self.ui.degreeJoint1Label.setText(f"{past_degree}°")
        
        if self.sender() == self.ui.joint2MinusBtn:
           past_degree = int(self.ui.degreeJoint2Label.text().replace("°", ""))-1
           self.ui.degreeJoint2Label.setText(f"{past_degree}°")
        
        if self.sender() == self.ui.joint2PlusBtn:
           past_degree = int(self.ui.degreeJoint2Label.text().replace("°", ""))+1
           self.ui.degreeJoint2Label.setText(f"{past_degree}°")
        
        if self.sender() == self.ui.joint3MinusBtn:
           past_degree = int(self.ui.degreeJoint3Label.text().replace("°", ""))-1
           self.ui.degreeJoint3Label.setText(f"{past_degree}°")
        
        if self.sender() == self.ui.joint3PlusBtn:
           past_degree = int(self.ui.degreeJoint3Label.text().replace("°", ""))+1
           self.ui.degreeJoint3Label.setText(f"{past_degree}°")
        
        if self.sender() == self.ui.joint4MinusBtn:
           past_degree = int(self.ui.degreeJoint4Label.text().replace("°", ""))-1
           self.ui.degreeJoint4Label.setText(f"{past_degree}°")
        
        if self.sender() == self.ui.joint4PlusBtn:
           past_degree = int(self.ui.degreeJoint4Label.text().replace("°", ""))+1
           self.ui.degreeJoint4Label.setText(f"{past_degree}°")
        
        if self.sender() == self.ui.joint5MinusBtn:
           past_degree = int(self.ui.degreeJoint5Label.text().replace("°", ""))-1
           self.ui.degreeJoint5Label.setText(f"{past_degree}°")
        
        if self.sender() == self.ui.joint5PlusBtn:
           past_degree = int(self.ui.degreeJoint5Label.text().replace("°", ""))+1
           self.ui.degreeJoint5Label.setText(f"{past_degree}°")
        
        if self.sender() == self.ui.joint6MinusBtn:
           past_degree = int(self.ui.degreeJoint6Label.text().replace("°", ""))-1
           self.ui.degreeJoint6Label.setText(f"{past_degree}°")
        
        if self.sender() == self.ui.joint6PlusBtn:
           past_degree = int(self.ui.degreeJoint6Label.text().replace("°", ""))+1
           self.ui.degreeJoint6Label.setText(f"{past_degree}°")
           
    
    def change_manual_control_menu_handler(self):
        
        if self.sender() == self.ui.jointsManControlBtn:
            self.ui.manControllerPages.setCurrentIndex(1)
        else:
            self.ui.manControllerPages.setCurrentIndex(0)
        
    
    def keyboardLoginSettingEvent(self):
        
        past_pass_text = self.ui.passwordEdt.text()
        
        if self.sender() == self.ui.num0Btn:
            new_pass_text = past_pass_text + "0"
        
        if self.sender() == self.ui.num1Btn:
            new_pass_text = past_pass_text + "1"
        
        if self.sender() == self.ui.num2Btn:
            new_pass_text = past_pass_text + "2"
        
        if self.sender() == self.ui.num3Btn:
            new_pass_text = past_pass_text + "3"
        
        if self.sender() == self.ui.num4Btn:
            new_pass_text = past_pass_text + "4"
        
        if self.sender() == self.ui.num5Btn:
            new_pass_text = past_pass_text + "5"
        
        if self.sender() == self.ui.num6Btn:
            new_pass_text = past_pass_text + "6"
        
        if self.sender() == self.ui.num7Btn:
            new_pass_text = past_pass_text + "7"
        
        if self.sender() == self.ui.num8Btn:
            new_pass_text = past_pass_text + "8"
        
        if self.sender() == self.ui.num9Btn:
            new_pass_text = past_pass_text + "9"
        
        if self.sender() == self.ui.backspaceBtn:
            new_pass_text = past_pass_text[0:-1]
        
        self.ui.passwordEdt.setText(new_pass_text)    
            
    
    def changeLanguageEvent(self):
        
        if self.sender() == self.ui.chineseLangBtn:
            self.ui.chineseLangBtn.setIcon(QtGui.QIcon(":/icons/Icons/check.png"))
            self.ui.englishLangBtn.setIcon(QtGui.QIcon())
            self.ui.persianLangBtn.setIcon(QtGui.QIcon())
        
        if self.sender() == self.ui.englishLangBtn:
            self.ui.chineseLangBtn.setIcon(QtGui.QIcon())
            self.ui.englishLangBtn.setIcon(QtGui.QIcon(":/icons/Icons/check.png"))
            self.ui.persianLangBtn.setIcon(QtGui.QIcon())

        
        if self.sender() == self.ui.persianLangBtn:
            self.ui.chineseLangBtn.setIcon(QtGui.QIcon())
            self.ui.englishLangBtn.setIcon(QtGui.QIcon())
            self.ui.persianLangBtn.setIcon(QtGui.QIcon(":/icons/Icons/check.png"))
        
    
    def backToMenuCustomizePositions(self):
        self.ui.changeRobotPositionsPages.slideToPreviousWidget()
    
    def goToSettingPositionPage(self):
        self.ui.changeRobotPositionsPages.slideToNextWidget()

        if self.sender() == self.ui.customizeTakePosBtn:
            self.ui.titleSettingPositionsLabel.setText("Customize Take Positions")
            self.ui.titleCountLabel.setText("Take Position 1")
            self.ui.previusMenuCumstomPosBtn.setVisible(False)
            self.ui.nextMenuCumstomPosBtn.setVisible(True)
            self.max_custom_position_setting_page = 2


        if self.sender() == self.ui.customizeWaitPosBtn:
            self.ui.titleSettingPositionsLabel.setText("Customize Wait Position")
            self.ui.titleCountLabel.setText("Wait Position")
            self.ui.previusMenuCumstomPosBtn.setVisible(False)
            self.ui.nextMenuCumstomPosBtn.setVisible(False)

        if self.sender() == self.ui.customizeCollPathPosBtn:
            self.ui.titleSettingPositionsLabel.setText("Customize Collision free path positions")
            self.ui.titleCountLabel.setText("For Pallet 1")
            self.ui.previusMenuCumstomPosBtn.setVisible(False)
            self.ui.nextMenuCumstomPosBtn.setVisible(True)
            self.max_custom_position_setting_page = 6
            

        if self.sender() == self.ui.customizeFirstTilePosBtn:
            self.ui.titleSettingPositionsLabel.setText("Customize The position of the first tile on pallets")
            self.ui.titleCountLabel.setText("For Pallet 1")
            self.ui.previusMenuCumstomPosBtn.setVisible(False)
            self.ui.nextMenuCumstomPosBtn.setVisible(True)
            self.max_custom_position_setting_page = 6
            

    def menuButtonsClickEvent(self):

        if self.sender() == self.ui.settingBtn:

            self.ui.settingBtn.setIcon(QtGui.QIcon(":/icons/Icons/settings_focus.png"))
            self.ui.homeBtn.setIcon(QtGui.QIcon(":/icons/Icons/home.png"))
            self.ui.logBtn.setIcon(QtGui.QIcon(":/icons/Icons/file.png"))
        
            self.ui.settingBtn.setIconSize(QtCore.QSize(60, 60))
            self.ui.homeBtn.setIconSize(QtCore.QSize(55, 55))
            self.ui.logBtn.setIconSize(QtCore.QSize(55, 55))
        
        if self.sender() == self.ui.homeBtn:
            
            self.logout_to_setting()
            
            self.ui.settingBtn.setIcon(QtGui.QIcon(":/icons/Icons/settings.png"))
            self.ui.homeBtn.setIcon(QtGui.QIcon(":/icons/Icons/home_focus.png"))
            self.ui.logBtn.setIcon(QtGui.QIcon(":/icons/Icons/file.png"))
            
            self.ui.settingBtn.setIconSize(QtCore.QSize(55, 55))
            self.ui.homeBtn.setIconSize(QtCore.QSize(60, 60))
            self.ui.logBtn.setIconSize(QtCore.QSize(55, 55))
        
        if self.sender() == self.ui.logBtn:
            
            self.logout_to_setting()

            self.ui.settingBtn.setIcon(QtGui.QIcon(":/icons/Icons/settings.png"))
            self.ui.homeBtn.setIcon(QtGui.QIcon(":/icons/Icons/home.png"))
            self.ui.logBtn.setIcon(QtGui.QIcon(":/icons/Icons/file_focus.png"))
            
            self.ui.settingBtn.setIconSize(QtCore.QSize(55, 55))
            self.ui.homeBtn.setIconSize(QtCore.QSize(55, 55))
            self.ui.logBtn.setIconSize(QtCore.QSize(60, 60))

    
    def changeSettingPagesEvent(self):
        
        if self.sender() == self.ui.item1Btn:
            self.ui.mainSettingPages.setCurrentIndex(0)
        
        if self.sender() == self.ui.item2Btn:
            self.ui.mainSettingPages.setCurrentIndex(1)
        
        if self.sender() == self.ui.item3Btn:
            self.ui.mainSettingPages.setCurrentIndex(2)
        
        if self.sender() == self.ui.item4Btn:
            self.ui.mainSettingPages.setCurrentIndex(3)
        
        if self.sender() == self.ui.item5Btn:
            self.ui.mainSettingPages.setCurrentIndex(4)

    def playPauseBtnClickedEvent(self):
        
        if self.robot_is_run:
            self.ui.playPauseBtn.setIcon(QtGui.QIcon(":/icons/Icons/play-circle.png"))
            self.ui.playPasuStatus.setText("Play")
            self.robot_is_run = False
        
        else:
            self.ui.playPauseBtn.setIcon(QtGui.QIcon(":/icons/Icons/pause-circle.png"))
            self.ui.playPasuStatus.setText("Pause")
            self.robot_is_run = True
    
    def definition_local_variables(self):
        
        self.robot_is_run = False
        self.time_holder = QtCore.QTimer()
        self.time_holder.start()
        self.time_holder.timeout.connect(self.tik_tak_time)
        self.max_custom_position_setting_page = 1

    def login_to_setting(self):
        
        if self.ui.passwordEdt.text() == "1234":
            self.ui.settingPages.slideToNextWidget()

        else:
            self.ui.infoLabel.setText("Invalid Password!")


    def logout_to_setting(self):

        self.ui.settingPages.setCurrentIndex(0)
        self.ui.passwordEdt.setText("")
        self.ui.infoLabel.setText("")

    def startup(self):
        
        local_datetime = datetime.now()
        date_format = f"{local_datetime.day}/{local_datetime.month}/{local_datetime.year}"
        time_format = "%02d:%02d" % (local_datetime.hour, local_datetime.minute)
        
        self.ui.dateLabel.setText(date_format)
        self.ui.timeLabel.setText(time_format)

    def tik_tak_time(self):
        local_datetime = datetime.now()
        time_format = "%02d:%02d" % (local_datetime.hour, local_datetime.minute)
        self.ui.timeLabel.setText(time_format)

    def robotPositionsChangePageEvent(self):

        if self.ui.robotPositionSetting.currentIndex() == 0:
            self.ui.robotPositionSetting.slideToNextWidget()
        
        if self.ui.robotPositionSetting.currentIndex() == 1:
            self.ui.changeRobotPositionsPages.setCurrentIndex(0)
            self.ui.robotPositionSetting.slideToPreviousWidget()
    
    def changeCustomTakePositionSettingEvent(self):
        
        if self.sender() == self.ui.backCustomPosSetting:
            self.ui.customTakePositions.slideToPreviousWidget()
        if self.sender() == self.ui.nextCustomPosSetting:
            if self.ui.customTakePositions.currentIndex() == 1 and \
                self.ui.titlePositionTypeLabel2.text() == "Set Take Position 2":
                    pass
            else:
                self.ui.customTakePositions.slideToNextWidget()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
