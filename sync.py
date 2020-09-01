import os
import sys
# import re

# Environment variables to configure the AWS CLI
os.environ["AWS_ACCESS_KEY_ID"] = os.environ['INPUT_ACCESS_KEY']
os.environ["AWS_SECRET_ACCESS_KEY"] = os.environ['INPUT_SECRET_ACCESS_KEY']
os.environ["AWS_DEFAULT_REGION"] = os.environ['INPUT_REGION']

# Source and destination locations
source = os.environ['INPUT_SOURCE']
destination_bucket = os.environ['INPUT_DESTINATION_BUCKET']
destination_prefix = os.environ['INPUT_DESTINATION_PREFIX']

# Flags
# Will keep adding more ...
exclude = os.environ['INPUT_EXCLUDE']
delete = os.environ['INPUT_DELETE']
quiet = os.environ['INPUT_QUIET']

args = ['aws s3 sync']

# Checks

# Check if the source directory is provided and is in the current workspace
if source:
    if source not in os.listdir(os.environ['GITHUB_WORKSPACE']):
        print(f'Source "{source}" does not exist in the workspace. Please check and try again ...')
        print("Below are the available files/directories in the current workspace:")
        print(os.listdir(os.environ['GITHUB_WORKSPACE']))
        sys.exit(1)
    else:
        args.append(source)
else:
    args.append(".")

# Check if a destination prefix was provided:
if destination_prefix:
    destination = f's3://{destination_bucket}/{destination_prefix}/'
else:
    destination = f's3://{destination_bucket}/'

args.append(destination)

# Check if 'exclude' flag is used:
if exclude:
    args.append(f'--exclude "{exclude}"')

# Check if 'delete' flag is used:
if delete.lower() == "true":
    args.append("--delete")

# Check if 'quiet' flag is used:
if quiet.lower() == "true":
    args.append("--quiet")


cmd = ' '.join(args)
print("Running the AWS Sync command with the following arguments...")
print(cmd)

try:
    os.system(cmd)
except:
    print("Error executing the sync command !!!")
    sys.exit(1)