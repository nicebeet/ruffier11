from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test
from seconds import Seconds
age = 16
name = ""
p1, p2, p3 = 0, 0, 0
def cheak_int(str_num):
    try:
        return int(str_num)
    except:
        return False
    
class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        instr=Label(text=txt_instruction, size_hint=(0.8,0.2), pos_hint={'center_x':0.5, 'center_y':0.7} )
        lbl1=Label(text='Введіть імя',size_hint=(0.4,0.1), pos_hint={'x':0, 'center_y':0.3} )
        self.in_name=TextInput(multiline=False,size_hint=(0.4,0.1), pos_hint={'x':0.5, 'center_y':0.3} )
        lbl2=Label(text='Введіть вік',size_hint=(0.4,0.1), pos_hint={'x':0, 'center_y':0.2} )
        self.in_age=TextInput(multiline=False,size_hint=(0.4,0.1), pos_hint={'x':0.5, 'center_y':0.2} )
        self.btn=Button(text='Почати', size_hint=(0.3,0.1), pos_hint={'x':0.5, 'center_y':0.1})
        self.btn.on_press=self.next
        layout.add_widget(instr)
        layout.add_widget(lbl1)
        layout.add_widget(self.in_name)
        layout.add_widget(lbl2)
        layout.add_widget(self.in_age)
        layout.add_widget(self.btn)
        self.add_widget(layout)
    def next(self):
        global name
        name=self.in_name.text
        age= cheak_int(self.in_age.text)
        if age==False or age<7:
            age=7
            self.in_age.text=str(age)
        else:
            self.manager.current='pulse1'

class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        self.next_screen= False
        instr=Label(text=txt_test1, size_hint=(0.8,0.2), pos_hint={'center x':0.5, 'top':1} )
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)
        lbl_rezultat = Label(text='Введіть результат:',size_hint=(0.4,0.1),pos_hint={'x':0, 'center_y':0.7})
        self.in_rezult=TextInput(text='0',size_hint=(0.4,0.1), pos_hint={'x':0.5, 'center_y':0.7})
        self.in_rezult.set_disabled(True)
        self.btn=Button(text="Продовжити",size_hint=(0.3,0.1), pos_hint={'center_x':0.5, 'center_y':0.4})
        self.btn.on_press=self.next
        layout.add_widget(self.btn)
        layout.add_widget(instr)
        layout.add_widget(lbl_rezultat)
        layout.add_widget(self.in_rezult)
        layout.add_widget(self.lbl_sec)
        self.add_widget(layout)
    def sec_finished(self,*args):
        self.next_screen = True
        self.in_rezult.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = "Продовжити"
    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p1
            p1=int(self.in_rezult.text)
            if p1 == False or p1 <= 0:
                p1 = 0
                self.in_rezult.text = str(p1)
                print("Введіть заміри пульсу")
            else:
                self.manager.current='sits'

class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        instr=Label(text=txt_sits, size_hint=(0.8,0.2), pos_hint={'center x':0.5, 'top':1} )
        self.btn = Button(text="Продовжити",size_hint=(0.3,0.1), pos_hint={'center_x':0.5, 'center_y':0.4})

        self.btn.on_press=self.next
        layout.add_widget(self.btn)
        layout.add_widget(instr)
        self.add_widget(layout)
    def next(self):
        self.manager.current='pulse2'
class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        instr=Label(text=txt_test3, size_hint=(0.8,0.2), pos_hint={'center x':0.5, 'top':1} )
        lbl_result1=Label(text='Результат',size_hint=(0.4,0.1), pos_hint={'x':0, 'center_y':0.7} )
        self.in_result1=TextInput(multiline=False,size_hint=(0.4,0.1), pos_hint={'x':0.5, 'center_y':0.7} )
        lbl_result2=Label(text='Результат пусля відпочинку',size_hint=(0.4,0.1), pos_hint={'x':0, 'center_y':0.6} )
        self.in_result2=TextInput(multiline=False,size_hint=(0.4,0.1), pos_hint={'x':0.5, 'center_y':0.6} )
        self.btn=Button(text='Завершити', size_hint=(0.3,0.1), pos_hint={'x':0.5, 'center_y':0.4})
        self.btn.on_press=self.next
        layout.add_widget(instr)
        layout.add_widget(lbl_result1)
        layout.add_widget(self.in_result1)
        layout.add_widget(lbl_result2)
        layout.add_widget(self.in_result2)
        layout.add_widget(self.btn)
        self.add_widget(layout)
    def next(self):
        global p2, p3
        p2=cheak_int(self.in_result1.text)
        p3=cheak_int(self.in_result2.text)
        if p2 == False:
            p2 = 0
            self.in_result1.text = str(p2)
        elif p3 == False:
            p3=0
            self.in_result2.text = str(p3)
        else:
            self.manager.current='result'

class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        self.instr=Label(text='',size_hint=(0.8,0.2), pos_hint={'center x':0.5, 'center_y':0.7} )
        layout.add_widget(self.instr)
        self.add_widget(layout)
        self.on_enter=self.before
    
    def before(self):
        global name
        self.instr.text=name+'\n'+test(p1,p2,p3,age)



class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='instr'))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(CheckSits(name='sits'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(Result(name='result'))
        return sm
    
app=HeartCheck()
app.run()
