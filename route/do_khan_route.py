from flask import Blueprint, render_template, redirect, url_for, request, flash
from db import execute_query

do_khan_bp = Blueprint('do_khan_bp', __name__, template_folder='../templates/admin/')

@do_khan_bp.route('/danh_sach_do_khan')
def danh_sach_do_khan():
    query = "SELECT * FROM do_khan"
    list_do_khan = execute_query(query, fetchall=True)
    return render_template('danh_sach_do_khan.html', list_do_khan=list_do_khan)

@do_khan_bp.route('/them_do_khan', methods=['GET', 'POST'])
def them_do_khan():
    if request.method == 'POST':
        ten_do_khan = request.form['ten_do_khan']
        query = "INSERT INTO do_khan (ten_do_khan) VALUES (%s)"
        execute_query(query, values=(ten_do_khan,), commit=True)
        flash('Thêm độ khẩn thành công', 'success')
        return redirect(url_for('do_khan_bp.danh_sach_do_khan'))
    return render_template('them_do_khan.html')

@do_khan_bp.route('/sua_do_khan/<int:ma_do_khan>', methods=['GET', 'POST'])
def sua_do_khan(ma_do_khan):
    if request.method == 'POST':
        ten_do_khan = request.form['ten_do_khan']
        query = "UPDATE do_khan SET ten_do_khan = %s WHERE ma_do_khan = %s"
        execute_query(query, values=(ten_do_khan, ma_do_khan), commit=True)
        flash('Sửa độ khẩn thành công', 'success')
        return redirect(url_for('do_khan_bp.danh_sach_do_khan'))
    else:
        query = "SELECT * FROM do_khan WHERE ma_do_khan = %s"
        do_khan_data = execute_query(query, values=(ma_do_khan,), fetchone=True)
        return render_template('sua_do_khan.html', do_khan_data=do_khan_data)

@do_khan_bp.route('/xoa_do_khan/<int:ma_do_khan>')
def xoa_do_khan(ma_do_khan):
    query = "DELETE FROM do_khan WHERE ma_do_khan = %s"
    execute_query(query, values=(ma_do_khan,), commit=True)
    flash('Xóa độ khẩn thành công', 'success')
    return redirect(url_for('do_khan_bp.danh_sach_do_khan'))
