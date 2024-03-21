from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from db import execute_query
import hashlib
can_bo_bp = Blueprint('can_bo_bp', __name__, template_folder='../templates/admin/')

@can_bo_bp.route('/danh_sach_can_bo')
def danh_sach_can_bo():
    query = "SELECT * FROM can_bo"
    list_can_bo = execute_query(query, fetchall=True)
    return render_template('danh_sach_can_bo.html', list_can_bo=list_can_bo)

@can_bo_bp.route('/them_can_bo', methods=['GET', 'POST'])
def them_can_bo():
    if request.method == 'POST':
        ma_can_bo = request.form['ma_can_bo']
        ten_can_bo = request.form['ten_can_bo']
        mat_khau = hashlib.md5((request.form['mat_khau']).encode()).hexdigest()
        vai_tro = request.form['vai_tro']
        query = "INSERT INTO can_bo (ma_can_bo, ten_can_bo, mat_khau, vai_tro) VALUES (%s, %s, %s, %s)"
        execute_query(query, values=(ma_can_bo, ten_can_bo, mat_khau, vai_tro), commit=True)
        flash('Thêm cán bộ thành công', 'success')
        return redirect(url_for('can_bo_bp.danh_sach_can_bo'))
    return render_template('them_can_bo.html')

@can_bo_bp.route('/sua_can_bo/<ma_can_bo>', methods=['GET', 'POST'])
def sua_can_bo(ma_can_bo):
    if request.method == 'POST':
        ma_can_bo = request.form['ma_can_bo']
        ten_can_bo = request.form['ten_can_bo']
        mat_khau = hashlib.md5((request.form['mat_khau']).encode()).hexdigest()
        vai_tro = request.form['vai_tro']
        query = "UPDATE can_bo SET ten_can_bo = %s, mat_khau = %s, vai_tro = %s WHERE ma_can_bo = %s"
        execute_query(query, values=(ten_can_bo, mat_khau, vai_tro, ma_can_bo), commit=True)
        flash('Sửa cán bộ thành công', 'success')
        return redirect(url_for('can_bo_bp.danh_sach_can_bo'))
    else:
        query = "SELECT * FROM can_bo WHERE ma_can_bo = %s"
        employee_data = execute_query(query, values=(ma_can_bo,), fetchone=True)
        return render_template('sua_can_bo.html', employee_data=employee_data)

@can_bo_bp.route('/xoa_can_bo/<ma_can_bo>')
def xoa_can_bo(ma_can_bo):
    query = "DELETE FROM can_bo WHERE ma_can_bo = %s"
    execute_query(query, values=(ma_can_bo,), commit=True)
    flash('Xóa cán bộ thành công', 'success')
    return redirect(url_for('can_bo_bp.danh_sach_can_bo'))

@can_bo_bp.route('/', methods=['GET', 'POST'])
def dang_nhap():
    if request.method == 'POST':
        ma_can_bo = request.form['ma_can_bo']
        mat_khau = request.form['mat_khau']

        # Fetch the user from the database
        query = "SELECT * FROM can_bo WHERE ma_can_bo = %s"
        can_bo = execute_query(query, values=(ma_can_bo,), fetchone=True)

        if can_bo:
            # Hash the entered password using MD5
            hashed_password = hashlib.md5(mat_khau.encode()).hexdigest()

            # Check if the hashed password matches the stored hashed password
            if can_bo['mat_khau'] == hashed_password:
                flash('Đăng nhập thành công!', 'success')
                session['ma_can_bo'] = can_bo['ma_can_bo']
                if can_bo['vai_tro'] == "Nhân viên":
                    return redirect(url_for('van_ban_bp.them_van_ban'))
                else:
                    return redirect(url_for('can_bo_bp.danh_sach_can_bo'))
        
        flash('Đăng nhập thất bại. Vui lòng kiểm tra lại thông tin đăng nhập.', 'danger')

    return render_template('index.html')
@can_bo_bp.route('/dang_ky', methods=['GET', 'POST'])
def dang_ky():
    if request.method == 'POST':
        ma_can_bo = request.form['ma_can_bo']
        ten_can_bo = request.form['ten_can_bo']
        mat_khau = hashlib.md5((request.form['mat_khau']).encode()).hexdigest()
        vai_tro = "Nhân viên"

        # Check if the user already exists
        query_check_user = "SELECT * FROM can_bo WHERE ma_can_bo = %s"
        existing_user = execute_query(query_check_user, values=(ma_can_bo,), fetchone=True)

        if existing_user:
            flash('Tài khoản đã tồn tại. Vui lòng chọn tên khác.', 'danger')
        else:
            # Insert the new user into the database
            query_insert_user = "INSERT INTO can_bo (ma_can_bo, ten_can_bo, mat_khau, vai_tro) VALUES (%s, %s, %s, %s)"
            execute_query(query_insert_user, values=(ma_can_bo, ten_can_bo, mat_khau, vai_tro), commit=True)
            flash('Đăng ký thành công. Bạn có thể đăng nhập ngay!', 'success')
            return redirect(url_for('can_bo_bp.dang_nhap'))

    return render_template('dang_ky.html')

@can_bo_bp.route('/dang_xuat')
def dang_xuat():
    session.pop('ma_can_bo', None)
    flash('Đăng xuất thành công!', 'success')
    return redirect(url_for('can_bo_bp.dang_nhap'))