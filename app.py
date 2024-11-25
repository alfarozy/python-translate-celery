from flask import Flask, request, jsonify
from tasks import translate_text

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    """
    Endpoint untuk menerjemahkan teks menggunakan Celery.
    """
    data = request.json

    # Validasi input
    if not all(key in data for key in ('text', 'src_lang', 'dest_lang')):
        return jsonify({'error': 'Missing required fields'}), 400

    # Kirim tugas ke Celery
    task = translate_text.delay(data['text'], data['src_lang'], data['dest_lang'])

    return jsonify({
        'task_id': task.id,
        'status': 'Processing'
    }), 202

@app.route('/status/<task_id>', methods=['GET'])
def get_status(task_id):
    task = translate_text.AsyncResult(task_id)

    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'status': 'Task is still in the queue'
        }
    elif task.state == 'SUCCESS':
        response = {
            'state': task.state,
            'result': task.result if task.result else 'No result available'
        }
    else:
        response = {
            'state': task.state,
            'status': str(task.info) if task.info else 'No additional info available'
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
