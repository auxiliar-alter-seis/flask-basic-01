from flask import Flask, jsonify, render_template, redirect, url_for, request, session
from app import app#, mysql


@app.route('/', methods=["GET", "POST"])
@app.route('/inicio/', methods=["GET", "POST"])
def home_page():
    return render_template('home_page.html')