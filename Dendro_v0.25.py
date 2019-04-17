#!/usr/bin/env python3
#    2018-2019, Misha, Andrei, Edward

from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import font
import pickle
from tkcolorpicker import askcolor
from tkinter import messagebox
import re
import sys
import os



#================================================================================================

vaccine_reference = {'>A/Michigan/45/2015','>A/Singapore/INFIMH-16-0019/2016', '>B/Colorado/06/2017', '>B/Phuket/3073/2013', '>A/Brisbane/02/2018', '>A/Kansas/14/2017', }
qdict={'09':'#4B0082', '10':'#8B00FF', '11' :'#CC00CC', '12':'#0000FF', '01':'#00CCFF', '02':'#006633','03':'#33CC33', '04':'#FF6600', '05':'#CC3366', '06':'#996633', '07':'#996633'}


#****************************************************************************
#start palette---------------------------------------------------------------

def LaunchEditor():
    CpopU = Toplevel(root) #ColorPopUp
    CpopU.title("PhiloPalette")
    CpopU.geometry("660x435")

    global MyFont, MyFont2
    MyFont = font.Font(family="Lucida", size=10, weight=font.BOLD)
    MyFont2 = font.Font(family="Lucida", size=12, weight=font.BOLD)
    ButtonColor='#D8C3B1'
    StdColorsL = ['#00CCFF','#006633','#33CC33','#FF6600','#CC3366','#996633','#999999','#222222','#4B0082','#8B00FF','#CC00CC','#0000FF']


    def ShowTool():
        askcolor(color="red", parent=f00, title="Color Chooser", alpha=False)


    def SaveColors():
        SavedName=ColorProfileBox.get()
        with open(('3_ColorProfiles/' + SavedName + '_profile.dcp'),'wb') as outF:
            a=pickle.dumps(NewColorList)
            outF.write(a)


    def LoadColors():
        InputFileName = filedialog.askopenfilename(title = "Select color profile",initialdir = "3_ColorProfiles/", filetypes = (("Dendro Color Profiles","*.dcp"),("all files","*.*")))
        with open(InputFileName, 'rb') as inF:
            b=inF.read()
            unpickledLIST= pickle.loads(b)
        accept('FromFile', unpickledLIST)


    def accept(x,y):
        GetList = [ncolor1,ncolor2,ncolor3,ncolor4,ncolor5,ncolor6,ncolor7,ncolor8,ncolor9,ncolor10,ncolor11,ncolor12]
        global NewColorList
        NewColorList=[]  
        global qdict
        qdict={'09':'#4B0082', '10':'#8B00FF', '11' :'#CC00CC', '12':'#0000FF', '01':'#00CCFF', '02':'#006633','03':'#33CC33', '04':'#FF6600', '05':'#CC3366', '06':'#996633', '07':'#996633'}
        if x=='FromKybd':
            for item in GetList:
                g=item.get()
                NewColorList.append(g)

        else:
            for item in GetList:
                item.delete(0, 'end')        
                        
        if x=='FromFile':
            NewColorList = y
            z=0
            for item in GetList:            
                item.insert(END, y[z])
                z+=1

            
        if x=='Defaults':
            x=0
            for item in GetList:            
                item.insert(END, StdColorsL[x])
                x+=1
            NewColorList = StdColorsL

        
        #NEW COLORS DISPLAYED -----------------------------------------------------------------------------
        month1n = Label(f00, padx=10, anchor='w', text='January', fg=NewColorList[0], bg="white", font=MyFont2) 
        month1n.place(x = 273, y = 50, width=120, height=25)
        month2n = Label(f00, padx=10, anchor='w', text='February', fg=NewColorList[1], bg="white", font=MyFont2) 
        month2n.place(x = 273, y = 80, width=120, height=25)
        month3n = Label(f00, padx=10, anchor='w',text='March', fg=NewColorList[2], bg="white", font=MyFont2) 
        month3n.place(x = 273, y = 110, width=120, height=25)
        month4n = Label(f00, padx=10, anchor='w',text='April', fg=NewColorList[3], bg="white", font=MyFont2) 
        month4n.place(x = 273, y = 140, width=120, height=25)
        month5n = Label(f00, padx=10, anchor='w',text='May', fg=NewColorList[4], bg="white", font=MyFont2) 
        month5n.place(x = 273, y = 170, width=120, height=25)
        month6n = Label(f00, padx=10, anchor='w',text='June', fg=NewColorList[5], bg="white", font=MyFont2) 
        month6n.place(x = 273, y = 200, width=120, height=25)
        month7n = Label(f00, padx=10, anchor='w',text='July', fg=NewColorList[6], bg="white", font=MyFont2) 
        month7n.place(x = 273, y = 230, width=120, height=25)
        month8n = Label(f00,  padx=10, anchor='w',text='August', fg=NewColorList[7], bg="white", font=MyFont2) 
        month8n.place(x = 273, y = 260, width=120, height=25)
        month9n = Label(f00, padx=10, anchor='w',text='September', fg=NewColorList[8], bg="white", font=MyFont2) 
        month9n.place(x = 273, y = 290, width=120, height=25)
        month10n = Label(f00, padx=10, anchor='w',text='October', fg=NewColorList[9], bg="white", font=MyFont2) 
        month10n.place(x = 273, y = 320, width=120, height=25)
        month11n = Label(f00, padx=10, anchor='w',text='November', fg=NewColorList[10], bg="white", font=MyFont2) 
        month11n.place(x = 273, y = 350, width=120, height=25)
        month12n = Label(f00, padx=10, anchor='w',text='December', fg=NewColorList[11], bg="white", font=MyFont2) 
        month12n.place(x = 273, y = 380, width=120, height=25)

    def CloseThePalette():
        CpopU.destroy()

    # BUTTONS----------------------------------------------------------------------------------------
    f00 = Label(CpopU, bg='#4d4949')
    f00.place(x = 10, y = 0, width=640, height=425)

    f00w04=Button(CpopU, font=MyFont, bg=ButtonColor, text="Accept Entered Codes",  anchor="w", padx=12,  command= lambda: accept('FromKybd',[]))
    f00w04.place(x = 425, y = 40, width=200, height=30)
    f00w06=Button(CpopU, font=MyFont, bg=ButtonColor, text="Save Custom Profile",  anchor="w", padx=12, command=SaveColors)
    f00w06.place(x = 425 , y = 80, width=200, height=30)
    f00w07=Button(CpopU, font=MyFont, bg=ButtonColor, text="Load Custom Profile",  anchor="w", padx=12, command=LoadColors)
    f00w07.place(x = 425 , y = 160, width=200, height=30)
    f00w08=Button(CpopU, font=MyFont, bg=ButtonColor, text="Restore Default Profile",  anchor="w", padx=12, command= lambda: accept('Defaults',[]))
    f00w08.place(x = 425 , y = 200, width=200, height=30)
    f00w09=Button(CpopU, font=MyFont, bg=ButtonColor, text="Show Color Tool",  anchor="w", padx=12, command=ShowTool )
    f00w09.place(x = 425 , y = 240, width=200, height=30)
    f00w10=Button(CpopU, font=MyFont, bg=ButtonColor, text="Export Into Dendro",  anchor="w", padx=12, command= lambda: push(NewColorList) )
    f00w10.place(x = 425 , y = 280, width=200, height=30)
    f00w20=Button(CpopU, font=MyFont,  bg=ButtonColor,text="Close", padx=12, command= CloseThePalette)
    f00w20.place(x = 540, y = 385, width=80, height=30)

    #HEADINGS---------------------------------------------------------------------------------------------
    Head1 = Label(CpopU, padx=10, anchor='w',font=MyFont, text='Custom Code', bg="#B4835B", fg="black") 
    Head1.place(x = 150, y = 10, width=120, height=25)
    Head2 = Label(CpopU, padx=10, anchor='w',font=MyFont, text='Default Code', bg="#B4835B", fg="black") 
    Head2.place(x = 15, y = 10, width=120, height=25)
    Head3 = Label(CpopU, padx=10, anchor='w',font=MyFont, text='New Code', bg="#B4835B", fg="black") 
    Head3.place(x = 285, y = 10, width=120, height=25)

    #Default LEFT display of months----------------------------------------------------------------------
    month1 = Label(CpopU, padx=10, anchor='w', text='January', fg=StdColorsL[0], bg="white", font=MyFont2) 
    month1.place(x = 15, y = 50, width=120, height=25)
    month2 = Label(CpopU, padx=10, anchor='w', text='February', fg=StdColorsL[1], bg="white", font=MyFont2) 
    month2.place(x = 15, y = 80, width=120, height=25)
    month3 = Label(CpopU, padx=10, anchor='w',text='March', fg=StdColorsL[2], bg="white", font=MyFont2) 
    month3.place(x = 15, y = 110, width=120, height=25)
    month4 = Label(CpopU, padx=10, anchor='w',text='April', fg=StdColorsL[3], bg="white", font=MyFont2) 
    month4.place(x = 15, y = 140, width=120, height=25)
    month5 = Label(CpopU, padx=10, anchor='w',text='May', fg=StdColorsL[4], bg="white", font=MyFont2) 
    month5.place(x = 15, y = 170, width=120, height=25)
    month6 = Label(CpopU, padx=10, anchor='w',text='June', fg=StdColorsL[5], bg="white", font=MyFont2) 
    month6.place(x = 15, y = 200, width=120, height=25)
    month7 = Label(CpopU, padx=10, anchor='w',text='July', fg=StdColorsL[6], bg="white", font=MyFont2) 
    month7.place(x = 15, y = 230, width=120, height=25)
    month8 = Label(CpopU,  padx=10, anchor='w',text='August', fg=StdColorsL[7], bg="white", font=MyFont2) 
    month8.place(x = 15, y = 260, width=120, height=25)
    month9 = Label(CpopU, padx=10, anchor='w',text='September', fg=StdColorsL[8], bg="white", font=MyFont2) 
    month9.place(x = 15, y = 290, width=120, height=25)
    month10 = Label(CpopU, padx=10, anchor='w',text='October', fg=StdColorsL[9], bg="white", font=MyFont2) 
    month10.place(x = 15, y = 320, width=120, height=25)
    month11 = Label(CpopU, padx=10, anchor='w',text='November', fg=StdColorsL[10], bg="white", font=MyFont2) 
    month11.place(x = 15, y = 350, width=120, height=25)
    month12 = Label(CpopU, padx=10, anchor='w',text='December', fg=StdColorsL[11], bg="white", font=MyFont2) 
    month12.place(x = 15, y = 380, width=120, height=25)

    #ENTRY BOXES ------------------------------------------------
    ncolor1=Entry(CpopU, bg="#B4835B", fg="black", font=MyFont2)
    ncolor1.place(x = 150, y = 50, width=120, height=25)
    ncolor2=Entry(CpopU, bg="#B4835B", fg="black", font=MyFont2)
    ncolor2.place(x = 150, y = 80, width=120, height=25)
    ncolor3=Entry(CpopU, bg="#B4835B", fg="black", font=MyFont2)
    ncolor3.place(x = 150, y = 110, width=120, height=25)
    ncolor4=Entry(CpopU, bg="#B4835B", fg="black", font=MyFont2)
    ncolor4.place(x = 150, y = 140, width=120, height=25)
    ncolor5=Entry(CpopU, bg="#B4835B", fg="black", font=MyFont2)
    ncolor5.place(x = 150, y = 170, width=120, height=25)
    ncolor6=Entry(CpopU, bg="#B4835B", fg="black", font=MyFont2)
    ncolor6.place(x = 150, y = 200, width=120, height=25)
    ncolor7=Entry(CpopU, bg="#B4835B", fg="black", font=MyFont2)
    ncolor7.place(x = 150, y = 230, width=120, height=25)
    ncolor8=Entry(CpopU, bg="#B4835B", fg="black", font=MyFont2)
    ncolor8.place(x = 150, y = 260, width=120, height=25)
    ncolor9=Entry(CpopU, bg="#B4835B", fg="black", font=MyFont2)
    ncolor9.place(x = 150, y = 290, width=120, height=25)
    ncolor10=Entry(CpopU, bg="#B4835B", fg="black", font=MyFont2)
    ncolor10.place(x = 150, y = 320, width=120, height=25)
    ncolor11=Entry(CpopU, bg="#B4835B", fg="black", font=MyFont2)
    ncolor11.place(x = 150, y = 350, width=120, height=25)
    ncolor12=Entry(CpopU, bg="#B4835B", fg="black", font=MyFont2)
    ncolor12.place(x = 150, y = 380, width=120, height=25)

    c=0
    for thing in[ncolor1,ncolor2,ncolor3,ncolor4,ncolor5,ncolor6,ncolor7,ncolor8,ncolor9,ncolor10,ncolor11,ncolor12]:
        thing.insert(END, StdColorsL[c])
        c+=1

    #Person's profile name 
    ColorProfileBox=Entry(CpopU, bg="#B4835B", fg="black", font=MyFont2)
    ColorProfileBox.place(x = 425, y = 120, width=200, height=30)


#**************************************************************************
#end palette---------------------------------------------------------------


root = Tk()
root.geometry('695x370')
root.configure(background='#4d4949')
root.title ( ' Dendrophyl - beta version' )


background_image = PhotoImage(file = '4_sys/like2.png')
background_label = Label(root, image=background_image)
background_label.place(x=10,y=10)

TheFont1 = font.Font(family="Lucida", size=10, weight=font.BOLD)
ButtonColor='#D8C3B1'
StatusBox = Text(root, font=TheFont1, wrap="word", height=9, width=50, padx=25, pady=5, fg='#333333', bg='#DDDDDD') 
StatusBox.place(x = 505, y = 10, width=180, height=285)
StatusBox.insert(END, '\nReady to process phylogenetic tree files\n\nDefault Color Profile Loaded')

DendroMonthSTDColorsL = ['#00CCFF','#006633','#33CC33','#FF6600','#CC3366','#996633','#999999','#222222','#4B0082','#8B00FF','#CC00CC','#0000FF']

#================================================================================================

def push(x):  
    StatusBox.delete(1.0, 'end')   
    StatusBox.insert(END, '\n\nNew Color Profile Imported\n\nReady to process phylogenetic tree files')
    qdict.clear()
    for z in range(1,13):
        qdict[str(z).zfill(2)] = NewColorList[z-1] 

#================================================================================================

def GetInputData():
    global InputFileName
    InputFileName = filedialog.askopenfilename(initialdir = "1_DendroINPUT/",title = "Select SVG file",filetypes = (("svg files","*.svg"),("all files","*.*")))
    with open (InputFileName, 'r') as ifo:
        content = ifo.read()
        content = content.replace('_(Day_unknown)','-01')
        global tail
        head, tail = os.path.split(InputFileName)
    return content

#================================================================================================

def GetInputData2():
    global InputFileName2
    InputFileName2 = filedialog.askopenfilename(initialdir = "1_DendroINPUT/",title = "Select TXT file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    with open (InputFileName2, 'r') as ifo2:
        content2 = ifo2.read().splitlines()
        global tail
        head, tail = os.path.split(InputFileName2)
    return content2

#================================================================================================

def GetInputData4():
    global InputFileName4
    InputFileName4 = filedialog.askopenfilename(initialdir = "1_DendroINPUT/",title = "Select TXT file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    with open (InputFileName4, 'r') as ifo4:
        content4 = ifo4.read()
        content4 = content4.replace('_(Day_unknown)','-01')
        global tail
        head, tail = os.path.split(InputFileName4)
    return content4


#================================================================================================

def FirstCircleFn(x):
    a1 = str(re.findall(r'stroke:none;"\n\s*>[A-Z\,\s0-9]*<', x))
    a2 = re.findall(r'>[A-Z][0-9]*[A-Z][^>]*<', a1)
    b1 = str(re.findall(r'stroke:none;"\n\s*>[A-Z\,\s0-9]*<', x))
    b2 = re.findall(r'>[A-Z][0-9]*[A-Z]<', a1)
    return (a2,b2)

#================================================================================================

def DiskWritingFunction(p, q):
    OutNamingDct = {1:'_onlySNP.svg', 2:'_normal_auto.svg', 3:'_bold_auto.svg',4:'_list_normal.svg',5:'_list_bold.svg',6:'_special.svg', 7:'_monocolor.svg'}

    outputfile = filedialog.asksaveasfilename(initialdir='2_DendroOUTPUT/', title = "Select save directory", filetypes = (("svg files","*.svg"),("all files","*.*")), initialfile = tail[:-4] + OutNamingDct[p])
    with open (outputfile, 'w') as savedfile:
        savedfile.write(q)

#================================================================================================



def SVGch():
    l = rbvar.get()
    if l == 0 :
        myregex=r'stroke:none;font-weight:normal;fill:'
        myregex_bold=r'stroke:none;font-weight:bold;fill:'
        endregex ='\"\n\t>'
        vaccine_color = r'stroke:none;font-weight:bold;fill:#000000"\n\t'
        red_text = r'stroke:none;font-weight:bold;fill:#FF0000"\n\t'
        stroke_ft = r'stroke:none;"[ \s]*'
    # elif l == 1 :
    #     myregex=r'style="font-weight:bold;fill:'   
    #     endregex = ';stroke:none"\n       x="0">'
    #     vaccine_color = r'style="font-weight:bold;fill:#000000;stroke:none"\n       x="0">'
    #     red_text = r'style="font-weight:bold;fill:#FF0000;stroke:none"\n       x="0">'

    return (myregex, endregex, vaccine_color, red_text, stroke_ft, myregex_bold)

#================================================================================================

def func1():
    content = GetInputData()
    ReturnedInfo = FirstCircleFn(content)
    SVGpicker=SVGch()
    a2 = ReturnedInfo[0]
    b2 = ReturnedInfo[1]

    myregex = SVGpicker[0]
    endregex = SVGpicker[1]
    vaccine_color = SVGpicker[2]
    red_text = SVGpicker[3]
    stroke_ft = SVGpicker[4]

    for color in qdict.keys():

        search = r'[ABC][^>]*\_[0-9]*[\-\_]'
        re_circle = re.findall(search  + color + r'[^>]*<', content)

        for j in b2:
            content = re.sub(stroke_ft + j , red_text + j , content, flags=re.MULTILINE)

        for y in a2:
            content = re.sub(stroke_ft + y , red_text + y , content, flags=re.MULTILINE)
        
        for i in vaccine_reference:
            content = re.sub(stroke_ft + i, vaccine_color + i + '*', content, flags=re.MULTILINE)
        
        for e in re_circle:
            var1= e
            var2 = re.findall(r'[ABC]\/[A-Za-z0-9\-\/\_]*\/[0-9]*', e)
            var3 = str(var2)[2:-2]
            content = re.sub(var1, var3 + '<', content)
            
    DiskWritingFunction(1, content) 
    messagebox.showinfo(" Complete! ", " Complete! ")

#================================================================================================


def func2():
    content = GetInputData()
    ReturnedInfo = FirstCircleFn(content)
    SVGpicker=SVGch()
    a2 = ReturnedInfo[0]
    b2 = ReturnedInfo[1]

    myregex = SVGpicker[0]
    endregex = SVGpicker[1]
    vaccine_color = SVGpicker[2]
    red_text = SVGpicker[3]
    stroke_ft = SVGpicker[4]

    for color in qdict.keys():

        rgb_code = qdict.get(color)
        search = r'[ABC][^>]*\_[0-9]*[\-\_]' 
        re_circle = re.findall( search  + color + r'[^>]*<', content)

        for u in re_circle: 
            content = re.sub(stroke_ft + r'>' + u, myregex + rgb_code + endregex + u, content, flags=re.MULTILINE)
        for j in b2:
            content = re.sub(stroke_ft + j , red_text + j , content, flags=re.MULTILINE)
        for y in a2:
            content = re.sub(stroke_ft + y , red_text + y , content, flags=re.MULTILINE)
        for i in vaccine_reference:
            content = re.sub(stroke_ft + i, vaccine_color + i + '*', content, flags=re.MULTILINE)
        for e in re_circle:
            var1 = e
            var2 = re.findall(r'[ABC]\/[A-Za-z0-9\-\/\_]*\/[0-9]*', e)
            var3 = str(var2)[2:-2]
            content = re.sub(var1, var3 + '<', content)

    DiskWritingFunction(2, content)
    messagebox.showinfo(" Complete! ", " Complete! ")

#================================================================================================

def func3():
    content = GetInputData()
    ReturnedInfo = FirstCircleFn(content)
    SVGpicker=SVGch()
    a2 = ReturnedInfo[0]
    b2 = ReturnedInfo[1]

    myregex = SVGpicker[5]
    endregex = SVGpicker[1]
    vaccine_color = SVGpicker[2]
    red_text = SVGpicker[3]
    stroke_ft = SVGpicker[4]

    for color in qdict.keys():

        rgb_code = qdict.get(color)
        search = r'[ABC][^>]*\_[0-9]*[\-\_]' 
        re_circle = re.findall( search  + color + r'[^>]*<', content)

        for u in re_circle: 
            content = re.sub(stroke_ft + r'>' + u, myregex + rgb_code + endregex + u, content, flags=re.MULTILINE)
        for j in b2:
            content = re.sub(stroke_ft + j , red_text + j , content, flags=re.MULTILINE)
        for y in a2:
            content = re.sub(stroke_ft + y , red_text + y , content, flags=re.MULTILINE)
        for i in vaccine_reference:
            content = re.sub(stroke_ft + i, vaccine_color + i + '*', content, flags=re.MULTILINE)
        for e in re_circle:
            var1 = e
            var2 = re.findall(r'[ABC]\/[A-Za-z0-9\-\/\_]*\/[0-9]*', e)
            var3 = str(var2)[2:-2]
            content = re.sub(var1, var3 + '<', content)

    DiskWritingFunction(3, content)
    messagebox.showinfo(" Complete! ", " Complete! ")

#================================================================================================


def func4():    
    content = GetInputData()
    content2 = GetInputData2()
    ReturnedInfo = FirstCircleFn(content)
    SVGpicker=SVGch()
    a2 = ReturnedInfo[0]
    b2 = ReturnedInfo[1]

    myregex = SVGpicker[0]
    endregex = SVGpicker[1]
    vaccine_color = SVGpicker[2]
    red_text = SVGpicker[3]
    stroke_ft = SVGpicker[4]
    
    for color in qdict.keys():       
        rgb_code = qdict.get(color)
        search = r'[ABC][^>]*\_[0-9]*[\-]'
        re_circle1 = list(re.findall(search  + color + r'[^>]*<', content))

        for one in content2:

            re_circle = re.findall(r'>'+ search  + color + r'[^>]*<', one)
                        
            for u in re_circle: 
                content = re.sub(stroke_ft + u, myregex + rgb_code + endregex + u[1:], content, flags=re.MULTILINE)

        for j in b2:
            content = re.sub(stroke_ft + j , red_text + j , content, flags=re.MULTILINE)
        for y in a2:
            content = re.sub(stroke_ft + y , red_text + y , content, flags=re.MULTILINE)
        for i in vaccine_reference:
            content = re.sub(stroke_ft + i, vaccine_color + i + '*', content, flags=re.MULTILINE)

        for e in re_circle1:
            var1 = e
            var2 = re.findall(r'[ABC]\/[A-Za-z0-9\-\/\_]*\/[0-9]*', e)
            var3 = str(var2)[2:-2]
            content = re.sub(var1, var3  + '<', content)
    
    DiskWritingFunction(4, content)
    messagebox.showinfo(" Complete! ", " Complete! ")
    
# #================================================================================================

def func5():  

    content = GetInputData()
    content2 = GetInputData2()
    ReturnedInfo = FirstCircleFn(content)
    SVGpicker=SVGch()
    a2 = ReturnedInfo[0]
    b2 = ReturnedInfo[1]

    myregex = SVGpicker[5]
    endregex = SVGpicker[1]
    vaccine_color = SVGpicker[2]
    red_text = SVGpicker[3]
    stroke_ft = SVGpicker[4]
    
    for color in qdict.keys():       
        rgb_code = qdict.get(color)
        search = r'[ABC][^>]*\_[0-9]*[\-]'
        re_circle1 = list(re.findall(search  + color + r'[^>]*<', content))

        for one in content2:

            re_circle = re.findall(r'>'+ search  + color + r'[^>]*<', one)
                        
            for u in re_circle: 
                content = re.sub(stroke_ft + u, myregex + rgb_code + endregex + u[1:], content, flags=re.MULTILINE)

        for j in b2:
            content = re.sub(stroke_ft + j , red_text + j , content, flags=re.MULTILINE)
        for y in a2:
            content = re.sub(stroke_ft + y , red_text + y , content, flags=re.MULTILINE)
        for i in vaccine_reference:
            content = re.sub(stroke_ft + i, vaccine_color + i + '*', content, flags=re.MULTILINE)

        for e in re_circle1:
            var1 = e
            var2 = re.findall(r'[ABC]\/[A-Za-z0-9\-\/\_]*\/[0-9]*', e)
            var3 = str(var2)[2:-2]
            content = re.sub(var1, var3  + '<', content)
    
    DiskWritingFunction(5, content)
    messagebox.showinfo(" Complete! ", " Complete! ")
    
#================================================================================================+
def func6():
    global content
    content = GetInputData()
    content2 = GetInputData2()

    def get_smbl(event):
        smbl = Entry_win.get()
        window_new.destroy()
        global content
        
        for line in content2:
            content = re.sub(line, line + smbl, content, flags=re.MULTILINE)

        DiskWritingFunction(6, content)
        messagebox.showinfo(" Complete! ", " Complete! ")

    window_new = Toplevel(root)
    window_new.geometry('300x100')
    window_new.title('New window')
    label_text = Label(window_new, text=' Write your symbol')
    label_text.place(x=20, y=10)
    Entry_win = Entry (window_new, width= 15, font= 15)
    Entry_win.place(x=20, y=50)
    button_win = Button(window_new, text= ' Check!')
    button_win.place(x=165, y=50)
    button_win.bind("<Button-1>", get_smbl)


#=============================================================================================

# def func7():
#     content = GetInputData()
#     content2 = GetInputData2()
#     ReturnedInfo = FirstCircleFn(content)
#     a2 = ReturnedInfo[0]
#     b2 = ReturnedInfo[1]

#     myregex = SVGch()

#     for color in dict.keys():       
#         rgb_code = dict.get(color)
#         vaccine_color = r'stroke:none;font-weight:bold;fill:#000000"\n\t>'
#         red_text = r'stroke:none;font-weight:bold;fill:#FF0000"\n\t'
#         search = r'[ABC][^>]*\_[0-9]*[\-\_]' 
#         delete_tails = list(re.findall(search  + r'[^>]*<', content))
    
#         for i in content2:
#             content = re.sub('x="0">' + i, myregex + i, content, flags=re.MULTILINE)
#         for j in b2:
#             content = re.sub(r'stroke:none;"[ \n\t]*' + j , red_text + j , content, flags=re.MULTILINE)
#         for y in a2:
#             content = re.sub(r'stroke:none;"[ \n\t]*' + y , red_text + y , content, flags=re.MULTILINE)
#         for i in vaccine_reference:
#             content = re.sub(r'stroke:none;"[ \n\t]*>' + i, vaccine_color + i + '*', content, flags=re.MULTILINE)

#         for e in delete_tails:
#             var1 = e
#             var2 = re.findall(r'[ABC]\/[A-Za-z0-9\-\/\_]*\/[0-9]*', e)
#             var3 = str(var2)[2:-2]
#             content = re.sub(var1, var3 + '<', content)

    
#     DiskWritingFunction(7, content)
    # messagebox.showinfo(" Complete! ", " Complete! ")

#=============================================================================================

def about():
    global StatusBox
    StatusBox.delete(1.0, 'end')
    StatusBox = Text(root, font=TheFont1, wrap="word", height=9, width=50, padx=25, pady=5, fg='#333333', bg='#DDDDDD') 
    StatusBox.place(x = 505, y = 10, width=180, height=285)
    StatusBox.insert(END, '\n\n  M. Bakaev\n  A. Komissarov\n  E. Ramsay\n\n\n\n\n   Smorodintsev Research Institute \n    of Influenza \n\n\n\n      2018-2019')



#=============================================================================================

def nothing():
    abc=0

button1 = Button(root, text = ' Only SNP ', anchor='w', bg=ButtonColor, font=TheFont1, command=func1 )
button1.place(x=10,y=155, width= 240)
button2 = Button(root, text = 'Special character', anchor='w', bg=ButtonColor, font=TheFont1, command = func6)
button2.place(x=10,y=190, width= 240)
button3 = Button(root, text = 'SNP + list (bold)', anchor='w',  bg=ButtonColor,font=TheFont1, command = func5)
button3.place(x=10,y=225, width= 240)
button4 = Button(root, text = 'SNP + list (normal)', anchor='w',  bg=ButtonColor,font=TheFont1, command = func4)
button4.place(x=10,y=260, width= 240)
button5 = Button(root, text = 'SNP, automatic (normal)', anchor='w',  bg=ButtonColor,font=TheFont1, command = func2)
button5.place(x=10,y=295, width= 240)
button6 = Button(root, text = 'SNP, automatic (bold)', anchor='w',  bg=ButtonColor,font=TheFont1, command = func3)
button6.place(x=10,y=330, width= 240)
button7 = Button(root, text = 'Open Color Profile Editor', anchor='w',  bg=ButtonColor,font=TheFont1, command = LaunchEditor)
button7.place(x=255,y=155, width= 240)


# button8 = Button(root, text = ' EXPERIMENTAL, MUHAHAHA', anchor='w', bg=ButtonColor, font=TheFont1, command = func7)
# button8.place(x=255,y=225, width= 240)
# button9 = Button(root, text = ' 2', anchor='w',  bg=ButtonColor,font=TheFont1, command = nothing)
# button9.place(x=255,y=330, width= 240)
# button10 = Button(root, text = ' 3', anchor='w',  bg=ButtonColor,font=TheFont1, command = nothing)
# button10.place(x=255,y=260, width= 240)
# button11 = Button(root, text = ' 4', anchor='w',  bg=ButtonColor,font=TheFont1, command = nothing)
# button11.place(x=255,y=295, width= 240)

button12 = Button(root, text = ' About', anchor='w',  bg=ButtonColor,font=TheFont1, command = about)
button12.place(x=255,y=190, width= 240)
button20 = Button(root, text = 'exit', bg=ButtonColor, font=TheFont1, command =sys.exit)
button20.place(x=625,y=330, width= 60)


#=============================================================================================

rbvar = IntVar()
rbvar.set(0)

rb01 = Radiobutton(text= 'After FigTree', value = 0,  variable = rbvar, command = SVGch)
rb01.place(x=505, y = 310, width = 100)
# rb02 = Radiobutton(text = "After InkScape", value = 1, variable = rbvar, command = SVGch )
# rb02.place(x=505, y = 330, width = 100)

#=============================================================================================




root.mainloop()