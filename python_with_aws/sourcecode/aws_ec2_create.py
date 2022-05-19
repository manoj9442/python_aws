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
        instances = resource_ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]).get("Reservations")
        for instance in instances:
            if "spot_instance_request_id" in instance:
                print("instance is not on-demand")
            else:
                response = resource_ec2.get_reservation_purchase_recommendation()
    except Exception as e:
        print(e)
create_aws_ec2()
check_instance()