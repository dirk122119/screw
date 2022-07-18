from flask_wtf import FlaskForm as Form
from wtforms import StringField,FloatField,SubmitField, validators,ValidationError,IntegerField
from wtforms import BooleanField
from flask import flash
from wtforms.fields.core import SelectField

from user.ManualInput.model import ScrewClass
from user import db


class Update_form(Form):
    
    Screw_number=StringField('螺絲編號')
    Headtype=StringField('頭部形狀')
    Head_Label=StringField('標籤')
    Head_Whole_Num=StringField('頭部鑿洞數')
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
    Body_Width_us=StringField('身直徑(番數)')    
    Coat=StringField('鍍膜種類')
    Price=IntegerField('價錢 NTD')

    submit = SubmitField(u'修改')

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


class Create_form(Form):
    Screw_number=StringField('螺絲編號')
    Headtype=StringField('頭部形狀')
    Head_Label=StringField('標籤')
    Head_Whole_Num=StringField('頭部鑿洞數')
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
    Body_Width_us=StringField('身直徑(番數)')    
    Coat=StringField('鍍膜種類')
    Price=IntegerField('價錢 NTD')

    submit = SubmitField(u'新增螺絲種類')

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