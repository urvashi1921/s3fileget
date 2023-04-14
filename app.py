from flask import Flask
import boto3

app = Flask(__name__)

@app.route('/')
def get_file():
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket='zeeurvashi', Key='test_file.json')
    file_content = response['Body'].read().decode('utf-8')
    return file_content

