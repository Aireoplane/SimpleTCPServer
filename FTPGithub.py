from twisted.cred.checkers import AllowAnonymousAccess, InMemoryUsernamePasswordDatabaseDontUse
from twisted.cred.portal import Portal
from twisted.internet import reactor
from twisted.protocols.ftp import FTPFactory, FTPRealm
from rich.prompt import Prompt, Confirm
import os


hosting_destination: str = Prompt.ask("Enter port to host: ", default="2700")
confirm_hosting = Confirm.ask("Are you sure you want to host? ")
checker = InMemoryUsernamePasswordDatabaseDontUse()

checker.addUser("user1", "user1password")
checker.addUser("user2", "user2password")

if hosting_destination < "1024":
    raise Exception("Port can't be under 1024 (commom world wide web ports are restricted)")
else:
    if hosting_destination > "9999":
        raise Exception("Port can't be over 9999")
    else:
        pass

# noinspection PyTypeChecker
portal = Portal(FTPRealm(r"C:\Users\maninithi\OneDrive\Desktop\FTPMain_Server"), [AllowAnonymousAccess()])
factory = FTPFactory(portal)

print(
    f"Hosting FTP server using File Transfer Protocol on port number {hosting_destination}. Allowed root and main directory is -Enter You Hosting Directory Here-")

print("""

| Anonymous access key                 |
|======================================|
|Username            Password          |
|======================================|
|Anonymous          youremail@gmail.com|


""")

print("Server is now active!")

try:
    reactor.listenTCP(int(hosting_destination), factory)
    reactor.run()

except:
    print("Unable to Host: Error 303")
