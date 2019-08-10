import sys, platform, socket, subprocess, os

class main():
    porta = 443

    def __init__(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if platform.system() != "Linux":
            print '[+] Versao compativel somente com o Linux'
            os._exit(1)

        try:
	        server.bind(('', self.porta))
        except socket.error as msg:
	        print '[+] Erro ao abrir o servidor'
	        os._exit(1)

        server.listen(10)

        print '[+] Trap na porta %s\n' %(str(self.porta))

        while True:
            conexao, addr = server.accept()
            self.droparip(addr[0])
            print '[+] IP Dropado: ' + addr[0]
            conexao.close()

        server.close()

    def droparip(self, ip):
        proc = subprocess.Popen('/bin/bash', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
        proc.communicate('iptables -I INPUT -s %s -j DROP' %(ip))

main()
