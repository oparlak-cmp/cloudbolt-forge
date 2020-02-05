"""
This action removes all the zip files from CloudBolt /tmp/systemd-private* directory.
"""
from common.methods import set_progress
import glob
import os

def run(job, *args, **kwargs):
    
    zip_file_list = glob.glob("/tmp/systemd-private*/tmp/*.zip")
    set_progress("Found following zip files in /tmp: {}".format(zip_file_list))
    for file in zip_file_list:
        set_progress("Removing these files {}".format(file))
        os.remove(file)

    return "SUCCESS", "", ""
