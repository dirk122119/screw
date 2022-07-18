from flask_wtf import FlaskForm as Form
from wtforms import StringField,FloatField,SubmitField, validators,ValidationError
from wtforms import BooleanField
from flask import flash
from wtforms.fields.core import SelectField


from user.ManualInput.model import ScrewClass
from user import db
items=ScrewClass.query.all()

def wholenum2choice(items):
    unique_wholenum=[]
    dic_wholenum=[]
    for item in items:
        if item.Screw_Head_wholenum not in unique_wholenum:
            unique_wholenum.append(item.Screw_Head_wholenum)
    for indx,item in enumerate(unique_wholenum):
        dic_wholenum.append((indx,item))
    return dic_wholenum

def headlabel2choice(items):
    unique_headlabel=[]
    dic_headlabel=[]
    for item in items:
        if item. Screw_label not in unique_headlabel:
            unique_headlabel.append(item.Screw_label)
    for indx,item in enumerate(unique_headlabel):
        dic_headlabel.append((indx,item))
    return dic_headlabel

def coat2choice(items):
    unique_coat2choice=[]
    dic_coat2choice=[]
    for item in items:
        if item.Screw_coat  not in unique_coat2choice:
            unique_coat2choice.append(item.Screw_coat)
    for indx,item in enumerate(unique_coat2choice):
        dic_coat2choice.append((indx,item))
    return dic_coat2choice

class Form_AI_uk(Form):
    '''
    手動輸入要找的螺絲資料
    '''    
    Head_Label=SelectField('標籤',choices=headlabel2choice(items))
    Coat=SelectField('鍍膜種類',choices=coat2choice(items))

    submit = SubmitField(u'查詢')



class Form_AI_us(Form):
    '''
    手動輸入要找的螺絲資料
    '''
    Head_Label=SelectField('標籤',choices=headlabel2choice(items))
    Coat=SelectField('鍍膜種類',choices=coat2choice(items))

    submit = SubmitField(u'查詢')


    submit = SubmitField(u'查詢')


    