import socket
import threading

# SOCK_STREAMcar on utilise du tcp
# AF_INET CAR ON use le réseau
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# toutes les interfaces
bind_ip = "0.0.0.0"
# #OUVERTURE DU PORT
bind_port = 8090
# creation de l'objet socket()
server.bind((bind_ip, bind_port))

server.listen(5)  # nombre maximun de connection autorisé sans les accepter
print("[+] Lintening on adresse %s an dport %d" % (bind_ip, bind_port))

# a chaque connexion le server un objet client unique  a récupère l'IP et le numéro de port utilisé par le client
(client, (ip, port)) = server.accept()

print("Client @IP: %s" % ip)
print(" Client Remote port : %d" % port)

data = 'rien'
reponse = "Thanks for contacting me \n"
while len(data):
    data = client.recv(2048).decode('utf-8')  # affiche la donné que el client entre
    print("Client sent: ", data)

    client.send(reponse.encode('utf-8'))

print("closing the connections")
client.close()
server.close()

# lancer l'application puis à l'aide dr netcat lancer un econnection vers le server pour vérifier
# nc @ip_machine_server 8090 puis l'affichage en console
