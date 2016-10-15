#!/usr/bin/python
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    # Entry point for Lambda Execution
    print format(event)


if __name__ == '__main__':
    # Entry point for local testing
    pass
