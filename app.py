from flask import Flask, jsonify
import boto3

app = Flask(__name__)

@app.route('/get_file')
def get_file():
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket='zeeurvashi', Key='test_file.json')
    file_content = response['Body'].read().decode('utf-8')
    return file_content
# print(response)
if __name__ == '__main__':
    app.run()