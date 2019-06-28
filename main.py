import cv2 as cv
import ast
import dlib
import face_recognition
import pickle
import time
from datetime import datetime
import wx
from gui import frame_main,MyDialog_Exit,MyDialog_Setting,MyFrame_Sleep
from camera import camera
from define import *
import pygame
import socket

try:
    import mysql.connector
    import RPi.GPIO as GPIO
except Exception as e:
    pass
    print(e)
import json

class dialog_exit(MyDialog_Exit):
    """docstring for dialog_exit"""
    def __init__(self, parent):
        super(dialog_exit, self).__init__(parent)
        self.parent = parent
        self.exit = False
    def m_button0OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '0'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button1OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '1'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button2OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '2'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button3OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '3'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button4OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '4'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button5OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '5'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button6OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '6'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button7OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '7'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button8OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '8'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button_cleanOnButtonClick( self, event ):
        self.m_textCtrl_password.Clear()

    def m_button9OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '9'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button_cancelOnButtonClick( self, event ):
        self.Destroy()

    def m_button_confirmOnButtonClick( self, event ):
        if self.m_textCtrl_password.GetValue()=='12345':
            print("exit program !")
            self.exit = True
            self.Close()
        else:
            answer = wx.MessageBox("Wrong password ?", "Confirm",
                       wx.YES_NO | wx.CANCEL, self)
            if answer == wx.YES:
                self.exit = False
class dialog_setting(MyDialog_Setting):
    """docstring for dialog_exit"""
    def __init__(self, parent):
        super(dialog_setting, self).__init__(parent)
        self.parent = parent
        self.opendoor = False
        self.locker = 2
        self.sensor_locker = 3
        self.sensor_pir = 4
    def m_button0OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '0'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button1OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '1'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button2OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '2'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button3OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '3'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button4OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '4'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button5OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '5'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button6OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '6'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button7OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '7'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button8OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '8'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button_cleanOnButtonClick( self, event ):
        self.m_textCtrl_password.Clear()

    def m_button9OnButtonClick( self, event ):
        tam = self.m_textCtrl_password.GetValue()
        tam = tam + '9'
        self.m_textCtrl_password.ChangeValue(tam)

    def m_button_cancelOnButtonClick( self, event ):
        self.Destroy()
    def m_button_opendoorOnButtonClick( self, event ):
        if self.m_textCtrl_password.GetValue()=='12345':
            self.opendoor = True
            try:
                control_locker(GPIO,self.locker,1)
                time.sleep(0.2)
                control_locker(GPIO,self.locker,0)
            except BaseException as e:
                print(str(e))
        else:
            answer = wx.MessageBox("Wrong password ?", "Confirm",
                       wx.YES_NO | wx.CANCEL, self)
            if answer == wx.YES:
                self.exit = False        
class frame(frame_main):
    """docstring for frame"""
    def __init__(self, parent):
        super(frame, self).__init__(parent)
        self.parent = parent

        #timer
        self.timer = wx.Timer(self)
        self.timer.Start(1000./30.)
        self.Bind(wx.EVT_TIMER, self.onUpdate_timer, self.timer)
        self.updating = False

        #init camera
        self.cap = camera()
        self.fw, self.fh = self.cap.get_size()
        self.m_panel_video.SetSize(self.fh,self.fw)
        #------------------------
        """ App states """
        self.STATE_RUNNING = 1
        self.STATE_CLOSING = 2
        self.finish_proccessing = True
        self.state = self.STATE_RUNNING

        #------------------------
        self.face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.data = pickle.loads(open("encodings.pickle","rb").read())

        #-------------------------
        try:
            self.config = pickle.loads(open("config.pickle","rb").read())
        except:
            with open("config.pickle","wb") as f:
                pickle.dump(config_default,f)
            self.config = config_default

        #---------------------------
        self.frame_sleep = MyFrame_Sleep(None)
        #DATABASE
        #'''
        try:
            #self.mydb = mysql.connector.connect(host=config["local"]["host"],
            #                        user=config["local"]["user"],
            #                        passwd=config["local"]["password"])
            self.mydb = mysql.connector.connect(host=self.config["server"]["host"],
                                    user=self.config["server"]["user"],
                                    passwd=self.config["server"]["password"])
            print("Connect localhost ok")
            #checking database
            self.mycursor = self.mydb.cursor()
            #create database
            try:
                self.mycursor.execute("CREATE DATABASE face_detect")
                print("database ok")
            except:
                pass
        except Exception as e:
            print("Can not connect to server --> EXIT...")
            print(e)
            #exit()
        #---------------------------------------------------
        #play sound start up
        #'''
        self.sound = pygame.mixer.init(16000,-16,1,4096)
        #play sound start up
        try:
            while(pygame.mixer.music.get_busy()):
                pass
            pygame.mixer.music.load(path_sound1["startup"])
            pygame.mixer.music.play()
            while(pygame.mixer.music.get_busy()):
                pass
        except Exception as e:
            print("error sound")
            print(e)
        #'''
        self.detector = dlib.get_frontal_face_detector()
        self.list_name_dectect = {}
        #define IO
        self.locker = 2
        self.sensor_locker = 3
        self.sensor_pir = 4
        try:
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.locker,GPIO.OUT,initial=GPIO.LOW)
            #-------------
            GPIO.setup(self.sensor_locker,GPIO.IN)
            GPIO.setup(self.sensor_pir,GPIO.IN)
        except Exception as e:
            pass
            print("IO ERROR")
            print(e)
        #send data to server
        self.HOST = '192.168.0.124'  # The server's hostname or IP address
        self.PORT = 65432        # The port used by the server

        self.process_this_frame = True

    def onUpdate_timer(self,event):
        if (self.state == self.STATE_RUNNING) and (self.finish_proccessing == True):
            try:                
                if GPIO.input(self.sensor_pir):
                    self.m_panel_video.Refresh()
                    #print("detect person")
                    self.frame_sleep.Show(False)
                else:
                    #print("no detect person")
                    self.frame_sleep.Show(True)         
            except Exception as e:
                self.m_panel_video.Refresh()
                print(e)            
            #check sensor pir here
    def m_menuItem_exitOnMenuSelection( self, event ):
        self.Close()
    def m_panel_videoOnEraseBackground( self, event ):
        return
    #view image in windows
    def m_panel_videoOnPaint( self, event ):
        self.finish_proccessing = False
        
        #fw, fh = self.m_panel_video.GetSize()
        fw, fh = self.cap.get_size()
        self.m_panel_video.SetSize(fh,fw)
        frame =  self.cap.get_image()
        gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
        #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #proccessing image here
        faces = self.face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5,minSize = (150,150),flags=cv.CASCADE_SCALE_IMAGE)
        #faces = self.detector(frame,0)
        #dets = [[d.left(),d.top(),d.right()-d.left(),d.bottom()-d.top()] for d in faces]
        dets = faces
        #Device context
        dc = wx.BufferedPaintDC(self.m_panel_video)
        h, w = frame.shape[:2]
        image = wx.Bitmap.FromBuffer(w, h, frame)       
        #draw to panel  
        dc.DrawBitmap(image, 0, 0)
        #---------------------------------------
        time_login = 30
        pygame.mixer.init(16000,-16,1,4096)
        for (x,y,w,h) in dets:
            boxe = [(int(y),int(x+w),int(y+h),int(x))]
            #boxe = [(y,x+w,y+h,x)]
            #boxe = dlib.rectangle(int(y), int(w+w), int(y+h), int(x))
            # print [(160, 327, 311, 176)]
            #print(boxe)
            #setting pen and brush
            dc.SetPen(wx.Pen(wx.Colour(0, 255, 0, alpha=wx.ALPHA_OPAQUE), width=2, style=wx.PENSTYLE_SOLID))
            dc.SetBrush(wx.Brush(wx.Colour(0, 255, 0, alpha=wx.ALPHA_OPAQUE),wx.BRUSHSTYLE_TRANSPARENT))
            dc.DrawRectangle(x,y,w,h)
            #encoding it
            encoding =  face_recognition.face_encodings(frame,boxe)
            #send/reivecer data to server
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((self.HOST, self.PORT))
                    #gui du lieu
                    data_string = pickle.dumps(encoding)
                    s.sendall(data_string)
                    #nhan du lieu tra ve
                    data = s.recv(2048)
                    matches = pickle.loads(data)
                    #print("connected server")
                    s.close()
            except Exception as e:
                print(e)
                #compare it with data encoding,if no server
                matches = face_recognition.compare_faces(self.data["encodings"],encoding[0],tolerance = 0.4)               
            #=================
            name = "unknown"
            counts = {}
            names = []
            if True in matches:
                matchesID = [i for (i,b) in enumerate(matches, start=0) if b]
                for i in matchesID:
                    name =  self.data["names"][i]
                    counts[name] = counts.get(name,0) + 1
                name = max(counts,key=counts.get)

            #print to debug
            self.m_textCtrl_debug.write("xin chao: ")
            self.m_textCtrl_debug.write(name)
            self.m_textCtrl_debug.write(" at ")
            self.m_textCtrl_debug.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            self.m_textCtrl_debug.write("\n")

            #draw text in panel
            dc.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, underline=False,faceName="", encoding=wx.FONTENCODING_SYSTEM))
            #set color for text
            dc.SetTextForeground(wx.Colour(250, 0, 0, alpha=wx.ALPHA_OPAQUE))
            #draw test in panel
            dc.DrawText(name,x,y-20)

            if name != "unknown":
                # name is detected
                if name in self.list_name_dectect:
                    time_now = datetime.now()
                    delta = (time_now - datetime.strptime(self.list_name_dectect[name],'%Y-%m-%d %H:%M:%S')).total_seconds()
                    #compare time
                    if delta > time_login :
                        #print("login again in time > 10 second, save date login !")
                        #update time
                        self.list_name_dectect[name] = time_now.strftime('%Y-%m-%d %H:%M:%S')
                        #save here
                        name_table = "history_" + str(time_now.year) +"_" + str(time_now.month)
                        #creat table if non exits
                        try:
                            self.mycursor.execute("CREATE TABLE `face_detect`.`"+name_table + "` (id VARCHAR(5), time_log DATETIME, confirm VARCHAR(20))")
                        except:
                            pass

                        sql_insert = "INSERT INTO `face_detect`.`"+name_table+"` (`id`,`time_log`, `confirm`) VALUES (%s , %s, %s)"
                        val_insert = (id_name[name],time_now.strftime('%Y-%m-%d %H:%M:%S'),None)
                        #print(sql_insert)
                        #print(val_insert)
                        try:
                            #connect ok
                            self.mycursor.execute(sql_insert,val_insert)
                            self.mydb.commit()
                            print(self.mycursor.rowcount, "record inserted.")
                            #check file backup to save if have data
                            with open("backup.txt") as fp:  
                                line = fp.readline()
                                while line:
                                    line.rstrip()
                                    val_insert = parse_tuple(line)
                                    #----
                                    if val_insert != None:    
                                        self.mycursor.execute(sql_insert,val_insert)
                                        self.mydb.commit()
                                        print(self.mycursor.rowcount, "record inserted.")
                                    line = fp.readline()
                                fp.close()
                                f = open("backup.txt", "w")
                                f.write("")
                                f.close()

                        except BaseException as e:
                            print("Can not insert database,reconnecting !")
                            print(e)
                            try:
                                self.mydb = mysql.connector.connect(host=self.config["server"]["host"],user=self.config["server"]["user"],passwd=self.config["server"]["password"])
                                print("Connect localhost ok")
                                #checking database
                                self.mycursor = self.mydb.cursor()
                                #-----------------
                                self.mycursor.execute(sql_insert,val_insert)
                                self.mydb.commit()
                                print(self.mycursor.rowcount, "record inserted.")
                                #check backup file
                                with open("backup.txt") as fp:  
                                    line = fp.readline()
                                    while line:                                       
                                        line.rstrip()
                                        val_insert = parse_tuple(line)
                                        line = fp.readline()
                                        #----
                                        if val_insert != None: 
                                            self.mycursor.execute(sql_insert,val_insert)
                                            self.mydb.commit()
                                            print(self.mycursor.rowcount, "record inserted.")
                                    fp.close()
                                    f = open("backup.txt", "w")
                                    f.write("")
                                    f.close()
                            except BaseException as ee:
                                print(ee)
                                print("save to file backup")
                                f = open("backup.txt", "a")
                                f.write(str(val_insert))
                                f.write("\n")
                                f.close()
                        #play sound
                        try:
                            while(pygame.mixer.music.get_busy()):
                                pass
                            if time_now.hour <= 12:
                                pygame.mixer.music.load(path_sound1[name])
                            else:
                                pygame.mixer.music.load(path_sound2[name])
                            pygame.mixer.music.play()
                            while(pygame.mixer.music.get_busy()):
                                pass
                        except BaseException as e:
                            print("conflit sound !")
                            print(str(e))
                        # control open door
                        try:
                            control_locker(GPIO,self.locker,1)
                            time.sleep(0.2)
                            control_locker(GPIO,self.locker,0)
                        except Exception as e:
                            pass
                    else:
                        #print("login again in time < 10 second, don't save here !")
                        pass
                # name no detected before
                else:
                    time_now = datetime.now()
                    #initilize time
                    self.list_name_dectect[name] = time_now.strftime('%Y-%m-%d %H:%M:%S')
                    #print("first time login, save data here !")
                    #save
                    name_table = "history_" + str(time_now.year) +"_" + str(time_now.month)
                    try:
                        self.mycursor.execute("CREATE TABLE `face_detect`.`"+name_table + "` (id VARCHAR(5), time_log DATETIME, confirm VARCHAR(20))")
                    except:
                        pass
                    sql_insert = "INSERT INTO `face_detect`.`"+name_table+"` (`id`,`time_log`, `confirm`) VALUES (%s , %s, %s)"
                    val_insert = (id_name[name],time_now.strftime('%Y-%m-%d %H:%M:%S'),None)
                    #print(sql_insert)
                    #print(val_insert)
                    try:
                        self.mycursor.execute(sql_insert,val_insert)
                        self.mydb.commit()
                        print(self.mycursor.rowcount, "record inserted.")
                        #check file backup to save if have data
                        with open("backup.txt") as fp:  
                            line = fp.readline()
                            while line:
                                line.rstrip()
                                val_insert = parse_tuple(line)
                                line = fp.readline()
                                #----
                                if val_insert != None: 
                                    self.mycursor.execute(sql_insert,val_insert)
                                    self.mydb.commit()
                                    print(self.mycursor.rowcount, "record inserted by file.")
                            fp.close()
                            f = open("backup.txt", "w")
                            f.write("")
                            f.close()
                    except Exception as e:
                        print("Can not insert database !")
                        print(e)
                        try:
                            #try connect again
                            self.mydb = mysql.connector.connect(host=self.config["server"]["host"],user=self.config["server"]["user"],passwd=self.config["server"]["password"])
                            print("Connect localhost ok")
                            #checking database
                            self.mycursor = self.mydb.cursor()
                            #-----------------
                            #connect ok
                            self.mycursor.execute(sql_insert,val_insert)
                            self.mydb.commit()
                            print(self.mycursor.rowcount, "record inserted.")
                            #check file backup to save if have data
                            with open("backup.txt") as fp:  
                                line = fp.readline()
                                while line:
                                    line.rstrip()
                                    val_insert = parse_tuple(line)
                                    line = fp.readline()
                                    #----
                                    if val_insert != None: 
                                        self.mycursor.execute(sql_insert,val_insert)
                                        self.mydb.commit()
                                        print(self.mycursor.rowcount, "record inserted.")
                                fp.close()
                                f = open("backup.txt", "w")
                                f.write("")
                                f.close()
                        except:
                            print("save to file backup")
                            f = open("backup.txt", "a")
                            f.write(str(val_insert))
                            f.write("\n")
                            f.close()

                    #playsound
                    try:
                        while(pygame.mixer.music.get_busy()):
                            pass
                        if time_now.hour <= 12:
                            pygame.mixer.music.load(path_sound1[name])
                        else:
                            pygame.mixer.music.load(path_sound2[name])
                        pygame.mixer.music.play()
                        while(pygame.mixer.music.get_busy()):
                            pass
                    except BaseException as e:
                        print("conflit sound !")
                        print(str(e))

                    # control open door
                    try:
                        control_locker(GPIO,self.locker,1)
                        time.sleep(0.2)
                        control_locker(GPIO,self.locker,0)
                    except Exception as e:
                        pass
                                
        self.finish_proccessing = True
    def m_button_exitOnButtonClick(self,event):
        view_dialog_exit = dialog_exit(None)
        view_dialog_exit.ShowModal()
        if view_dialog_exit.exit:
            view_dialog_exit.Destroy()
            self.state = self.STATE_CLOSING
            self.cap.release()
            self.Close()
    def m_button_settingOnButtonClick( self, event ):
        view_dialog_setting = dialog_setting(None)
        view_dialog_setting.ShowModal()
        if view_dialog_setting.opendoor:
            control_locker(GPIO,self.locker,1)
            time.sleep(0.2)
            control_locker(GPIO,self.locker,0)
        view_dialog_setting.Destroy()

def control_locker(gpio_object,pin,status):
    if status:
        gpio_object.output(pin,gpio_object.HIGH)
    else:
        gpio_object.output(pin,gpio_object.LOW)
    return 0        
# APP
def parse_tuple(string):
    try:
        s = ast.literal_eval(str(string))
        if type(s) == tuple:
            return s
        return
    except:
        return

app = wx.App(False)
frame_ = frame(None)
frame_.Show()
app.MainLoop()
