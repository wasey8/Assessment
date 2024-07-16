from app import app, db, auth
from models import BlogPost
from flask import jsonify, request, g

@app.route('/posts', methods=['POST'])
@auth.login_required
def create_post():
    data = request.get_json() or {}
    title = data.get('title')
    content = data.get('content')
    if not title or not content:
        return jsonify({'message': 'Title and content are required'}), 400
    post = BlogPost(title=title, content=content, user_id=g.user.id)
    db.session.add(post)
    db.session.commit()
    return jsonify({'message': 'Post created successfully'}), 201

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = BlogPost.query.all()
    return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'user_id': post.user_id} for post in posts])

@app.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = BlogPost.query.get_or_404(id)
    return jsonify({'id': post.id, 'title': post.title, 'content': post.content, 'user_id': post.user_id})

@app.route('/posts/<int:id>', methods=['PUT'])
@auth.login_required
def update_post(id):
    post = BlogPost.query.get_or_404(id)
    if post.user_id != g.user.id:
        return jsonify({'message': 'Unauthorized'}), 403
    data = request.get_json() or {}
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    db.session.commit()
    return jsonify({'message': 'Post updated successfully'})

@app.route('/posts/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_post(id):
    post = BlogPost.query.get_or_404(id)
    if post.user_id != g.user.id:
        return jsonify({'message': 'Unauthorized'}), 403
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted successfully'})
