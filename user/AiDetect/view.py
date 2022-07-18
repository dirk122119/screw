from flask import render_template,flash,request,redirect,url_for,Blueprint,Response
import cv2
import numpy as np
import os
from user.AiDetect import simple_camera
from user.AiDetect import imgwrap
from user.darknet import darknet
from user.ManualInput.model import ScrewClass,AddScrewTotable,Img
from flask_login import login_user, current_user, login_required,logout_user
from user import db
import socket


items=ScrewClass.query.all()
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

head_choice=headlabel2choice(items)
coat_choice=coat2choice(items)

AiDetect=Blueprint('AiDetect',__name__)

@AiDetect.route('/option', methods=['GET', 'POST'])
def Option_select():
    return render_template('AiDetect/AiDetect_choose.html')

@AiDetect.route('/ai_option_uk', methods=['GET', 'POST'])
def AI_DataInput_UK():
    from user.AiDetect.form import Form_AI_uk
    form=Form_AI_uk()
    table_list=[]
    items=AddScrewTotable.query.filter_by().all()

    for item in items:
        table_list.append(item)

    if form.validate_on_submit():
        flash("已接收啟動訊號",category='success')
        print("********************************")
        print("******已接收啟動訊號***********")
        print("********************************")

        Head_Label=form.Head_Label.data
        Coat=form.Coat.data
        ##========================================================##
        ##=============strings convert from form to view===============##
        ##========================================================##

        Headtype_dict={
            "cross":"十字",
            "square":"方型",
            'six':'六邊型',
            'star':'星型',
            'sp_a':'特殊型A',
        }
        
        img1=simple_camera.show_camera()
        HOST = '0.0.0.0'
        PORT = 7000

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))


        outdata ='images/1.png'
        print('send: ' + outdata)
        s.send(outdata.encode())
        indata = s.recv(1024)
        print("receive : "+indata.decode())

        if indata.decode()=="no_object":
            flash("無待辨識物",category='danger')
            return redirect(url_for('AiDetect.AI_DataInput_UK'))
        flash("執行辨識 ",category='success')
        if not ScrewClass.query.filter_by(
            Screw_Head_Type =Headtype_dict[indata.decode()],
            Screw_coat=coat_choice[int(Coat)][-1],
            Screw_label=head_choice[int(Head_Label)][-1]
            ).all():
            flash("找不到對應的螺絲",category='danger')

            return redirect(url_for('AiDetect.AI_DataInput_UK'))
        else:
            all_find_screw=ScrewClass.query.filter_by(
                Screw_Head_Type =Headtype_dict[indata.decode()],
                Screw_coat=coat_choice[int(Coat)][-1],
                Screw_label=head_choice[int(Head_Label)][-1]
            ).all()
            for find_screw in all_find_screw:
                add_item=AddScrewTotable(user_name=current_user.username,screw_number=find_screw.number)
            
                if not AddScrewTotable.query.filter_by(screw_number=find_screw.number).all():
                    db.session.add(add_item)
                    db.session.commit()
                    flash("加入編號 : "+str(find_screw.number),category='success')
                else:
                    flash("以存在"+str(find_screw.number),category='danger')
            return redirect(url_for('AiDetect.AI_DataInput_UK'))

    return render_template('AiDetect/OpenCamera_uk.html',form=form,table_list=table_list)

@AiDetect.route('/ai_option_us', methods=['GET', 'POST'])
def AI_DataInput_US():
    from user.AiDetect.form import Form_AI_us
    form=Form_AI_us()
    table_list=[]
    items=AddScrewTotable.query.filter_by().all()

    for item in items:
        table_list.append(item)

    if form.validate_on_submit():
        Head_Label=form.Head_Label.data
        Coat=form.Coat.data
        ##========================================================##
        ##=============strings convert from form to view===============##
        ##========================================================##
        Headtype_dict={
            "cross":"十字",
            "square":"方型",
            'six':'六邊型',
            'star':'星型',
            'sp_a':'特殊型A',
        }

    
        img1=simple_camera.show_camera()
        HOST = '0.0.0.0'
        PORT = 7000

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))


        outdata ='images/1.png'
        print('send: ' + outdata)
        s.send(outdata.encode())
        indata = s.recv(1024)
        print("receive : "+indata.decode())

        if indata.decode()=="no_object":
            flash("無待辨識物",category='danger')
            return redirect(url_for('AiDetect.AI_DataInput_US'))
        flash("執行辨識 ",category='success')
        if not ScrewClass.query.filter_by(
            Screw_Head_Type =Headtype_dict[indata.decode()],
            Screw_coat=coat_choice[int(Coat)][-1],
            Screw_label=head_choice[int(Head_Label)][-1]
            ).all():
            flash("找不到對應的螺絲",category='danger')
            return redirect(url_for('AiDetect.AI_DataInput_US'))
        else:
            all_find_screw=ScrewClass.query.filter_by(
                Screw_Head_Type =Headtype_dict[indata.decode()],
                Screw_coat=coat_choice[int(Coat)][-1],
            Screw_label=head_choice[int(Head_Label)][-1]
            ).all()
            for find_screw in all_find_screw:
                add_item=AddScrewTotable(user_name=current_user.username,screw_number=find_screw.number)
                if not AddScrewTotable.query.filter_by(screw_number=find_screw.number).all():
                    db.session.add(add_item)
                    db.session.commit()
                    flash("加入"+str(find_screw.number),category='success')
                else:
                    flash("以存在"+str(find_screw.number),category='danger')
            return redirect(url_for('AiDetect.AI_DataInput_US'))

    return render_template('AiDetect/OpenCamera_us.html',form=form,table_list=table_list)
    
@AiDetect.route('/test', methods=['GET', 'POST'])
def OpenCamera():

    cfg_file = 'user/darknet/cfg/yolov4-obj.cfg'
    data_file = 'user/darknet/cfg/obj.data'
    weight_file = 'user/darknet/yolov4-obj_last.weights'
    thre = 0.25
    show_coordinates = True

    img1=simple_camera.show_camera()
    flash("start")
    network, class_names, class_colors = darknet.load_network(
            cfg_file,
            data_file,
            weight_file,
            batch_size=1
    )

    width = darknet.network_width(network)
    height = darknet.network_height(network)

    
    frame_rgb = cv2.cvtColor( img1, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize( frame_rgb, (width, height))
    darknet_image = darknet.make_image(width, height, 3)
    darknet.copy_image_from_bytes(darknet_image, frame_resized.tobytes())
    detections = darknet.detect_image(network, class_names, darknet_image, thresh=thre)
    print("===========================")
    print(detections[0][0])
    print("===========================")
    darknet.print_detections(detections, show_coordinates)
    darknet.free_image(darknet_image)
    image = darknet.draw_boxes(detections, frame_resized, class_colors)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imwrite(os.path.abspath(os.getcwd())+"/images/predict.png", image, [cv2.IMWRITE_PNG_COMPRESSION, 9])
    return render_template('AiDetect/OpenCamera_uk.html',img=image)

@AiDetect.route('/ai_delete_uk/<number>',methods=['GET', 'POST'])
def Ai_DeleteItem_UK(number):
    DeleteItem=AddScrewTotable.query.filter_by(screw_number=number).first()
    ##db.session.delete(DeleteItem)
    DeleteItem.chose=True
    db.session.commit()
    return redirect(url_for('AiDetect.AI_DataInput_UK'))

@AiDetect.route('/ai_delete_us/<number>',methods=['GET', 'POST'])
def Ai_DeleteItem_US(number):
    DeleteItem=AddScrewTotable.query.filter_by(screw_number=number).first()
    ##db.session.delete(DeleteItem)
    DeleteItem.chose=True
    db.session.commit()
    return redirect(url_for('AiDetect.AI_DataInput_US'))