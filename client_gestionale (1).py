import socket
import facilities
def inizio_conn(indirizzo):
    diz={"nome":"","cognome":"","posizione_lavorativa":"","data_ass":"","data_n":"","luogo_n":""}
    diz2={"nome_zona":"","numero_clienti":"","sesso":""}
    password_v="1234"
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(indirizzo)
    data=s.recv(1024)
    print(data.decode())
    password=input()
    s.send(password.encode())
    istruzione=s.recv(1024).decode()
    #print(istruzione)
    while istruzione=="password sbagliata":
        print(istruzione)
        password=input()
        s.send(password.encode())
        istruzione=s.recv(1024).decode()
    if password==password_v:
        print (istruzione)
        operazione=input()
        s.send(operazione.encode())
        database=input("inserisci C o Z: ")
        s.send(database.encode())
        if operazione=="r":
            valore=s.recv(1024)
            diz=facilities.bytes_to_list(valore)
            print(diz)
        if operazione=="d":
            ident=input("inserisci l'id da eliminare: ")
            s.send(ident.encode())
        if operazione=="c":
            if database=="C":
                diz["nome"]=input("inserisci il nome: ")
                diz["cognome"]=input("inserisci il cognome: ")
                diz["posizione_lavorativa"]=input("inserisci la posizione lavorativa: ")
                diz["data_ass"]=input("inserisci la data di assunzione(a/m/g): ")
                diz["data_n"]=input("inserisci la data di nascita(a/m/g): ")
                diz["luogo_n"]=input("inserisci il luogo di nascita: ")
                #print(diz)
                valore=facilities.dict_to_bytes(diz)
                s.send(valore)
            else:
                diz2["nome_zona"]=input("inserisci il nome della zona: ")
                diz2["numero_clienti"]=input("inserisci il numero di clienti: ")
                diz2["sesso"]=input("inserisci il sesso: ")
                valore=facilities.dict_to_bytes(diz2)
                s.send(valore)
        if operazione=="u":
            if database=="C":
                id=input("inserisci l'id da modificare: ")
                s.send(id.encode())
                attributo=input("inserisci l'attributo da modificare(nome,cognome,posizione_lavorativa,data_ass,data_n,luogo_n): ")
                s.send(attributo.encode())
                val_attr=input("inserisci il valore dell'attributo: ")
                s.send(val_attr.encode())
            else:
                id=input("inserisci l'id da modificare: ")
                s.send(id.encode())
                attributo=input("inserisci l'attributo da modificare(nome_zona,numero_clienti,sesso): ")
                s.send(attributo.encode())
                val_attr=input("inserisci il valore dell'attributo: ")
                s.send(val_attr.encode())



                



        

    

    



if __name__=="__main__":
    inizio_conn(("127.0.0.1",51000))