from urllib import response
from flask import render_template,flash,request,redirect,url_for,Blueprint,Response
from flask_login import login_user, current_user, login_required,logout_user
from user.ManualInput.model import ScrewClass,AddScrewTotable,Img
from flask_wtf import FlaskForm as Form
from werkzeug.utils import secure_filename
from user import db

Database=Blueprint('Database',__name__)
@Database.route('/showdatabase', methods=['GET', 'POST'])
def show_data():
    table_list=[]
    items=ScrewClass.query.all()
    for item in items:
        table_list.append(item)
    return render_template('Database/showdata.html',table_list=table_list)

@Database.route('/Create/',methods=['GET', 'POST'])
def Create_new():
    from user.Database.form import Create_form
    form=Create_form()
    if request.method =='POST':

       
        new_item=ScrewClass()
        number=form.Screw_number.data
        Headtype=form.Headtype.data
        Head_Label=form.Head_Label.data
        Head_Whole_Num=form.Head_Whole_Num.data
        Head_Legth= form.Head_Legth.data
        Head_Width=form.Head_Width.data
        Body_Length=form.Body_Length.data
        Body_Width=form.Body_Width.data
        Body_Width_us=form.Body_Width_us.data
        Coat=form.Coat.data
        Price=form.Price.data

        new_item.number=number
        new_item.Screw_Head_Type=Headtype
        new_item.Screw_label=Head_Label
        new_item.Screw_Head_wholenum=Head_Whole_Num
        new_item.Screw_Head_length=float(Head_Legth)
        new_item.Screw_Head_Width=float(Head_Width)
        new_item.Screw_Body_Length=float(Body_Length)
        new_item.Screw_Body_Width=float(Body_Width)
        new_item.Screw_Body_Width_us=Body_Width_us
        new_item.Screw_coat=Coat
        new_item.ScrewPrice=int(Price)

        db.session.add(new_item)
        db.session.commit()
        flash("已建立新螺絲編號"+str(form.Screw_number.data),category='success')

        return redirect(url_for('Database.show_data'))
    return render_template('Database/create_new.html',form=form)

@Database.route('/Update/<number>',methods=['GET', 'POST'])
def Update_datable(number):
    from user.Database.form import Update_form
    Update_Item=ScrewClass.query.filter_by(number=number).first()
    form=Update_form()
    ##defaut value
    form.Screw_number.render_kw={"value":Update_Item.number}
    form.Headtype.render_kw={"value": Update_Item.Screw_Head_Type}
    form.Head_Label.render_kw={"value": Update_Item.Screw_label}
    form.Head_Whole_Num.render_kw={"value": Update_Item.Screw_Head_wholenum}
    form.Head_Legth.render_kw={"value": Update_Item.Screw_Head_length}
    form.Head_Width.render_kw={"value": Update_Item.Screw_Head_Width}
    form.Body_Length.render_kw={"value": Update_Item.Screw_Body_Length}
    form.Body_Width.render_kw={"value": Update_Item.Screw_Body_Width}
    form.Body_Width_us.render_kw={"value": Update_Item.Screw_Body_Width_us}
    form.Coat.render_kw={"value": Update_Item.Screw_coat}
    form.Price.render_kw={"value": Update_Item.ScrewPrice}

    if request.method =='POST':
        number=form.Screw_number.data
        Headtype=form.Headtype.data
        Head_Label=form.Head_Label.data
        Head_Whole_Num=form.Head_Whole_Num.data
        Head_Legth= form.Head_Legth.data
        Head_Width=form.Head_Width.data
        Body_Length=form.Body_Length.data
        Body_Width=form.Body_Width.data
        Body_Width_us=form.Body_Width_us.data
        Coat=form.Coat.data
        Price=form.Price.data

        Update_Item.number=number
        Update_Item.Screw_Head_Type=Headtype
        Update_Item.Screw_label=Head_Label
        Update_Item.Screw_Head_wholenum=Head_Whole_Num
        Update_Item.Screw_Head_length=float(Head_Legth)
        Update_Item.Screw_Head_Width=float(Head_Width)
        Update_Item.Screw_Body_Length=float(Body_Length)
        Update_Item.Screw_Body_Width=float(Body_Width)
        Update_Item.Screw_Body_Width_us=Body_Width_us
        Update_Item.Screw_coat=Coat
        Update_Item.ScrewPrice=int(Price)

        
        db.session.commit()
        flash("已更新螺絲編號"+str(number),category='success')
        return redirect(url_for('Database.show_data'))
    ##db.session.delete(DeleteItem)
    return render_template('Database/update.html',number=number,form=form)

@Database.route('/Remove/<number>',methods=['GET', 'POST'])
def Remove_datable(number):
    DeleteItem=ScrewClass.query.filter_by(number=number).first()
    db.session.delete(DeleteItem)
    db.session.commit()
    return redirect(url_for('Database.show_data'))
