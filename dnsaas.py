import sys
import os
from os import mkdir
from pathlib import Path


def health_stats(vpc_name):
    my_dir = Path("/etc/dnsaas/"+vpc_name)
    if my_dir.is_file():
        os.system("sh health_stats.sh")
        #check the health status
    else:
        print("Error VPC-Name Entered. Please Try Again")

def status(vpc_name):
    my_dir = Path("/etc/dnsaas/"+vpc_name)
    if my_dir.is_file():
        os.system("ansible-playbook get-status.yml -i inventory")
        #check the health status
    else:
        print("Error VPC-Name Entered. Please Try Again")

def start(vpc_name):
    my_dir = Path("/etc/dnsaas/"+vpc_name)
    if not my_dir.is_file():
        os.system("ansible-playbook start.yml -i inventory")
        #check the health status
    else:
        print("Duplicate VPC-Name Entered. Please Enter a Unique one.")

def main(*arg):
    if (arg[0] == "help"):
        print("Usage: <VPC-Name> <options>")
        print("Options:")
        print("     - init  (to setup the VPC-DNS servers)")
        print("     - start (to start the server setup)")
        print("     - get-status (to get the status of the server)")
        print("     - health-stats (to get the cpu and mem stats of the servers)")
    elif ((arg[1]) == "init"):
        #vpc_name = raw_input("Enter the VPC name.")
        vpc_name = arg[0]
        mkdir("/etc/dnsaas/"+vpc_name)
        location = "/etc/dnsaas/"+vpc_name
        print("All the required templates for "+ vpc_name + " have been created and located at "+ location + ". Kindly move to the location and fill in the necessary details.")
    elif(arg == "start"):
        print("The  deployment has been started and the status of it will be updated shortly.")
        #call start function
        vpc_name = arg[0]
        start(vpc_name)
        return
    elif(arg[1] == "get-status"):
        #call status function
        print("Status is this")
    elif(arg[1] == "health-stats"):
        #call health function
        vpc_name = arg[0]
        print("This is the current health")
