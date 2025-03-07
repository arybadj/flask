from flask import Flask, render_template, redirect,url_for,jsonify

app= Flask(__name__)

# static routing
@app.route("/hello")
def hello_world():
    return "hello-world"

@app.route("/")
def home():
    return "welcome to home page"
    #return render_template("index.html")

@app.route("/about")
def about():
    return "welcome to the about page"


#dynamic routing
@app.route("/user/<username>")
def user(username):
    return f"welcome user {username}"

@app.route("/post/<int:post_id>")
def post_number(post_id):
    return f"this is a post number: {post_id}"

#url rule handler
def contact():
    return f"this is a contact page"

app.add_url_rule('/contact', view_func=contact)

@app.route("/new-home")
def new_home():
    return redirect(url_for('home'))

#error handler
@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "error": "404 not found",
        "message": "The requested URL was not found on the server"      
                    }),404

@app.errorhandler(500)
def internal_server_error(e):
    return f"An internal error has occured. please try again later",500




if __name__=="__main__":
    app.run(debug=True)