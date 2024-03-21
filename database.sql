CREATE TABLE can_bo (
    ma_can_bo VARCHAR(20) PRIMARY KEY,
    ten_can_bo VARCHAR(100) NOT NULL,
    mat_khau VARCHAR(128) NOT NULL,
    vai_tro VARCHAR(20) NOT NULL CHECK (vai_tro IN ('Admin', 'Nhân viên'))
);
CREATE TABLE don_vi (
    ma_don_vi INT AUTO_INCREMENT PRIMARY KEY,
    ten_don_vi VARCHAR(100) NOT NULL UNIQUE
);
CREATE TABLE linh_vuc (
    ma_linh_vuc INT AUTO_INCREMENT PRIMARY KEY,
    ten_linh_vuc VARCHAR(100) NOT NULL UNIQUE
);
CREATE TABLE loai_van_ban (
    ma_loai_van_ban INT AUTO_INCREMENT PRIMARY KEY,
    ten_loai_van_ban VARCHAR(50) NOT NULL UNIQUE
);
CREATE TABLE muc_do_quan_trong (
    ma_muc_do_quan_trong INT AUTO_INCREMENT PRIMARY KEY,
    ten_muc_do_quan_trong VARCHAR(50) NOT NULL UNIQUE
);
CREATE TABLE do_khan (
    ma_do_khan INT AUTO_INCREMENT PRIMARY KEY,
    ten_do_khan VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE van_ban (
    so_thu_tu_van_ban INT AUTO_INCREMENT PRIMARY KEY,
    so_ky_hieu_van_ban VARCHAR(20) NOT NULL,
    ngay_ban_hanh DATE NOT NULL,
    ma_nguoi_ky VARCHAR(20),
    ma_don_vi_soan_thao INT,
    ma_don_vi_ban_hanh INT,
    ma_linh_vuc INT,
    la_van_ban_qppl BOOLEAN,
    duong_dan_file VARCHAR(200) NOT NULL,
    so_van_ban VARCHAR(50) NOT NULL,
    ma_loai_van_ban INT,
    ma_nguoi_nhan VARCHAR(20),
    ma_nguoi_soan VARCHAR(20),
    ma_muc_do_quan_trong INT,
    ma_do_khan INT,
    la_van_ban_di BOOLEAN,
    ma_noi_nhan INT,
    trich_yeu VARCHAR(200),
    FOREIGN KEY (ma_nguoi_ky) REFERENCES can_bo(ma_can_bo) ON DELETE NO ACTION,
    FOREIGN KEY (ma_don_vi_soan_thao) REFERENCES don_vi(ma_don_vi) ON DELETE NO ACTION,
    FOREIGN KEY (ma_don_vi_ban_hanh) REFERENCES don_vi(ma_don_vi) ON DELETE NO ACTION,
    FOREIGN KEY (ma_linh_vuc) REFERENCES linh_vuc(ma_linh_vuc) ON DELETE NO ACTION,
    FOREIGN KEY (ma_loai_van_ban) REFERENCES loai_van_ban(ma_loai_van_ban) ON DELETE NO ACTION,
    FOREIGN KEY (ma_nguoi_nhan) REFERENCES can_bo(ma_can_bo) ON DELETE NO ACTION,
    FOREIGN KEY (ma_nguoi_soan) REFERENCES can_bo(ma_can_bo) ON DELETE NO ACTION,
    FOREIGN KEY (ma_muc_do_quan_trong) REFERENCES muc_do_quan_trong(ma_muc_do_quan_trong) ON DELETE NO ACTION,
    FOREIGN KEY (ma_do_khan) REFERENCES do_khan(ma_do_khan) ON DELETE NO ACTION,
    FOREIGN KEY (ma_noi_nhan) REFERENCES don_vi(ma_don_vi) ON DELETE NO ACTION
);

-- Chèn dữ liệu vào bảng 'can_bo'
INSERT INTO can_bo (ma_can_bo, ten_can_bo, mat_khau, vai_tro) VALUES 
('CB0001', 'Nguyễn Văn A', md5('123'), 'Nhân viên'),
('CB0002', 'Trần Thị B', md5('123'), 'Nhân viên'),
('CB0003', 'Lê Văn C', md5('123'), 'Nhân viên'),
('CB0004', 'Phạm Thị D', md5('123'), 'Nhân viên'),
('CB0005', 'Hoàng Văn E', md5('123'), 'Nhân viên'),
('CB0006', 'Nguyễn Thị F', md5('123'), 'Nhân viên'),
('CB0007', 'Trần Văn G', md5('123'), 'Nhân viên'),
('CB0008', 'Lê Thị H', md5('123'), 'Nhân viên'),
('CB0009', 'Phan Văn I', md5('123'), 'Nhân viên'),
('CB0010', 'Vũ Thị K', md5('123'), 'Admin');

-- Chèn dữ liệu vào bảng 'don_vi'
INSERT INTO don_vi (ten_don_vi) VALUES ('Phòng ban A');
INSERT INTO don_vi (ten_don_vi) VALUES ('Phòng ban B');
-- Chèn dữ liệu vào bảng 'linh_vuc'
INSERT INTO linh_vuc (ten_linh_vuc) VALUES ('Công nghệ thông tin');
INSERT INTO linh_vuc (ten_linh_vuc) VALUES ('Kinh tế');
-- Chèn dữ liệu vào bảng 'loai_van_ban'
INSERT INTO loai_van_ban (ten_loai_van_ban) VALUES ('Đơn');
INSERT INTO loai_van_ban (ten_loai_van_ban) VALUES ('Biên bản');
INSERT INTO loai_van_ban (ten_loai_van_ban) VALUES ('Công văn');
INSERT INTO loai_van_ban (ten_loai_van_ban) VALUES ('Giấy đề nghị');

-- Chèn dữ liệu vào bảng 'muc_do_quan_trong'
INSERT INTO muc_do_quan_trong (ten_muc_do_quan_trong) VALUES ('Cao');
INSERT INTO muc_do_quan_trong (ten_muc_do_quan_trong) VALUES ('Thấp');

-- Chèn dữ liệu vào bảng 'do_khan'
INSERT INTO do_khan (ten_do_khan) VALUES ('Khẩn cấp');
INSERT INTO do_khan (ten_do_khan) VALUES ('Bình thường');

-- Chèn dữ liệu vào bảng 'van_ban'
INSERT INTO van_ban (
    so_ky_hieu_van_ban, 
    ngay_ban_hanh, 
    ma_nguoi_ky, 
    ma_don_vi_soan_thao, 
    ma_don_vi_ban_hanh, 
    ma_linh_vuc, 
    la_van_ban_qppl, 
    duong_dan_file, 
    so_van_ban, 
    ma_loai_van_ban, 
    ma_nguoi_nhan, 
    ma_nguoi_soan, 
    ma_muc_do_quan_trong, 
    ma_do_khan, 
    la_van_ban_di, 
    ma_noi_nhan, 
    trich_yeu
) VALUES (
    'ABC123', 
    '2024-01-12', 
    'CB0002', 
    1, 
    2, 
    1, 
    1, 
    '/duong/dan/to/file', 
    'VB001', 
    1, 
    'CB0003', 
    'CB0004', 
    1, 
    1, 
    0, 
    2, 
    'Văn bản quan trọng'
);
