# 🏗 Management System – Modular CLI Backend Architecture

A modular Command-Line Interface (CLI) based Management System designed using layered backend architecture principles in Python.

This project demonstrates structured application design through clear separation of concerns and scalable module organization.

---

## Overview

The system simulates role-based access between Admin, Manager, and Employee users.

It is structured to reflect backend architectural patterns used in real-world applications, focusing on maintainability and modular design.

---

## Core Engineering Principles

- Separation of Concerns
- Layered Architecture
- Repository Pattern
- Service Layer Abstraction
- Input Validation Isolation
- Secure Password Hashing
- Database Connection Encapsulation
- Clean Entry Point (`main.py`)

Each component is isolated to maintain clarity, scalability, and testability.

---

## Project Structure

ManagementSystem/
│
├── cli/ # CLI interaction layer
│ ├── init.py
│ ├── admin_menu.py
│ ├── employee_menu.py
│ └── main_menu.py
│
├── services/ # Business logic layer
│ ├── init.py
│ └── auth.py
│
├── repositories/ # Data access layer
│ └── employee_repo.py
│
├── db_pool/ # Database connection management
│ ├── init.py
│ └── connection.py
│
├── validation/ # Input validation layer
│ ├── email_validator.py
│ └── pass_validator.py
│
├── utils/ # Utility functions
│ ├── init.py
│ └── pass_hash.py
│
├── main.py # Application entry point
├── requirements.txt # Dependencies (if applicable)
└── .gitignore

---

## Architectural Flow

User (CLI)
↓
CLI Layer
↓
Service Layer
↓
Repository Layer
↓
Database Layer

Each layer maintains a single responsibility and communicates through defined interfaces.

---

## Security Considerations

- Password hashing implemented
- Input validation enforced before database interaction
- Database operations abstracted from business logic

---

## Tech Stack

- Python 3
- SQLite
- Object-Oriented Programming
- Layered Backend Design
- Git

---

## How to Run

1.Clone the repository:

git clone https://github.com/kai-praneel/ManagementSystem.git

2.Navigate into the project:

cd ManagementSystem

3.Run the application:

python main.py


---

## Planned Improvements

- REST API version using FastAPI
- Docker containerization
- Logging integration
- Unit testing (pytest)
- Deployment configuration

---

## Author

Katta Praneel  
Computer Science (AI & ML)  
Focused on backend systems, machine learning engineering, and scalable application design.




