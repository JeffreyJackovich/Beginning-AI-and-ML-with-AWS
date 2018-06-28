import boto3

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    
    if event:
        print("Event: ", event)
        file_obj = event["Records"][0]
        filename = str(file_obj['s3']['object']['key'])
        print("Filename: ", filename)
        file_obj = s3.get_object(Bucket = "aws-ml-and-ai-s3-trigger", Key=filename)
        file_content = file_obj["Body"].read().decode('utf-8')
        print(file_content)
        
    return 'Hello from Lambda'