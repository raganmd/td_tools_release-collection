import wget
import json
import os

allRemotes = open("releaseFiles.json", "r")
workingDict = json.load(allRemotes)
allRemotes.close()

release_dir = "releaseVersions"

# delete old versions
def delete_old_files(del_dir):
    for each_file in os.listdir(del_dir):
        target_file = '{}\{}'.format(del_dir, each_file)
        os.remove(target_file)
        print('deleting {}'.format(target_file))

    pass

def download_files():
    for each_remote in workingDict['targets']:
        save_name = each_remote['name']
        target_url = each_remote['url'] 

        target_path = "{dir}\\{file}.tox".format(dir=release_dir, file=save_name)
        wget.download(target_url, target_path)    

        print("\ndownloading {save_url} \nsaving to {target_path} \n".format(target_path=target_path, save_url=target_url))
    pass

print("Deleting Old Files")
delete_old_files(release_dir)

print('- ' * 5)
print('\n')

print("Downloading New Files")
download_files()