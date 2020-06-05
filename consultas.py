# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
from app import db, Artist, Venue, Show
from sqlalchemy import func
import datetime
from flask import Flask,request

venue = Venue.query.get(5)
db.session.delete(venue)
db.session.commit()

    