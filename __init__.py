from sqlite3.dbapi2 import connect
import pandas as pd
from flask import Flask, jsonify
import sqlite3
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from category_encoders import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, render_template, redirect, request, url_for
import numpy as np
import random
import joblib
from sklearn.metrics import recall_score, precision_score, f1_score

app = Flask(__name__)

@app.route('/')
def index():
        conn = sqlite3.connect('project3.db')
        import psycopg2

        
        cur = conn.cursor()
        cur.execute("""SELECT * FROM coronaa_csv cc""")
    
        model = joblib.load('C:/Users/alswn/project/coronaa.pkl')

        return str(model)

if __name__ == '__main__':
        app.run(debug=True)

    
