from config import app, db, Flask, jsonify, ma, Marshmallow, Post, Post_schema, Posts_schema, PostSchema, redirect, render_template, request, SQLAlchemy, url_for


@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return ('index.html/post')
    return ('index.html/get')


@app.route("/post", methods=['POST'])
def create_post():
    title = request.json['title']
    body = request.json['body']
    
    new_post = Post(title,body)
    db.session.add(new_post)
    db.session.commit()

    return Post_schema.jsonify(new_post)


@app.route("/post/<id>", methods=['GET'])
def get_post_by_id(id):
    post = Post.query.get(id)
    return Post_schema.jsonify(post)


@app.route("/post/<id>", methods=['PUT'])
def update_post(id):
    post = Post.query.get(id)

    title = request.json['title']
    body = request.json['body']

    post.title = title
    post.body = body

    db.session.commit()
    return Post_schema.jsonify(post)



@app.route("/post", methods=['GET'])
def fget_all_posts():
    all_posts = Post.query.all()
    res = Posts_schema.dump(all_posts)
    return jsonify(res)


if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PRODs
    app.run(port=5000,debug=True)