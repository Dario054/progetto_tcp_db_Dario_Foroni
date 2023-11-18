import socket
import threading
import mysql.connector
import facilities


def leggi():
    diz={}
    conn = mysql.connector.connect(
    host="10.10.0.10",
    user="dario_foroni",
    password="foroni1234",
    database="5ATepsit",
    port=3306, # voi qui mettete la porta 3306!! quella di default per mySQL, io ho dovuto mettere la 3307 perche la mia 3306 era gia occupata dal database SQL sul mio PC!
    )
    cur = conn.cursor()
    query = "SELECT * FROM clienti_dario_foroni"
    cur.execute(query)
    dati = cur.fetchall()
    return dati


def leggi_z():
    conn = mysql.connector.connect(
    host="10.10.0.10",
    user="dario_foroni",
    password="foroni1234",
    database="5ATepsit",
    port=3306, # voi qui mettete la porta 3306!! quella di default per mySQL, io ho dovuto mettere la 3307 perche la mia 3306 era gia occupata dal database SQL sul mio PC!
    )
    cur = conn.cursor()
    query = "SELECT * FROM zona_di_lavoro_dario_foroni"
    cur.execute(query)
    dati = cur.fetchall()
    return dati

def delete_c(data):
    conn = mysql.connector.connect(
    host="10.10.0.10",
    user="dario_foroni",
    password="foroni1234",
    database="5ATepsit",
    port=3306, # voi qui mettete la porta 3306!! quella di default per mySQL, io ho dovuto mettere la 3307 perche la mia 3306 era gia occupata dal database SQL sul mio PC!
    )
    cur = conn.cursor()
    query1 = f"DELETE FROM clienti_dario_foroni where id=\'{data}\'"
    cur.execute(query1)
    conn.commit()

def delete_z(data):
    conn = mysql.connector.connect(
    host="10.10.0.10",
    user="dario_foroni",
    password="foroni1234",
    database="5ATepsit",
    port=3306, # voi qui mettete la porta 3306!! quella di default per mySQL, io ho dovuto mettere la 3307 perche la mia 3306 era gia occupata dal database SQL sul mio PC!
    )
    cur = conn.cursor()
    query1 = f"DELETE FROM zona_di_lavoro_dario_foroni where id_zona=\'{data}\'"
    cur.execute(query1)
    conn.commit()

def scrivi(diz_valori):
    conn = mysql.connector.connect(
    host="10.10.0.10",
    user="dario_foroni",
    password="foroni1234",
    database="5ATepsit",
    port=3306, # voi qui mettete la porta 3306!! quella di default per mySQL, io ho dovuto mettere la 3307 perche la mia 3306 era gia occupata dal database SQL sul mio PC!
    )
    cur = conn.cursor()
    query1 = f"INSERT INTO clienti_dario_foroni(nome, cognome, posizione_lavorativa, data_ass, data_n, luogo_n) VALUES(\'{diz_valori['nome']}\', \'{diz_valori['cognome']}\', \'{diz_valori['posizione_lavorativa']}\', \'{diz_valori['data_ass']}\', \'{diz_valori['data_n']}\', \'{diz_valori['luogo_n']}\')"
    cur.execute(query1)
    conn.commit()

def scrivi_z(diz_valori):
    conn = mysql.connector.connect(
    host="10.10.0.10",
    user="dario_foroni",
    password="foroni1234",
    database="5ATepsit",
    port=3306, # voi qui mettete la porta 3306!! quella di default per mySQL, io ho dovuto mettere la 3307 perche la mia 3306 era gia occupata dal database SQL sul mio PC!
    )
    cur = conn.cursor()
    query1 = f"INSERT INTO zona_di_lavoro_dario_foroni(nome_zona, numero_clienti, sesso) VALUES(\'{diz_valori['nome_zona']}\', \'{diz_valori['numero_clienti']}\', \'{diz_valori['sesso']}\')"
    cur.execute(query1)
    conn.commit()
def agg_c(id,att,val):
    conn = mysql.connector.connect(
    host="10.10.0.10",
    user="dario_foroni",
    password="foroni1234",
    database="5ATepsit",
    port=3306, # voi qui mettete la porta 3306!! quella di default per mySQL, io ho dovuto mettere la 3307 perche la mia 3306 era gia occupata dal database SQL sul mio PC!
    )
    query1 = f"UPDATE clienti_dario_foroni SET {att}=\'{val}\' WHERE id={id}"
    cur = conn.cursor()
    cur.execute(query1)
    conn.commit()
def agg_z(id,att,val):
    conn = mysql.connector.connect(
    host="10.10.0.10",
    user="dario_foroni",
    password="foroni1234",
    database="5ATepsit",
    port=3306, # voi qui mettete la porta 3306!! quella di default per mySQL, io ho dovuto mettere la 3307 perche la mia 3306 era gia occupata dal database SQL sul mio PC!
    )
    query1 = f"UPDATE zona_di_lavoro_dario_foroni SET {att}=\'{val}\' WHERE id_zona={id}"
    cur = conn.cursor()
    cur.execute(query1)
    conn.commit()




def inizio_com(lista_conn,num):
        password="1234"
        cont=0
        diz_valori={}
        try:
            while True:
                lista_conn[num].send(("benvenuto inserisci la password").encode())
                data_password=lista_conn[num].recv(1024).decode()
                #print (data_password)
                for i in range(0,2):
                    if data_password!=password:
                        lista_conn[num].send(("password sbagliata").encode())
                        data_password=lista_conn[num].recv(1024).decode()
                        #print(data_password==password)
                        if data_password==password:
                            break
                        if i==1:
                            sys.exit()
                lista_conn[num].send(("che operazione vuoi effetuare(r/c/d/u)").encode())
                data_operazione=lista_conn[num].recv(1024).decode()
                nome_data=lista_conn[num].recv(1024).decode()
                #print(data_operazione)
                if data_operazione=="r":
                    if nome_data=="C":
                        dati=leggi()
                        valori=facilities.list_to_bytes(dati)
                        lista_conn[num].send(valori)
                    else:
                        dati=leggi_z()
                        valori=facilities.list_to_bytes(dati)
                        lista_conn[num].send(valori)
                if data_operazione=="d":
                    if nome_data=="C":
                        data=lista_conn[num].recv(1024).decode()
                        print (data)
                        delete_c(data)
                    else:
                        data=lista_conn[num].recv(1024).decode()
                        delete_z(data)
                if data_operazione=="c":
                    if nome_data=="C":
                        val_diz=lista_conn[num].recv(1024)
                        diz_valori=facilities.bytes_to_dict(val_diz)
                        scrivi(diz_valori)
                    else:
                        val_diz=lista_conn[num].recv(1024)
                        diz_valori=facilities.bytes_to_dict(val_diz)
                        scrivi_z(diz_valori)
                if data_operazione=="u":
                    if nome_data=="C":
                        id=lista_conn[num].recv(1024).decode()
                        att=lista_conn[num].recv(1024).decode()
                        val=lista_conn[num].recv(1024).decode()
                        agg_c(id,att,val)
                    else:
                        id=lista_conn[num].recv(1024).decode()
                        att=lista_conn[num].recv(1024).decode()
                        val=lista_conn[num].recv(1024).decode()
                        agg_z(id,att,val)


        except:
            pass
        
    

            






def connessione_client(indirizzo,backlog=2):
    thread=[]  #variabili per tenere traccia delle connesioni
    i=0    #variabili per tenere traccia del numero delle connesioni
    lista_connessioni=[]
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(indirizzo)
    s.listen(backlog)
    while i<2:
        print("sto aspettando che un client si connetta")
        conn,addr=s.accept()
        lista_connessioni.append(conn)
        print("si è connesso ",lista_connessioni[i])
        i=i+1
    thread.append(threading.Thread(target=inizio_com, args = (lista_connessioni,0) )) 
    thread.append(threading.Thread(target=inizio_com, args = (lista_connessioni,1) )) 
    thread[0].start()
    thread[1].start()




    
    
    


if __name__=="__main__":
    connessione_client(("",51000))