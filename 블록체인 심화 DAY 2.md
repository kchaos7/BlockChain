# 블록체인 심화 DAY 2



비트코인 블록

bits(목표)

difficulty(난이도)

nonce(넌스)

![1530663705677](C:\Users\Kchaos7\AppData\Local\Temp\1530663705677.png)블록 #530372

해시 [000000000000000000077ec7ba43e088551acf07c92f133b7172a0636724178f](https://www.blockchain.com/btc/block/000000000000000000077ec7ba43e088551acf07c92f133b7172a0636724178f) 

난이도 :	5,363,678,461,481.36 

bits	: 389315112   (가장 중요) 

해시 난수 : 1239298697 

------



### #nBits

- 난이도 구하는 공식에 현재 목표 난이도에 이용
- 해시 난수를 구하는 목표값에 이용



### #난이도

difficulty = difficulty_1_target / current_target

(난이도 = 최고 난이도/현재 난이도)



최고난이도는 상수 고정 (미리 정해져있음)

현재난이도 구함 : Bits를 Hex로 변환

​	

​	첫바이트 + 3바이트로 분할

​	(4byte)



1. bits	: 389315112   계산기 입력

![1530664037835](C:\Users\Kchaos7\AppData\Local\Temp\1530664037835.png)

2. Hex 값 출력

![1530664078266](C:\Users\Kchaos7\AppData\Local\Temp\1530664078266.png)



공식 = Hex값 * { *2** (8*0x17-3)) }

38935112 = hex(17 347A28)

​			0x17  ,  0x347A28

현재난이도 : 0x347A28 *2** (8 * 0x17-3)

​					  =============

​					0을 몇개 채울지

​			0x17-3 = 0x14(20)

​		20*2 = 

0x347A28000000000000000000000000

=> print hex(0x347A28 *2** (8 *0x17-3))

0x68f450000000000000000000000000000000000000000000000L0은 총 40개

---

### #nBits

- 넌스가 찾아야 할 해시 목표값

- PoW(작업 증명)

- 합의 알고리즘 : 넌스 값 찾는 것

  > 합의 : 분산 네트워크에서 서로의 상태를 공유하는 것
  >
  > 즉, 자신이 채굴(블록 생성) 한 상태를 알려주는 것 ! (브로드캐스팅 포함)

- 38935112 - hex(17347A28)

  - 0x17이 목표치의 바이트 수.(0을 얼마나 채울지)
  - 256 비트 
    - 0x17 (23) 23*8 = 184
      - ​			256 - 184 = 72 비트
  - 해시는 64 length
    - 1 length = 4비트
    - 72비트가 0으로 18개 채워짐 즉, 해시 중에 0인 숫자가 18개인 해시값 찾는 것이 Nonce

- 해시 [000000000000000000077ec7ba43e088551acf07c92f133b7172a0636724178f](https://www.blockchain.com/btc/block/000000000000000000077ec7ba43e088551acf07c92f133b7172a0636724178f) 

  - 0이 18개 인 것을 확인 할 수 있다. 

---

### #예제

![1530665468851](C:\Users\Kchaos7\AppData\Local\Temp\1530665468851.png)

| 해시   | [000000000001f657aad04f95503e76a6ee02641deea87721de00d34ad3a9f8e8](https://www.blockchain.com/btc/block/000000000001f657aad04f95503e76a6ee02641deea87721de00d34ad3a9f8e8) |
| ------ | ------------------------------------------------------------ |
| 난이도 | 14,484.16                                                    |
| Bits   | 453281356                                                    |



난이도 = 최고 난이도 / 현재 난이도



최고 난이도 =

0x00000000FFFF...

‬

현재 난이도

453281356 = 1B 04864C

​			0x1B + 0x04864C

현재난이도 = 0x04864C *2** (8 * 0x17-3)

=> print hex(0x04864C*2** (8 * 0x17-3)) 

​		0x90d8000000000000000000000000000000000000000000000L



이걸 최고 난이도/ 현재 난이도 한 값이 앞에 0 개수가 된다. 해당 해시 찾음

---

★정리 : 일단 주어진 Bits를 Hex로 변환 하여 공식대로 분리한뒤 공식을 입혀 계산 나온 값은 현재 난이도 이고, 고정된 상수인 최고 난이도를 현재난이도로 나누게되면 해당 값이 난이도가 됨

---

---

### #Python hash test

```python
import hashlib
import binascii

# 1. Getting header values from blockexplorer.com
version = "20000000" # 2
hashPrevBlock = "00000000000000000060e66690d8a6646b7f8bb4aeb3fa7be258ae4011e362b5"
hashMerkleRoot = "98f0bb94fc154733f22ac54994e9637981900fcee8a0db7d5880b5b79ca3853d"
time = "5A7BEAA4" 
bits = "1761E9F8" 
nonce = 2699712111 # in decimal notation
nonce = hex(int(0x100000000)+nonce)[-8:] 

# 2. Convert them in little-endian hex notation
version = binascii.hexlify(binascii.unhexlify(version)[::-1])
hashPrevBlock = binascii.hexlify(binascii.unhexlify(hashPrevBlock)[::-1])
hashMerkleRoot = binascii.hexlify(binascii.unhexlify(hashMerkleRoot)[::-1])
time = binascii.hexlify(binascii.unhexlify(time)[::-1])
bits = binascii.hexlify(binascii.unhexlify(bits)[::-1])
nonce = binascii.hexlify(binascii.unhexlify(nonce)[::-1])

# 3. Concatenating header values
header = version+hashPrevBlock+hashMerkleRoot+time+bits+nonce

# 4. Taking the double-SHA256 hash value
header = binascii.unhexlify(header)
hash = hashlib.sha256(hashlib.sha256(header).digest()).digest()
hash = binascii.hexlify(hash)

# 5. Converting the hash value in big-endian hex notation
hash = binascii.hexlify(binascii.unhexlify(hash)[::-1])
print  hash

```

> python FILENAME.py

user01@ubuntu:~$ vi hash.py
user01@ubuntu:~$ python hash.py
000000000000000000081759445e2a44cb808c2b5e144c41d5d24d8fe7149269



---

## #해시함수

### #SHA (Secure Hash Algorithm)

### [SHA Test](www.sha1-online.com)

![1530670941127](C:\Users\Kchaos7\AppData\Local\Temp\1530670941127.png)![1530671006230](C:\Users\Kchaos7\AppData\Local\Temp\1530671006230.png)

> Hello와 Hello. 은 완전히 다른 것



---

# #해시검증

- PrevBlock(이전해시)

- Merkle Root(머클루트해시)

- TimeStamp(타임 스탬프, 변환 필요)  

- Bits(변환 필요) 

- Nonce (해시 난수)

  > 이 값들을 통해 해당 블록의 해시 검증 가능.



### #예제. 508217 블록 해시 검증

```python
/* FILENAME 508217.py*/
import hashlib
import binascii

# 1. Getting header values from blockexplorer.com
version = "20000000" # 2
hashPrevBlock = "00000000000000000060e66690d8a6646b7f8bb4aeb3fa7be258ae4011e362b5"
hashMerkleRoot = "98f0bb94fc154733f22ac54994e9637981900fcee8a0db7d5880b5b79ca3853d"
time = "5A7BEAA4"
bits = "1761E9F8"
nonce = 2699712111 # in decimal notation
nonce = hex(int(0x100000000)+nonce)[-8:]

# 2. Convert them in little-endian hex notation
version = binascii.hexlify(binascii.unhexlify(version)[::-1])
hashPrevBlock = binascii.hexlify(binascii.unhexlify(hashPrevBlock)[::-1])
hashMerkleRoot = binascii.hexlify(binascii.unhexlify(hashMerkleRoot)[::-1])
time = binascii.hexlify(binascii.unhexlify(time)[::-1])
bits = binascii.hexlify(binascii.unhexlify(bits)[::-1])
nonce = binascii.hexlify(binascii.unhexlify(nonce)[::-1])

# 3. Concatenating header values
header = version+hashPrevBlock+hashMerkleRoot+time+bits+nonce

# 4. Taking the double-SHA256 hash value
header = binascii.unhexlify(header)
hash = hashlib.sha256(hashlib.sha256(header).digest()).digest()
hash = binascii.hexlify(hash)

# 5. Converting the hash value in big-endian hex notation
hash = binascii.hexlify(binascii.unhexlify(hash)[::-1])
print  hash

```



1. 이전 해시(hashPrevBlock),  머클 루트 해시(hashMerkleRoot) 입력.

#### [#블록 508217](https://www.blockchain.com/btc/block/000000000000000000081759445e2a44cb808c2b5e144c41d5d24d8fe7149269)

![1530680429929](C:\Users\Kchaos7\AppData\Local\Temp\1530680429929.png)



2.시간(time)을  http://www.4webhelp.net/us/timestamp.php 홈페이지에 입력시켜 변환시키고,

 그 값을 계산기를 통해  Hex로 변환. (※Time zone : GMT)

ex) #508217 Block's time = 2018-02-08 06:13:56 

2018-02-08 06:13:56  >> 1518070436 >> 5A7BEAA4

![1530680273725](C:\Users\Kchaos7\AppData\Local\Temp\1530680273725.png)



3. Bits를 계산기로 Hex 변환.

   ![1530681204392](C:\Users\Kchaos7\AppData\Local\Temp\1530681204392.png)

   > #508217 블록 Bits = 392292856  >>변환>> Hex = 1761E9F8

   ​			

4. Nonce 입력.

   

5. 수정 및 저장 후, "python 508217.py" 로 컴파일 시켜 해시 검증.



- ### 결과

  ```
  user01@ubuntu:~$ python 508217.py
  000000000000000000081759445e2a44cb808c2b5e144c41d5d24d8fe7149269
  ```

![1530682728231](C:\Users\Kchaos7\AppData\Local\Temp\1530682728231.png)



- ### 요약

  ```
  hashPrevBlock = "00000000000000000060e66690d8a6646b7f8bb4aeb3fa7be258ae4011e362b5"
  hashMerkleRoot = "98f0bb94fc154733f22ac54994e9637981900fcee8a0db7d5880b5b79ca3853d"
  time = "5A7BEAA4"
  bits = "1761E9F8"
  nonce = 2699712111 # in decimal notation
  ```

  > 총 5개의 블록 헤더를 수정하면 된다.(version은 그대로 유지)
  >
  > 이 때, time 과 bits는 변환이 필요.
  >
  > 최종적으로 해당 블록의 해시를 확인 가능.

---

---

# #이더리움

----

----

### #MetaMask 설치



[MetaMask 홈페이지](https://metamask.io)

![1530683229049](C:\Users\Kchaos7\AppData\Local\Temp\1530683229049.png)

1. GET CHROME EXTENSION 클릭

2. ADD TO CHROME 클릭 후 설치![1530683341641](C:\Users\Kchaos7\AppData\Local\Temp\1530683341641.png)

3. 8자 이상 안전한 패스워드 입력, 12개의 단어가 생성되는데 지갑의 Privte Key를 의미하고 매우 중요한 비밀키 이므로 자신만 볼 수 있는 곳에 따로 저장.

   

   ---

   

### #이더리움  클라이언트 - Private 네트워크 구축



- #### genesis.json 생성

  ##### timestamp는 홀수 자리면 오류 가능성이 있어 짝수 자리로 변경해야함.	ex) 0x0 >> 0x00

- ```
  user01@ubuntu:~$ mkdir data_testnet
  
  user01@ubuntu:~$ cd data_testnet/
  
  user01@ubuntu:~/data_testnet$ vi genesis.json
  /*genesis.json*/
  {
  
    "config": {
  
      "chainId": 33,
  
      "homesteadBlock": 0,
  
      "eip155Block": 0,
  
      "eip158Block": 0
  
    },
  
    "nonce": "0x0000000000000033",
  
    "timestamp": "0x00",				
  
    "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  
    "gasLimit": "0x8000000",
  
    "difficulty": "0x100",
  
    "mixhash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  
    "coinbase": "0x3333333333333333333333333333333333333333",
  
    "alloc": {}
  
  }
  
  ```

  #### Geth 초기화 및 실행 

  - init 양 옆 공백 필수, 초기화 하는 용도(initializing).

  ```
  user01@ubuntu:~/data_testnet$ geth --datadir /home/user01/data_testnet/ init /home/user01/data_testnet/genesis.json
  
  INFO [05-01|23:42:46] Maximum peer count                       ETH=25 LES=0 total=25
  
  INFO [05-01|23:42:46] Allocated cache and file handles         database=/home/user01/data_testnet/geth/chaindata cache=16 handles=16
  
  .... 생략 ....
  
  INFO [05-01|23:42:46] Successfully wrote genesis state         database=lightchaindata                                hash=5704d0â€¦9bc5b0
  
  
  user01@ubuntu:~/data_testnet$ sudo apt install tree
  
  [sudo] password for user01:
  Reading package lists... Done
  Building dependency tree
  Reading state information... Done
  The following NEW packages will be installed:
    tree
  0 upgraded, 1 newly installed, 0 to remove and 27 not upgraded.
  Need to get 40.6 kB of archives.
  After this operation, 138 kB of additional disk space will be used.
  Get:1 http://kr.archive.ubuntu.com/ubuntu xenial/universe amd64 tree amd64 1.7.0-3 [40.6 kB]
  Fetched 40.6 kB in 13s (3,069 B/s)
  Selecting previously unselected package tree.
  (Reading database ... 77569 files and directories currently installed.)
  Preparing to unpack .../tree_1.7.0-3_amd64.deb ...
  Unpacking tree (1.7.0-3) ...
  Processing triggers for man-db (2.7.5-1) ...
  Setting up tree (1.7.0-3) ...
  
  user01@ubuntu:~/data_testnet$ cd ..
  user01@ubuntu:~$ tree data_testnet/
  data_testnet/
  ├── genesis.json
  ├── geth
  │   ├── chaindata
  │   │   ├── 000025.log
  │   │   ├── 000027.ldb
  │   │   ├── CURRENT
  │   │   ├── LOCK
  │   │   ├── LOG
  │   │   └── MANIFEST-000026
  │   ├── lightchaindata
  │   │   ├── 000001.log
  │   │   ├── CURRENT
  │   │   ├── LOCK
  │   │   ├── LOG
  │   │   └── MANIFEST-000000
  │   ├── LOCK
  │   ├── nodekey
  │   └── transactions.rlp
  ├── geth.ipc
  ├── geth.log
  ├── history
  └── keystore
      ├── UTC--2018-07-04T07-48-06.832386759Z--0dce71b0c1691d968d3f4d9263403b11942d2cb3
      ├── UTC--2018-07-04T07-49-23.431109235Z--387ad5ccb8617644d6296b41c47a9d7bc933df3f
      ├── UTC--2018-07-04T08-04-41.580582966Z--4ec79af968bf96232235b2483da7d70a338f26e8
      └── UTC--2018-07-04T08-04-57.865834939Z--dd96da6502e78d1fcf20a99b846d007c03489df9
  
  4 directories, 22 files
  ```

  > 참고 : 삭제 ( rm -rf FILENAME .json), 
  >
  > 일반 파일의 경우 rm FILENAME, 
  >
  > 디렉터리 인 경우 rm -r DIRECTORY_NAME , 
  >
  > json 파일 소스 읽으려면 위해 WordPad or Visual Studio 이용

# 

## #Geth

#### #Geth 실행

```
 user01@ubuntu:~$ nohup geth --networkid 4689 --nodiscover --datadir /home/user01/data_testnet --mine --minerthreads 1 --rpc  --rpcaddr "0.0.0.0" --rpcport 8545  --rpccorsdomain "*" --rpcapi "admin,db,eth,miner,net,personal,web3" --verbosity 6 2>> /home/user01/data_testnet/geth.log &
```

- nohup 방식은 shell 꺼져도 계속 돌아가게 함.
- nohup : no hang up : 종료되지 않고 계속 실행
           

```
user01@ubuntu:~$ geth --identity "PrivateNetwork" --datadir "/home/user01/data_testnet/" --port "30303" --rpc --rpcaddr 0.0.0.0 --rpcport "8123" --rpccorsdomain "*" --nodiscover --networkid 1900 --nat "any" --rpcapi "db,eth,net,we,miner" console 2>> /home/user01/data_testnet/geth.log

Welcome to the Geth JavaScript console!

instance: Geth/PrivateNetwork/v1.8.2-stable-b8b9f7f4/linux-amd64/go1.9.4

 modules: admin:1.0 debug:1.0 eth:1.0 miner:1.0 net:1.0 personal:1.0 rpc:1.0 txpool:1.0 web3:1.0
> personal.newAccount("pass0")
"0x0dce71b0c1691d968d3f4d9263403b11942d2cb3"

> eth.accounts
["0x0dce71b0c1691d968d3f4d9263403b11942d2cb3"]

> personal.newAccount("pass1")
"0x387ad5ccb8617644d6296b41c47a9d7bc933df3f"

> eth.accounts
["0x0dce71b0c1691d968d3f4d9263403b11942d2cb3", "0x387ad5ccb8617644d6296b41c47a9d7bc933df3f"]

> eth.getBalance(eth.accounts[0])	//잔고확인 - 배열로 확인
0

> eth.getBalance(eth.coinbase)	//잔고확인 - coinbase 변수로 확인 - wei로 출력.
0



```

- 일반 콘솔 방식(교재)

---



##### #Geth 실행 옵션

![1530697506071](C:\Users\Kchaos7\AppData\Local\Temp\1530697506071.png)

- --rpc : RPC 인터페이스를 실행.
- --rpcPort "8485" : RPC 포트.(default : 8485)
- --rpccorsdomain "*" : 접속 가능한 RPC 클라이언트 지정.
  - "*"  : 모든 클라이언트 접속 허용보다 URL을 지정하는 것이 좋음.
- --datadir : 사용자 데이터 디렉토리 지정.
- --port"30303" : 네트워크 리스닝 포트 지정.(default : 30303)
- --nodiscover : 같은 제너시스 블록과 네트워크 ID에 있는 블록에 대한 연결 방지.
- --rpcapi "db,eth,net,web3" : RPC에 의해서 접근을 허락할 API 요소
- --networkid 15 : 1-Fronier, 2-Modern(disused), 3-Ropsten, 4-Rinkeby (default : 1)
- console : 출력을 콘솔로 지정.
- --dev : 개발자 네트워크 접속.

---

##### #verbosity

--verbosity 0 : silent

--verbosity 1 : error 

--verbosity 2 : warn

--verbosity 3 : info(default)

--verbosity 4 : core

--verbosity 5 : debug

--verbosity 6 : detail, 출력 수준 지정 명령어

---

##### #프로세스 번호 확인

```
	ps  -eaf | grep geth
```

##### #kill

    	kill -9 프로세스번호

---

#### #Solidity

![1530688182482](C:\Users\Kchaos7\AppData\Local\Temp\1530688182482.png)

- 상단 Account 주소는 진짜 주소.
- Deploy를 클릭했을 때 나타나는, Ballot 주소는  Smart Contract 주소(계약서만 실행 가능한 주소), 이 주소를 통해 돈을 받고 계약을 체결함.
- 즉, 진짜 주소와 계약서 주소 2개가 생성됨.

---

#### #채굴

- Private 네트워크는 기본적으로 채굴 기능 비 활성화.
- Geth 실행 시 --mining 옵션 추가 or 자바스크립트 콘솔 환경모드에서 실시간 활성화.
- miner.start(thread_num) : thread_num은 채굴 시 사용할 스레드 수 (default : "()")
- miner는 --rpcapi  옵션에 추가한 모듈 중 하나임.



#### #miner.start()

> miner.start()
> null

#### #miner.stop()

> miner.stop()
> true

#### #Check Mining

> eth.mining
> true/false

#### #Check Hash Rate(velosity)

> eth.hashrate
> 0

#### #Check Block Number

> eth.blockNumber
> 1297

---

### #Attach

- 기존 중요한 서버 자료의 변형을 막기위해, 작업용 서버를 붙혀줌.

- 즉, 처음 Root 서버는 그대로 두고, Attach를 통해 붙은 서버로 수정 및 관리하면 안정성 향상

  ```
  user01@ubuntu:~$ geth attach http://10.0.2.15:8123
  Welcome to the Geth JavaScript console!
  
   modules: eth:1.0 miner:1.0 net:1.0 rpc:1.0
  
  > miner.start()
  null
  > eth.getBalance(eth.coinbase)
  565000000000000000000
  
  ```

  - http:// 10.0.2.15:***8123***

    geth --identity "PrivateNetwork" --datadir "/home/user01/data_testnet/" --port "30303" --rpc --rpcaddr 0.0.0.0 ***--rpcport "8123"*** --rpccorsdomain "*" --nodiscover --networkid 1900 --nat "any" --rpcapi "db,eth,net,we,miner" console 2>> /home/user01/data_testnet/geth.log

    - "8123"은 geth 실행시 입력한 Port 번호를 의미.

    ![1530700328973](C:\Users\Kchaos7\AppData\Local\Temp\1530700328973.png![1530700354119](C:\Users\Kchaos7\AppData\Local\Temp\1530700354119.png)

---

### #20190704.txt

```
계산기 실행
메모장 실행
VirtualBox - Bitcoin 실행 - Putty접속

* 비트코인 블록
bits(목표)
difficulty(난이도)
nonce(넌스)


https://www.blockchain.com/

블록 #530372
000000000000000000077ec7ba43e088551acf07c92f133b7172a0636724178f

난이도	   5,363,678,461,481.36
Bits	   389315112
해시 난수  1239298697


1)nBits
- 난이도를 구하는 공식에 현재 목표 난이도에 이용
- 해시 난수를 구하는 목표값에 이용

난이도:
 difficulty = difficulty_1_target / current_target
   (난이도 = 최고난이도/현재 난이도)

 최고난이도 : 상수 고정
0x00000000FFFF0000000000000000000000000000000000000000000000000000

현재난이도 구함: Bits를 Hex로 변환
                 4byte
                  첫바이트+3바이트로 분리

  389315112 - hex(17347A28)
               0x17 , 0x347A28
  현재난이도: 0x347A28*2**(8*(0x17-3)
                       --------------
                       0를 몇개 채울지.
                        0x17-3  =0x14(20)
                       20*2 =                     40개 0으로 채우짐
          0x347A28000000000000000000000000
          

  >>>print hex(0x347A28*2**(8*(0x17-3)))

0x347a280000000000000000000000000000000000000000L





0x00000000FFFF0000000000000000000000000000000000000000000000000000/0x347a280000000000000000000000000000000000000000


2)nBits
 - 넌스가 찾아야 할 해시 목표값
 - PoW(작업증명)

  합의 알고리즘 - 넌스 값 찾는 것
 =>분산네트워크에서 서로 상태를 공유하는 것
 =>자신이 채굴(블록) 생성한 상태를 알려주는 것

  389315112 - hex(17347A28)

  0x17이 목표치의 바이트 수.

  256비트
  0x17 (23) 23*8=184
                 256-184 = 72비트
  해시는 64 length
         1 - length : 4비트
         72비트가 0으로 18개 숫자가 0으로 시작되는
         해쉬값을 찾는게 넌스



                

블록 #99997
해시	000000000001f657aad04f95503e76a6ee02641deea87721de00d34ad3a9f8e8
난이도	14,484.16
Bits	453281356


난이도 = 최고난이도/현재 난이도)

최고난이도=
0x00000000FFFF0000000000000000000000000000000000000000000000000000/0x347a280000000000000000000000000000000000000000

현재난이도
453281356 - 1B04864C
            0x1B  +  0x04864C
 >>>print hex(0x04864C*2**(8*(0x1B-3)))

             (0x1B-3)
  


블록 #150000
해시	0000000000000a3290f20e75860d505ce0e948a1d1d846bec7e39015d242884b
난이도	1,468,195.43

Bits	436956491

1) 난이도 구하기
난이도 = 최고난이도/현재 난이도
 
 현재난이도 = nBits - Hex변환
                    - 1byte + 3byte분리
                    
                    1byte가 0으로 채워질 숫자

                    1A0B6D4B
            0x1A   0x0B6D4B

           0x0B6D4B*2**(8*(1A-3))

 










17 347A28

000000000000000000 0
77ec7ba43e088551acf07c92f133b7172a0636724178f



https://bitnodes.earn.com/


* ethereum private network 구축

1) geth 실행
- 로그아웃 이후에도 계속 백그라운드로 실행

 nohup : no hang up : 종료되지 않고 계속 실행

 
 nohup geth --networkid 4689 --nodiscover --datadir /home/user01/data_testnet --mine --minerthreads 1 --rpc  --rpcaddr "0.0.0.0" --rpcport 8545  --rpccorsdomain "*" --rpcapi "admin,db,eth,miner,net,personal,web3" --verbosity 6  2>> /home/user01/data_testnet/geth.log &

 nohup : no hang up : 종료되지 않고 계속 실행
         동작중인 geth를 kill할려면
       콘솔  ps -eaf | grep geth    
             프로세스 번호 확인

       kill -9 프로세스번호


> personal.newAccount("pass0")
"0x11d2ad6da9c07edf5c106f4995aa81a2aec9a550"
> personal.newAccount("pass1")
"0xb33bb32c90cf7c7e1370d1c3b6b8c823278e1885"


 0x692a70d2e424a56d2c6c27aa97d1a86395877b3a


--verbosity 6 : 로그 출력 수준 지정하는 명령어
            0 : silent
            1 : error
            2 : warn
            3 : info (default)
            4 : core
            5 : debug
            6 : detail
        
```

