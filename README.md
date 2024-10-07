# Hospital Management Application

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/nohan-ahmed/docoria) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 🚧 Project Status: **Under Development**

This project is currently in the development phase. We are actively working on new features, bug fixes, and improvements. Some aspects may be incomplete or subject to change.

---

## 📜 Overview

The **Hospital Management Application** allows hospitals to list their services and provides patients with the ability to book appointments at their nearby hospitals. 
The system simplifies appointment management and aims to streamline hospital-patient interaction through a real-time notification system.

### Features (Planned)

- **Hospital Registration**: Hospitals can register and manage their profiles on the platform.
- **Patient Appointment Booking**: Patients can book appointments in nearby hospitals using a location-based search.
- **Real-time Notifications**: Hospitals and patients will receive real-time updates on booking status and confirmations.
- **Push Notifications**: Patients and hospitals will receive push notifications on important events such as appointment confirmation or changes.
- **User Authentication**: Secure login for both hospitals and patients.
- **Search Functionality**: Advanced search filters for finding the right hospital based on specialties, services, and location.

---

## 🛠️ Tech Stack

### Backend

- **Language**: Python
- **Framework**: Django, Django Rest Framework (DRF)
- **Real-time Communication**: Django Channels & Redis for real-time notifications
- **Push Notifications**: Firebase
- **Database**: PostgreSQL

### Frontend (To Be Decided)

At this moment, the front-end technology is yet to be finalized. We are open to collaborating with developers who are proficient in:

- **React/Next.js**: If we find a collaborator with expertise in React or Next.js, we will go with this stack.
- **Vue/Nuxt.js**: If no React developers are available, we will proceed with Vue or Nuxt.js.

Feel free to get in touch if you're interested in contributing to the frontend!

---

## 🚀 Getting Started

### Prerequisites

- **Python** (version 3.10 or higher)
- **Django** (version 5.0 or higher)
- **PostgreSQL** (version 12 or higher)
- **Redis** (version 5.x or higher)
- **Firebase** setup for push notifications

### Installation

1. Clone the repository:
    ```bash
    git clone Redis](https://github.com/nohan-ahmed/docoria.git
    ```
2. Navigate into the project directory:
    ```bash
    cd docoria
    ```
3. Set up a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Set up PostgreSQL database and apply migrations:
    ```bash
    python manage.py migrate
    ```

6. Start Redis (if not already running):
    ```bash
    redis-server
    ```

7. Start the development server:
    ```bash
    python manage.py runserver
    ```

### Frontend Setup (When Available)

Instructions for setting up the frontend will be added once the frontend framework is finalized.

---

## 🛠️ Development

Contributions are highly welcome! If you'd like to contribute to the project, especially to the frontend (React/Next.js or Vue/Nuxt.js), please feel free to reach out.

### Working on a Feature

1. Create a new branch for your feature:
    ```bash
    git checkout -b feature-branch-name
    ```
2. Make your changes.
3. Commit your changes:
    ```bash
    git commit -m "Add feature description"
    ```
4. Push the branch:
    ```bash
    git push origin feature-branch-name
    ```
5. Open a pull request.

### Running Tests

If you've implemented any tests, you can run them using:
```bash
python manage.py test
```

## 🗒️ Changelog

### v0.1.0
- Initial setup with Django, PostgreSQL, Redis, and Django Channels integration.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

For any questions, collaboration requests (especially for frontend development), or suggestions, feel free to reach out:

- **Email**: [mluv5603@gmail.com.com](mailto:mluv5603@gmail.com)
- **GitHub Issues**: [here](https://github.com/nohan-ahmed/docoria/issues)

---

*This README will be updated as the project evolves.*
