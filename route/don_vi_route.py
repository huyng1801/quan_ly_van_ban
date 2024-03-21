from flask import Blueprint, render_template, redirect, url_for, request, flash
from db import execute_query

don_vi_bp = Blueprint('don_vi_bp', __name__, template_folder='../templates/admin/')

@don_vi_bp.route('/danh_sach_don_vi')
def danh_sach_don_vi():
    query = "SELECT * FROM don_vi"
    list_don_vi = execute_query(query, fetchall=True)
    return render_template('danh_sach_don_vi.html', list_don_vi=list_don_vi)

@don_vi_bp.route('/them_don_vi', methods=['GET', 'POST'])
def them_don_vi():
    if request.method == 'POST':
        ten_don_vi = request.form['ten_don_vi']
        query = "INSERT INTO don_vi (ten_don_vi) VALUES (%s)"
        execute_query(query, values=(ten_don_vi,), commit=True)
        flash('Thêm đơn vị thành công', 'success')
        return redirect(url_for('don_vi_bp.danh_sach_don_vi'))
    return render_template('them_don_vi.html')

@don_vi_bp.route('/sua_don_vi/<int:ma_don_vi>', methods=['GET', 'POST'])
def sua_don_vi(ma_don_vi):
    if request.method == 'POST':
        ten_don_vi = request.form['ten_don_vi']
        query = "UPDATE don_vi SET ten_don_vi = %s WHERE ma_don_vi = %s"
        execute_query(query, values=(ten_don_vi, ma_don_vi), commit=True)
        flash('Sửa đơn vị thành công', 'success')
        return redirect(url_for('don_vi_bp.danh_sach_don_vi'))
    else:
        query = "SELECT * FROM don_vi WHERE ma_don_vi = %s"
        don_vi_data = execute_query(query, values=(ma_don_vi,), fetchone=True)
        return render_template('sua_don_vi.html', don_vi_data=don_vi_data)

@don_vi_bp.route('/xoa_don_vi/<int:ma_don_vi>')
def xoa_don_vi(ma_don_vi):
    query = "DELETE FROM don_vi WHERE ma_don_vi = %s"
    execute_query(query, values=(ma_don_vi,), commit=True)
    flash('Xóa đơn vị thành công', 'success')
    return redirect(url_for('don_vi_bp.danh_sach_don_vi'))
