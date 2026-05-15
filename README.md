# Secure Authentication System 

## Overview

This project is a backend authentication system built with FastAPI and SQLModel.
It provides user registration, login, and secure access using JWT tokens.
The system is designed to demonstrate a basic but secure authentication flow for modern web applications.

The main goal of the system is to ensure secure handling of user credentials while protecting sensitive data and preventing unauthorized access.

## Features

User registration (create account)

User login with email and password

Password hashing with bcrypt

JWT token authentication

Protected routes using OAuth2

Get current authenticated user (/me endpoint)

## Technologies Used

Python

FastAPI

SQLModel

SQLite (or other relational database)

JWT (python-jose)

Passlib (bcrypt)

## Project Structure

app/

├── models/        # Database models (SQLModel)

├── routes/        # API endpoints

├── security/      # Authentication (JWT, password hashing)

├── database/      # Database configuration

└── main.py        # Application entry point

## System Logic

Users register with email and password

Passwords are hashed before being stored in the database

Users log in and receive a JWT token

The token is used to access protected routes

The /me endpoint returns the authenticated user
