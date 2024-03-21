import secrets
from flask import Flask
from route.van_ban_route import van_ban_bp
from route.can_bo_route import can_bo_bp
from route.don_vi_route import don_vi_bp
from route.do_khan_route import do_khan_bp
from route.linh_vuc_route import linh_vuc_bp
from route.loai_van_ban_route import loai_van_ban_bp
from route.muc_do_quan_trong_route import muc_do_quan_trong_bp


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Register the blueprint with the main application

app.register_blueprint(van_ban_bp, url_prefix='/van_ban')
app.register_blueprint(can_bo_bp, url_prefix='/')
app.register_blueprint(don_vi_bp, url_prefix='/don_vi')
app.register_blueprint(do_khan_bp, url_prefix='/do_khan')
app.register_blueprint(linh_vuc_bp, url_prefix='/linh_vuc')
app.register_blueprint(loai_van_ban_bp, url_prefix='/loai_van_ban')
app.register_blueprint(muc_do_quan_trong_bp, url_prefix='/muc_do_quan_trong')

if __name__ == '__main__':
    app.run(debug=True)
