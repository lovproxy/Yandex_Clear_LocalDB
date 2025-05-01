import os
import shutil
import wx
import sys
import wx.grid
class Fr(wx.Frame):
    def __init__(self,parent,title='Очистка присутствия'):
        wx.Frame.__init__(self, parent, title=title, size=(500, 190),pos=(600,340))
        wx.StaticText(self, wx.ID_ANY, "Хотите ли вы очистить признаки своего присутствия в браузере?",size=(500,50))
        yea = wx.Button(self,label='Да', size=(500,50),pos=(0,50))
        no = wx.Button(self,label='Нет', size=(500,50),pos=(0,100))
        yea.Bind(wx.EVT_BUTTON,self.Onyea)
        no.Bind(wx.EVT_BUTTON,self.Onno)
    def Onyea(self,a=0):
        try:
            os.remove("C:/Users/rvapv/AppData/Local/Yandex/YandexBrowser/User Data/Default/History")
            os.remove("C:/Users/rvapv/AppData/Local/Yandex/YandexBrowser/User Data/Default/Passman Logs")
            os.remove("C:/Users/rvapv/AppData/Local/Yandex/YandexBrowser/User Data/Default/Shortcuts")
            os.remove("C:/Users/rvapv/AppData/Local/Yandex/YandexBrowser/User Data/Default/Network Action Predictor")
            os.remove("C:/Users/rvapv/AppData/Local/Yandex/YandexBrowser/User Data/Default/Favicons")
            os.remove("C:/Users/rvapv/AppData/Local/Yandex/YandexBrowser/User Data/Default/Web Data")
            os.remove("C:/Users/rvapv/AppData/Local/Yandex/YandexBrowser/User Data/Default/Network/Cookies")
            shutil.rmtree("C:/Users/rvapv/AppData/Local/Yandex/YandexBrowser/User Data/Default/Cache/Cache_data")
            a = 3
        except PermissionError:
            dial = wx.MessageDialog(None, 'Приложение в котором нужно провести очистку открыто!Закройте его в принудительном порядке для проведения очистки вашего присутствия!','Ошибка очистки', wx.CENTER|wx.ICON_ERROR,pos=(960,540))
            dial.ShowModal()
        except FileNotFoundError:
            dial = wx.MessageDialog(None, 'Ваши следы присутствия отсутствуют.Приложение будет закрыто!','Ошибка очистки',wx.ICON_ERROR,pos=(960,540))
            dial.ShowModal()
            sys.exit()
        finally:
            b = 3
        if a ==3:
            dial = wx.MessageDialog(None,
                                    'Очистка выполнена успешно.Приложение будет закрыто!',
                                    'Успешная очистка', wx.OK,pos=(960,540))
            dial.ShowModal()
            a = 0
            sys.exit()
    def Onno(self,c):
        self.que(self)
    def que(self,event):
        dial = wx.MessageDialog(None, 'Вы отменили очистку памяти.Приложение будет закрыто!', 'Отмена очистки',wx.ICON_ERROR,pos=(960,540))
        dial.ShowModal()
        sys.exit()




app = wx.App()
wnd = Fr(None)
wnd.Show(True)
app.MainLoop()
