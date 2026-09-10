"""
Web application for Vortex Dump
Beautiful dashboard for analyzing messenger data
"""

from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import json
import os
from datetime import datetime
from vortex_dump import VortexDump

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Store current dump instance
current_dump = None


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/api/upload', methods=['POST'])
def upload_file():
    """Handle file upload"""
    global current_dump
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    try:
        data = json.load(file)
        current_dump = VortexDump()
        
        # Save temporarily
        temp_path = f'temp_{datetime.now().timestamp()}.json'
        with open(temp_path, 'w') as f:
            json.dump(data, f)
        
        if current_dump.load_data(temp_path):
            return jsonify({
                'success': True,
                'message': 'File uploaded successfully',
                'stats': {
                    'total_messages': len(current_dump.messages),
                    'unique_users': len(set(m.get('user_id') for m in current_dump.messages))
                }
            })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/statistics')
def get_statistics():
    """Get statistics"""
    if not current_dump:
        return jsonify({'error': 'No data loaded'}), 400
    
    chat_id = request.args.get('chat_id')
    stats = current_dump.get_statistics(chat_id)
    
    return jsonify(stats)


@app.route('/api/activity')
def get_activity():
    """Get activity analysis"""
    if not current_dump:
        return jsonify({'error': 'No data loaded'}), 400
    
    chat_id = request.args.get('chat_id')
    activity = current_dump.analyze_activity(chat_id)
    
    return jsonify(activity)


@app.route('/api/search', methods=['POST'])
def search():
    """Search messages"""
    if not current_dump:
        return jsonify({'error': 'No data loaded'}), 400
    
    data = request.json
    query = data.get('query', '')
    chat_id = data.get('chat_id')
    limit = data.get('limit', 100)
    
    results = current_dump.search(query, chat_id, limit)
    
    return jsonify({
        'count': len(results),
        'results': results[:limit]
    })


@app.route('/api/export', methods=['POST'])
def export_data():
    """Export data"""
    if not current_dump:
        return jsonify({'error': 'No data loaded'}), 400
    
    data = request.json
    chat_id = data.get('chat_id')
    format_type = data.get('format', 'json')
    
    output_file = f"export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{format_type}"
    
    if current_dump.export_messages(chat_id, format_type, output_file):
        return send_file(output_file, as_attachment=True)
    else:
        return jsonify({'error': 'Export failed'}), 400


@app.route('/api/chats')
def get_chats():
    """Get list of chats"""
    if not current_dump:
        return jsonify({'error': 'No data loaded'}), 400
    
    chats = list(set(m.get('chat_id') for m in current_dump.messages if m.get('chat_id')))
    
    return jsonify({'chats': chats})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
