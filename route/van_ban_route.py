from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory, session
from flask.helpers import flash
from db import execute_query
import os
van_ban_bp = Blueprint('van_ban_bp', __name__)

UPLOAD_FOLDER = 'static\\upload'
van_ban_bp.config = {'UPLOAD_FOLDER': UPLOAD_FOLDER}

@van_ban_bp.route('/danh_sach_van_ban_la_nguoi_soan')
def danh_sach_van_ban_la_nguoi_soan():
    query = """
        SELECT
            vb.so_thu_tu_van_ban,
            vb.so_ky_hieu_van_ban,
            vb.ngay_ban_hanh,
            cb_ky.ten_can_bo AS nguoi_ky,
            dv_soan.ten_don_vi AS don_vi_soan_thao,
            dv_ban_hanh.ten_don_vi AS don_vi_ban_hanh,
            lv.ten_linh_vuc,
            vb.la_van_ban_qppl,
            vb.duong_dan_file,
            vb.so_van_ban,
            lvb.ten_loai_van_ban,
            cb_nhan.ten_can_bo AS nguoi_nhan,
            cb_soan.ten_can_bo AS nguoi_soan,
            mdqt.ten_muc_do_quan_trong,
            dk.ten_do_khan,
            vb.la_van_ban_di,
            dv_nhan.ten_don_vi AS noi_nhan,
            vb.trich_yeu
        FROM van_ban vb
        LEFT JOIN can_bo cb_ky ON vb.ma_nguoi_ky = cb_ky.ma_can_bo
        LEFT JOIN don_vi dv_soan ON vb.ma_don_vi_soan_thao = dv_soan.ma_don_vi
        LEFT JOIN don_vi dv_ban_hanh ON vb.ma_don_vi_ban_hanh = dv_ban_hanh.ma_don_vi
        LEFT JOIN linh_vuc lv ON vb.ma_linh_vuc = lv.ma_linh_vuc
        LEFT JOIN loai_van_ban lvb ON vb.ma_loai_van_ban = lvb.ma_loai_van_ban
        LEFT JOIN can_bo cb_nhan ON vb.ma_nguoi_nhan = cb_nhan.ma_can_bo
        LEFT JOIN can_bo cb_soan ON vb.ma_nguoi_soan = cb_soan.ma_can_bo
        LEFT JOIN muc_do_quan_trong mdqt ON vb.ma_muc_do_quan_trong = mdqt.ma_muc_do_quan_trong
        LEFT JOIN do_khan dk ON vb.ma_do_khan = dk.ma_do_khan
        LEFT JOIN don_vi dv_nhan ON vb.ma_noi_nhan = dv_nhan.ma_don_vi WHERE vb.ma_nguoi_soan = %s
    """
    values = (session['ma_can_bo'],)
    
    danh_sach_van_ban = execute_query(query, values, fetchall=True)
    return render_template('danh_sach_van_ban.html', danh_sach_van_ban=danh_sach_van_ban)

@van_ban_bp.route('/danh_sach_van_ban_la_nguoi_ky')
def danh_sach_van_ban_la_nguoi_ky():
    query = """
        SELECT
            vb.so_thu_tu_van_ban,
            vb.so_ky_hieu_van_ban,
            vb.ngay_ban_hanh,
            cb_ky.ten_can_bo AS nguoi_ky,
            dv_soan.ten_don_vi AS don_vi_soan_thao,
            dv_ban_hanh.ten_don_vi AS don_vi_ban_hanh,
            lv.ten_linh_vuc,
            vb.la_van_ban_qppl,
            vb.duong_dan_file,
            vb.so_van_ban,
            lvb.ten_loai_van_ban,
            cb_nhan.ten_can_bo AS nguoi_nhan,
            cb_soan.ten_can_bo AS nguoi_soan,
            mdqt.ten_muc_do_quan_trong,
            dk.ten_do_khan,
            vb.la_van_ban_di,
            dv_nhan.ten_don_vi AS noi_nhan,
            vb.trich_yeu
        FROM van_ban vb
        LEFT JOIN can_bo cb_ky ON vb.ma_nguoi_ky = cb_ky.ma_can_bo
        LEFT JOIN don_vi dv_soan ON vb.ma_don_vi_soan_thao = dv_soan.ma_don_vi
        LEFT JOIN don_vi dv_ban_hanh ON vb.ma_don_vi_ban_hanh = dv_ban_hanh.ma_don_vi
        LEFT JOIN linh_vuc lv ON vb.ma_linh_vuc = lv.ma_linh_vuc
        LEFT JOIN loai_van_ban lvb ON vb.ma_loai_van_ban = lvb.ma_loai_van_ban
        LEFT JOIN can_bo cb_nhan ON vb.ma_nguoi_nhan = cb_nhan.ma_can_bo
        LEFT JOIN can_bo cb_soan ON vb.ma_nguoi_soan = cb_soan.ma_can_bo
        LEFT JOIN muc_do_quan_trong mdqt ON vb.ma_muc_do_quan_trong = mdqt.ma_muc_do_quan_trong
        LEFT JOIN do_khan dk ON vb.ma_do_khan = dk.ma_do_khan
        LEFT JOIN don_vi dv_nhan ON vb.ma_noi_nhan = dv_nhan.ma_don_vi WHERE vb.ma_nguoi_ky = %s
    """
    values = (session['ma_can_bo'],)
    danh_sach_van_ban = execute_query(query, values, fetchall=True)
    return render_template('danh_sach_van_ban.html', danh_sach_van_ban=danh_sach_van_ban)

@van_ban_bp.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(van_ban_bp.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@van_ban_bp.route('/them_van_ban', methods=['GET', 'POST'])
def them_van_ban():
    if request.method == 'GET':
        query_nguoi_ky = "SELECT ma_can_bo, ten_can_bo FROM can_bo"
        list_nguoi_ky = execute_query(query_nguoi_ky, fetchall=True)

        query_don_vi_soan_thao = "SELECT ma_don_vi, ten_don_vi FROM don_vi"
        list_don_vi_soan_thao = execute_query(query_don_vi_soan_thao, fetchall=True)

        query_don_vi_ban_hanh = "SELECT ma_don_vi, ten_don_vi FROM don_vi"
        list_don_vi_ban_hanh = execute_query(query_don_vi_ban_hanh, fetchall=True)

        query_linh_vuc = "SELECT ma_linh_vuc, ten_linh_vuc FROM linh_vuc"
        list_linh_vuc = execute_query(query_linh_vuc, fetchall=True)

        query_loai_van_ban = "SELECT ma_loai_van_ban, ten_loai_van_ban FROM loai_van_ban"
        list_loai_van_ban = execute_query(query_loai_van_ban, fetchall=True)

        query_nguoi_nhan = "SELECT ma_can_bo, ten_can_bo FROM can_bo"
        list_nguoi_nhan = execute_query(query_nguoi_nhan, fetchall=True)

        query_nguoi_soan = "SELECT ma_can_bo, ten_can_bo FROM can_bo"
        list_nguoi_soan = execute_query(query_nguoi_soan, fetchall=True)

        query_muc_do_quan_trong = "SELECT ma_muc_do_quan_trong, ten_muc_do_quan_trong FROM muc_do_quan_trong"
        list_muc_do_quan_trong = execute_query(query_muc_do_quan_trong, fetchall=True)

        query_do_khan = "SELECT ma_do_khan, ten_do_khan FROM do_khan"
        list_do_khan = execute_query(query_do_khan, fetchall=True)

        query_noi_nhan = "SELECT ma_don_vi, ten_don_vi FROM don_vi"
        list_noi_nhan = execute_query(query_noi_nhan, fetchall=True)

        return render_template('them_van_ban.html',
                            list_nguoi_ky=list_nguoi_ky,
                            list_don_vi_soan_thao=list_don_vi_soan_thao,
                            list_don_vi_ban_hanh=list_don_vi_ban_hanh,
                            list_linh_vuc=list_linh_vuc,
                            list_loai_van_ban=list_loai_van_ban,
                            list_nguoi_nhan=list_nguoi_nhan,
                            list_nguoi_soan=list_nguoi_soan,
                            list_muc_do_quan_trong=list_muc_do_quan_trong,
                            list_do_khan=list_do_khan,
                            list_noi_nhan=list_noi_nhan)
        
    elif request.method == 'POST':
        so_ky_hieu_van_ban = request.form.get('so_ky_hieu_van_ban')
        ngay_ban_hanh = request.form.get('ngay_ban_hanh')
        ma_nguoi_ky = request.form.get('ma_nguoi_ky')
        ma_don_vi_soan_thao = request.form.get('ma_don_vi_soan_thao')
        ma_don_vi_ban_hanh = request.form.get('ma_don_vi_ban_hanh')
        ma_linh_vuc = request.form.get('ma_linh_vuc')
        la_van_ban_qppl = request.form.get('la_van_ban_qppl')
        so_van_ban = request.form.get('so_van_ban')
        ma_loai_van_ban = request.form.get('ma_loai_van_ban')
        ma_nguoi_nhan = request.form.get('ma_nguoi_nhan')
        ma_nguoi_soan = request.form.get('ma_nguoi_soan')
        ma_muc_do_quan_trong = request.form.get('ma_muc_do_quan_trong')
        ma_do_khan = request.form.get('ma_do_khan')
        la_van_ban_di = request.form.get('la_van_ban_di')
        ma_noi_nhan = request.form.get('ma_noi_nhan')
        trich_yeu = request.form.get('trich_yeu')
        file_path = ''
        if 'van_ban_file' in request.files:
            print("hello")
            file = request.files['van_ban_file']
            if file.filename != '':
                file_path = os.path.join(van_ban_bp.config['UPLOAD_FOLDER'], file.filename)
                file.save(file_path)
                if file_path:
                    flash('Tải tập tin thành công!', 'success')
                else:
                    flash('Không có tập tin được tải lên hoặc có lỗi xảy ra!', 'danger')
        query = """
            INSERT INTO van_ban 
            (so_ky_hieu_van_ban, ngay_ban_hanh, ma_nguoi_ky, ma_don_vi_soan_thao, ma_don_vi_ban_hanh, 
            ma_linh_vuc, la_van_ban_qppl, duong_dan_file, so_van_ban, ma_loai_van_ban, ma_nguoi_nhan, 
            ma_nguoi_soan, ma_muc_do_quan_trong, ma_do_khan, la_van_ban_di, ma_noi_nhan, trich_yeu) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (so_ky_hieu_van_ban, ngay_ban_hanh, ma_nguoi_ky, ma_don_vi_soan_thao, ma_don_vi_ban_hanh, 
                ma_linh_vuc, la_van_ban_qppl, file_path, so_van_ban, ma_loai_van_ban, ma_nguoi_nhan, 
                ma_nguoi_soan, ma_muc_do_quan_trong, ma_do_khan, la_van_ban_di, ma_noi_nhan, trich_yeu)
   
        execute_query(query, values, commit=True)
        

        flash('Thêm văn bản thành công!', 'success')

        return redirect(url_for('van_ban_bp.them_van_ban'))

@van_ban_bp.route('/xoa_van_ban/<int:ma_van_ban>')
def xoa_van_ban(document_id):
    query = "DELETE FROM van_ban WHERE id=%s"
    values = (document_id,)

    execute_query(query, values, commit=True)
    flash('Xóa văn bản thành công!', 'success')
    return redirect(url_for('danh_sach_van_ban'))

@van_ban_bp.route('/tim_kiem', methods=['GET', 'POST'])
def tim_kiem():
    if request.method == 'GET':
        return render_template('tim_kiem_van_ban.html', search_results=None)

    elif request.method == 'POST':
        search_query = request.form.get('search_query')

        query = """ SELECT
            vb.so_thu_tu_van_ban,
            vb.so_ky_hieu_van_ban,
            vb.ngay_ban_hanh,
            cb_ky.ten_can_bo AS nguoi_ky,
            dv_soan.ten_don_vi AS don_vi_soan_thao,
            dv_ban_hanh.ten_don_vi AS don_vi_ban_hanh,
            lv.ten_linh_vuc,
            vb.la_van_ban_qppl,
            vb.duong_dan_file,
            vb.so_van_ban,
            lvb.ten_loai_van_ban,
            cb_nhan.ten_can_bo AS nguoi_nhan,
            cb_soan.ten_can_bo AS nguoi_soan,
            mdqt.ten_muc_do_quan_trong,
            dk.ten_do_khan,
            vb.la_van_ban_di,
            dv_nhan.ten_don_vi AS noi_nhan,
            vb.trich_yeu
        FROM van_ban vb
        LEFT JOIN can_bo cb_ky ON vb.ma_nguoi_ky = cb_ky.ma_can_bo
        LEFT JOIN don_vi dv_soan ON vb.ma_don_vi_soan_thao = dv_soan.ma_don_vi
        LEFT JOIN don_vi dv_ban_hanh ON vb.ma_don_vi_ban_hanh = dv_ban_hanh.ma_don_vi
        LEFT JOIN linh_vuc lv ON vb.ma_linh_vuc = lv.ma_linh_vuc
        LEFT JOIN loai_van_ban lvb ON vb.ma_loai_van_ban = lvb.ma_loai_van_ban
        LEFT JOIN can_bo cb_nhan ON vb.ma_nguoi_nhan = cb_nhan.ma_can_bo
        LEFT JOIN can_bo cb_soan ON vb.ma_nguoi_soan = cb_soan.ma_can_bo
        LEFT JOIN muc_do_quan_trong mdqt ON vb.ma_muc_do_quan_trong = mdqt.ma_muc_do_quan_trong
        LEFT JOIN do_khan dk ON vb.ma_do_khan = dk.ma_do_khan
        LEFT JOIN don_vi dv_nhan ON vb.ma_noi_nhan = dv_nhan.ma_don_vi WHERE trich_yeu LIKE %s"""
        values = (f"%{search_query}%",)
        search_results = execute_query(query, values, fetchall=True)
        return render_template('tim_kiem_van_ban.html', search_results=search_results)

