# FitZone — Gym Management System

## 📌 Project Overview

FitZone is a Gym Management System developed using Python and Tkinter. It provides a graphical user interface for managing gym members, trainers, memberships, payments, and attendance records.

The system is designed to simplify daily gym operations through an easy-to-use dashboard and organized management pages.

## ✨ Features

- **Dashboard:** View gym statistics, including total members, trainers, active memberships, and total revenue.
- **Member Management:** Add, update, delete, search, and view members.
- **Trainer Management:** Add trainers with their contact information and specialties.
- **Membership Management:** Create memberships, set prices and durations, and track expiration dates.
- **Payment Management:** Record payments, payment methods, and payment dates.
- **Attendance Management:** Record member check-ins with the current date and time.
- **Trainer Assignment:** Assign trainers to gym members.
- **Membership Status:** Identify active, upcoming, and expired memberships.
- **Modern GUI:** User-friendly interface with a dashboard, tables, and styled navigation tabs.

## 🛠️ Technologies Used

- **Python** — Main programming language.
- **Tkinter** — Graphical user interface.
- **ttk** — Styled interface components and tables.
- **datetime** — Date and time management.
- **Git and GitHub** — Version control and project hosting.

## 📂 Project Structure

```text
Gym-Management-System/
│
├── gym_management.py
├── README.md
└── .gitignore
```

The Python filename may differ depending on how the project is organized.

## ⚙️ Requirements

- Python 3.10 or later recommended.
- Tkinter, usually included with standard Python installations.
- Git, if you want to clone or contribute to the repository.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Navigate to the project folder

```bash
cd Gym-Management-System
```

### 3. Run the application

If the main file is named `gym_management.py`, run:

```bash
python gym_management.py
```

On Windows, you can also use:

```bash
py gym_management.py
```

If you are using Jupyter Notebook, run the cell containing the application code.

## 📖 How to Use

1. Launch the application.
2. Open the **Dashboard** to view the gym's current statistics.
3. Use **Members** to register members and assign trainers.
4. Use **Trainers** to add trainer information.
5. Use **Memberships** to create plans and set their prices and durations.
6. Use **Payments** to record payments made by members.
7. Use **Attendance** to record member check-ins.

## 📋 Business Rules

- Member names are required.
- Assigned trainers must exist in the system.
- Memberships must belong to existing members.
- Membership prices cannot be negative.
- Membership duration must be greater than zero.
- Payment amounts must be greater than zero.
- Attendance can only be recorded for existing members.
- Membership status is determined by its start and end dates.

## ⚠️ Current Limitations

- Data is stored in memory and is lost when the application closes.
- The application does not currently use a database.
- User authentication and role-based access control are not implemented.
- Membership creation and payment recording are separate operations.

## 🔮 Future Improvements

- Integrate an SQLite database for permanent storage.
- Add login and user authentication.
- Add membership renewal functionality.
- Generate payment receipts and reports.
- Add trainer editing and deletion.
- Add data export to CSV or Excel.
- Improve dashboard analytics and reporting.

## 👥 Contributors

Abdelrahman helaly
Ekramy rabie
## 📄 License

This project is intended for educational purposes. Add a license if you plan to distribute or reuse the project publicly.
