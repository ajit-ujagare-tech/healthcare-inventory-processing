Healthcare Inventory Processing Automation
Overview

This project simulates a healthcare debt collection inventory processing workflow commonly found in Application Support and Production Support environments.

The solution processes incoming inventory files, applies business validation rules, generates logs, and loads eligible accounts into Amazon RDS MySQL.

Business Scenario

Healthcare clients send account inventory files for collection activities.

Before accounts can be loaded into the collection platform, the inventory must be validated and filtered according to business rules.

Features
Inventory file processing
Duplicate removal
Compliance filtering
Missing phone identification
Logging and monitoring
MySQL database loading
AWS EC2 deployment
Amazon RDS integration
Technology Stack
Python
Linux (Ubuntu)
Shell Scripting
MySQL
AWS EC2
AWS RDS
Git & GitHub
Project Structure

healthcare_inventory_project

├── config

├── data

├── scripts

├── sql

├── src

├── requirements.txt

└── README.md

Execution

Run inventory processing:

python src/process_inventory.py

Load data into MySQL:

python src/db_load.py

Sample Business Rules
Remove duplicate accounts
Exclude BANKRUPT accounts
Exclude DISPUTE accounts
Identify missing phone numbers
Generate production-ready output
Application Support Concepts Demonstrated
Batch Processing
Log Monitoring
SQL Validation
Incident Troubleshooting
Linux Operations
Database Support
Production Support Activities
Future Enhancements
Cron Scheduling
SFTP File Retrieval
Email Alerts
Audit Tables
Health Check Scripts
Monitoring Dashboard
