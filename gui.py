# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frame_main
###########################################################################

class frame_main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ASTI - FACE DETECT", pos = wx.DefaultPosition, size = wx.Size( 800,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 128, 64 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap_logo = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"logo.PNG", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_bitmap_logo, 0, wx.ALL, 5 )

		self.m_staticText_info = wx.StaticText( self, wx.ID_ANY, u"FACE RECOGNITION SYSTEM", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText_info.Wrap( -1 )

		self.m_staticText_info.SetFont( wx.Font( 50, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText_info.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

		bSizer4.Add( self.m_staticText_info, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button_exit = wx.Button( self, wx.ID_ANY, u"EXIT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_exit.SetFont( wx.Font( 30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer4.Add( self.m_button_exit, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_panel_video = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel_video.SetBackgroundColour( wx.Colour( 0, 255, 255 ) )

		bSizer2.Add( self.m_panel_video, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl_debug = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,100 ), wx.TE_MULTILINE )
		bSizer3.Add( self.m_textCtrl_debug, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_setting = wx.Button( self, wx.ID_ANY, u"SETTING", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_setting.SetFont( wx.Font( 30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer5.Add( self.m_button_setting, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer5, 0, 0, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.frame_mainOnActivate )
		self.m_button_exit.Bind( wx.EVT_BUTTON, self.m_button_exitOnButtonClick )
		self.m_panel_video.Bind( wx.EVT_ERASE_BACKGROUND, self.m_panel_videoOnEraseBackground )
		self.m_panel_video.Bind( wx.EVT_PAINT, self.m_panel_videoOnPaint )
		self.m_button_setting.Bind( wx.EVT_BUTTON, self.m_button_settingOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def frame_mainOnActivate( self, event ):
		event.Skip()

	def m_button_exitOnButtonClick( self, event ):
		event.Skip()

	def m_panel_videoOnEraseBackground( self, event ):
		event.Skip()

	def m_panel_videoOnPaint( self, event ):
		event.Skip()

	def m_button_settingOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog_Exit
###########################################################################

class MyDialog_Exit ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"CONFIRM TO EXIT PROGRAM", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"PASSWORD:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer9.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		bSizer9.Add( self.m_textCtrl_password, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer22.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_cancel = wx.Button( self, wx.ID_ANY, u"CANCEL", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button_cancel, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button_confirm = wx.Button( self, wx.ID_ANY, u"CONFIRM", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button_confirm, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer22.Add( bSizer7, 1, wx.EXPAND, 5 )


		bSizer6.Add( bSizer22, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button0 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button0, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer10.Add( bSizer11, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button3, 1, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button4, 1, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button5, 1, wx.ALL, 5 )


		bSizer10.Add( bSizer12, 1, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button6, 1, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button7, 1, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button8, 1, wx.ALL, 5 )


		bSizer10.Add( bSizer13, 1, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_clean = wx.Button( self, wx.ID_ANY, u"CLEAN ALL", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button_clean, 1, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button9, 1, wx.ALL, 5 )


		bSizer10.Add( bSizer14, 1, wx.EXPAND, 5 )


		bSizer6.Add( bSizer10, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()
		bSizer6.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button_cancel.Bind( wx.EVT_BUTTON, self.m_button_cancelOnButtonClick )
		self.m_button_confirm.Bind( wx.EVT_BUTTON, self.m_button_confirmOnButtonClick )
		self.m_button0.Bind( wx.EVT_BUTTON, self.m_button0OnButtonClick )
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
		self.m_button2.Bind( wx.EVT_BUTTON, self.m_button2OnButtonClick )
		self.m_button3.Bind( wx.EVT_BUTTON, self.m_button3OnButtonClick )
		self.m_button4.Bind( wx.EVT_BUTTON, self.m_button4OnButtonClick )
		self.m_button5.Bind( wx.EVT_BUTTON, self.m_button5OnButtonClick )
		self.m_button6.Bind( wx.EVT_BUTTON, self.m_button6OnButtonClick )
		self.m_button7.Bind( wx.EVT_BUTTON, self.m_button7OnButtonClick )
		self.m_button8.Bind( wx.EVT_BUTTON, self.m_button8OnButtonClick )
		self.m_button_clean.Bind( wx.EVT_BUTTON, self.m_button_cleanOnButtonClick )
		self.m_button9.Bind( wx.EVT_BUTTON, self.m_button9OnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button_cancelOnButtonClick( self, event ):
		event.Skip()

	def m_button_confirmOnButtonClick( self, event ):
		event.Skip()

	def m_button0OnButtonClick( self, event ):
		event.Skip()

	def m_button1OnButtonClick( self, event ):
		event.Skip()

	def m_button2OnButtonClick( self, event ):
		event.Skip()

	def m_button3OnButtonClick( self, event ):
		event.Skip()

	def m_button4OnButtonClick( self, event ):
		event.Skip()

	def m_button5OnButtonClick( self, event ):
		event.Skip()

	def m_button6OnButtonClick( self, event ):
		event.Skip()

	def m_button7OnButtonClick( self, event ):
		event.Skip()

	def m_button8OnButtonClick( self, event ):
		event.Skip()

	def m_button_cleanOnButtonClick( self, event ):
		event.Skip()

	def m_button9OnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog_Setting
###########################################################################

class MyDialog_Setting ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"SETTING PROGRAM", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"PASSWORD:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer9.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		bSizer9.Add( self.m_textCtrl_password, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer23.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_cancel = wx.Button( self, wx.ID_ANY, u"CANCEL", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button_cancel, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button_opendoor = wx.Button( self, wx.ID_ANY, u"OPEN DOOR", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button_opendoor, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer23.Add( bSizer7, 1, wx.EXPAND, 5 )


		bSizer6.Add( bSizer23, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button0 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button0, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer10.Add( bSizer11, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button3, 1, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button4, 1, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button5, 1, wx.ALL, 5 )


		bSizer10.Add( bSizer12, 1, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button6, 1, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button7, 1, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button8, 1, wx.ALL, 5 )


		bSizer10.Add( bSizer13, 1, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_del = wx.Button( self, wx.ID_ANY, u"Del", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button_del, 1, wx.ALL, 5 )

		self.m_button_clean = wx.Button( self, wx.ID_ANY, u"CLEAN ALL", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button_clean, 1, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button9, 1, wx.ALL, 5 )


		bSizer10.Add( bSizer14, 1, wx.EXPAND, 5 )


		bSizer6.Add( bSizer10, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()
		bSizer6.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button_cancel.Bind( wx.EVT_BUTTON, self.m_button_cancelOnButtonClick )
		self.m_button_opendoor.Bind( wx.EVT_BUTTON, self.m_button_opendoorOnButtonClick )
		self.m_button0.Bind( wx.EVT_BUTTON, self.m_button0OnButtonClick )
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
		self.m_button2.Bind( wx.EVT_BUTTON, self.m_button2OnButtonClick )
		self.m_button3.Bind( wx.EVT_BUTTON, self.m_button3OnButtonClick )
		self.m_button4.Bind( wx.EVT_BUTTON, self.m_button4OnButtonClick )
		self.m_button5.Bind( wx.EVT_BUTTON, self.m_button5OnButtonClick )
		self.m_button6.Bind( wx.EVT_BUTTON, self.m_button6OnButtonClick )
		self.m_button7.Bind( wx.EVT_BUTTON, self.m_button7OnButtonClick )
		self.m_button8.Bind( wx.EVT_BUTTON, self.m_button8OnButtonClick )
		self.m_button_del.Bind( wx.EVT_BUTTON, self.m_button_delOnButtonClick )
		self.m_button_clean.Bind( wx.EVT_BUTTON, self.m_button_cleanOnButtonClick )
		self.m_button9.Bind( wx.EVT_BUTTON, self.m_button9OnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button_cancelOnButtonClick( self, event ):
		event.Skip()

	def m_button_opendoorOnButtonClick( self, event ):
		event.Skip()

	def m_button0OnButtonClick( self, event ):
		event.Skip()

	def m_button1OnButtonClick( self, event ):
		event.Skip()

	def m_button2OnButtonClick( self, event ):
		event.Skip()

	def m_button3OnButtonClick( self, event ):
		event.Skip()

	def m_button4OnButtonClick( self, event ):
		event.Skip()

	def m_button5OnButtonClick( self, event ):
		event.Skip()

	def m_button6OnButtonClick( self, event ):
		event.Skip()

	def m_button7OnButtonClick( self, event ):
		event.Skip()

	def m_button8OnButtonClick( self, event ):
		event.Skip()

	def m_button_delOnButtonClick( self, event ):
		event.Skip()

	def m_button_cleanOnButtonClick( self, event ):
		event.Skip()

	def m_button9OnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame_Sleep
###########################################################################

class MyFrame_Sleep ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SLEEP", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


