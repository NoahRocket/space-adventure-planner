from flask import Flask, render_template, request
import random
import json

app = Flask(__name__)

# Load data from JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

# Itinerary template
template = """
<h2>Your Space Adventure Itinerary</h2>
<p><strong>Destination:</strong> {destination}</p>
<p><strong>Mission Type:</strong> {mission_type}</p>
<p><strong>Launch Vehicle:</strong> {launch_vehicle}</p>
<p><strong>Launch Year:</strong> {launch_year}</p>
<p><strong>Transit Time:</strong> {transit_time}</p>
<p><strong>Activities:</strong></p>
<ul>
    <li>{activity1}</li>
    <li>{activity2}</li>
</ul>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        destination = request.form['destination']
        mission_type = request.form['mission_type']
        
        # Get data for the selected destination
        dest_data = data[destination]
        
        # Randomly select options
        launch_vehicle = random.choice(dest_data['launch_vehicles'])
        launch_year = random.choice(["2028", "2029", "2030"])
        transit_time = random.choice(dest_data['transit_time'])
        activities = random.sample(dest_data['activities'][mission_type], 2)
        
        # Generate itinerary
        itinerary = template.format(
            destination=destination,
            mission_type=mission_type,
            launch_vehicle=launch_vehicle,
            launch_year=launch_year,
            transit_time=transit_time,
            activity1=activities[0],
            activity2=activities[1]
        )
        
        return render_template('index.html', itinerary=itinerary)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
