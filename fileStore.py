from java.io import FileInputStream

def createFilestore(line):
    try:
        startEdit()
        cd('/')
        items = line.split(',')
        items = [item.strip() for item in items]
        (tag,filestore_name,directory,server_target) = items

        #check if filestore exists
        redirect('/dev/null','false')
        exists = ls('/FileStores/',returnMap='true')
        print "filestore name: " +filestore_name
        if filestore_name in exists:
            print('filestore '+ filestore_name + ' already exists !')
            exit(exitcode=1,defaultAnswer='y')

        #create FileStores
        cmo.createFileStore(filestore_name)

        #set directory
        cd('/FileStores/'+ filestore_name)
        if directory != 'None':
            cmo.setDirectory(directory)

        #set target filestore
        cd('/')
        cd('/FileStores/'+ filestore_name)
        targetsForDeployment = []
        targets = server_target.split('|')
        for target in targets:
            if(target == ''):
                break;
            index= target.find(':')
            server_name= target[0:index]
            type_target= target[index+1:]
            print "servername: "  +server_name
            print "type target: " +type_target
            nextName =str('com.bea:Name='+server_name+',Type='+type_target)
            targetsForDeployment.append(ObjectName(nextName))
        #set('Targets',jarray,array([ObjectName('com.bea:Name=' +server_name + ',Type=' +type_target)], ObjectName))
        set('Targets',jarray.array(targetsForDeployment, ObjectName))
        print "create filestore " +filestore_name + " successfully"
        save()
        activate()

    except Exception, e:
        print e


def main():
    propInputStream = FileInputStream(sys.argv[1])
    configProps = Properties()
    configProps.load(propInputStream)

    url=configProps.get("adminUrl")
    username = configProps.get("importUser")
    password = configProps.get("importPassword")
    csvLoc = configProps.get("csvLoc")

    connect(username,password,url)
    edit()
    file=open(csvLoc)
    for line in file.readlines():
        if line.strip().startswith('filestore'):
            createFilestore(line)
            
    disconnect()

main()
