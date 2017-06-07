import subprocess
import pdb

def get_images():
   
    output = subprocess.Popen(["docker", "images"], stdout=subprocess.PIPE)
    return map(str.split, output.communicate()[0].split("\n"))

def no_tag(images):
    for image in images[:-1]:
        if "<none>" == image[1]:
            yield image[2] 

def delete_images(images):
    for image in images:
        output = subprocess.Popen(["docker", "rmi", "-f", image], 
                                  stdout=subprocess.PIPE)
        print(output.communicate())
   
if __name__ == "__main__":

    delete_images(no_tag(get_images()))


'''
output = subprocess.Popen(["docker", "images"], stdout=subprocess.PIPE)

result = output.communicate()[0].split("\n")
image_list = []
 
for line in result[1:]:
    
    if ("<none>" == line.split("  ")[0]):
        image_list.append(filter(None,line.split("  "))[2])

for image in image_list:
     output = subprocess.Popen(["docker", "rmi", "-f", image], stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
     print(output.communicate()[0])
'''
