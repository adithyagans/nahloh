#!/usr/bin/python

import sys

def utama():

    print "---SEPUTAR INTECT---"
    
    print "1 = biodata INTECT"
    
    print "2 = kumpulan Tools"
    
    dipilih = raw_input("pilih nomor ( 1 / 2 ) : ")
    
    if dipilih == "1":
    
        print '"Nama Asli = Adithya Yusup.s"'
        print '"Sekolah = smpn188 jakarta"'
        print '"Team = W3LL SQUAD,hallu cyber team,bekasi cyber team,L4EFY"'
        print '"Hoby = Deface,baperin orang:v "'
        print '"Kontak = 081911226887 "'     
        print '"Status = jomblo:( "'
        
    elif dipilih == "2":
    
        print '"---Tools installer INTECT--- "'
        print '"ketik perintah perintah berikut: "'
        print '" -apt update && apt upgrade "'
        print '" -apt install python2 "'
        print '" -apt install ruby "'
        print '" -apt install git "'
        print '" -git clone https://github.com/adithyagans/INTECT_ "'
        print '" -cd INTECT_ "'
        print '" -sh INTECT_.sh "'
        print '" =======END======= "'
        print '"Tersedia banyak tools di dalamnya"'
        
    else :
    
        print  "gua cape anying:v,pilihan nya cuma itu doank kmvrt-_- "
        
    ulangi()
    
    
    
def ulangi():
        
    dicobalagi = raw_input("Coba lagi ? [Y/T] : ")
    
    if dicobalagi.lower() == "y":
    
        utama()
        
    elif dicobalagi.lower() == "t":
    
        sys.exit("tq udeh baca>:)")
    
    else :
     
        print "Pilihannya Cuma Y sama T doank o'on-_- "
        
        ulangi()


utama()
        
        
        
        
    
    
        
       
