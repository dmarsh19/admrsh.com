from smtplib import SMTP
from email.mime.text import MIMEText

from flask import render_template, request, flash, redirect, url_for, abort

from admrsh import app
from . import base_bp


@base_bp.route('/')
def home():
    return render_template('home.html', title='Home')


@base_bp.route('/email', methods=['POST'])
def email():
    if (request.form["emailAddress"] and
            request.form["emailSubject"] and
            request.form["emailMessage"]):
        msg = MIMEText('From: {0}\n\n{1}'.format(request.form["emailAddress"],
                                                 request.form["emailMessage"]))
        msg['Subject'] = request.form["emailSubject"]
        msg['From'] = app.config['SMTP_USER']
        msg['To'] = app.config['EMAIL_ADDR']
        # TLS mode required to use Yahoo SMTP
        s = SMTP(app.config['SMTP_SERVER'], app.config['SMTP_PORT'])
        s.starttls()
        s.login(app.config['SMTP_USER'], app.config['SMTP_PASSWD'])
        s.send_message(msg)
        s.quit()
    #     flash("Message Sent!")
    # return redirect(url_for('.home'))
        return "Message Sent!"
    abort(400)
