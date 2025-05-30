from tkinter import*
from mydb import Database
from tkinter import messagebox
from myapi import API
# tkinter is a librabry we are importing all of the classes from it

class NLPApp:
    # constrcutoe
    def __init__(self):

        # create database object()
        self.dbo = Database()
        self.apio = API()

        # Tk() is a class in tkinter
        # root is a variable and we are storing tk() class object into it
        # load GUI
        self.root = Tk()
        # to keep GUI on screen
        self.root.title('NLPApp')
        self.root.iconbitmap('favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#fcebd2')

        self.login_GUI()
        self.root.mainloop() 
    
    def login_GUI(self):
        self.clear()
        heading = Label(self.root,text='NLP App',bg='#fcebd2',fg='Black')      
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        lablel1 = Label(self.root,text='Enter Email')
        lablel1.pack(pady=(10,10))

        self.email_input= Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        lablel2 = Label(self.root,text='Enter Password')
        lablel2.pack(pady=(10,10))

        self.password_input= Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)

        login_button = Button(self.root,text='Login',width=30,height=2,command=self.perfrom_login)
        login_button.pack(pady=(10,10))

        lablel3 = Label(self.root,text='Not a Member')
        lablel3.pack(pady=(20,10))

        redirect = Button(self.root,text='Register',width=30,height=2,command=self.register_GUI)
        redirect.pack(pady=(10,10))

    def register_GUI(self):
        self.clear()
        heading = Label(self.root,text='NLP App',bg='#fcebd2',fg='Black')      
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        lablel0 = Label(self.root,text='Enter Name')
        lablel0.pack(pady=(10,10))

        self.name_input= Entry(self.root,width=50)
        self.name_input.pack(pady=(5,10),ipady=4)

        lablel1 = Label(self.root,text='Enter Email')
        lablel1.pack(pady=(10,10))

        self.email_input= Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        lablel2 = Label(self.root,text='Enter Password')
        lablel2.pack(pady=(10,10))

        self.password_input= Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)

        login_button = Button(self.root,text='Register',width=30,height=2,command=self.perfrom_registration)
        login_button.pack(pady=(10,10))

        lablel3 = Label(self.root,text='Already a Member')
        lablel3.pack(pady=(20,10))

        redirect = Button(self.root,text='Login',width=30,height=2,command=self.login_GUI)
        redirect.pack(pady=(10,10))

    def clear(self):
            for i in self.root.pack_slaves():
                i.destroy()

    def perfrom_registration(self):
         name =  self.name_input.get()
         email = self.email_input.get()
         password = self.password_input.get() 
         
         response = self.dbo.add_data(name,email,password)

         if response:
              messagebox.showinfo('Success','Registration Successfull. You can login Know')
         else:
                messagebox.showerror('Error','email exists')

    def perfrom_login(self):
         email = self.email_input.get()
         password = self.password_input.get() 

         response = self.dbo.search(email,password)

         if response:
              messagebox.showinfo('Success','Login Successfull')  
              self.home()           
         else:
              messagebox.showinfo('Error','Wrong email/password')

    def home(self):
        self.clear()

        heading = Label(self.root,text='NLP App',bg='#fcebd2',fg='Black')      
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        sentiment_button = Button(self.root,text='Sentiment Analysis',width=30,height=4,command=self.sentiment_gui)
        sentiment_button.pack(pady=(10,10))

        ner_button = Button(self.root,text='Named Entity Recognition',width=30,height=4,command=self.ner_gui)
        ner_button.pack(pady=(10,10))

        emotion_button = Button(self.root,text='Emotion Prediction',width=30,height=4,command=self.emotion_gui)
        emotion_button.pack(pady=(10,10))

        Logout = Button(self.root,text='Logout',width=30,height=2,command=self.login_GUI)
        Logout.pack(pady=(10,10))

    
    def sentiment_gui(self):
         self.clear()
         heading = Label(self.root,text='NLP App',bg='#fcebd2',fg='Black')      
         heading.pack(pady=(30,30))
         heading.configure(font=('verdana',24,'bold'))
         
         heading2 = Label(self.root,text='Sentiment Analysis',bg='#fcebd2',fg='Black')      
         heading2.pack(pady=(10,20))
         heading2.configure(font=('verdana',20,'bold'))

         lablel1 = Label(self.root,text='Enter the Text')
         lablel1.pack(pady=(10,10))

         self.sentiment_input= Entry(self.root,width=50)
         self.sentiment_input.pack(pady=(5,10),ipady=4)

         sent_button = Button(self.root,text='Analyze Sentiment',width=30,height=2,command=self.do_sentiment_analysis)
         sent_button.pack(pady=(10,10))

         self.sentiment_result = Label(self.root,text='',bg='#fcebd2',fg='Black')      
         self.sentiment_result.pack(pady=(10,10))
         self.sentiment_result.configure(font=('verdana',16))

         goback_button = Button(self.root,text='Go back',width=30,height=2,command=self.home)
         goback_button.pack(pady=(10,10))

    def do_sentiment_analysis(self):
         
         text=self.sentiment_input.get()
         result = self.apio.sentiment_analysis(text)
         
         txt=''
         for i in result['sentiment']:
              txt =txt+ i+' -> '+str(result['sentiment'][i])+'\n'
              
         self.sentiment_gui['text']=txt

    def ner_gui(self):
         self.clear()
         heading = Label(self.root,text='NLP App',bg='#fcebd2',fg='Black')      
         heading.pack(pady=(30,30))
         heading.configure(font=('verdana',24,'bold'))
         
         heading2 = Label(self.root,text='NER Analysis',bg='#fcebd2',fg='Black')      
         heading2.pack(pady=(10,20))
         heading2.configure(font=('verdana',20,'bold'))

         lablel1 = Label(self.root,text='Enter the Text')
         lablel1.pack(pady=(10,10))

         self.ner_input= Entry(self.root,width=50)
         self.ner_input.pack(pady=(5,10),ipady=4)

         sent_button = Button(self.root,text='Analyze NER',width=30,height=2,command=self.do_ner_analysis)
         sent_button.pack(pady=(10,10))

         self.ner_result = Label(self.root,text='',bg='#fcebd2',fg='Black')      
         self.ner_result.pack(pady=(10,10))
         self.ner_result.configure(font=('verdana',16))

         goback_button = Button(self.root,text='Go back',width=30,height=2,command=self.home)
         goback_button.pack(pady=(10,10))
    
    def do_ner_analysis(self):
         text=  self.ner_input.get()
         result = self.apio.ner_analysis(text)
         
         txt=''
         for i in result['ner']:
              txt =txt+ i+' -> '+str(result['ner'][i])+'\n'
              
         self.ner_analysis['ner']=txt
    
    def emotion_gui(self):
         self.clear()
         heading = Label(self.root,text='NLP App',bg='#fcebd2',fg='Black')      
         heading.pack(pady=(30,30))
         heading.configure(font=('verdana',24,'bold'))
         
         heading2 = Label(self.root,text='Emotion Analysis',bg='#fcebd2',fg='Black')      
         heading2.pack(pady=(10,20))
         heading2.configure(font=('verdana',20,'bold'))

         lablel1 = Label(self.root,text='Enter the Text')
         lablel1.pack(pady=(10,10))

         self.Emotion_input= Entry(self.root,width=50)
         self.Emotion_input.pack(pady=(5,10),ipady=4)

         sent_button = Button(self.root,text='Analyze Emotion',width=30,height=2,command=self.do_emotion_analysis)
         sent_button.pack(pady=(10,10))

         self.Emotion_result = Label(self.root,text='',bg='#fcebd2',fg='Black')      
         self.Emotion_result.pack(pady=(10,10))
         self.Emotion_result.configure(font=('verdana',16))

         goback_button = Button(self.root,text='Go back',width=30,height=2,command=self.home)
         goback_button.pack(pady=(10,10))

    def do_emotion_analysis(self) :
         text=self.Emotion_input.get()
         result = self.apio.emotion_analysis(text)
         
         txt=''
         for i in result['emotion']:
              txt =txt+ i+' -> '+str(result['emotion'][i])+'\n'
              
         self.ner_analysis['emotion']=txt



nlp = NLPApp()

