from flask import Blueprint, render_template, request, redirect, jsonify
from flask_login import login_required
from services.itinerary_service import ItineraryService
from services.location_service import LocationService
from models import Itinerary, db

itineraries_bp = Blueprint('itineraries', __name__)

@itineraries_bp.route('/')
@login_required
def home():
    itineraries = ItineraryService.get_all_itineraries()
    return render_template('index.html', itineraries=itineraries)

@itineraries_bp.route('/reports')
@login_required
def reports():
    total_itineraries = Itinerary.query.count()
    total_participants = db.session.query(db.func.sum(Itinerary.participants)).scalar() or 0
    
    # Destination Analytics
    popular_dest = db.session.query(Itinerary.location, db.func.count(Itinerary.location))\
        .group_by(Itinerary.location)\
        .order_by(db.func.count(Itinerary.location).desc())\
        .first()
    most_popular_destination = popular_dest[0] if popular_dest else "None"
    
    unique_destinations = db.session.query(Itinerary.location)\
        .distinct()\
        .count()
    
    # Advanced Metrics
    avg_duration = db.session.query(db.func.avg(Itinerary.duration)).scalar() or 0
    total_days_planned = db.session.query(db.func.sum(Itinerary.duration)).scalar() or 0
    
    from datetime import datetime
    current_month = datetime.utcnow().month
    current_year = datetime.utcnow().year
    trips_this_month = Itinerary.query.filter(
        db.extract('month', Itinerary.created_date) == current_month,
        db.extract('year', Itinerary.created_date) == current_year
    ).count()
    
    return render_template('reports.html', 
        total_itineraries=total_itineraries,
        total_participants=total_participants,
        most_popular_destination=most_popular_destination,
        unique_destinations=unique_destinations,
        avg_duration=round(avg_duration, 1),
        total_days_planned=total_days_planned,
        trips_this_month=trips_this_month
    )

@itineraries_bp.route('/create_itinerary')
@login_required
def create_itinerary_page():
    # Get all available locations from the database
    locations = list(LocationService.LOCATION_DATABASE.keys())
    locations.sort()  # Sort alphabetically
    return render_template('create_itinerary.html', locations=locations)

@itineraries_bp.route('/generate_itinerary', methods=['POST'])
@login_required
def generate_itinerary():
    try:
        participants = int(request.form.get('participants', 0))
        itinerary = ItineraryService.create_itinerary(
            title=request.form.get('itinerary_title'),
            location=request.form.get('itinerary_location'),
            duration=int(request.form.get('itinerary_days', 3))
        )
        # Update participants
        itinerary.participants = participants
        from models import db
        db.session.commit()
        return redirect('/itinerary/{}'.format(itinerary.id))
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@itineraries_bp.route('/itinerary/<int:itinerary_id>')
@login_required
def view_itinerary(itinerary_id):
    itinerary = ItineraryService.get_itinerary_by_id(itinerary_id)
    if not itinerary:
        return redirect('/')
    days = itinerary.duration
    cost_estimate = ItineraryService.estimate_cost(
        itinerary.location,
        itinerary.duration,
        itinerary.participants
    )
    return render_template('itinerary.html', itinerary=itinerary, days=days, cost_estimate=cost_estimate)

@itineraries_bp.route('/update_itinerary/<int:itinerary_id>', methods=['POST'])
@login_required
def update_itinerary(itinerary_id):
    day_updates = {}
    for key, value in request.form.items():
        if key.startswith('day_'):
            parts = key.split('_')
            if len(parts) >= 2:
                day_num = int(parts[1])
                field = '_'.join(parts[2:])
                day_key = "day_{}".format(day_num)
                if day_key not in day_updates:
                    day_updates[day_key] = {}
                day_updates[day_key][field] = value

    if ItineraryService.update_itinerary_days(itinerary_id, day_updates):
        return redirect('/itinerary/{}'.format(itinerary_id))
    return jsonify({'error': 'Itinerary not found'}), 404

@itineraries_bp.route('/edit_itinerary/<int:itinerary_id>')
@login_required
def edit_itinerary_page(itinerary_id):
    itinerary = ItineraryService.get_itinerary_by_id(itinerary_id)
    if not itinerary:
        return redirect('/')
    # Get all available locations from the database
    locations = list(LocationService.LOCATION_DATABASE.keys())
    locations.sort()  # Sort alphabetically
    return render_template('edit_itinerary.html', itinerary=itinerary, locations=locations)

@itineraries_bp.route('/update_basic_itinerary/<int:itinerary_id>', methods=['POST'])
@login_required
def update_basic_itinerary(itinerary_id):
    try:
        title = request.form.get('title')
        location = request.form.get('location')
        duration = int(request.form.get('duration', 3))
        participants = int(request.form.get('participants', 0))
        
        if ItineraryService.update_basic_itinerary(itinerary_id, title, location, duration, participants):
            return redirect('/itinerary/{}'.format(itinerary_id))
        return jsonify({'error': 'Itinerary not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@itineraries_bp.route('/delete_itinerary/<int:itinerary_id>', methods=['POST'])
@login_required
def delete_itinerary(itinerary_id):
    if ItineraryService.delete_itinerary(itinerary_id):
        return redirect('/')
    return jsonify({'error': 'Itinerary not found'}), 404

# API endpoints for itineraries
@itineraries_bp.route('/api/itineraries', methods=['GET'])
@login_required
def get_itineraries_api():
    itineraries = ItineraryService.get_all_itineraries()
    return jsonify([itinerary.to_dict() for itinerary in itineraries])

@itineraries_bp.route('/api/itineraries', methods=['POST'])
@login_required
def create_itinerary_api():
    data = request.get_json()
    try:
        itinerary = ItineraryService.create_itinerary(
            title=data['title'],
            location=data['location'],
            duration=data['duration']
        )
        return jsonify(itinerary.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@itineraries_bp.route('/api/itineraries/<int:itinerary_id>', methods=['GET'])
@login_required
def get_itinerary_api(itinerary_id):
    itinerary = ItineraryService.get_itinerary_by_id(itinerary_id)
    if itinerary:
        return jsonify(itinerary.to_dict())
    return jsonify({'error': 'Itinerary not found'}), 404

@itineraries_bp.route('/api/itineraries/<int:itinerary_id>', methods=['PUT'])
@login_required
def update_itinerary_api(itinerary_id):
    data = request.get_json()
    itinerary = ItineraryService.update_itinerary_days(itinerary_id, data)
    if itinerary:
        return jsonify(itinerary.to_dict())
    return jsonify({'error': 'Itinerary not found'}), 404

@itineraries_bp.route('/api/itineraries/<int:itinerary_id>', methods=['DELETE'])
@login_required
def delete_itinerary_api(itinerary_id):
    if ItineraryService.delete_itinerary(itinerary_id):
        return jsonify({'message': 'Itinerary deleted successfully'})
    return jsonify({'error': 'Itinerary not found'}), 404