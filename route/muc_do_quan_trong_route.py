from flask import Blueprint, render_template, redirect, url_for, request, flash
from db import execute_query

muc_do_quan_trong_bp = Blueprint('muc_do_quan_trong_bp', __name__, template_folder='../templates/admin/')

@muc_do_quan_trong_bp.route('/danh_sach_muc_do_quan_trong')
def danh_sach_muc_do_quan_trong():
    query = "SELECT * FROM muc_do_quan_trong"
    list_muc_do_quan_trong = execute_query(query, fetchall=True)
    return render_template('danh_sach_muc_do_quan_trong.html', list_muc_do_quan_trong=list_muc_do_quan_trong)

@muc_do_quan_trong_bp.route('/them_muc_do_quan_trong', methods=['GET', 'POST'])
def them_muc_do_quan_trong():
    if request.method == 'POST':
        ten_muc_do_quan_trong = request.form['ten_muc_do_quan_trong']
        query = "INSERT INTO muc_do_quan_trong (ten_muc_do_quan_trong) VALUES (%s)"
        execute_query(query, values=(ten_muc_do_quan_trong,), commit=True)
        flash('Thêm mức độ quan trọng thành công', 'success')
        return redirect(url_for('muc_do_quan_trong_bp.danh_sach_muc_do_quan_trong'))
    return render_template('them_muc_do_quan_trong.html')

@muc_do_quan_trong_bp.route('/sua_muc_do_quan_trong/<int:ma_muc_do_quan_trong>', methods=['GET', 'POST'])
def sua_muc_do_quan_trong(ma_muc_do_quan_trong):
    if request.method == 'POST':
        ten_muc_do_quan_trong = request.form['ten_muc_do_quan_trong']
        query = "UPDATE muc_do_quan_trong SET ten_muc_do_quan_trong = %s WHERE ma_muc_do_quan_trong = %s"
        execute_query(query, values=(ten_muc_do_quan_trong, ma_muc_do_quan_trong), commit=True)
        flash('Sửa mức độ quan trọng thành công', 'success')
        return redirect(url_for('muc_do_quan_trong_bp.danh_sach_muc_do_quan_trong'))
    else:
        query = "SELECT * FROM muc_do_quan_trong WHERE ma_muc_do_quan_trong = %s"
        muc_do_quan_trong_data = execute_query(query, values=(ma_muc_do_quan_trong,), fetchone=True)
        return render_template('sua_muc_do_quan_trong.html', muc_do_quan_trong_data=muc_do_quan_trong_data)

@muc_do_quan_trong_bp.route('/xoa_muc_do_quan_trong/<int:ma_muc_do_quan_trong>')
def xoa_muc_do_quan_trong(ma_muc_do_quan_trong):
    query = "DELETE FROM muc_do_quan_trong WHERE ma_muc_do_quan_trong = %s"
    execute_query(query, values=(ma_muc_do_quan_trong,), commit=True)
    flash('Xóa mức độ quan trọng thành công', 'success')
    return redirect(url_for('muc_do_quan_trong_bp.danh_sach_muc_do_quan_trong'))
