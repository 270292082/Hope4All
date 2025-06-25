# Hope4All
Hope4All is an open-source application designed to assist in locating missing persons by enabling quick and anonymous reporting. The system captures vital information—such as where someone was last seen—and stores it securely in a SQLite3 database to aid rescue and recovery teams.

## Features
- Anonymous Reporting: No login required, ensuring speed and accessibility in urgent situations.
- Location Tracking: Report the last known location of a missing person.
- SQLite3 Database: Efficiently stores and manages submitted data.
- Languages selection
- Google Maps Integration (In development): Visual representation of reported cases on an interactive map.
- Admin Dashboard (Coming soon): For monitoring, validating and managing submitted reports. 

## Technologies Used
- Frontend: HTML, CSS, Javascript
- Backend: Python (Flask)
- Database: SQLite3
- APIs: Google Maps API (planned)

## Getting Started to Launch Server
- Python3.X
- SQLite3

### Installation
1. Clone the repository:
```
git clone https://github.com/270292082/Hope4All.git
```
2. Install dependencies:
```
pip install flask, flask_babel, sqlite3
```
3. Run the Server:
```
python3 run.py
```
4. The app is now accessible through
```
http://localhost:5000
```