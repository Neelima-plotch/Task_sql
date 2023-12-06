from flask import Flask, request, jsonify
from movie import *


app = Flask(__name__)

# Assume db_config is defined or imported correctly

@app.route('/getvisitors', methods=['GET'])
def get_visitors():
    try:
        # Get movie ID from the request parameters
        movie_id = request.args.get('movie_id')

        # Validate movie_id parameter
        if movie_id is None:
            return jsonify({'error': 'Missing movie_id parameter'}), 400
        else:
            num_of_visitors = get_num_of_visitors(movie_id)

        # Return a successful response
        return jsonify({'movie_id': movie_id, 'num_visitors': num_of_visitors}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)