class ContextoSinples:

    def __enter__(self):
        print ("Iniciar conexãp....")
        return self
    
    def __exit__(self, exc_type, exe_val, exec_tb):
        print("Fechando conexão com segurança")

with ContextoSinples() as cs:
    print ("Execuções em Banco de dados!")