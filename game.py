# by default every thing is in accesabble 
# chack for subgit instalation 
# check for gitlab instalation

# \/ this is the address of the svnserve root dir
from os import system
addr="/home/yash/Desktop/svn/repos/"

def get_file_as_list(repo,file,view=False):

	file = addr+repo + '/conf/'+file
	with open(file) as file:
	    file=file.read()
	file_as_list=file.split("\n")
	if view==True:
		system("clear")
		for line in file_as_list:
			print (line)
	else:
	    return file_as_list

def render(repo,file,file_as_list):
	if render_dev(repo,file, file_as_list) :
		print (repo+" "+file+" modified successfully")
	else :
		print ("admin error contact administrator")

def render_dev(repo,file,file_as_list):
	new_file = addr+repo + '/conf/'+file
	with open(new_file,'w') as realfile:
	    for line in file_as_list:
	        if type(line)=="<class 'list'>":
	        	print (line)
	        realfile.write(line+'\n')
	        print(line+'\n')
	return True
    
#worksfine
def update_pass(repo , user , old_passwd, new_passwd , comment = ''):
	file='passwd'
	file_as_list=get_file_as_list(repo, file)

	for line in file_as_list:
		if line[0] == '#' :
			continue
		if user in line:
			k=line
			comment = k.split('#')[1]
			k=k.split('#')[0]
			k=k.split('=')
			if k[1]==old_passwd:
				k[1]=new_passwd
			else :
				print ("admin error contact administrator")
				return False
			k="=".join(k)
			if comment:
				k = k+ "# "+ comment 
			print ("new line is \n"+ k +"\n")
			file_as_list[file_as_list.index(line)]=k
			break
	render(repo,file, file_as_list)
    # open old passwd file and for each entry request email ids for gitlab account

#works fine
def update_username(repo , user , new_username):
	# when
	file='passwd'
	file_as_list=get_file_as_list(repo, file)

	# print str.replace("is", "was")

	for i in range (len(file_as_list)):
		file_as_list[i]=file_as_list[i].replace(user, new_username)
	render(repo,file, file_as_list)
	# authz
	file='authz'
	file_as_list=get_file_as_list(repo, file)

	for i in range (len(file_as_list)):
		file_as_list[i]=file_as_list[i].replace(user, new_username)
	render(repo,file, file_as_list)

    # open old passwd file and for each entry request email ids for gitlab account


#works good
def delete_user(repo, username):
	file='passwd'
	file_as_list=get_file_as_list(repo, file)

	for line in file_as_list:
		if len(line)==0:
			continue
		if line[0] == '#' :
			continue
		if username in line:
			file_as_list.remove(line) 
	render(repo,file, file_as_list)
    # open old passwd file and for each entry request email ids for gitlab account

# works good
def add_user(repo, username , password, comment = ''):
	file='passwd'
	file_as_list=get_file_as_list(repo, file)

	for line in file_as_list:
		if len(line)==0 :
			continue
		if line[0] == '#' :  
			continue
		if username in line.split("#")[0]:
			print ("user already exist")
			return False
						
	k="=".join([username,password])
	if comment:
		k = k + " # " + comment 
	print ("new line is "+ k +"\n")
	file_as_list[file_as_list.index(line)]=k
	render(repo,file, file_as_list)
    # open old passwd file and for each entry request email ids for gitlab account


def add_permit_author ( repo , addr , *authors ,rights = "rw" ):
    file= "authz"
    file_as_list  =get_file_as_list(repo,file)
    addrexist=False
    
    for line in file_as_list:
    	if len(line)==0 :
			continue
		if line[0] == '#' :  
			continue
    	if addr in line :
    		addrexist=True
    		k=file_as_list.index(addr)+1
    		for author in authors:
    			permition= author + '=' + rights+'\n'
    			file_as_list.insert( permition ,k)
    			k=k+1
    		continue
	if !addrexist:
		addr="["+addr+"]"
		file_as_list.append(addr)
		for author in authors:
			permition= author + '=' + rights+'\n'
			file_as_list.append( permition)
    render(repo,file, file_as_list)


def list_groups(repo):
    pass

def list_users():
	# for 
	pass

def group_mod (repo , *authors , old_name , new_name ='', remove=False):
	if new_name:
		pass
		# this is a name change operation
	else:
		if remove:
			pass
			# remove the users in authors list
		else:
			pass
			# add the users in authors list

def group_add (repo , name , *authors):
    file = repo + '/conf/authz'
    with open(file,'a') as file:
        file.write('[groups]\n')
        auths =''
        for i in authors:
            auths+= i+','
        auths.pop()
        file.write('name = '+auths)

def group_del (repo , name):
    pass