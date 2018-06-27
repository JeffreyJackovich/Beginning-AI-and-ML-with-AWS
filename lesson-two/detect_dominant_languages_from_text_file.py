import boto3
import json
import sys 
import os

		 
file_name = "<insert text filename>.txt"

total_bytes_processed = 0
per_file_processed = 0
total_file_size = os.path.getsize(file_name)

dominant_language_unique = set()

with open(file_name, "r", encoding="utf-8") as f:
	while True:
		# Max Bytes size supported by AWS Comprehend
    	# https://docs.aws.amazon.com/comprehend/latest/dg/API_BatchDetectDominantLanguage.html
		bytes_per_chunk = 4990
		chunk = f.read(bytes_per_chunk)
		if not chunk:
			print("All file chunks processed! \n")
			break
		
		plain_text = ''
		plain_text = chunk

		comprehend = boto3.client(service_name='comprehend', region_name='<insert region>')
		
		dominant_language_response = comprehend.detect_dominant_language(Text = plain_text) 
		dominant_language = sorted(dominant_language_response['Languages'], key=lambda k: k['LanguageCode'])[0]['LanguageCode']
		dominant_language_unique.add(dominant_language) 

		total_bytes_processed += bytes_per_chunk
		per_file_processed = (total_bytes_processed / total_file_size) * 100
		
		if len(dominant_language_unique) == 1:
			print("%s dominant language code is, %s after processing %d percent of the file.\n"  % (file_name, dominant_language_unique, per_file_processed))
		else:
			print("%s dominant language codes are, %s after processing %d percent of the file.\n"  % (file_name, dominant_language_unique, per_file_processed))


	  
