import google.cloud.compute_v1 as compute_v1

class gcp_instance_manager():
    project_id=None
    zone=None
    instances_client=None
    def __init__(self, project_id: str, zone: str):
        self.project_id = project_id
        self.zone=zone
        self.instances_client=compute_v1.InstancesClient()

    # instance status check
    def check_instances_status(self, instance_list: list) -> list:
        instance_status_list=[]
        for instance in instance_list:
            try:
                instance_status=self.instances_client.get(project=self.project_id, zone=self.zone, instance=instance)
                instance_status_list.append(instance_status)
            except:
                instance_status_list.append({instance:"Not Exist"})

        return instance_status_list
