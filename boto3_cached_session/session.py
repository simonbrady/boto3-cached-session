import boto3
import botocore
import os

def get(cache_dir=None):
    """Return a boto3 Session object using the CLI credential cache for MFA"""
    cache_dir = cache_dir or os.path.join(os.path.expanduser('~'), '.aws/cli/cache')
    cli_cache = botocore.credentials.JSONFileCache(cache_dir)
    botocore_session = botocore.session.get_session()
    botocore_session.get_component('credential_provider').get_provider('assume-role').cache = cli_cache
    return boto3.Session(botocore_session=botocore_session)

def client(service, cache_dir=None):
    """Return a boto3 client using the CLI credential cache for MFA"""
    return get(cache_dir).client(service)

def resource(service, cache_dir=None):
    """Return a boto3 resource using the CLI credential cache for MFA"""
    return get(cache_dir).resource(service)
