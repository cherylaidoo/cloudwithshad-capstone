# AWS Serverless Feedback Analytics System

## Project Overview

This project is a serverless feedback analytics application built on AWS. Users can submit feedback through a web form, and the system automatically analyzes sentiment using Amazon Comprehend and stores results in DynamoDB. An analytics dashboard provides real-time insights into submitted feedback.

## Features

* Feedback submission form
* Sentiment analysis (Positive, Neutral, Negative)
* Entity extraction using Amazon Comprehend
* Real-time analytics dashboard
* DynamoDB data storage
* Serverless AWS architecture

## Technologies Used

* Amazon S3
* Amazon API Gateway
* AWS Lambda
* Amazon DynamoDB
* Amazon Comprehend
* Chart.js
* GitHub

## Repository Files

### Frontend

* index.html – User feedback form
* dashboard.html – Analytics dashboard

### Backend

* lambda-feedback.py – Processes feedback and performs sentiment analysis
* lambda-stats.py – Aggregates analytics data for the dashboard

## Live Application

### Feedback Form

http://cloudwithshad-capstone-form-cheryl-aidoo.s3-website-us-east-1.amazonaws.com

### Dashboard

http://cloudwithshad-capstone-form-cheryl-aidoo.s3-website-us-east-1.amazonaws.com/dashboard.html

## Architecture

User → Amazon S3 → API Gateway → AWS Lambda → Amazon Comprehend → DynamoDB → Stats Lambda → Dashboard

## Testing

The system was tested using positive, neutral, and negative feedback samples. All submissions were successfully analyzed, stored, and displayed on the dashboard.

## Author

Cheryl Aidoo
