import os
import subprocess
import sys
import pandas as pd
import math
import time
    
print("PID: ",os.getpid())
print("\n")


numExecucoes = 30
caminhoDir = "cmake-build-debug"
metodo = "IG"
parametros = " --pasta '" + "cmake-build-debug/resultados" + "' --resulCSV 'resultados.csv' --execTotal "+str(numExecucoes)+ " --alphaSeg 0.05 --betaPrim 0.75 --difBest 0.05 --numItIG 2500 --torneio 1 --taxaRm 0.25 "
parametros = parametros +  " --execAtual "

print("PARAMETROS: \n", parametros, "\n")


instancia = "/home/igor/Documentos/Projetos/2E-EVRP-TW/Código/instancias/2e-vrp-tw/all/C104_21x.txt"
        
for j in range(1):
    
    start = int(0)
    
    for i in range(start, numExecucoes, 1):

      strExecutavel = caminhoDir+'//run ' + str(instancia) + parametros + str(i)
      os.system(strExecutavel)
      #print(strExecutavel)
      
    #print(instancias)
    print("\n\n")
    sys.stdout.flush()
