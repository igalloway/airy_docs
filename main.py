'''
Requires mkdocs-macros-plugin:
pip3 install mkdocs-macros-plugin

listfiles() function used in:
print_b3rb.md

Generates in those files a 3D viewable tree structure of model files.

Set env.variables['branch'] to the branch with your updated file structures pushed, ex: "jinja-ninja".
Set env.variables['org'] to your github organization name, ex: "rudislabs".
Set env.variables['render_size_limit'] to max size in kB of stl file for 3D viewing, if above set size include a png image in file structure for viewer to use.

Currently using details in local .git to generate branch and org names.
'''

import os

class cl:
    GRN = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

# Begining of optional block and can be commented out if setting env.variables manually
try:
    from git import Repo                    
except ImportError:
    print('\n\n{:s}{:s}ERROR\t -  Unable to import Python module "git", check to see if GitPython is installed.{:s}\n\n'.format(cl.FAIL,cl.BOLD,cl.END))
    currentGitBranch = 'main'
    currentGitOrg = 'iRobotEducation'
    print('\n{:s}WARN\t -  Using github organization in main.py:{:s} {:s}'.format(cl.WARN,cl.END,currentGitOrg))
    print('{:s}WARN\t -  Using git branch in main.py:{:s} {:s}\n'.format(cl.WARN,cl.END,currentGitBranch))
else:
    repo = Repo(os.getcwd())
    assert not repo.bare
    currentGitOrg = repo.remotes.origin.url.split('.git')[0].replace('git@github.com:','').replace('https://github.com/','').split('/')[-2]
    currentGitBranch = repo.active_branch.name
    print('INFO\t -  {:s}Using github organization in main.py:{:s} {:s}'.format(cl.GRN,cl.END,currentGitOrg))
    print('INFO\t -  {:s}Using git branch in main.py:{:s} {:s}'.format(cl.GRN,cl.END,currentGitBranch))
# End of optional block

flagImageMesh = False
flagImageMeshCleanup = False

try:
    from stl.mesh import Mesh                   
except ImportError:
    print('\n\n{:s}{:s}WARN\t -  Unable to import Python module "stl", check to see if numpy-stl is installed, disregard if not building STL images.{:s}\n\n'.format(cl.WARN,cl.BOLD,cl.END))
else:
    try:
        import vtkplotlib as vpl                   
    except ImportError:
        flag_gen_image = False
        print('\n\n{:s}{:s}WARN\t -  Unable to import Python module "vtkplotlib", check to see if vtkplotlib is installed, disregard if not building STL images.{:s}\n\n'.format(cl.WARN,cl.BOLD,cl.END))
    else:
        flagImageMesh = True
        try:
            from PIL import Image
        except ImportError:
            print('\n\n{:s}{:s}WARN\t -  Unable to import Python module "PIL", check to see if PIL is installed, disregard if not building STL images.{:s}\n\n'.format(cl.WARN,cl.BOLD,cl.END))
        else:
            flagImageMeshCleanup = True



def define_env(env):
    env.variables['branch'] = currentGitBranch
    env.variables['org'] = currentGitOrg
    env.variables['render_size_limit'] = "5000"

    @env.macro
    def listfiles(path):
        fileDetails={}
        for root, dirs, files in os.walk(path, topdown=False):
            dirs.sort()
            for file in files:
                if ".stl" in file:
                    has_step = False
                    stepFileSize = 0
                    stepFileSize_str = ""
                    dirDepth=[]
                    root_str=os.path.join(root,file)
                    fileSize=float(os.path.getsize(os.path.join(root,file)))/1000.0
                    fileSize_str=f"{int(fileSize):d} kB"
                    if fileSize > 500:
                        # Switch to using MB if above 500 kB
                        fileSize_str=f"{fileSize/1000.0:.2f} MB"
                    while path != os.path.dirname(root_str):
                        # Replace underscores in file folders with spaces, this creates the ToC tree.
                        dirDepth.append(os.path.basename(os.path.dirname(root_str)).replace('_',' '))
                        root_str=os.path.dirname(root_str)
                    for step_file in files:
                        if file.replace(".stl", ".step") in step_file:
                            has_step = True
                            stepFileSize=float(os.path.getsize(os.path.join(root,step_file)))/1000.0
                            stepFileSize_str=f"{int(stepFileSize):d} kB"
                            if stepFileSize > 500:
                                # Switch to using MB if above 500 kB
                                stepFileSize_str=f"{stepFileSize/1000.0:.2f} MB"
                        
                    entry={"name": file,
                        "path": root.replace('docs/',''),
                        "size_str": fileSize_str,
                        "size_raw_kb": str(fileSize),
                        "has_step": has_step,
                        "step_size_str": stepFileSize_str,
                        "step_size_raw_kb": str(stepFileSize),
                        "extension": "stl"}
                    
                    if len(dirDepth) == 1:
                        if dirDepth[0] not in fileDetails:
                            fileDetails.update({dirDepth[0]:{}})
                        fileDetails[dirDepth[0]].update(entry)
                    if len(dirDepth) == 2:
                        if dirDepth[1] not in fileDetails:
                            fileDetails.update({dirDepth[1]:{dirDepth[0]:{}}})
                        if dirDepth[0] not in fileDetails[dirDepth[1]]:
                            fileDetails[dirDepth[1]].update({dirDepth[0]:{}})
                        fileDetails[dirDepth[1]][dirDepth[0]].update(entry)
                    if len(dirDepth) == 3:
                        if dirDepth[2] not in fileDetails:
                            fileDetails.update({dirDepth[2]:{dirDepth[1]:{dirDepth[0]:{}}}})
                        if dirDepth[1] not in fileDetails[dirDepth[2]]:
                            fileDetails[dirDepth[2]].update({dirDepth[1]:{dirDepth[0]:{}}})
                        if dirDepth[0] not in fileDetails[dirDepth[2]][dirDepth[1]]:
                            fileDetails[dirDepth[2]][dirDepth[1]].update({dirDepth[0]:{}})
                        fileDetails[dirDepth[2]][dirDepth[1]][dirDepth[0]].update(entry)
        return fileDetails


    @env.macro
    def check_generate(file_path):
        name_file = './docs/'+file_path
        image_name = name_file.replace(".stl",".png")
        if not os.path.exists(image_name):
            if flagImageMesh:
                print('INFO\t -  {:s}Attempting to generate:{:s} {:s} -> {:s}'.format(cl.GRN,cl.END,name_file,image_name))
                try:
                    mesh = Mesh.from_file(name_file)
                    fig=vpl.figure()
                    vpl.mesh_plot(mesh,fig=fig,color=(60,116,179))
                    vpl.save_fig(path=image_name, trim_pad_width=5, pixels=640, off_screen=True, fig=fig)
                except:
                    return False
                    print('ERROR\t -  {:s}Failed to generate:{:s} {:s} -> {:s}'.format(cl.FAIL,cl.END,name_file,image_name))
                else:
                    if flagImageMeshCleanup:
                        try:
                            img = Image.open(image_name)
                            img = img.convert("RGBA")
                            pixdata = img.load()
                            width, height = img.size
                            for y in range(height):
                                for x in range(width):
                                    if pixdata[x, y] == (216, 220, 214, 255):
                                        pixdata[x, y] = (255, 255, 255, 0)

                            img.save(image_name, "PNG")
                        except:
                            print('WARN\t -  {:s}Failed to remove background in:{:s} {:s}'.format(cl.WARN,cl.END,image_name))
                            return True
                        else:
                            return True
                    else:
                        return True
            else:
                print('WARN\t -  {:s}Image does not exist and is not generated, not using in docs:{:s} {:s}'.format(cl.WARN,cl.END,image_name))
                return False
        
        return True