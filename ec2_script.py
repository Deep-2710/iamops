import boto3

session = boto3.Session(profile_name='Deep-Admin')

def check_health(region_name='us-east-1', output_file= 'output.txt'):
    try :
        ec2_client = boto3.client('ec2', region_name=region_name)
        response = ec2_client.describe_instance_status(IncludeAllInstances= True)
        with open(output_file, "w") as file:
            for instance in response['InstanceStatuses']:
                instance_id = instance['InstanceId']
                state = instance['InstanceState']['Name']
                status = instance['InstanceStatus']['Status']
                system_status = instance['SystemStatus']['Status']
            
                file.write(f"Instance ID: {instance_id}\n")
                file.write(f"  State: {state}\n")
                file.write(f"  Instance Status: {status}\n")
                file.write(f"  System Status: {system_status}\n")
                file.write("-" * 40 + "\n")

        if not response['InstanceStatuses']:
            print("No instances found in the region.")

            print(f"EC2 instance status saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace with your desired region
    check_health(region_name="us-east-1", output_file = "output.txt")

    

