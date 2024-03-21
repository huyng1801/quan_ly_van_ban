from flask import Blueprint, render_template, redirect, url_for, request, flash
from db import execute_query

linh_vuc_bp = Blueprint('linh_vuc_bp', __name__, template_folder='../templates/admin/')

@linh_vuc_bp.route('/danh_sach_linh_vuc')
def danh_sach_linh_vuc():
    query = "SELECT * FROM linh_vuc"
    list_linh_vuc = execute_query(query, fetchall=True)
    return render_template('danh_sach_linh_vuc.html', list_linh_vuc=list_linh_vuc)

@linh_vuc_bp.route('/them_linh_vuc', methods=['GET', 'POST'])
def them_linh_vuc():
    if request.method == 'POST':
        ten_linh_vuc = request.form['ten_linh_vuc']
        query = "INSERT INTO linh_vuc (ten_linh_vuc) VALUES (%s)"
        execute_query(query, values=(ten_linh_vuc,), commit=True)
        flash('Thêm lĩnh vực thành công', 'success')
        return redirect(url_for('linh_vuc_bp.danh_sach_linh_vuc'))
    return render_template('them_linh_vuc.html')

@linh_vuc_bp.route('/sua_linh_vuc/<int:ma_linh_vuc>', methods=['GET', 'POST'])
def sua_linh_vuc(ma_linh_vuc):
    if request.method == 'POST':
        ten_linh_vuc = request.form['ten_linh_vuc']
        query = "UPDATE linh_vuc SET ten_linh_vuc = %s WHERE ma_linh_vuc = %s"
        execute_query(query, values=(ten_linh_vuc, ma_linh_vuc), commit=True)
        flash('Sửa lĩnh vực thành công', 'success')
        return redirect(url_for('linh_vuc_bp.danh_sach_linh_vuc'))
    else:
        query = "SELECT * FROM linh_vuc WHERE ma_linh_vuc = %s"
        linh_vuc_data = execute_query(query, values=(ma_linh_vuc,), fetchone=True)
        return render_template('sua_linh_vuc.html', linh_vuc_data=linh_vuc_data)

@linh_vuc_bp.route('/xoa_linh_vuc/<int:ma_linh_vuc>')
def xoa_linh_vuc(ma_linh_vuc):
    query = "DELETE FROM linh_vuc WHERE ma_linh_vuc = %s"
    execute_query(query, values=(ma_linh_vuc,), commit=True)
    flash('Xóa lĩnh vực thành công', 'success')
    return redirect(url_for('linh_vuc_bp.danh_sach_linh_vuc'))
from flask import Blueprint, render_template, redirect, url_for, request, flash
from db import execute_query

linh_vuc_bp = Blueprint('linh_vuc_bp', __name__, template_folder='../templates/admin/linh_vuc/')

@linh_vuc_bp.route('/danh_sach_linh_vuc')
def danh_sach_linh_vuc():
    query = "SELECT * FROM linh_vuc"
    list_linh_vuc = execute_query(query, fetchall=True)
    return render_template('danh_sach_linh_vuc.html', list_linh_vuc=list_linh_vuc)

@linh_vuc_bp.route('/them_linh_vuc', methods=['GET', 'POST'])
def them_linh_vuc():
    if request.method == 'POST':
        ten_linh_vuc = request.form['ten_linh_vuc']
        query = "INSERT INTO linh_vuc (ten_linh_vuc) VALUES (%s)"
        execute_query(query, values=(ten_linh_vuc,), commit=True)
        flash('Thêm lĩnh vực thành công', 'success')
        return redirect(url_for('linh_vuc_bp.danh_sach_linh_vuc'))
    return render_template('them_linh_vuc.html')

@linh_vuc_bp.route('/sua_linh_vuc/<int:ma_linh_vuc>', methods=['GET', 'POST'])
def sua_linh_vuc(ma_linh_vuc):
    if request.method == 'POST':
        ten_linh_vuc = request.form['ten_linh_vuc']
        query = "UPDATE linh_vuc SET ten_linh_vuc = %s WHERE ma_linh_vuc = %s"
        execute_query(query, values=(ten_linh_vuc, ma_linh_vuc), commit=True)
        flash('Sửa lĩnh vực thành công', 'success')
        return redirect(url_for('linh_vuc_bp.danh_sach_linh_vuc'))
    else:
        query = "SELECT * FROM linh_vuc WHERE ma_linh_vuc = %s"
        linh_vuc_data = execute_query(query, values=(ma_linh_vuc,), fetchone=True)
        return render_template('sua_linh_vuc.html', linh_vuc_data=linh_vuc_data)

@linh_vuc_bp.route('/xoa_linh_vuc/<int:ma_linh_vuc>')
def xoa_linh_vuc(ma_linh_vuc):
    query = "DELETE FROM linh_vuc WHERE ma_linh_vuc = %s"
    execute_query(query, values=(ma_linh_vuc,), commit=True)
    flash('Xóa lĩnh vực thành công', 'success')
    return redirect(url_for('linh_vuc_bp.danh_sach_linh_vuc'))
