#@clintsoff

import secp256k1 as ice
from bloomfilter import BloomFilter, ScalableBloomFilter, SizeGrowthRate
from pathlib import Path
import random
import gmpy2
from rich import print

print('[+] Starting... Please Wait... BF Files Loading ...')
bloombtc1 = Path(__file__).resolve()
ressbtc1 = bloombtc1.parents[0] / 'btc.bf'
with open(ressbtc1, "rb") as fp:
	bloom1 = BloomFilter.load(fp)
    
bloombtc2 = Path(__file__).resolve()
ressbtc2 = bloombtc2.parents[0] / 'eth.bf'
with open(ressbtc2, "rb") as fp:
	bloom2 = BloomFilter.load(fp)
addr_countbtc = len(bloom1)+len(bloom2)
print("[yellow][+] flipper.py <-> Loaded addresses:",str (addr_countbtc),)

range1 = 0x1000000000000000000000000000000000000000000000000000000000000000
range2 = 0x2000000000000000000000000000000000000000000000000000000000000000
range3 = 0x3000000000000000000000000000000000000000000000000000000000000000
range4 = 0x4000000000000000000000000000000000000000000000000000000000000000
range5 = 0x5000000000000000000000000000000000000000000000000000000000000000
range6 = 0x6000000000000000000000000000000000000000000000000000000000000000
range7 = 0x7000000000000000000000000000000000000000000000000000000000000000
range8 = 0x8000000000000000000000000000000000000000000000000000000000000000
range9 = 0x9000000000000000000000000000000000000000000000000000000000000000
rangeA = 0xa000000000000000000000000000000000000000000000000000000000000000
rangeB = 0xb000000000000000000000000000000000000000000000000000000000000000
rangeC = 0xc000000000000000000000000000000000000000000000000000000000000000
rangeD = 0xd000000000000000000000000000000000000000000000000000000000000000
rangeE = 0xe000000000000000000000000000000000000000000000000000000000000000
rangeF = 0xf000000000000000000000000000000000000000000000000000000000000000

lmda = 0x5363ad4cc05c30e0a5261c028812645a122e22ea20816678df02967c1b23bd72
lmdadiv =0x29B1D6A6602E187052930E014409322D091711751040B33C6F814B3E0D91DEB9
lmda2 = 0xac9c52b33fa3cf1f5ad9e3fd77ed9ba4a880b9fc8ec739c2e0cfc810b51283ce
lmda2div =0x564E29599FD1E78FAD6CF1FEBBF6CDD254405CFE47639CE17067E4085A8941E7
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
Ndiv = 0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF5D576E7357A4501DDFE92F46681B20A0

startrange = 0x100000000000000000000000000000000000000000000000000000000000001
stoprange = 0xffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140
randomstart = random.randint(startrange,stoprange)

start = randomstart
stop = random.randint(randomstart,stoprange)

#TEST
#start = 17799667357578236627
#stop = 17799667357578296628

print("Bitflip (0-252) + Parent bit (1-F) + Random hex")

count = 0
total = 0

def data_wallet():
   for flips in range(0,252):
       PVK = int(gmpy2.bit_flip(ranges, flips))
       HEX = hex(PVK)
       #print(HEX)
       PVK2 = range1 + PVK
       HEX2 = hex(PVK2)
       #print(HEX2)
       PVK3 = range2 + PVK
       HEX3 = hex(PVK3)
       #print(HEX3)
       PVK4 = range3 + PVK
       HEX4 = hex(PVK4)
       #print(HEX4)
       PVK5 = range4 + PVK
       HEX5 = hex(PVK5)
       #print(HEX5)
       PVK6 = range5 + PVK
       HEX6 = hex(PVK6)
       #print(HEX6)
       PVK7 = range6 + PVK
       HEX7 = hex(PVK7)
       #print(HEX7)
       PVK8 = range7 + PVK
       HEX8 = hex(PVK8)
       #print(HEX8)
       PVK9 = range8 + PVK
       HEX9 = hex(PVK9)
       #print(HEX9)
       PVK10 = range9 + PVK
       HEX10 = hex(PVK10)
       #print(HEX10)
       PVK11 = rangeA + PVK
       HEX11 = hex(PVK11)
       #print(HEX11)
       PVK12 = rangeB + PVK
       HEX12 = hex(PVK12)
       #print(HEX12)
       PVK13 = rangeC + PVK
       HEX13 = hex(PVK13)
       #print(HEX13)
       PVK14 = rangeD + PVK
       HEX14 = hex(PVK14)
       #print(HEX14)
       PVK15 = rangeE + PVK
       HEX15 = hex(PVK15)
       #print(HEX15)
       PVK16 = rangeF + PVK
       HEX16 = hex(PVK16)
       #print(HEX16)
       PVK17 = (PVK * lmdadiv % N)
       HEX17 = hex(PVK17)
       #print(HEX17)
       PVK18 = (PVK * lmda2div % N)
       HEX18 = hex(PVK18)
       #print(HEX18)
       PVK19 = (Ndiv - PVK)%start
       HEX19 = hex(PVK19)
       #print(HEX19)
       PVK20 = (Ndiv - PVK * lmda % start)
       HEX20 = hex(PVK20)
       #print(HEX20)
       PVK21 = (Ndiv - PVK * lmda2 % start)
       HEX21 = hex(PVK21)
       #print(HEX21)
       PVK22 = (PVK * lmdadiv % N)
       HEX22 = hex(PVK22)
       #print(HEX22)
       PVK23 = (PVK * lmda2div % N)
       HEX23 = hex(PVK23)
       #print(HEX23)
       PVK24 = (PVK * lmda2div % Ndiv)
       HEX24 = hex(PVK24)
       #print(HEX24)
       caddr = ice.privatekey_to_address(0, True, PVK)
       uaddr = ice.privatekey_to_address(0, False, PVK)
       p2sh = ice.privatekey_to_address(1, True, PVK)
       bech = ice.privatekey_to_address(2, True, PVK)
       ethaddr = ice.privatekey_to_ETH_address(PVK)[2:]
       
       caddr2 = ice.privatekey_to_address(0, True, PVK2)
       uaddr2 = ice.privatekey_to_address(0, False, PVK2)
       p2sh2 = ice.privatekey_to_address(1, True, PVK2)
       bech2 = ice.privatekey_to_address(2, True, PVK2)
       ethaddr2 = ice.privatekey_to_ETH_address(PVK2)[2:]
       if caddr2 in bloom1 or uaddr2 in bloom1 or p2sh2 in bloom1 or bech2 in bloom1 or ethaddr2 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX2,'\nCompressed:',caddr2,)
           with open("FLIPPERHEX2.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX2} Compressed:  {caddr2}""")
               f.close
       caddr3 = ice.privatekey_to_address(0, True, PVK3)
       uaddr3 = ice.privatekey_to_address(0, False, PVK3)
       p2sh3 = ice.privatekey_to_address(1, True, PVK3)
       bech3 = ice.privatekey_to_address(2, True, PVK3)
       ethaddr3 = ice.privatekey_to_ETH_address(PVK3)[2:]
       if caddr3 in bloom1 or uaddr3 in bloom1 or p2sh3 in bloom1 or bech3 in bloom1 or ethaddr3 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX3,'\nCompressed:',caddr3,)
           with open("FLIPPERHEX3.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX3} Compressed:  {caddr3}""")
               f.close
       caddr4 = ice.privatekey_to_address(0, True, PVK4)
       uaddr4 = ice.privatekey_to_address(0, False, PVK4)
       p2sh4 = ice.privatekey_to_address(1, True, PVK4)
       bech4 = ice.privatekey_to_address(2, True, PVK4)
       ethaddr4 = ice.privatekey_to_ETH_address(PVK4)[2:]
       if caddr4 in bloom1 or uaddr4 in bloom1 or p2sh4 in bloom1 or bech4 in bloom1 or ethaddr4 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX4,'\nCompressed:',caddr4,)
           with open("FLIPPERHEX4.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX4} Compressed:  {caddr4}""")
               f.close
       caddr5 = ice.privatekey_to_address(0, True, PVK5)
       uaddr5 = ice.privatekey_to_address(0, False, PVK5)
       p2sh5 = ice.privatekey_to_address(1, True, PVK5)
       bech5 = ice.privatekey_to_address(2, True, PVK5)
       ethaddr5 = ice.privatekey_to_ETH_address(PVK5)[2:]
       if caddr5 in bloom1 or uaddr5 in bloom1 or p2sh5 in bloom1 or bech5 in bloom1 or ethaddr5 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX5,'\nCompressed:',caddr5,)
           with open("FLIPPERHEX5.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX5} Compressed:  {caddr5}""")
               f.close
       caddr6 = ice.privatekey_to_address(0, True, PVK6)
       uaddr6 = ice.privatekey_to_address(0, False, PVK6)
       p2sh6 = ice.privatekey_to_address(1, True, PVK6)
       bech6 = ice.privatekey_to_address(2, True, PVK6)
       ethaddr6 = ice.privatekey_to_ETH_address(PVK6)[2:]
       if caddr6 in bloom1 or uaddr6 in bloom1 or p2sh6 in bloom1 or bech6 in bloom1 or ethaddr6 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX6,'\nCompressed:',caddr6,)
           with open("FLIPPERHEX6.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX6} Compressed:  {caddr6}""")
               f.close
       caddr7 = ice.privatekey_to_address(0, True, PVK7)
       uaddr7 = ice.privatekey_to_address(0, False, PVK7)
       p2sh7 = ice.privatekey_to_address(1, True, PVK7)
       bech7 = ice.privatekey_to_address(2, True, PVK7)
       ethaddr7 = ice.privatekey_to_ETH_address(PVK7)[2:]
       if caddr7 in bloom1 or uaddr7 in bloom1 or p2sh7 in bloom1 or bech7 in bloom1 or ethaddr7 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX7,'\nCompressed:',caddr7,)
           with open("FLIPPERHEX7.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX7} Compressed:  {caddr7}""")
               f.close
       caddr8 = ice.privatekey_to_address(0, True, PVK8)
       uaddr8 = ice.privatekey_to_address(0, False, PVK8)
       p2sh8 = ice.privatekey_to_address(1, True, PVK8)
       bech8 = ice.privatekey_to_address(2, True, PVK8)
       ethaddr8 = ice.privatekey_to_ETH_address(PVK8)[2:]
       if caddr8 in bloom1 or uaddr8 in bloom1 or p2sh8 in bloom1 or bech8 in bloom1 or ethaddr8 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX8,'\nCompressed:',caddr8,)
           with open("FLIPPERHEX8.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX8} Compressed:  {caddr8}""")
               f.close
       caddr9 = ice.privatekey_to_address(0, True, PVK9)
       uaddr9 = ice.privatekey_to_address(0, False, PVK9)
       p2sh9 = ice.privatekey_to_address(1, True, PVK9)
       bech9 = ice.privatekey_to_address(2, True, PVK9)
       ethaddr9 = ice.privatekey_to_ETH_address(PVK9)[2:]
       if caddr9 in bloom1 or uaddr9 in bloom1 or p2sh9 in bloom1 or bech9 in bloom1 or ethaddr9 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX9,'\nCompressed:',caddr9,)
           with open("FLIPPERHEX9.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX9} Compressed:  {caddr9}""")
               f.close
       caddr10 = ice.privatekey_to_address(0, True, PVK10)
       uaddr10 = ice.privatekey_to_address(0, False, PVK10)
       p2sh10 = ice.privatekey_to_address(1, True, PVK10)
       bech10 = ice.privatekey_to_address(2, True, PVK10)
       ethaddr10 = ice.privatekey_to_ETH_address(PVK10)[2:]
       if caddr10 in bloom1 or uaddr10 in bloom1 or p2sh10 in bloom1 or bech10 in bloom1 or ethaddr10 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX10,'\nCompressed:',caddr10,)
           with open("FLIPPERHEX10.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX10} Compressed:  {caddr10}""")
               f.close
       caddr11 = ice.privatekey_to_address(0, True, PVK11)
       uaddr11 = ice.privatekey_to_address(0, False, PVK11)
       p2sh11 = ice.privatekey_to_address(1, True, PVK11)
       bech11 = ice.privatekey_to_address(2, True, PVK11)
       ethaddr11 = ice.privatekey_to_ETH_address(PVK11)[2:]
       if caddr11 in bloom1 or uaddr11 in bloom1 or p2sh11 in bloom1 or bech11 in bloom1 or ethaddr11 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX11,'\nCompressed:',caddr11,)
           with open("FLIPPERHEX11.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX11} Compressed:  {caddr11}""")
               f.close
       caddr12 = ice.privatekey_to_address(0, True, PVK12)
       uaddr12 = ice.privatekey_to_address(0, False, PVK12)
       p2sh12 = ice.privatekey_to_address(1, True, PVK12)
       bech12 = ice.privatekey_to_address(2, True, PVK12)
       ethaddr12 = ice.privatekey_to_ETH_address(PVK12)[2:]
       if caddr12 in bloom1 or uaddr12 in bloom1 or p2sh12 in bloom1 or bech12 in bloom1 or ethaddr12 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX12,'\nCompressed:',caddr12,)
           with open("FLIPPERHEX12.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX12} Compressed:  {caddr12}""")
               f.close
       caddr13 = ice.privatekey_to_address(0, True, PVK13)
       uaddr13 = ice.privatekey_to_address(0, False, PVK13)
       p2sh13 = ice.privatekey_to_address(1, True, PVK13)
       bech13 = ice.privatekey_to_address(2, True, PVK13)
       ethaddr13 = ice.privatekey_to_ETH_address(PVK13)[2:]
       if caddr13 in bloom1 or uaddr13 in bloom1 or p2sh13 in bloom1 or bech13 in bloom1 or ethaddr13 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX13,'\nCompressed:',caddr13,)
           with open("FLIPPERHEX13.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX13} Compressed:  {caddr13}""")
               f.close
       caddr14 = ice.privatekey_to_address(0, True, PVK14)
       uaddr14 = ice.privatekey_to_address(0, False, PVK14)
       p2sh14 = ice.privatekey_to_address(1, True, PVK14)
       bech14 = ice.privatekey_to_address(2, True, PVK14)
       ethaddr14 = ice.privatekey_to_ETH_address(PVK14)[2:]
       if caddr14 in bloom1 or uaddr14 in bloom1 or p2sh14 in bloom1 or bech14 in bloom1 or ethaddr14 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX14,'\nCompressed:',caddr14,)
           with open("FLIPPERHEX14.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX14} Compressed:  {caddr14}""")
               f.close
       caddr15 = ice.privatekey_to_address(0, True, PVK15)
       uaddr15 = ice.privatekey_to_address(0, False, PVK15)
       p2sh15 = ice.privatekey_to_address(1, True, PVK15)
       bech15 = ice.privatekey_to_address(2, True, PVK15)
       ethaddr15 = ice.privatekey_to_ETH_address(PVK15)[2:]
       if caddr15 in bloom1 or uaddr15 in bloom1 or p2sh15 in bloom1 or bech15 in bloom1 or ethaddr15 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX15,'\nCompressed:',caddr15,)
           with open("FLIPPERHEX15.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX15} Compressed:  {caddr15}""")
               f.close
       caddr16 = ice.privatekey_to_address(0, True, PVK16)
       uaddr16 = ice.privatekey_to_address(0, False, PVK16)
       p2sh16 = ice.privatekey_to_address(1, True, PVK16)
       bech16 = ice.privatekey_to_address(2, True, PVK16)
       ethaddr16 = ice.privatekey_to_ETH_address(PVK16)[2:]
       if caddr16 in bloom1 or uaddr16 in bloom1 or p2sh16 in bloom1 or bech16 in bloom1 or ethaddr16 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX16,'\nCompressed:',caddr16,)
           with open("FLIPPERHEX16.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX16} Compressed:  {caddr16}""")
               f.close
       caddr17 = ice.privatekey_to_address(0, True, PVK17)
       uaddr17 = ice.privatekey_to_address(0, False, PVK17)
       p2sh17 = ice.privatekey_to_address(1, True, PVK17)
       bech17 = ice.privatekey_to_address(2, True, PVK17)
       ethaddr17 = ice.privatekey_to_ETH_address(PVK17)[2:]
       if caddr17 in bloom1 or uaddr17 in bloom1 or p2sh17 in bloom1 or bech17 in bloom1 or ethaddr17 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX17,'\nCompressed:',caddr17,)
           with open("FLIPPERHEX17.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX17} Compressed:  {caddr17}""")
               f.close
       caddr18 = ice.privatekey_to_address(0, True, PVK18)
       uaddr18 = ice.privatekey_to_address(0, False, PVK18)
       p2sh18 = ice.privatekey_to_address(1, True, PVK18)
       bech18 = ice.privatekey_to_address(2, True, PVK18)
       ethaddr18 = ice.privatekey_to_ETH_address(PVK18)[2:]
       if caddr18 in bloom1 or uaddr18 in bloom1 or p2sh18 in bloom1 or bech18 in bloom1 or ethaddr18 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX18,'\nCompressed:',caddr18,)
           with open("FLIPPERHEX18.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX18} Compressed:  {caddr18}""")
               f.close
       caddr19 = ice.privatekey_to_address(0, True, PVK19)
       uaddr19 = ice.privatekey_to_address(0, False, PVK19)
       p2sh19 = ice.privatekey_to_address(1, True, PVK19)
       bech19 = ice.privatekey_to_address(2, True, PVK19)
       ethaddr19 = ice.privatekey_to_ETH_address(PVK19)[2:]
       if caddr19 in bloom1 or uaddr19 in bloom1 or p2sh19 in bloom1 or bech19 in bloom1 or ethaddr19 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX19,'\nCompressed:',caddr19,)
           with open("FLIPPERHEX19.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX19} Compressed:  {caddr19}""")
               f.close
       caddr20 = ice.privatekey_to_address(0, True, PVK20)
       uaddr20 = ice.privatekey_to_address(0, False, PVK20)
       p2sh20 = ice.privatekey_to_address(1, True, PVK20)
       bech20 = ice.privatekey_to_address(2, True, PVK20)
       ethaddr20 = ice.privatekey_to_ETH_address(PVK20)[2:]
       if caddr20 in bloom1 or uaddr20 in bloom1 or p2sh20 in bloom1 or bech20 in bloom1 or ethaddr20 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX20,'\nCompressed:',caddr20,)
           with open("FLIPPERHEX20.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX20} Compressed:  {caddr20}""")
               f.close
       caddr21 = ice.privatekey_to_address(0, True, PVK21)
       uaddr21 = ice.privatekey_to_address(0, False, PVK21)
       p2sh21 = ice.privatekey_to_address(1, True, PVK21)
       bech21 = ice.privatekey_to_address(2, True, PVK21)
       ethaddr21 = ice.privatekey_to_ETH_address(PVK21)[2:]
       if caddr21 in bloom1 or uaddr21 in bloom1 or p2sh21 in bloom1 or bech21 in bloom1 or ethaddr21 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX21,'\nCompressed:',caddr21,)
           with open("FLIPPERHEX21.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX21} Compressed:  {caddr21}""")
               f.close
       caddr22 = ice.privatekey_to_address(0, True, PVK22)
       uaddr22 = ice.privatekey_to_address(0, False, PVK22)
       p2sh22 = ice.privatekey_to_address(1, True, PVK22)
       bech22 = ice.privatekey_to_address(2, True, PVK22)
       ethaddr22 = ice.privatekey_to_ETH_address(PVK22)[2:]
       if caddr22 in bloom1 or uaddr22 in bloom1 or p2sh22 in bloom1 or bech22 in bloom1 or ethaddr22 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX22,'\nCompressed:',caddr22,)
           with open("FLIPPERHEX22.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX22} Compressed:  {caddr22}""")
               f.close
       caddr23 = ice.privatekey_to_address(0, True, PVK23)
       uaddr23 = ice.privatekey_to_address(0, False, PVK23)
       p2sh23 = ice.privatekey_to_address(1, True, PVK23)
       bech23 = ice.privatekey_to_address(2, True, PVK23)
       ethaddr23 = ice.privatekey_to_ETH_address(PVK23)[2:]
       if caddr23 in bloom1 or uaddr23 in bloom1 or p2sh23 in bloom1 or bech23 in bloom1 or ethaddr23 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX23,'\nCompressed:',caddr23,)
           with open("FLIPPERHEX23.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX23} Compressed:  {caddr23}""")
               f.close
       caddr24 = ice.privatekey_to_address(0, True, PVK24)
       uaddr24 = ice.privatekey_to_address(0, False, PVK24)
       p2sh24 = ice.privatekey_to_address(1, True, PVK24)
       bech24 = ice.privatekey_to_address(2, True, PVK24)
       ethaddr24 = ice.privatekey_to_ETH_address(PVK24)[2:]
       if caddr24 in bloom1 or uaddr24 in bloom1 or p2sh24 in bloom1 or bech24 in bloom1 or ethaddr24 in bloom2:
           print('\n[green] +++ Bingo! +++','\nPVK: ', HEX24,'\nCompressed:',caddr24,)
           with open("FLIPPERHEX24.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX24} Compressed:  {caddr24}""")
               f.close
       data.append({
       'HEX': HEX,
       'caddr': caddr,
       'uaddr': uaddr,
       'p2sh': p2sh,
       'bech': bech,
       'ethaddr': ethaddr,
       })
data = []

for ranges in range(start,stop):
    data = []
    count+=1
    total+=30600
    data_wallet()
    for check in data:
        HEX = check['HEX']
        caddr = check['caddr']
        uaddr = check['uaddr']
        p2sh = check['p2sh']
        bech = check['bech']
        ethaddr = check['ethaddr']
        if caddr in bloom1 or uaddr in bloom1 or p2sh in bloom1 or bech in bloom1 or ethaddr in bloom2:
           print('\nMatch!:','\nPVK: ', HEX,'\nPublic Address Compressed:',caddr,)
           with open("FLIPPER.TXT", "a") as f:
               f.write(f"""\nScan#: {count} PVK: {HEX} Compressed:  {caddr}""")
               f.close
    print('[+] Scan:', count ,'(hex):', HEX, 'Total:',total,end='\r')
    if count > 4096:
       exit()
       #dont forget to run it in a loop trough BAT file
