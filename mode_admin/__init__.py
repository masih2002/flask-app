from flask import Blueprint

ad=Blueprint('admin',__name__,url_prefix='/admin/')

@ad.route('/')
def admin_index():
    return 'hello from admin index'