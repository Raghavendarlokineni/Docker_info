import requests
from prettytable import PrettyTable

def container_status(status):

    url = "http://127.0.0.1:6000/containers/json?all"

    if status == "all": 
       url += "=1"
    elif status == "running":
       pass 
    else: raise ValueError("status should be either 'all' or 'running'")
    
    return requests.get(url)

def active_containers(status):

    response = container_status(status) 
    table = PrettyTable(["Container Name", "Container ID", "Status", "IP ADDR"])
    for i in response.json():
        try:
            network_details, = i["NetworkSettings"]["Networks"].values()
            
        except ValueError:
            continue
        table.add_row([i["Names"][0].encode('utf-8').replace('/', ''),
                          i['Id'].encode('utf-8')[:12],
                          i["State"],
                          network_details["IPAddress"]])

    print(table)        
  
def containers(container_info):

    response = requests.get("http://127.0.0.1:6000/info")
    
    docker_info =  container_info(response.json()["Containers"], 
            response.json()["ContainersRunning"], 
            response.json()["ContainersPaused"], 
            response.json()["ContainersStopped"]
           )
    return docker_info

def specify_container(container_id):

    #fetch the all containers info and get the required container url
    response = container_status("all")
    url = None
    for i in response.json():
        for a in i["Names"]:
            if ((a.encode('utf-8').replace('/', '') == container_id) | 
               (i['Id'].encode('utf-8')[:12] == container_id)):
                
                list_cmd = ["http://127.0.0.1:6000/containers", container_id ,"json" ]
                url = "/".join(list_cmd)          
    response = requests.get(url)
    #print(response.json()["HostConfig"]["Privileged"])
     
def images():
    
    response = requests.get("http://127.0.0.1:6000/images/json")
    images_list = {}
    for i in response.json()[:-1]:
        pass
        #print(i)
        #images_list[i["RepoTags"][0].encode("utf-8")] = i["Id"].encode("utf-8")[7:19]

    #print(images_list)

