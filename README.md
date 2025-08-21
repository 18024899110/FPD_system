Facial Recognition Access Control System
System Overview
The system consists of two main subsystems: Access Control System and User Management System.
Access Control System
The access control system is divided into two components: main gate and unit door systems.

Main Gate System: Detects whether visitors are residents of the community
Unit Door System: Verifies if visitors belong to the specific unit

Functionality:

Performs facial recognition to match visitor information against the database
Grants access and records entry time upon successful match
For failed matches, prompts visitors to input unit number and uploads visit requests to the user management system
Sends email notifications to residents via email API for approval
Grants access only after resident confirmation

User Management System
Users can log in using either username/password or facial recognition.
User Roles:
Community Administrator:

View, modify, and delete all user information
Access comprehensive entry/exit records and statistics for all residents
Manage facial recognition data for all users
View and delete user facial recognition enrollment data

Residents:

Enroll facial recognition data
Process visitor access requests
Monitor entry/exit records for underage family members

Technical Features

Real-time facial recognition with OpenCV
PostgreSQL database integration
Role-based access control
Email notification system
Comprehensive logging and statistics

The updated resume now better reflects the complexity and functionality of your facial recognition system project.RetryClaude can make mistakes. Please double-check responses.
