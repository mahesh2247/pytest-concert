import json
import boto3
import os


def handler(event, context):
    try:
        dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
        table = dynamodb.Table(os.getenv("TABLE_NAME"))

        
        response = table.scan(
            AttributesToGet=[
                "ticket_count",
            ]
        )
    except Exception as e:
        print(response)
        print(e)
        return {
            "statusCode": 500,
            "body": json.dumps({"message": response}),
        }

    ticket_counts = response["Items"]
    total_tickets = sum(ticket["ticket_count"] for ticket in ticket_counts)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Total tickets booked: {total_tickets}."}),
    }