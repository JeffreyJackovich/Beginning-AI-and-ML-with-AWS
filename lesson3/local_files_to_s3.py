
import boto
from boto.s3.key import Key
import os


AWS_ACCESS_KEY_ID = '<input your id>'
AWS_SECRET_ACCESS_KEY = '<input your secret key>'
END_POINT = '<input your end_point>'                          # eg. us-east-1
S3_HOST = '<input your host name>'                           # eg. s3.us-east-1.amazonaws.com
BUCKET = 'aws-ml-and-ai-input-for-topic-model'
BUCKET_DIRECTORY = 'tech_xplore_articles/'             


LOCAL_PATH = os.getcwd() +'\\text_files\\infozine__all_categories_output\\'
text_files_list = [f for f in os.listdir(LOCAL_PATH) if f.endswith('.txt')]


conn = boto.s3.connect_to_region(END_POINT,
                       aws_access_key_id=AWS_ACCESS_KEY_ID,
                       aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                       host=S3_HOST)


for file in text_files_list:
	bucket_obj = conn.get_bucket(BUCKET)
	k = Key(bucket_obj)
	k.key = BUCKET_DIRECTORY + file
	k.set_contents_from_filename(LOCAL_PATH + file)

