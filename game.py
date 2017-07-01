# by default every thing is in accesabble 
# 
addr="/home/yash/Desktop/svn/repos"


def get_file_as_list(repo,file):
    file = addr+repo + '/conf/'+file
    with open(file) as file:
        file=file.read()
    file_as_list=file.split("\n")
    return file_as_list

def render(repo,file):
    new_file = addr+repo + '/conf/'+file
    with open(new_file,'w') as realfile:
        for line in file:
            realfile.write(file)
    

def update_old_repo():
    # open old passwd file and for each entry request email ids for gitlab account
    pass

def modify_user(repo , username , password , email , comment=''):
    file=get_file_as_list(repo,"passwd")
    req_line=""
    user_exist=False
    for i in file:
        if username == i.split()[0]:
            req_line=i
            user_exist=True
            break
    if user_exist:
        # change i.password to new password with email as a feild and do delete the old line
        # then render
    else:
        line = username + " = " + password + " #"+email
        file.append(line)
    # also add coresponding user to the gitlab repo 
    # whole lot of code will go in there
    render(repo,file)

def delete_user(repo, username):
    file=get_file_as_list(repo,"passwd")
        req_line=""
        user_exist=False
        for i in file:
            if username == i.split()[0]:
                req_line=i
                # delete this line 
                # delete from the gitlab db too

def file_render():
    # file=get_file_as_list()
    # enter the modifications in file or save a new file all togther 
    pass


def change_permit ( repo , addr , *authors ,rights = "rw" ):
    file=get_file_as_list(repo,"authz")



def all_groups(repo):
    pass

def add_to_group (repo , name , *authors):
    pass

def add_group (repo , name , *authors):
    file = repo + '/conf/authz'
    with open(file,'a') as file:
        file.write('[groups]\n')
        auths =''
        for i in authors:
            auths+= i+','
        auths.pop()
        file.write('name = '+auths)

def delete_group (repo , name):
    
    pass