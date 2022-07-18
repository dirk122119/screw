from flask import render_template,flash,request,redirect,url_for,Blueprint,Response
from user.ManualInput.model import ScrewClass,AddScrewTotable,Img
from user import db
QuotationSheet=Blueprint('QuotationSheet',__name__)

@QuotationSheet.route('/get_sheet', methods=['GET', 'POST'])
def get_sheet():
    AddScrewTotable.query.filter_by(chose=False).delete()
    db.session.commit()
    table_list=[]
    total_price=0
    items=AddScrewTotable.query.filter_by(chose=True).all()
    for item in items:
        total_price=total_price+item.screwclass.ScrewPrice
        table_list.append(item)
        print(item)
    return render_template('QuotationSheet/QuotationSheet.html',table_list=table_list,total_price=total_price)

@QuotationSheet.route('/remove_item', methods=['GET', 'POST'])
def remove_item():
    db.session.query(AddScrewTotable).delete()
    db.session.commit()
    print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrremove")
    return "remove"