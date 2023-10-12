# thermosensor_wio-terminal
thermosensor using a wio terminal with arduino, python

## Requirements
* [Wio Terminal](https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/)
* [MCP9700A-E/TQ](https://akizukidenshi.com/catalog/g/gI-14300/) (thermosensor IC)

## How to use
1. Clone this repository `git clone https://github.com/1taroh/thermosensor_wio-terminal.git`
2. python -m venv venv
3. `venv\Scripts\activate`
4. `pip install -r requirements.txt`
5. download Arduino IDE
6. Upload `thermosensor.ino` to your wio Terminal
7. Create a circuit like the following
8. `python3 main.py`

You will see the ambient temperature by serial communications.

![circuit](./figure/circuit.jpeg)