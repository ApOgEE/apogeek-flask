# apogeek.py
# Created by: M. Fauzilkamil 

from flask import Flask, render_template
apogeek = Flask(__name__, static_url_path = "/assets")

@apogeek.route('/')
def index():
    config = {
        "tajuk" : "APOGEEK Python Flask Project",
        "apogeek" : "M. Fauzilkamil"
    }

    return render_template( 'apogeekbase.html', data = config)

@apogeek.route("/admin")
def admin():
    # this is the admin area

    admdata = {
       "name" : "M. Fauzilkamil",
       "email" : "apogee@apogeek.com",
       "tajuk" : "APOGEEK Python Flask Admin Page"
    }

    return render_template('admin/adminhome.html', data = admdata)

@apogeek.route("/members")
def members():
    member = "This is member area"

    return member

@apogeek.route("/members/<string:name>/")
def getMember(name):
    return name

if __name__ == '__main__':
    fupjar.run(host='0.0.0.0')