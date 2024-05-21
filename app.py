from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify
import requests
import jsonify, json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicijalizacija baze i tablica

db = SQLAlchemy(app)


class Posao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_slug = db.Column(db.String(255), unique=True, nullable=False)
    job_title = db.Column(db.String(255), nullable=False)
    company_name = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    job_industry = db.Column(db.String(255), nullable=False)
    job_location = db.Column(db.String(255), nullable=False)
    job_level = db.Column(db.String(50))
    job_excerpt = db.Column(db.Text)
    pub_date = db.Column(db.Date)


class Lokacija(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(255), unique=True, nullable=False)


class Industrija(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    industry_name = db.Column(db.String(255), unique=True, nullable=False)


# --inicijalizacija baze i tablica
