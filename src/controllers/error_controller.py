from flask import Blueprint, request, jsonify
from src.utils.db_utils import db
from src.models.error_model import ErrorLog
from src.services.categorization_service import categorize_error
from src.services.alert_service import send_alert

error_bp = Blueprint('error_bp', __name__)

@error_bp.route('/', methods=['POST'])
def log_error():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid JSON payload'}), 400
    message = data.get('message')
    metadata = data.get('metadata', {})

    if not message:
        return jsonify({'error': 'Error message is required'}), 400

    category = categorize_error(message, metadata)

    error_log = ErrorLog(message=message, category=category, metadata=metadata)
    db.session.add(error_log)
    db.session.commit()

    send_alert(error_log)

    return jsonify({'id': error_log.id, 'category': category}), 201

@error_bp.route('/', methods=['GET'])
def get_errors():
    errors = ErrorLog.query.order_by(ErrorLog.timestamp.desc()).all()
    result = []
    for error in errors:
        result.append({
            'id': error.id,
            'message': error.message,
            'category': error.category,
            'timestamp': error.timestamp.isoformat(),
            'metadata': error.metadata
        })
    return jsonify(result)

@error_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = db.session.query(ErrorLog.category).distinct().all()
    categories_list = [c[0] for c in categories]
    return jsonify(categories_list)
