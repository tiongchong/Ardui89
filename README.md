#Ardui89 8051 C IDE 0.4.2 for Arduino IDE

#Under GPL license

Adds 8051 architecture family to the Arduino IDE :
STC89C52RC, STC89C516RD+, STC15W408AS-DIP16

* DISCLAIMER OF ALL WARRANTIES *

Allows you to COMPILE a .ino file of the 8051 C family program and UPLOAD it into the STC89C5x, STC15..., etc. family.

#Versions
0.0.1  : first Mac OS try (compiling only) (Arch 8051 STC89C51RC(4kb) and STC89C52RC(8kb))
0.0.6   : Mac OS completed (compiling and programming)
0.1.1   : tone function builtin, bugs fixed
0.2.0   : first windows try (compilling only)
0.2.1   : fist windows version completed (compilling and programming)
0.2.2   : Warning : new PINOUT for 805x Arduino equivalent and add STC32G12K128 = 8952 with 128k flash memory
0.2.3   : PINOUT fixed, bugs fixed. Variants STC15F2K32S2, STC32G12K128 fixed
0.3.0   : Replace stcflash by stcgal -> stc15 best process, add STC15W408AS-DIP16
0.3.1   : Bugs fixed
0.3.2   : Mini bugs fixed. Primary linux beta version ready : See dependencies packages installation.
0.3.3   : Mini bugs fixed. Speed uplaod bug fixed / choice speed upload menu added
0.3.7   : Add Serial.readString / Add push-pull output configuration for STC micro-controllers
0.3.8   : (25/04/25) Ardui89 Cinque-Uno replaced by Uno 5X, any bugs fixed
0.3.9   : (25/05/23) Any bugs fixed : compiling core problem on Mac OS Sequoia and Windows 11
0.3.10  : (25/05/27) Add int_to_string like function (same to_string but for int exclusively), and 8051/pgmspace.h 
0.3.11  : (25/05/31) add STC89C516RD+ (62464 bytes (64kb-internal isp)) and 22.1184 Mhz clock option
BETA 0.3.12 : (25/06/14) add #include <string.h> + Prévoir les STC15F2K16 et K32 et STC32G12k128.
0.4.0   : (25/07/27) better RAM management
0.4.1   : (25/10/16) add 29.4912 Mhz external and internal clock option
0.4.1.1 : (26/03/08) same 0.4.1, just UNO Cinque X Board Revision (R2)
0.4.2   : (26/05/16) analogRead and analogPin functions add for STC15 / pwd/tone compute modifed, based on F_CPU (not only 11059200Mhz) / new programme size compute.
    analogPin(A0) or pinMode(A0,INPUT_ANALOG) / analogRead(A0)


#Platforms
MacOS, Wind'Oz. (Stable)

#To do
analogWrite with ST15 and ST32 series.
Stable Linux version.

#Installation and test

1/ Donwload Arduino >= V1.8.19 

2/ Launch Arduino

3/ In Arduino->Preferences->Additional Board Manager URLS
    add for Arduino All Versions
    https://master.dl.sourceforge.net/project/stc89/packages/package_ardui89_index.json?viasf=1
    
4/ In Tools->Boards:...->Board Manager
    search "8051"
    select and install "ardui89 8051 family Boards"
    
5/ In Tools->Board:...
    select "Board : "STC89C52RC" "STC89C516RD+" "STC15W408AS-DIP16""
    
6/ Demos :
    Use Blink.ino in basics examples or in Ardui89_demos path :
    Hello.ino
    Howareyou.ino
    
    and build and upload !

#Linux Dependencies

python3 / python3-pip / stcgal / sdcc

Under terminal :

1/ Installing stcgal :

sudo apt-get install python3 python3-pip

sudo python3 -m pip stcgal

2/ Installing SDCC :

sudo apt-get install sdcc

#Important

Under Wind'Oz, using absoluty last version (>=3.8) of CH340 drivers (CH341SER.ZIP) (Included in this package).


Many thanks

Cyril BARBATO

https://sourceforge.net/projects/stc89
cyril.barbato@gmx.com

# Arduino <=> STC89C51/STC89C52/STC89C5x/STC89C51x pinout equivalent
(Ardui89 Cinque Uno/Due/128k R0)

D : Arduino digital pins
A : Arduino analog pins
LED_BULTIN : D13 (P3.5)

 D                                                                 D  A
               +---------------\/--------------+
               |                               |
 7 P1.0 -------|  1  P1.0              VCC  40 |------ VCC
 8 P1.1 -------|  2  P1.1             P0.0  39 |------ P0.0 (AD0) 31 A7
 2 P1.2 -------|  3  P1.2             P0.1  38 |------ P0.1 (AD1) 30 A6
 3 P1.3 -------|  4  P1.3             P0.2  37 |------ P0.2 (AD2) 29 A5 SCL
 4 P1.4 -------|  5  P1.4             P0.3  36 |------ P0.3 (AD3) 28 A4 SDA
 5 P1.5 (MOSI)-|  6  P1.5 (MOSI)      P0.4  35 |------ P0.4 (AD4) 27 A3
 6 P1.6 (MISO)-|  7  P1.6 (MISO)      P0.5  34 |------ P0.5 (AD5) 26 A2
 7 P1.7 (SCK)--|  8  P1.7 (SCK)       P0.6  33 |------ P0.6 (AD6) 25 A1
    RST -------|  9  RST              P0.7  32 |------ P0.7 (AD7) 24 A0
 0 P3.0 -------| 10  P3.0 (RXD)   (VPP) EA  31 |------ EA   (VPP)
 1 P3.1 -------| 11  P3.1 (TXD)  (PRG) ALE  30 |------ ALE  (PRG)
10 P3.2 -------| 12  P3.2 (INT0)     /PSEN  29 |------ /PSEN
11 P3.3 -------| 13  P3.3 (INT1)      P2.7  28 |------ P2.7 (A15) 23
12 P3.4 -------| 14  P3.4 (T0)        P2.6  27 |------ P2.6 (A14) 22
13 P3.5 -------| 15  P3.5 (T1)        P2.5  26 |------ P2.5 (A13) 21
14 P3.6 -------| 16  P3.6 (WR)        P2.4  25 |------ P2.4 (A12) 20
15 P3.7 -------| 17  P3.7 (RD)        P2.3  24 |------ P2.3 (A11) 19
  XTAL2 -------| 18  XTAL2            P2.2  23 |------ P2.2 (A10) 18
  XTAL1 -------| 19  XTAL1 P          P2.1  22 |------ P2.1 (A9)  17
    GND -------| 20  GND              P2.0  21 |------ P2.0 (A8)  16
               +-------------------------------+

# Arduino <=> STC15W408AS-DIP28 / STC15F2K16 or 32 pinout equivalent
(Ardui89 UNO R0)

D : Arduino digital pins
A : Arduino analog pins
LED_BULTIN : D13 (P2.5)
SDA : A4 (D22/P1.4)
SCL : A5 (D23/P1.5)

A   D                                                                         D
                  +---------------------\_/--------------------+
   14 P2.6 -------|  1 P2.6 (CCP1)            (CCP0_3) P2.5 28 |------- P2.5 13
   15 P2.7 -------|  2 P2.7 (CCP2)             (ECI_3) P2.4 27 |------- P2.4 12
A0 18 P1.0 -------|  3 P1.0 (RxD2)            (MOSI_2) P2.3 26 |------- P2.3 11
A1 19 P1.1 -------|  4 P1.1 (TxD2)            (MISO_2) P2.2 25 |------- P2.2 10
A2 20 P1.2 -------|  5 P1.2 (ECI)             (SCLK_2) P2.1 24 |------- P2.1  9
A3 21 P1.3 -------|  6 P1.3 (MOSI)        (RSTOUT_LOW) P2.0 23 |------- P2.0  8
A4 22 P1.4 -------|  7 P1.4 (MISO) (INT3/TxD_2/CCP2_2) P3.7 22 |------- P3.7  7
A5 23 P1.5 -------|  8 P1.5 (SCLK)  (NT2/RxD_2/CCP1_2) P3.6 21 |------- P3.6  6
       XT2 -------|  9 P1.6 (XTAL2) (T1/T0CLKO/CCP0_2) P3.5 20 |------- P3.5  5
       XT1 -------| 10 P1.7 (XTAL1)  (T0/T1CLKO/ECI_2) P3.4 19 |------- P3.4  4
   16  RST -------| 11 P5.4 (MCLKO)             (INT1) P3.3 18 |------- P3.3  3
       Vcc -------| 12 Vcc                      (INT0) P3.2 17 |------- P3.2  2
   17 P5.5 -------| 13 P5.5                   (TxD/T2) P3.1 16 |------- P3.1  1
      Gnd  -------| 14  Gnd          (RxD/INT4/T2CLKO) P3.0 15 |------- P3.0  0
                  +--------------------------------------------+

# Arduino <=> STC15W408AS-DIP16
(Ardui89 MINI R0)

D : Arduino digital pins
A : Arduino analog pins
LED_BULTIN : D7 (P3.7)
SDA : A4 (D12/P1.4)
SCL : A5 (D13/P1.5)

 D   A                                                                 A D
                   +-----------------\_/----------------+
 10 A2 P1.2 -------| 1 P1.2                     P1.1 16 |------- P1.1 A1 9
 11 A3 P1.3 -------| 2 P1.3 (MOSI)              P1.0 15 |------- P1.0 A0 8
 12 A4 P1.4 -------| 3 P1.4 (MISO) (/INT3-TxD2) P3.7 14 |------- P3.7    7
 13 A5 P1.5 -------| 4 P1.5 (SLK)  (/INT2-RxD2) P3.6 13 |------- P3.6    6
  4    P5.4 -------| 5 P5.4              (INT1) P3.3 12 |------- P3.3    3
        Vcc -------| 6 Vcc               (INT0) P3.2 11 |------- P3.2    2
  5    P5.5 -------| 7 P5.5               (TxD) P3.1 10 |------- P3.1    1
        Gnd -------| 8 Gnd                (RxD) P3.0  9 |------- P3.0    0
                   +------------------------------------+

