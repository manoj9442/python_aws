from curses.panel import bottom_panel
import boto3

def create_aws_ec2():
    try:
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-0022f774911c1d690",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="MYUSE1KP"
        )
        
    except Exception as e:
        print(e)


def check_instance():
    try:
        resource_ec2 = boto3.client("ec2")
        instances = resource_ec2.describe_instances().get("Reservations")
        for instance in instances:
            if "spot_instance_request_id" in instance:
                print("instance is not on-demand")
            else:
                client = boto3.client('ce')
                print("Reserved instance")
                response = client.get_reservation_purchase_recommendation(
                    AccountId='153543828477',
                    Service='ec2',
                    AccountScope='PAYER' or 'LINKED',
                    LookbackPeriodInDays='SEVEN_DAYS' or 'THIRTY_DAYS' or 'SIXTY_DAYS',
                    TermInYears='ONE_YEAR' or 'THREE_YEARS',
                    PaymentOption='NO_UPFRONT' or 'PARTIAL_UPFRONT' or 'ALL_UPFRONT' or 'LIGHT_UTILIZATION' or 'MEDIUM_UTILIZATION' or 'HEAVY_UTILIZATION',
                    ServiceSpecification={
                        'EC2Specification': {
                            'OfferingClass': 'STANDARD' or 'CONVERTIBLE'
                        }
                    },
                    PageSize=123
                    
                )
    except Exception as e:
        print(e)
create_aws_ec2()
check_instance()