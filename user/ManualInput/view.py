from flask import render_template,flash,request,redirect,url_for,Blueprint,Response
from flask_login import login_user, current_user, login_required,logout_user
from user.ManualInput.model import ScrewClass,AddScrewTotable,Img
from werkzeug.utils import secure_filename
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



ManualInput=Blueprint('ManualInput',__name__)
@ManualInput.route('/option', methods=['GET', 'POST'])
def Option_select():
    return render_template('ManualInput/ManualInput_choose.html')

@ManualInput.route('/option_uk', methods=['GET', 'POST'])
def DataInput_UK():
    from user.ManualInput.form import FormManualInput_uk
    form=FormManualInput_uk()
    table_list=[]
    items=AddScrewTotable.query.filter_by().all()

    all_screw_items=ScrewClass.query.all()
    headtype_choice=headtype2choice(all_screw_items) 
    wholenum_choice=wholenum2choice(all_screw_items)
    usbody_choice=usbody2choice(all_screw_items)
    headlabel_choice=headlabel2choice(all_screw_items)
    coat_choice=coat2choice(all_screw_items)



    for item in items:
        table_list.append(item)

    if form.validate_on_submit():
        Body_Length=form.Body_Length.data
        Body_Width=form.Body_Width.data
        Head_Width=form.Head_Width.data
        Head_Legth=form.Head_Legth.data
        Head_Whole_Num=form.Head_Whole_Num.data
        Headtype=form.Headtype.data
        Head_Label=form.Head_Label.data
        Coat=form.Coat.data

        Headtype_dict={
            "十字":"十字",
            "square":"方型",
            'six':'六邊型',
            'star':'星型',
            'sp_a':'特殊型A',
        }


        if not ScrewClass.query.filter_by(
                Screw_Head_Type =headtype_choice[int(Headtype)][-1],
                Screw_Head_wholenum = wholenum_choice[int(Head_Whole_Num)][-1],
                Screw_Head_length = Head_Legth,
                Screw_Head_Width = Head_Width,
                Screw_Body_Length=Body_Length,
                Screw_Body_Width=Body_Width,
                Screw_coat=coat_choice[int(Coat)][-1],
                Screw_label=headlabel_choice[int(Head_Label)][-1]
            ).all():
            flash("找不到對應的螺絲",category='danger')
            return redirect(url_for('ManualInput.DataInput_UK'))
        else:
            all_find_screws=ScrewClass.query.filter_by(
                Screw_Head_Type =headtype_choice[int(Headtype)][-1],
                Screw_Head_wholenum = wholenum_choice[int(Head_Whole_Num)][-1],
                Screw_Head_length = Head_Legth,
                Screw_Head_Width = Head_Width,
                Screw_Body_Length=Body_Length,
                Screw_Body_Width=Body_Width,
                Screw_coat=coat_choice[int(Coat)][-1],
                Screw_label=headlabel_choice[int(Head_Label)][-1]
            ).all()
            for find_screw in all_find_screws:
                add_item=AddScrewTotable(user_name=current_user.username,screw_number=find_screw.number)
                if not AddScrewTotable.query.filter_by(screw_number=find_screw.number).all():
                    db.session.add(add_item)
                    db.session.commit()
                    flash("加入"+str(find_screw.number),category='success')
                else:
                    flash("以存在"+str(find_screw.number),category='danger')
                return redirect(url_for('ManualInput.DataInput_UK'))

    return render_template('ManualInput/ManualInput_uk.html',form=form,table_list=table_list)

@ManualInput.route('/option_us', methods=['GET', 'POST'])
def DataInput_US():
    from user.ManualInput.form import FormManualInput_us
    form=FormManualInput_us()
    table_list=[]
    items=AddScrewTotable.query.filter_by().all()
    all_screw_items=ScrewClass.query.all()
    headtype_choice=headtype2choice(all_screw_items) 
    wholenum_choice=wholenum2choice(all_screw_items)
    usbody_choice=usbody2choice(all_screw_items)
    headlabel_choice=headlabel2choice(all_screw_items)
    coat_choice=coat2choice(all_screw_items)

    for item in items:
        table_list.append(item)

    if form.validate_on_submit():
        Body_Length=form.Body_Length.data
        Body_Width=form.Body_Width_us.data
        Head_Width=form.Head_Width.data
        Head_Legth=form.Head_Legth.data
        Head_Whole_Num=form.Head_Whole_Num.data
        Headtype=form.Headtype.data
        Head_Label=form.Head_Label.data
        Coat=form.Coat.data

        Headtype_dict={
            "cross":"十字",
            "square":"方型",
            'six':'六邊型',
            'star':'星型',
            'sp_a':'特殊型A',
        }


        if not ScrewClass.query.filter_by(
            Screw_Head_Type =headtype_choice[int(Headtype)][-1],
            Screw_Head_wholenum = wholenum_choice[int(Head_Whole_Num)][-1],
            Screw_Head_length = Head_Legth,
            Screw_Head_Width = Head_Width,
            Screw_Body_Length=Body_Length,
            Screw_Body_Width_us=usbody_choice[int(Body_Width)][-1],
            Screw_coat=coat_choice[int(Coat)][-1],
            Screw_label=headlabel_choice[int(Head_Label)][-1]
            ).all():
            
            flash("找不到對應的螺絲",category='danger')
            return redirect(url_for('ManualInput.DataInput_US'))
        else:
            all_find_screws=ScrewClass.query.filter_by(
                Screw_Head_Type =headtype_choice[int(Headtype)][-1],
                Screw_Head_wholenum = wholenum_choice[int(Head_Whole_Num)][-1],
                Screw_Head_length = Head_Legth,
                Screw_Head_Width = Head_Width,
                Screw_Body_Length=Body_Length,
                Screw_Body_Width_us=usbody_choice[int(Body_Width)][-1],
                Screw_coat=coat_choice[int(Coat)][-1],
                Screw_label=headlabel_choice[int(Head_Label)][-1]
            ).all()
            for find_screw in all_find_screws:
                add_item=AddScrewTotable(user_name=current_user.username,screw_number=find_screw.number)
                if  not AddScrewTotable.query.filter_by(screw_number=find_screw.number).all():
                    db.session.add(add_item)
                    db.session.commit()
                    flash("加入"+str(find_screw.number),category='success')
                else:
                    flash("以存在"+str(find_screw.number),category='danger')
                return redirect(url_for('ManualInput.DataInput_US'))

    return render_template('ManualInput/ManualInput_us.html',form=form,table_list=table_list)

@ManualInput.route('/manual_delete_uk/<number>',methods=['GET', 'POST'])
def Manual_DeleteItem_UK(number):
    DeleteItem=AddScrewTotable.query.filter_by(screw_number=number).first()
    ##db.session.delete(DeleteItem)
    DeleteItem.chose=True
    db.session.commit()
    return redirect(url_for('ManualInput.DataInput_UK'))

@ManualInput.route('/manual_delete_us/<number>',methods=['GET', 'POST'])
def Manual_DeleteItem_US(number):
    DeleteItem=AddScrewTotable.query.filter_by(screw_number=number).first()
    ##db.session.delete(DeleteItem)
    DeleteItem.chose=True
    db.session.commit()
    return redirect(url_for('ManualInput.DataInput_US'))

@ManualInput.route('/upload',methods=['GET', 'POST'])
def UploadImg():
    if request.method =='POST':
        pic = request.files['pic']
        if not pic:
            return 'No pic uploaded!', 400

        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype
        if not filename or not mimetype:
            return 'Bad upload!', 400

        img = Img(img=pic.read(), name=filename, mimetype=mimetype)
        db.session.add(img)
        db.session.commit()
    return render_template('ManualInput/UploadImg.html')


@ManualInput.route('check/<int:id>')
def get_img(id):
    img = Img.query.filter_by(id=id).first()
    if not img:
        return 'Img Not Found!', 404

    return Response(img.img, mimetype=img.mimetype)


@ManualInput.route('cam1check/<int:id>')
def get_info(id):
    from user.darknet import darknet
    import cv2,os
    from os import listdir
    from os.path import isfile, isdir, join

    screw = ScrewClass.query.filter_by(id=id).first()
    root='/home/ai_admin/yolov4_v2'
    cfg_file = root+'/yolov4-obj.cfg'
    data_file = root+'/obj.data'
    weight_file = root+'/backup/yolov4-obj_last.weights'
    thre = 0.25
    show_coordinates = True
    
    network, class_names, class_colors = darknet.load_network(
                cfg_file,
                data_file,
                weight_file,
                batch_size=1
        )

    width = darknet.network_width(network)
    height = darknet.network_height(network)

    

    filelist= [file for file in os.listdir('test') if file.endswith('.png')]
    for f in filelist:
        id=f[:-4].split("_")[1]
        screw = ScrewClass.query.filter_by(id=id).first()
        img=cv2.imread('test/'+f)
        print("*************************")
        print(id)
        print("*************************")
        frame_rgb = cv2.cvtColor( img, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize( frame_rgb, (width, height))
        darknet_image = darknet.make_image(width, height, 3)
        darknet.copy_image_from_bytes(darknet_image, frame_resized.tobytes())
        detections = darknet.detect_image(network, class_names, darknet_image, thresh=thre)
        darknet.print_detections(detections, show_coordinates)
        darknet.free_image(darknet_image)
        image = darknet.draw_boxes_for_cam1(detections, frame_resized, class_colors,screw.Screw_Head_Width)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.imwrite("output/"+f, image, [cv2.IMWRITE_PNG_COMPRESSION, 9])

    return Response("{}\\n [{:.2f}]".format(screw.Screw_Body_Length,screw.Screw_Body_Width))

@ManualInput.route('cam2check/<int:id>')
def get_cam2_info(id):
    from user.darknet import darknet
    import cv2,os
    from os import listdir
    from os.path import isfile, isdir, join

    screw = ScrewClass.query.filter_by(id=id).first()
    root='/home/ai_admin/yolov4_cam2'
    cfg_file = root+'/yolov4-obj.cfg'
    data_file = root+'/obj.data'
    weight_file = root+'/backup/yolov4-obj_best.weights'
    thre = 0.9
    show_coordinates = True
    
    network, class_names, class_colors = darknet.load_network(
                cfg_file,
                data_file,
                weight_file,
                batch_size=1
        )

    width = darknet.network_width(network)
    height = darknet.network_height(network)

    

    filelist= [file for file in os.listdir('cam2') if file.endswith('.png')]
    for f in filelist:
        id=f[:-4].split("_")[1]
        screw = ScrewClass.query.filter_by(id=id).first()
        img=cv2.imread('cam2/'+f)
        print("*************************")
        print(id)
        print("*************************")
        frame_rgb = cv2.cvtColor( img, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize( frame_rgb, (width, height))
        darknet_image = darknet.make_image(width, height, 3)
        darknet.copy_image_from_bytes(darknet_image, frame_resized.tobytes())
        detections = darknet.detect_image(network, class_names, darknet_image, thresh=thre)
        darknet.print_detections(detections, show_coordinates)
        darknet.free_image(darknet_image)
        image = darknet.draw_boxes_for_cam2(detections, frame_resized, class_colors,screw.Screw_Head_length,screw.Screw_Body_Length,screw.Screw_Body_Width)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.imwrite("cam2_output/"+f, image, [cv2.IMWRITE_PNG_COMPRESSION, 9])

    return Response("{}\\n [{:.2f}]".format(screw.Screw_Body_Length,screw.Screw_Body_Width))

@ManualInput.route('sql2csv')
def sql2csv():
    import pandas as pd
    Screw_Head_Width=[]
    Screw_Head_length=[]
    Screw_Body_Length=[]
    Screw_Body_Width=[]

    for i in range(1,21):
        screw = ScrewClass.query.filter_by(id=i).first()
        Screw_Head_Width.append(screw.Screw_Head_Width)
        Screw_Head_length.append(screw.Screw_Head_length)
        Screw_Body_Length.append(screw.Screw_Body_Length)
        Screw_Body_Width.append(screw.Screw_Body_Width)
    dataframe = pd.DataFrame({'Screw_Head_Width':Screw_Head_Width,'Screw_Head_length':Screw_Head_length,'Screw_Body_Length':Screw_Body_Length,'Screw_Body_Width':Screw_Body_Width})
    dataframe.to_csv("sql2csv.csv",index=False)
    return Response("done")      