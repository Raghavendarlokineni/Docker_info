import requests
from collections import namedtuple
import sys

#user defined library
from containers_info import *

HEADER = """
         *************************************************************************************
                  IP ADDR                    {} 
                  TOTAL IMAGES               {}
                  TOTAL CONTAINERS           {}
                  RUNNING CONTAINERS         {}   
                  STOPPED CONTAINERS         {}
                  PAUSED CONTAINERS          {} 
         *************************************************************************************
         """
cont_info = namedtuple("cont_info", 
                  "Containers ContainersRunning ContainersPaused ContainersStopped")


if __name__ == "__main__":
   
    print(HEADER.format("127.0.0.1",
                        images(),
                        containers(cont_info).Containers,
                        containers(cont_info).ContainersRunning,
                        containers(cont_info).ContainersPaused,
                        containers(cont_info).ContainersStopped)

         ) 


    print(active_containers(sys.argv[1]))
    #specify_container("4acdb75b3110")
    #print(images())

