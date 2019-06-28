#!/usr/bin/env python3

import socket
import pickle
import dlib
import face_recognition
import cv2 as cv

HOST = '192.168.0.124'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

data = pickle.loads(open("encodings.pickle","rb").read())
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        print("listening...")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data_rec = conn.recv(2048)          
                if not data_rec:
                    break
                encoding = pickle.loads(data_rec)
                matches = face_recognition.compare_faces(data["encodings"],encoding[0],tolerance = 0.4)
                print(matches)

                matches_dum = pickle.dumps(matches)
                conn.sendall(matches_dum)
        
