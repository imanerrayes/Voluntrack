# VolunTrack

*Track Your Time, Make a Difference*

VolunTrack is a smart volunteer hours tracking app that ensures accountability and task management with GPS integration, helping non-profits manage volunteers efficiently.

## Features

- GPS Clock In/Out: Volunteers log their hours by clocking in and out at assigned locations.
- Task Management: Admins can assign tasks to volunteers, and volunteers can update task statuses.
- Geofencing: Ensure volunteers are within assigned areas when clocking in.
- Volunteer Profiles: Track volunteer contributions over time and generate reports.
- Admin Dashboard: For organizations to manage volunteers, tasks, and view time logs.

## Tech Stack

- Frontend: React (web), React Native (mobile)
- Backend: Flask
- Database: PostgreSQL
- GPS Tracking: Geopy, Google Maps API

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- SQLAlchemy
- PostgreSQL

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/voluntrack.git
   ```

2. Install the required packages:
   ```
   cd voluntrack
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```
   python manage.py db init
   python manage.py db migrate
   python manage.py db upgrade
   ```

4. Start the development server:
   ```
   python app.py
   ```

The backend server will be running at `http://localhost:5000`.

## Contributing

We welcome contributions from the open-source community! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

Please ensure that your code follows the project's coding style and includes appropriate tests.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions, please feel free to reach out me. 
Happy tracking!
