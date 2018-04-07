from flask import Blueprint, render_template, redirect, request

admin = Blueprint('admin', __name__)


@admin.route('/')
def index():
    return render_template('admin/login.html')