#! /usr/bin/python
# -*- coding:utf-8 -*-

import logging
import boto3
from botocore.exceptions import ClientError

def put_object(dest_bucket_name, dest_object_name, src_data):
    # Construct Body= parameter
    if isinstance(src_data, bytes):
        object_data = src_data
    elif isinstance(src_data, str):
        try:
            object_data = open(src_data, 'rb')
            # possible FileNotFoundError/IOError exception
        except Exception as e:
            logging.error(e)
            return False
    else:
        logging.error('Type of ' + str(type(src_data)) +
                      ' for the argument \'src_data\' is not supported.')
        return False

    # Put the object
    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=dest_bucket_name, Key=dest_object_name, Body=object_data)
    except ClientError as e:
        logging.error(e)
        return False
    finally:
        if isinstance(src_data, str):
            object_data.close()
    return True


def go_main():
    test_bucket_name = 'BUCKET_NAME'
    test_object_name = 'OBJECT_NAME'
    filename = 'AWS_Sensor.db'
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')
    success = put_object(test_bucket_name, test_object_name, filename)
    if success:
        logging.info(f'Added {test_object_name} to {test_bucket_name}')


if __name__ == '__main__':
    go_main()