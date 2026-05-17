from http.server import HTTPServer, BaseHTTPRequestHandler

class MeuHandler(BaseHTTPRequestHandler):
    # Essa função roda toda vez que alguém envia um POST para o servidor
    def do_POST(self):
        # Descobre o tamanho do texto que está chegando
        conteudo_comprimento = int(self.headers['Content-Length'])
        # Lê o texto real enviado pelo ESP32
        dados_recebidos = self.read(conteudo_comprimento).decode('utf-8')
        
        print("\n--- DADO RECEBIDO DO ESP32! ---")
        print(dados_recebidos)
        print("--------------------------------\n")
        
        # Envia uma resposta de "OK" (Status 200) de volta para o ESP32
        self.send_response(200)
        self.end_headers()

# Aqui nós escolhemos a PORTA (vamos usar a 5000)
#endereco = ('localhost', 5000)
endereco = ('0.0.0.0', 5000)
servidor = HTTPServer(endereco, MeuHandler)

print("Servidor rodando e aguardando o ESP32 na porta 5000...")
servidor.serve_forever()


