from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime, timedelta

app = Flask(__name__)
db = mysql.connector.connect(host="localhost", user="root", password="", database="antrean_registrasi_medis")
cursor = db.cursor()