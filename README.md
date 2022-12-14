# api na komunikáciu s dronom
Tím:

- Daniel Fundárek
- Jakub Ivan
- Adam Bucko
- Matúš Jankech

Opis: 
Cieľom projektu je ovládať drona RYZE Tello pomocou akcelerometra/gyroskopu umiestnených na senzorovej doske IKS01A2.

Špecifikácia: 
Spracovanie dát posielaných pomocou seriovej linky a následne posielanie príkazov dronu, ktoré boli prijaté seriovou linkou.
V prípade prerušenia komunikácie cez seriovú linku dron automatický pristane.


mód1 - riadenie pohybu drona
mód2 - riadenie pristátia, vzlietnutia a flipov
V oboch módoch je možné riadiť drona len pri stlačenom tlačidle2 (signalizácia stlačenia pomocou zasvietenej zelenej ledky).

Opis riadenia drona:

mód - "RC mód" 
V tomto móde api posiela príkazy rc ktoré riadia rychlosti drona v jednotlivých smeroch(roll, pitch, yaw, up/down).

mód - "Príkazový mód"
V príkazovom móde api posiela príkazy typu LAND, TAKEOFF, FLIP.


