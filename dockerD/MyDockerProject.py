import os
import getpass
os.system("tput setaf 5")
print("---------------------------------------------------")
print("---------------------------------------------------")
os.system("tput setaf 7")
print("HEY ALL , THIS IS MY FIRST DOCKER TUI PROJECT")
os.system("tput setaf 4")
print("....................................................")
os.system("tput setaf 3")

pswrd = detpass.getpass("KINDLY ENTER YOUR PASSWORD : ")

apass = "redhat"

if pswrd!= apass:
    print("OOPS!! WRONG PASSWORD , TRY AGAIN")
    exit()
   
os.system("tput setaf 7")
print("What would you like : (local/remote) :" , end=" ")
location = input()
print(location)

if location == "remote" :
    remoteIP = input("Your IP please : ")

os.system("tput setaf 3")
os.system("figlet /t/t WELCOME!!! YOU ARE IN DOCKER WORLD")
os.system("tput setaf 8 ")

print("IN ORDER TO PERFORM ANY TASK , PRESS BUTTON 4 : ")
os.system("tput setaf 1")

while True :
    print("""
         PRESS 1: INSTALL DOCKER COMMUNITY EDITION.
         PRESS 2: GEDIT FILE CREATION
         PRESS 3: OPEN GEDIT FILE AND THEN GO THROUGH THE REPO LIST
         PRESS 4: START THE DOCKER AND FOR OTHER COMMANDS TO RUN
         PRESS 5: CHECK DOCKER VERSION
         PRESS 6: PULL IMAGES FROM DOCKER
         PRESS 7: CREATE NEW CONTAINER IMAGE BY USING IMAGE NAME
         PRESS 8: CREATE A NEW CONTAINER IMAGE WITH GIVING ANY NAME OF THE CONTAINER IMAGE i.e(topOs , pop etc.)
         PRESS 9: CHECK LIST OF CONTAINER
         PRESS 10:INSTALL wget,net-tools AND OTHER SOFTWARE USING yum install COMMAND
         PRESS 11:REMOVE ALL CONTAINERS
         PRESS 12:INSPECT , WHAT DO YOU WANT BY USNING docker inspect COMMAND
         PRESS 13:CHECK FREE SPACE AVAILABLE IN YOUR MEMORY
         PRESS 14:ENABLE httpd server INSIDE THE DOCKER
         PRESS 15:PUSH YOUR CONTAINER IMAGE INSIDE THE DOCKER HUB
         PRESS 16:CHECK netstat -tnlp
         PRESS 17:NUMBER OF IMAGES YOU HAVE
         PRESS 18:curl TO IP
         PRESS 19:INPUT URL USING SSL
         PRESS 20:COMMIT THE DOCKER IMAGE AND REPOSITORY FILE
         PRESS 21:CHECK THE GATEWAY OF YOUR CONTAINER
         PRESS 22:INSIDE THE DOCKER CREATE A NER CONTAINER
         PRESS 23:CHECK VOLUME LIST
         PRESS 24:START THE docker-compose file
         PRESS 25:EXIT
         """)
    print("Press any press button to perform the task you want : " , end="")
    ch = input()
    print(ch)

    if location == "local":
        if int(ch) == 1:
            os.system("tput setaf 7 ")
            os.system("yum install docker-ce --nobest")
        elif int(ch) == 2:
            print("Give file name :" , end = '')
            file_name = input()
            os.system("tput setaf 7")
            os.system("gedit {}".format(create_name))
        elif int(ch) == 3:
            os.system("tput setaf 7")
            os.system("gedit docker.repo")
        elif int(ch) == 4:
            print("Enter what you want to do start/stop/restart :" , end=" ")
            create_name = input()
            os.system("systemctl start {}" .format(create_name))
        elif int(ch) == 5:
            print("enter what do you want to check :" , end=' ')
            check_name = input(ch)
            os.system("tput setaf 6")
            os.system("docker {} " .format(check_name))
        elif int(ch) == 6:
            print("enter image name to pull :" , end= ' ')
            image__name = input(ch)
            os.system("tput setaf 6")
            os.system("docker pull {} " .format(image__name))
        elif int(ch) == 7:
            print("image name to create container :" , end= ' ')
            image__name = input(ch)
            os.system("tput setaf 6")
            os.system("docker run -it  {} " .format(image__name))
        elif int(ch) == 8:
            print("give name to the container:" , end = ' ')
            name = input()
            os.system("docker container run -it --name {}" .format(name))
            print("enter the image name to create container :" , end = ' ')
            image_name = input()
            os.system("docker run -it {}" .format(image_name))
            print("press 0 to exit")
            os.system("exit")
        elif int(ch) == 9:
            print("enter what you want to install :" , end = ' ')
            install_name = input()
            os.system("tput setaf 6")
            os.system("yum install {}" .format("install_name"))
        elif int(ch) == 10:
if int(ch) == 1:
            os.system("tput setaf 7 ")
            os.system("yum install docker-ce --nobest")
        elif int(ch) == 2:
            print("Give file name :" , end = '')
            file_name = input()
            os.system("tput setaf 7")
            os.system("gedit {}".format(create_name))
        elif int(ch) == 3:
            os.system("tput setaf 7")
            os.system("gedit docker.repo")
        elif int(ch) == 4:
            print("Enter what you want to do start/stop/restart :" , end=" ")
            create_name = input()
            os.system("systemctl start {}" .format(create_name))
        elif int(ch) == 5:
            print("enter what do you want to check :" , end=' ')
            check_name = input(ch)
            os.system("tput setaf 6")
            os.system("docker {} " .format(check_name))
        elif int(ch) == 6:
            print("enter image name to pull :" , end= ' ')
            image__name = input(ch)
            os.system("tput setaf 6")
            os.system("docker pull {} " .format(image__name))
        elif int(ch) == 7:
            print("image name to create container :" , end= ' ')
            image__name = input(ch)
            os.system("tput setaf 6")
            os.system("docker run -it  {} " .format(image__name))
        elif int(ch) == 8:
            print("give name to the container:" , end = ' ')
            name = input()
            os.system("docker container run -it --name {}" .format(name))
            os.system("tput setaf 5")
            os.system("docker rm -f $(docker os -a -q)")
        elif int(ch) == 11:
            print("what do you want to inspect :" ,end = ' ')
            inspect_name = input()
            os.system("tput setaf 5")
            os.system("docker inspect {} " .format(inspect_name))
       elif int(ch) == 12:
            os.system("tput setaf 6")
            os.system("free -m")
       elif int(ch) == 13:
            os.system("tput setaf 5")
            os.system("cd /var/run/httpd/")
       elif int(ch) == 14:
            print("enter user id and image name")
            enter_name = input()
            os.system("tput setaf 5")
            os.system("docker push {}" .format(enter_name))
       elif int(ch) == 15:
            os.system("tput setaf 5")
            os.system("netstat -tnlp")
       elif int(ch) == 16:
            os.system("tput setaf 5")
            os.system("docker rm -f $(docker os -a -q)")
       elif int(ch) == 17:
            print("enter image name :" , end = ' ')
            image_name  = input()
            os.system("tput setaf 5")
            os.system("docker images | grep {}" .format(image_name))
       elif int(ch) == 18:
            print("enter IP :" , end =' ')
            ip_no = input()
            os.system("tput setaf 5")
            os.system("curl {}" .format(URL_name))
       elif int(ch) == 19:
            print("Enter URL :" ,end = ' ')
            URL_name = input()
            os.system("tput setaf 5")
            os.system("curl -sSL {}" .format(URL_name))
       elif int(ch) == 20:
            print("enter the image name to commit :" , end = ' ')
            Image_name = input()
            os.system("docker commit {}" .format(Image_name))
            print("Enter repository file name to commit :" , end = ' ')
            file_name = input()
            os.system("tput setaf 5")
            os.system("docker commit {}" .format(file_name))
       elif int(ch) == 21:
            os.system("tput setaf 5")
            os.system("route -n")
      elif int(ch) == 17:
            print("enter image name :" , end = ' ')
            image_name  = input()
            os.system("tput setaf 5")
            os.system("docker images | grep {}" .format(image_name))
       elif int(ch) == 18:
            print("enter IP :" , end =' ')
            ip_no = input()
            os.system("tput setaf 5")
            os.system("curl {}" .format(URL_name))
       elif int(ch) == 19:
            print("Enter URL :" ,end = ' ')
            URL_name = input()
            os.system("tput setaf 5")
            os.system("curl -sSL {}" .format(URL_name))
       elif int(ch) == 20:
            print("enter the image name to commit :" , end = ' ')
            Image_name = input()
            os.system("docker commit {}" .format(Image_name))
            print("Enter repository file name to commit :" , end = ' ')
            file_name = input()
            os.system("tput setaf 5")
            os.system("docker commit {}" .format(file_name))
       elif int(ch) == 21:
            os.system("tput setaf 5")
            os.system("route -n")
       elif int(ch) == 22:
            print("enter volume name :" end = ' ')
            volume_name = input()
            os.system("tput setaf 5")
            os.system("docker volume create {}" .format(volume_name))
       elif int(ch) == 23:
            os.system("tput setaf 5")
            os.system("docker volume ls")
       elif int(ch) == 24:
            os.system("tput setaf 4")
            os.system("docker-compose up")
       elif int(ch) == 25:
           os.system("tput setaf 2")
           os.system("exit")
           os.system("figlet -f block \t\t THANKS A LOT !")

       else :
           print("OPTION NOT SUPPORTED")
       input("Enter to continue >>>>>>>>>>")
       os.system("clear")

   elif locatio == "remote" :
       os.system("tput setaf 3")
       if int(ch) == 1:
            os.system("tput setaf 7 ")
            os.system("yum install docker-ce --nobest")
        elif int(ch) == 2:
            print("Give file name :" , end = '')
            file_name = input()
            os.system("tput setaf 7")
            os.system("gedit {}".format(create_name))
        elif int(ch) == 3:
            os.system("tput setaf 7")
            os.system("gedit docker.repo")
        elif int(ch) == 4:
            print("Enter what you want to do start/stop/restart :" , end=" ")
            create_name = input()
            os.system("systemctl start {}" .format(create_name))
        elif int(ch) == 5:
            print("enter what do you want to check :" , end=' ')
            check_name = input(ch)
            os.system("tput setaf 6")
            os.system("docker {} " .format(check_name))
        elif int(ch) == 6:
            print("enter image name to pull :" , end= ' ')
            image__name = input(ch)
            os.system("tput setaf 6")
            os.system("docker pull {} " .format(image__name))
        elif int(ch) == 7:
            print("image name to create container :" , end= ' ')
            image__name = input(ch)
            os.system("tput setaf 6")
            os.system("docker run -it  {} " .format(image__name))
        elif int(ch) == 8:
            print("give name to the container:" , end = ' ')
            name = input()
            os.system("docker container run -it --name {}" .format(name))
         elif int(ch) == 11:
            print("what do you want to inspect :" ,end = ' ')
            inspect_name = input()
            os.system("tput setaf 5")
            os.system("docker inspect {} " .format(inspect_name))
       elif int(ch) == 12:
            os.system("tput setaf 6")
            os.system("free -m")
       elif int(ch) == 13:
            os.system("tput setaf 5")
            os.system("cd /var/run/httpd/")
       elif int(ch) == 14:
            print("enter user id and image name")
            enter_name = input()
            os.system("tput setaf 5")
            os.system("docker push {}" .format(enter_name))
       elif int(ch) == 15:
            os.system("tput setaf 5")
            os.system("netstat -tnlp")
       elif int(ch) == 16:
            os.system("tput setaf 5")
            os.system("docker rm -f $(docker os -a -q)")
       elif int(ch) == 17:
            print("enter image name :" , end = ' ')
            image_name  = input()
            os.system("tput setaf 5")
            os.system("docker images | grep {}" .format(image_name))
       elif int(ch) == 18:
            print("enter IP :" , end =' ')
            ip_no = input()
            os.system("tput setaf 5")
            os.system("curl {}" .format(URL_name))
       elif int(ch) == 19:
            print("Enter URL :" ,end = ' ')
            URL_name = input()
            os.system("tput setaf 5")
            os.system("curl -sSL {}" .format(URL_name))
       elif int(ch) == 20:
            print("enter the image name to commit :" , end = ' ')
            Image_name = input()
            os.system("docker commit {}" .format(Image_name))
            print("Enter repository file name to commit :" , end = ' ')
            file_name = input()
            os.system("tput setaf 5")
            os.system("docker commit {}" .format(file_name))
       elif int(ch) == 21:
            os.system("tput setaf 5")
            os.system("route -n")
        elif int(ch) == 22:
            print("enter volume name :" end = ' ')
            volume_name = input()
            os.system("tput setaf 5")
            os.system("docker volume create {}" .format(volume_name))
       elif int(ch) == 23:
            os.system("tput setaf 5")
            os.system("docker volume ls")
       elif int(ch) == 24:
            os.system("tput setaf 4")
            os.system("docker-compose up")
       elif int(ch) == 25:
           os.system("tput setaf 2")
           os.system("exit")
           os.system("figlet -f block \t\t THANKS A LOT !")

       else :
           print("OPTION NOT SUPPORTED")
       input("Enter to continue >>>>>>>>>>")
       os.system("clear")
 
    
                    
     
                    
      
     
      
            

            




