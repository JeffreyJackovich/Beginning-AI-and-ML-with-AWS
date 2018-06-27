import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
text = "Machine Learning is fascinating."

print('Calling DetectDominantLanguage')
print(json.dumps(comprehend.detect_dominant_language(Text = text), sort_keys=True, indent=4))
print("End of DetectDominantLanguage\n")
