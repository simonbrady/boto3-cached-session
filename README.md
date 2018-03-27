# boto3\_cached\_session

Wrapper for using the AWS CLI credential cache with boto3 so you don't have to enter
your MFA credentials every time you run a script, based on the example by
[Justin Menga](https://github.com/mixja) in [this thread](https://github.com/boto/botocore/pull/1338/).
Requires botocore 1.8.14 or later.

Example usage:

```python
import boto3_cached_session

ec2 = boto3_cached_session.client('ec2')
my_instances = ec2.describe_instances()

s3 = boto3_cached_session.resource('s3', '/path/to/nonstandard/cache')
my_bucket_resource = s3.Bucket('my-bucket')

region = boto3_cached_session.get().region_name
```
