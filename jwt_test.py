from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity,jwt_required
from flask import Flask, request, abort, render_template,jsonify



app = Flask(__name__)
jwt = JWTManager()

# 設定 JWT 密鑰
app.config['JWT_SECRET_KEY'] = '{SET YOUR KEY}'
jwt.init_app(app)


@app.route('/login', methods=['POST'])
def login(): 
    user_id = request.json.get('user_id',none)
    # password = request.json.get('password', None) 

    if user_id != 'test': 
        return jsonify({"msg": "Bad user_id"}), 401

    access_token = create_access_token(identity=user_id)
    return jsonify(access_token=access_token)



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


