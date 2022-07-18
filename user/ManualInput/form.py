from flask_wtf import FlaskForm as Form
from wtforms import StringField,FloatField,SubmitField, validators,ValidationError
from wtforms import BooleanField
from flask import flash
from wtforms.fields.core import SelectField

from user.ManualInput.model import ScrewClass
from user import db


def headtype2choice(items):
    unique_headtype=[]
    dic_headtype=[]
    for item in items:
        if item.Screw_Head_Type not in unique_headtype:
            unique_headtype.append(item.Screw_Head_Type)
    for indx,item in enumerate(unique_headtype):
        dic_headtype.append((indx,item))
    return dic_headtype

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

def usbody2choice(items):
    unique_usbody2choice=[]
    dic_usbody2choice=[]
    for item in items:
        if item.Screw_Body_Width_us  not in unique_usbody2choice:
            unique_usbody2choice.append(item.Screw_Body_Width_us)
    for indx,item in enumerate(unique_usbody2choice):
        dic_usbody2choice.append((indx,item))
    return dic_usbody2choice

class FormManualInput_uk(Form):

    items=ScrewClass.query.all()
    
    '''
    手動輸入要找的螺絲資料
    '''
    Head_Legth=FloatField(u'頭長(mm)', validators=[
        validators.DataRequired()
    ])

    Head_Width=FloatField(u'頭寬(mm)', validators=[
        validators.DataRequired()
    ])

    Body_Length=FloatField(u'身長(mm)', validators=[
        validators.DataRequired()
    ])

    Body_Width=FloatField(u'身直徑(mm)', validators=[
        validators.DataRequired()
    ])
    Head_Whole_Num=SelectField('頭部鑿洞數',choices=wholenum2choice(items))
    Headtype=SelectField('頭部形狀',choices=headtype2choice(items))
    Head_Label=SelectField('標籤',choices=headlabel2choice(items))
    Coat=SelectField('鍍膜種類',choices=coat2choice(items))


    submit = SubmitField(u'查詢')

    def validate_Head_Width(self,field):
        if field.data>200:
            raise ValidationError('超過200mm')
        if field.data<1:
            raise ValidationError('小於1mm')
    def validate_Head_Legth(self,field):
        if field.data>200:
            raise ValidationError('超過200mm')
        if field.data<1:
            raise ValidationError('小於1mm')
    def validate_Body_Length(self,field):
        if field.data>200:
            raise ValidationError('超過200mm')
        if field.data<1:
            raise ValidationError('小於1mm')
    def validate_Body_Width(self,field):
        if field.data>200:
            raise ValidationError('超過200mm')
        if field.data<1:
            raise ValidationError('小於1mm')

class FormManualInput_us(Form):
    items=ScrewClass.query.all()
    '''
    手動輸入要找的螺絲資料
    '''
    Head_Legth=FloatField(u'頭長(mm)', validators=[
        validators.DataRequired()
    ])
    Head_Width=FloatField(u'頭寬(mm)', validators=[
        validators.DataRequired()
    ])

    Body_Length=FloatField(u'身長(mm)', validators=[
        validators.DataRequired()
    ])

    Body_Width_us=SelectField('身直徑(番數)',choices=usbody2choice(items))

    Head_Whole_Num=SelectField('頭部鑿洞數',choices=wholenum2choice(items))
    Headtype=SelectField('頭部形狀',choices=headtype2choice(items))
    Head_Label=SelectField('標籤',choices=headlabel2choice(items))
    Coat=SelectField('鍍膜種類',choices=coat2choice(items))



    submit = SubmitField(u'查詢')

    def validate_Head_Width(self,field):
        if field.data>200:
            raise ValidationError('超過200mm')
        if field.data<1:
            raise ValidationError('小於1mm')
    def validate_Head_Legth(self,field):
        if field.data>200:
            raise ValidationError('超過200mm')
        if field.data<1:
            raise ValidationError('小於1mm')
    def validate_Body_Length(self,field):
        if field.data>200:
            raise ValidationError('超過200mm')
        if field.data<1:
            raise ValidationError('小於1mm')


items=ScrewClass.query.all()
dic_headtype=[]
for indx,item in enumerate(items):
    dic_headtype.append((indx,item.Screw_Head_Type))