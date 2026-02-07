from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# 1. SQL Database Setup (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel_blog.db'
db = SQLAlchemy(app)

# Blog Post Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    recommendation = db.Column(db.String(200)) # e.g. "Visit this cafe!"
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    location = db.Column(db.String(100)) # India locations

# Itinerary Model
class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    activities = db.Column(db.Text, nullable=False) # JSON format of day-wise activities

# Itinerary Day Model
class ItineraryDay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itinerary.id'), nullable=False)
    day_number = db.Column(db.Integer, nullable=False)
    morning = db.Column(db.String(200))
    afternoon = db.Column(db.String(200))
    evening = db.Column(db.String(200))
    notes = db.Column(db.Text)
    itinerary = db.relationship('Itinerary', backref=db.backref('days', cascade='all, delete-orphan'))

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    posts = Post.query.order_by(Post.date.desc()).all()
    itineraries = Itinerary.query.order_by(Itinerary.created_date.desc()).all()
    # Replace with your actual Google Maps API Key
    MAP_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
    # Stripe or PayPal link
    PAYMENT_LINK = "https://buy.stripe.com/your_link" 
    
    return render_template('index.html', posts=posts, itineraries=itineraries, map_key=MAP_API_KEY, pay_link=PAYMENT_LINK)

@app.route('/add', methods=['POST'])
def add_post():
    from datetime import datetime
    start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date() if request.form.get('start_date') else None
    end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d').date() if request.form.get('end_date') else None
    
    new_post = Post(
        title=request.form['title'],
        content=request.form['content'],
        recommendation=request.form['recommendation'],
        start_date=start_date,
        end_date=end_date,
        location=request.form.get('location')
    )
    db.session.add(new_post)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
    return redirect('/')

# Default itinerary suggestions for different day counts
ITINERARY_SUGGESTIONS = {
    1: {
        1: {"morning": "City center exploration", "afternoon": "Local markets & shopping", "evening": "Sunset viewpoint"}
    },
    2: {
        1: {"morning": "Arrival & local orientation", "afternoon": "Main attractions tour", "evening": "Local cuisine dinner"},
        2: {"morning": "Nature trek or museum visit", "afternoon": "Leisure & relaxation", "evening": "Departure"}
    },
    3: {
        1: {"morning": "Arrival & check-in", "afternoon": "Historical monuments", "evening": "Local market experience"},
        2: {"morning": "Adventure activity (trekking/water sports)", "afternoon": "Local villages exploration", "evening": "Bonfire/cultural show"},
        3: {"morning": "Scenic viewpoint sunrise", "afternoon": "Shopping & souvenirs", "evening": "Departure"}
    },
    4: {
        1: {"morning": "Arrival & local orientation", "afternoon": "Main attractions", "evening": "Welcome dinner"},
        2: {"morning": "Historical sites tour", "afternoon": "Adventure activity", "evening": "Sunset at viewpoint"},
        3: {"morning": "Nature walk in national park", "afternoon": "Local village homestay", "evening": "Folk performance"},
        4: {"morning": "Shopping & local markets", "afternoon": "Last-minute sightseeing", "evening": "Departure"}
    },
    5: {
        1: {"morning": "Arrival & rest", "afternoon": "City orientation tour", "evening": "Local cuisine tasting"},
        2: {"morning": "Historical monuments tour", "afternoon": "Museum & art galleries", "evening": "Sunset viewpoint"},
        3: {"morning": "Trekking or outdoor adventure", "afternoon": "Picnic at scenic location", "evening": "Bonfire night"},
        4: {"morning": "Village exploration", "afternoon": "Water sports or beach activity", "evening": "Cultural show"},
        5: {"morning": "Last attractions visit", "afternoon": "Souvenir shopping", "evening": "Departure"}
    },
    7: {
        1: {"morning": "Arrival & hotel check-in", "afternoon": "City exploration", "evening": "Welcome dinner"},
        2: {"morning": "Historical sites tour part 1", "afternoon": "Museum & galleries", "evening": "Local market walk"},
        3: {"morning": "Trekking adventure", "afternoon": "Picnic lunch at nature spot", "evening": "Bonfire & stargazing"},
        4: {"morning": "Village stay & rural experience", "afternoon": "Traditional craft workshop", "evening": "Folk dance show"},
        5: {"morning": "Water sports activity", "afternoon": "Beach or lake relaxation", "evening": "Sunset dinner"},
        6: {"morning": "Hidden gems exploration", "afternoon": "Photography tour", "evening": "Spa & wellness"},
        7: {"morning": "Breakfast with a view", "afternoon": "Shopping & final sightseeing", "evening": "Departure"}
    }
}

@app.route('/generate_itinerary', methods=['POST'])
def generate_itinerary():
    title = request.form.get('itinerary_title')
    location = request.form.get('itinerary_location')
    days = int(request.form.get('itinerary_days', 3))
    
    # Create itinerary
    new_itinerary = Itinerary(title=title, location=location, duration=days, activities="")
    db.session.add(new_itinerary)
    db.session.flush()  # Get the ID without committing
    
    # Get suggestions for the number of days
    suggestions = ITINERARY_SUGGESTIONS.get(days, ITINERARY_SUGGESTIONS[3])
    
    # Create itinerary days
    for day_num in range(1, days + 1):
        day_suggestion = suggestions.get(day_num, {"morning": "Explore & enjoy", "afternoon": "Local activities", "evening": "Relax"})
        itinerary_day = ItineraryDay(
            itinerary_id=new_itinerary.id,
            day_number=day_num,
            morning=day_suggestion.get("morning", "Explore"),
            afternoon=day_suggestion.get("afternoon", "Sightsee"),
            evening=day_suggestion.get("evening", "Relax"),
            notes=""
        )
        db.session.add(itinerary_day)
    
    db.session.commit()
    return redirect('/')

@app.route('/itinerary/<int:itinerary_id>')
def view_itinerary(itinerary_id):
    itinerary = Itinerary.query.get(itinerary_id)
    if not itinerary:
        return redirect('/')
    days = itinerary.duration
    return render_template('itinerary.html', itinerary=itinerary, days=days)

@app.route('/update_itinerary/<int:itinerary_id>', methods=['POST'])
def update_itinerary(itinerary_id):
    itinerary = Itinerary.query.get(itinerary_id)
    if itinerary:
        for day in itinerary.days:
            morning_key = f"day_{day.day_number}_morning"
            afternoon_key = f"day_{day.day_number}_afternoon"
            evening_key = f"day_{day.day_number}_evening"
            notes_key = f"day_{day.day_number}_notes"
            
            if morning_key in request.form:
                day.morning = request.form[morning_key]
            if afternoon_key in request.form:
                day.afternoon = request.form[afternoon_key]
            if evening_key in request.form:
                day.evening = request.form[evening_key]
            if notes_key in request.form:
                day.notes = request.form[notes_key]
        
        db.session.commit()
    return redirect(f'/itinerary/{itinerary_id}')

@app.route('/delete_itinerary/<int:itinerary_id>', methods=['POST'])
def delete_itinerary(itinerary_id):
    itinerary = Itinerary.query.get(itinerary_id)
    if itinerary:
        db.session.delete(itinerary)
        db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
