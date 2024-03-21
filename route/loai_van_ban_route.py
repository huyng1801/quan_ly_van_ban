from flask import Blueprint, render_template, redirect, url_for, request, flash
from db import execute_query

loai_van_ban_bp = Blueprint('loai_van_ban_bp', __name__, template_folder='../templates/admin/')

@loai_van_ban_bp.route('/danh_sach_loai_van_ban')
def danh_sach_loai_van_ban():
    query = "SELECT * FROM loai_van_ban"
    list_loai_van_ban = execute_query(query, fetchall=True)
    return render_template('danh_sach_loai_van_ban.html', list_loai_van_ban=list_loai_van_ban)

@loai_van_ban_bp.route('/them_loai_van_ban', methods=['GET', 'POST'])
def them_loai_van_ban():
    if request.method == 'POST':
        ten_loai_van_ban = request.form['ten_loai_van_ban']
        query = "INSERT INTO loai_van_ban (ten_loai_van_ban) VALUES (%s)"
        execute_query(query, values=(ten_loai_van_ban,), commit=True)
        flash('Thêm loại văn bản thành công', 'success')
        return redirect(url_for('loai_van_ban_bp.danh_sach_loai_van_ban'))
    return render_template('them_loai_van_ban.html')

@loai_van_ban_bp.route('/sua_loai_van_ban/<int:ma_loai_van_ban>', methods=['GET', 'POST'])
def sua_loai_van_ban(ma_loai_van_ban):
    if request.method == 'POST':
        ten_loai_van_ban = request.form['ten_loai_van_ban']
        query = "UPDATE loai_van_ban SET ten_loai_van_ban = %s WHERE ma_loai_van_ban = %s"
        execute_query(query, values=(ten_loai_van_ban, ma_loai_van_ban), commit=True)
        flash('Sửa loại văn bản thành công', 'success')
        return redirect(url_for('loai_van_ban_bp.danh_sach_loai_van_ban'))
    else:
        query = "SELECT * FROM loai_van_ban WHERE ma_loai_van_ban = %s"
        loai_van_ban_data = execute_query(query, values=(ma_loai_van_ban,), fetchone=True)
        return render_template('sua_loai_van_ban.html', loai_van_ban_data=loai_van_ban_data)

@loai_van_ban_bp.route('/xoa_loai_van_ban/<int:ma_loai_van_ban>')
def xoa_loai_van_ban(ma_loai_van_ban):
    query = "DELETE FROM loai_van_ban WHERE ma_loai_van_ban = %s"
    execute_query(query, values=(ma_loai_van_ban,), commit=True)
    flash('Xóa loại văn bản thành công', 'success')
    return redirect(url_for('loai_van_ban_bp.danh_sach_loai_van_ban'))
