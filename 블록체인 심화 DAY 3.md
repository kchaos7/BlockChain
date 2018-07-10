# 블록체인 심화 DAY 3



### #Ethereum Private Network 구축

- IP 확인

  - ifconfig -a

    - enp0s3	10.0.2.15

      ```
      user01@ubuntu:~$ ifconfig -a
      enp0s3    Link encap:Ethernet  HWaddr 08:00:27:de:84:b5
                inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
                inet6 addr: fe80::a00:27ff:fede:84b5/64 Scope:Link
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:187599 errors:0 dropped:0 overruns:0 frame:0
                TX packets:25161 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:1000
                RX bytes:247507490 (247.5 MB)  TX bytes:2226801 (2.2 MB)
      
      lo        Link encap:Local Loopback
                inet addr:127.0.0.1  Mask:255.0.0.0
                inet6 addr: ::1/128 Scope:Host
                UP LOOPBACK RUNNING  MTU:65536  Metric:1
                RX packets:160 errors:0 dropped:0 overruns:0 frame:0
                TX packets:160 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:1
                RX bytes:11840 (11.8 KB)  TX bytes:11840 (11.8 KB)
      
      ```

- Desktop IP 확인

  - cmd > ipconfig

    

무선 LAN 어댑터 Wi-Fi:

   연결별 DNS 접미사. . . . :
   링크-로컬 IPv6 주소 . . . . : fe80::11ba:d0:3908:58e6%11
   IPv4 주소 . . . . . . . . . : 172.17.144.122
   서브넷 마스크 . . . . . . . : 255.255.0.0
   기본 게이트웨이 . . . . . . : 172.17.0.1

- 네트워크 설정
  - ![1530750712472](C:\Users\Kchaos7\AppData\Local\Temp\1530750712472.png)
- Desktop 방화벽 해제

![1530750768183](C:\Users\Kchaos7\AppData\Local\Temp\1530750768183.png)

- Ethereum VM - IP추가 작업

  - putty 연결

    - ifconfig -a (추가된 랜 카드 확인 - enp0s8)

    enp0s8    Link encap:Ethernet  HWaddr 08:00:27:1e:31:b5
              BROADCAST MULTICAST  MTU:1500  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

    

    

    sudo ifconfig enp0s8 ip netmask 255.255.255.0 up

    ​	자신의 Ip 끝자리 + 100

    IPv4 주소 . . . . . . . . . : 172.17.144.122 

     IPv4 주소+100 . . . . . . . . . : 172.17.144.222

    ex)sudo ifconfig enp0s8 172.17.144.222

  - 254 넘어가면 안됨

  ```
    4) Ethereum VM  - IP추가 작업
     - putty 연결
      ifcofig -a   (추가된 랜카드 확인 - enp0s8 )
  
  sudo ifconfig enp0s8 ip netmask 255.255.255.0 up
  
        자신의 Desktop ip + 100 = max(254)
  
  sudo ifconfig enp0s8 192.168.0.205 netmask 255.255.255.0 up	#중간에 자신 IP+100
  
  sudo route add  default gw 192.168.0.1 #자신 게이트번호
  ping 192.168.0.x #상대방 Ip + 100
  ```

   

- login as: user01
  user01@127.0.0.1's password:
  Welcome to Ubuntu 16.04.4 LTS (GNU/Linux 4.4.0-116-generic x86_64)

   * Documentation:  https://help.ubuntu.com
   * Management:     https://landscape.canonical.com
   * Support:        https://ubuntu.com/advantage

  31 packages can be updated.
  12 updates are security updates.


  Last login: Tue May  1 23:28:07 2018 from 10.0.2.2
  ipuser01@ubuntu:~$ ipcofig -a
  ifipcofig: command not found
  user01@ubuntu:~$ ifconfig -a
  enp0s3    Link encap:Ethernet  HWaddr 08:00:27:de:84:b5
            inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
            inet6 addr: fe80::a00:27ff:fede:84b5/64 Scope:Link
            UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
            RX packets:414 errors:0 dropped:0 overruns:0 frame:0
            TX packets:166 errors:0 dropped:0 overruns:0 carrier:0
            collisions:0 txqueuelen:1000
            RX bytes:325287 (325.2 KB)  TX bytes:18862 (18.8 KB)

  enp0s8    Link encap:Ethernet  HWaddr 08:00:27:1e:31:b5
            BROADCAST MULTICAST  MTU:1500  Metric:1
            RX packets:0 errors:0 dropped:0 overruns:0 frame:0
            TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
            collisions:0 txqueuelen:1000
            RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

  lo        Link encap:Local Loopback
            inet addr:127.0.0.1  Mask:255.0.0.0
            inet6 addr: ::1/128 Scope:Host
            UP LOOPBACK RUNNING  MTU:65536  Metric:1
            RX packets:160 errors:0 dropped:0 overruns:0 frame:0
            TX packets:160 errors:0 dropped:0 overruns:0 carrier:0
            collisions:0 txqueuelen:1
            RX bytes:11840 (11.8 KB)  TX bytes:11840 (11.8 KB)

  user01@ubuntu:~$ ^C
  user01@ubuntu:~$ sudo ifconfig enp0s8 ip netmask 255.255.255.0 up
  [sudo] password for user01:
  ip: Unknown host
  ifconfig: `--help' gives usage information.
  user01@ubuntu:~$ sudo ifconfig enp0s8 ip netmask 255.255.255.0 up
  ip: Unknown host
  ifconfig: `--help' gives usage information.
  user01@ubuntu:~$ sudo ifconfig enp0s8 ip netmask 255.255.255.0 up
  ip: Unknown host
  ifconfig: `--help' gives usage information.
  user01@ubuntu:~$ sudo ifconfig enp0s8 ip netmask 255.255.0.0 up
  ip: Unknown host
  ifconfig: `--help' gives usage information.
  user01@ubuntu:~$ sudo ifconfig enp0s8 ip netmask 255.255.255.0 up
  ip: Unknown host
  ifconfig: `--help' gives usage information.
  user01@ubuntu:~$ sudo ifconfig enp0s8 172.17.144.222 netmask 255.255.255.0 up
  user01@ubuntu:~$ sudo route add  default gw 172.17.0.1
  SIOCADDRT: Network is unreachable
  user01@ubuntu:~$ ping 172.17.144.201
  PING 172.17.144.201 (172.17.144.201) 56(84) bytes of data.
  64 bytes from 172.17.144.201: icmp_seq=1 ttl=64 time=15.1 ms
  64 bytes from 172.17.144.201: icmp_seq=2 ttl=64 time=16.1 ms
  64 bytes from 172.17.144.201: icmp_seq=3 ttl=64 time=10.9 ms
  64 bytes from 172.17.144.201: icmp_seq=4 ttl=64 time=5.44 ms
  64 bytes from 172.17.144.201: icmp_seq=5 ttl=64 time=5.54 ms
  64 bytes from 172.17.144.201: icmp_seq=6 ttl=64 time=16.5 ms
  64 bytes from 172.17.144.201: icmp_seq=7 ttl=64 time=4.16 ms
  64 bytes from 172.17.144.201: icmp_seq=8 ttl=64 time=9.42 ms
  64 bytes from 172.17.144.201: icmp_seq=9 ttl=64 time=6.53 ms
  64 bytes from 172.17.144.201: icmp_seq=10 ttl=64 time=8.88 ms
  64 bytes from 172.17.144.201: icmp_seq=11 ttl=64 time=9.87 ms
  64 bytes from 172.17.144.201: icmp_seq=12 ttl=64 time=6.58 ms
  64 bytes from 172.17.144.201: icmp_seq=13 ttl=64 time=7.23 ms
  64 bytes from 172.17.144.201: icmp_seq=14 ttl=64 time=5.34 ms
  64 bytes from 172.17.144.201: icmp_seq=15 ttl=64 time=14.0 ms
  64 bytes from 172.17.144.201: icmp_seq=16 ttl=64 time=5.01 ms
  64 bytes from 172.17.144.201: icmp_seq=17 ttl=64 time=4.86 ms
  64 bytes from 172.17.144.201: icmp_seq=18 ttl=64 time=4.93 ms
  64 bytes from 172.17.144.201: icmp_seq=19 ttl=64 time=5.78 ms
  64 bytes from 172.17.144.201: icmp_seq=20 ttl=64 time=8.26 ms
  64 bytes from 172.17.144.201: icmp_seq=21 ttl=64 time=6.54 ms
  ^[64 bytes from 172.17.144.201: icmp_seq=22 ttl=64 time=5.77 ms
  ^C
  --- 172.17.144.201 ping statistics ---



- geth 실행

  - rpcaddr 0.0.0.0 rpcport 8545
  - ps -eaf | grep geth
  - Peer 연결 조건
    - genesis 블록이 같아야 함
    - networkid 가 같아야 함

  ```
  nohup geth --networkid 4689 --nodiscover --datadir /home/user01/data_testnet --rpc  --rpcaddr "0.0.0.0" --rpcport 8545  --rpccorsdomain "*" --rpcapi "admin,db,eth,miner,net,personal,web3" --verbosity 6  2>> /home/user01/data_testnet/geth.log &
  결과 >> [1] 1289
  cd data_
  ```



main shell

```
login as: user01
user01@127.0.0.1's password:
Welcome to Ubuntu 16.04.4 LTS (GNU/Linux 4.4.0-116-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

31 packages can be updated.
12 updates are security updates.


Last login: Thu Jul  5 09:49:34 2018

user01@ubuntu:~/data_testnet$ nohup geth --networkid 4689 --nodiscover --datadir /home/user01/data_testnet --rpc  --rpcaddr "0.0.0.0" --rpcport 8545  --rpccorsdomain "*" --rpcapi "admin,db,eth,miner,net,personal,web3" --verbosity 6  2>> /home/user01/data_testnet/geth.log &
[1] 17900
user01@ubuntu:~/data_testnet$ ps -eaf | grep geth
user01   17883 17792  0 10:10 pts/2    00:00:00 geth attach rpc:http://172.17.144.222:8123
user01   17900 17697 11 10:17 pts/1    00:00:00 geth --networkid 4689 --nodiscover --datadir /home/user01/data_testnet --rpc --rpcaddr 0.0.0.0 --rpcport 8545 --rpccorsdomain * --rpcapi admin,db,eth,miner,net,personal,web3 --verbosity 6
user01   17909 17697  0 10:17 pts/1    00:00:00 grep --color=auto geth
```

attach shell

```
user01@ubuntu:~$ geth attach rpc:http://172.17.144.222:8545
Welcome to the Geth JavaScript console!

instance: Geth/v1.8.2-stable-b8b9f7f4/linux-amd64/go1.9.4
coinbase: 0x718ffe1ff6f5e9c49a4aeb78e484ab441c1f4165
at block: 0 (Thu, 01 Jan 1970 09:00:00 JST)
 datadir: /home/user01/data_testnet
 modules: admin:1.0 eth:1.0 miner:1.0 net:1.0 personal:1.0 rpc:1.0 web3:1.0

> admin.nodeInfo
{
  enode: "enode://1d993e894ca1311241e46b481b6d6b24e04c7564e8e4d01549fc18ad377df18309d698f5dcd4d3e926a269ab433861c0c3865d1d88c83b7ba3e926606ecdf7c8@[::]:30303?discport=0",
  id: "1d993e894ca1311241e46b481b6d6b24e04c7564e8e4d01549fc18ad377df18309d698f5dcd4d3e926a269ab433861c0c3865d1d88c83b7ba3e926606ecdf7c8",
  ip: "::",
  listenAddr: "[::]:30303",
  name: "Geth/v1.8.2-stable-b8b9f7f4/linux-amd64/go1.9.4",
  ports: {
    discovery: 0,
    listener: 30303
  },
  protocols: {
    eth: {
      config: {
        chainId: 33,
        eip150Hash: "0x0000000000000000000000000000000000000000000000000000000000000000",
        eip155Block: 0,
        eip158Block: 0,
        homesteadBlock: 0
      },
      difficulty: 256,
      genesis: "0x5704d029fe80f4fb605c0cb5e31d591511f10a46a0cb8166f97d8d559f9bc5b0",
      head: "0x5704d029fe80f4fb605c0cb5e31d591511f10a46a0cb8166f97d8d559f9bc5b0",
      network: 4689
    }
  }
}
> admin.addPeer("enode://24c2599c54bd71944506f5e55a2f03fd5fb01cd9884c30b532fd40193da734e14329b9525b613b572e9162d5ddc52bfce56e0345ddb37cbdd673c21be37f9e78@172.17.144.201:30303?discport=0")
true
> net.peerCount
1
> admin.peers
[{
    caps: ["eth/63"],
    id: "24c2599c54bd71944506f5e55a2f03fd5fb01cd9884c30b532fd40193da734e14329b9525b613b572e9162d5ddc52bfce56e0345ddb37cbdd673c21be37f9e78",
    name: "Geth/v1.8.2-stable-b8b9f7f4/linux-amd64/go1.9.4",
    network: {
      inbound: false,
      localAddress: "172.17.144.222:59154",
      remoteAddress: "172.17.144.201:30303",
      static: true,
      trusted: false
    },
    protocols: {
      eth: {
        difficulty: 37964535,
        head: "0xeded843107b7eb6976986af64a7a157b91aca79a3d31857278fe06a73eb64db9",
        version: 63
      }
    }
}]
>

```



http://remix.ethereum.org/#optimize=false&version=soljson-v0.4.24+commit.e67f0147.js

에서 http 로 변경

run > web3 Provider > IP+100주소:8545 입력

---



```
user01@ubuntu:~/data_testnet$ cd ..
user01@ubuntu:~$ ls
data_testnet  go  my_ethereum  nohup.out
user01@ubuntu:~$ clear
user01@ubuntu:~$ ls -al
total 60
drwxr-xr-x 8 user01 user01 4096 Jul  5 10:04 .
drwxr-xr-x 3 root   root   4096 Apr 14 15:26 ..
-rw------- 1 user01 user01 2734 Jul  5 10:17 .bash_history
-rw-r--r-- 1 user01 user01  220 Apr 14 15:26 .bash_logout
-rw-r--r-- 1 user01 user01 3771 Apr 14 15:26 .bashrc
drwx------ 2 user01 user01 4096 Apr 14 15:27 .cache
drwxrwxr-x 4 user01 user01 4096 Jul  5 10:17 data_testnet
drwxr-xr-x 2 user01 user01 4096 Jul  5 10:59 .ethash
drwx------ 2 user01 user01 4096 Jul  5 10:10 .ethereum
drwxrwxr-x 3 user01 user01 4096 Apr 14 22:50 go
drwxrwxr-x 2 user01 user01 4096 May  1 23:25 my_ethereum
-rw------- 1 user01 user01  167 Jul  5 09:58 nohup.out
-rw-r--r-- 1 user01 user01  655 Apr 14 15:26 .profile
-rw-r--r-- 1 user01 user01    0 Apr 14 15:28 .sudo_as_admin_successful
-rw------- 1 user01 user01 4427 Jul  5 09:57 .viminfo
user01@ubuntu:~$ cd .ethash
user01@ubuntu:~/.ethash$ ls -al
total 1985588
drwxr-xr-x 2 user01 user01       4096 Jul  5 10:59 .
drwxr-xr-x 8 user01 user01       4096 Jul  5 10:04 ..
-rw-rw-r-- 1 user01 user01 1073739912 Jul  5 10:06 full-R23-0000000000000000
-rw-rw-r-- 1 user01 user01 1082130312 Jul  5 11:06 full-R23-290decd9548b62a8.6129484611666145821
-rw-rw-r-- 1 user01 user01 1082130312 Jul  5 10:17 full-R23-290decd9548b62a8.8674665223082153551
user01@ubuntu:~/.ethash$ cd ..
user01@ubuntu:~$ cd data_testnet/
user01@ubuntu:~/data_testnet$ tail -f geth.log
DEBUG[07-05|11:06:29] Skeleton fill terminated                 err="block header download canceled (requested)"
DEBUG[07-05|11:06:29] Skeleton chain invalid                   peer=24c2599c54bd7194 err="block header download canceled (requested)"
DEBUG[07-05|11:06:29] Header download terminated      
```

#### tail -f geth.log //로그확인





### #Transaction

75p

eth.blockNumber 통해 마지막 블록 확인 

```
> eth.blockNumber
277

```



eth.getBalance(eth.account[0]) 

eth.getBalance(eth.account[1]) 통해 각각 얼마 있는지확인

```
> eth.getBalance(eth.accounts[0])
1.385e+21
> eth.getBalance(eth.accounts[1])
0
```



### 송금

- account[0] pw : pass0 / account[1] pw : pass1

```
> personal.unlockAccount(eth.accounts[0])
Unlock account 0x718ffe1ff6f5e9c49a4aeb78e484ab441c1f4165
Passphrase:
true
> eth.sendTransaction({from:eth.accounts[0], to:eth.accounts[1], value:web3.toWei(10,"ether")})
"0x3897d047eb8b6333dbfc7cc903b5e571fbe01611c4f61534669949ea0a0eeb4a"
> eth.getTransaction("0x3897d047eb8b6333dbfc7cc903b5e571fbe01611c4f61534669949ea0a0eeb4a")
{
  blockHash: "0x0000000000000000000000000000000000000000000000000000000000000000",
  blockNumber: null,
  from: "0x718ffe1ff6f5e9c49a4aeb78e484ab441c1f4165",
  gas: 90000,
  gasPrice: 18000000000,
  hash: "0x3897d047eb8b6333dbfc7cc903b5e571fbe01611c4f61534669949ea0a0eeb4a",
  input: "0x",
  nonce: 0,
  r: "0x63df5b80de1cc514445bc6ff90054b138545fea4ab1c14eb0c49371f7f68382b",
  s: "0x8dfab0844b8d9c3dae56e384411bb269773559df774fba4a84616bacae917ce",
  to: "0x1098023a3dd96468afc65b1dd016784a97872fb5",
  transactionIndex: 0,
  v: "0x66",
  value: 10000000000000000000
}

```

- miner.stop() 되어 있는 상태에서 account[0]이 personal.unlockAccount(eth.accounts[0]) 하여 pw 입력시켜,  eth.sendTransaction({from:eth.accounts[0], to:eth.accounts[1], value:web3.toWei(10,"ether")}) 를 통해 account[1] 에게 10 ether 를 전송하면 트랜잭션은 전송되었고, 아직 채굴이 되지 않은 보류 상태이므로 잔고는 0 이지만 miner.start() 하게 되면 채굴이 진행되어 잔고가 account[1]에 들어오게 된다.
- 즉, miner.start() 활성화 시킨 상태에서 send 하게 되면 바로 돈이 입금되는 것 처럼 느껴짐

---

# #초기화 후 다시 해보기



#### Node#1								Node#2

---

### 공통작업

1. ##### 설정 (네트워크 - 2 - 어댑터에 브릿지)

2. #####  방화벽 제거

3. #####  랜카드 IP 추가

- ifconfig -a (랜카드 추가 확인)

  ![1530765094917](C:\Users\Kchaos7\AppData\Local\Temp\1530765094917.png)

  - sudo ifconfig  enp0s8 172.17.144.222 netmask 255.255.255.0 up	// IP +100, 255넘으면 안되고 가상의 IP 설정.

  - sudo route add default gw 172.17.0.1           // My gateway

  - ping 172.17.144.201    // 상대방 IP

    ```
    user01@ubuntu:~$ ping 172.17.144.201
    PING 172.17.144.201 (172.17.144.201) 56(84) bytes of data.
    64 bytes from 172.17.144.201: icmp_seq=1 ttl=64 time=3.20 ms
    64 bytes from 172.17.144.201: icmp_seq=2 ttl=64 time=6.23 ms
    64 bytes from 172.17.144.201: icmp_seq=3 ttl=64 time=4.22 ms
    64 bytes from 172.17.144.201: icmp_seq=4 ttl=64 time=4.33 ms
    64 bytes from 172.17.144.201: icmp_seq=5 ttl=64 time=5.85 ms
    64 bytes from 172.17.144.201: icmp_seq=6 ttl=64 time=4.81 ms
    ```

    ##### 4. 데이터 디렉터리 생성 및 제네시스 블록 생성(genesis.json) - timestamp는 짝수 자리

```
user01@ubuntu:~$ mkdir data_testnet
user01@ubuntu:~$ cd data_testnet/
user01@ubuntu:~/data_testnet$ vi genesis.json
/* input code */
// delete coinbase
```

##### 5. 제네시스 블록 초기화

```
geth --datadir /home/user01/data_testnet/ init /home/user01/data_testnet/genesis.json
```

![1530765828979](C:\Users\Kchaos7\AppData\Local\Temp\1530765828979.png)



##### 6. geth 데몬 실행

- networkid를 상대방과 동일하게 수정해야한다. 나머지 그대로

```
nohup geth --networkid 2500 --nodiscover --datadir /home/user01/data_testnet --rpc  --rpcaddr "0.0.0.0" --rpcport 8545  --rpccorsdomain "*" --rpcapi "admin,db,eth,miner,net,personal,web3" --verbosity 6  2>> /home/user01/data_testnet/geth.log &
```

![1530766114602](C:\Users\Kchaos7\AppData\Local\Temp\1530766114602.png)

![1530766161695](C:\Users\Kchaos7\AppData\Local\Temp\1530766161695.png)

##### 7. 로그확인

tail -f geth.log



##### 8. 다른 터미널(putty)

geth attach rpc:http://172.17.144.222:8545

![1530766630462](C:\Users\Kchaos7\AppData\Local\Temp\1530766630462.png)



##### 9. 계정생성

`>`personal.newAccount ("pass0")

`>`personal.newAccount ("pass1")

```
> personal.newAccount ("pass0")
"0xd66715f4250d3a5b193739707462249cbdf28c4c"

> personal.newAccount ("pass1")
"0x05fb23117eda987e80bc642bfd3bd00729778926"
```

---

$$

$$

#다른 쪽에서는(상대방, 내가할것 x)

`>`personal.newAccount ("pass3")

`>`personal.newAccount ("pass4")

---



10. ##### Peer 연결

    - admin.nodeInfo.enode 결과를 Txt 저장

      ```
      > admin.nodeInfo.enode
      "enode://897583d0c1e5a0973671770b86aa189436b779dcdc4d7500da62740b0bd0b2a0edd11bd7bf91869813e1b6cdd6c65c8f0528fb6162688b61c3f83688f201ffdd@[::]:30303?discport=0"
      >
      ```

    - -@[::]:30303 부분에 Node#1의 IP 입력 

      - admin.addPeer("enode값 추가")
      - #내가 지금 Node#1 이고 endoe 값을 전달하였고
      - 상대방은 Node#2 이고
        - admin.addPeer("내가보낸 enode 값 입력")
        - admin.addPeer("enode://897583d0c1e5a0973671770b86aa189436b779dcdc4d7500da62740b0bd0b2a0edd11bd7bf91869813e1b6cdd6c65c8f0528fb6162688b61c3f83688f201ffdd@172.17.144.222:30303?discport=0)

11. ##### 연결확인

    `>`net.peerCount

    `>`admin.peers

    ![1530767143076](C:\Users\Kchaos7\AppData\Local\Temp\1530767143076.png)

    ##### 

12. ##### Test

    | Node#1                                                       | Node#2                             |
    | ------------------------------------------------------------ | ---------------------------------- |
    | `>`eth.blockNumber                                           | `>`eth.blockNumber                 |
    | > 0                                                          | > 0                                |
    |                                                              |                                    |
    | `>`miner.start()                                             |                                    |
    | >null                                                        |                                    |
    |                                                              |                                    |
    | `>`eth.mining()                                              |                                    |
    | > true                                                       |                                    |
    |                                                              |                                    |
    | `>`miner.stop()                                              |                                    |
    | >true                                                        |                                    |
    | //Percentage가 100 될 때까지 wait                            |                                    |
    | //100이 되면 채굴 시작                                       |                                    |
    |                                                              |                                    |
    | `>`eth.getBalance(eth.accounts[0])                           | `>`eth.getBalance(eth.accounts[0]) |
    | > 20                                                         | > 20                               |
    |                                                              |                                    |
    | `>`personal.unlockAccount(eth.accounts[0])                   |                                    |
    | >Unlock account 0xd66715f4250d3a5b193739707462249cbdf28c4c   |                                    |
    | >true                                                        |                                    |
    |                                                              |                                    |
    | '>' eth.sendTransaction({from:eth.accounts[0], to:eth.accounts[1], value:web3.toWei(10, "ether")})"0x531a8b17db85c3bd102c6a1d3827603c7f632e0fe30b1fbd461d8ac6135bdf94" |                                    |
    |                                                              |                                    |
    | eth.getBalance(eth.accounts[1])                              |                                    |
    | >10000000000000000000                                        |                                    |

    

miner.start()

eth.getTransaction()

![1530770260354](C:\Users\Kchaos7\AppData\Local\Temp\1530770260354.png)

> 노드 1과 노드 2의 블록 개수가 같고 마지막 노드의 트랜젝션도 동일



### #상대방에게 송금



10. ```
    > personal.unlockAccount(eth.accounts[0])
    Unlock account 0xd66715f4250d3a5b193739707462249cbdf28c4c
    Passphrase:
    true
    
    > eth.sendTransaction({from:eth.accounts[0], to:"0xd8e68dd2b94d4de509f84be5ace87c82e7917d3e", value:web3.toWei(10, "ether")})
    "0x0b6efda7b6cd6910b2631e67a43c2eb6b65e1bd31aa9c2e009749d3d0b691c40"
    
    //이 때, to는 상대방 account[1]의 주소
    //상대방은 pass3 > account[0]
    //		  pass4 > account[1]
    
    > eth.pendingTransactions
    [{
        blockHash: null,
        blockNumber: null,
        from: "0xd66715f4250d3a5b193739707462249cbdf28c4c",
        gas: 90000,
        gasPrice: 18000000000,
        hash: "0x0b6efda7b6cd6910b2631e67a43c2eb6b65e1bd31aa9c2e009749d3d0b691c40",
        input: "0x",
        nonce: 2,
        r: "0xd4e84acb0ef8e0108b99253b85df804f83980c5fb97e7a471d16237440602bef",
        s: "0x5e578af8444c0fdae81702b2c96ebf5a6c4d2f6afff7b29f7edcfdf04b02e868",
        to: "0xd8e68dd2b94d4de509f84be5ace87c82e7917d3e",
        transactionIndex: 0,
        v: "0x65",
        value: 10000000000000000000
    }]
    
    // 트랜젝션을 전송하면 서버에 명부가 저장된 내용을 출력하고, 만약 전송하지 않았으면 [] NULL값이 나옴
    > miner.start()
    null
    
    // 채굴을 시작하면 명부로 블록을 전송
    // 상대방의 account[1]에 10 이더가 전송된 것을 확인 가능
    // 마찬가지로 내가 account[1] 주소를 알려주고 상대방이 send(to:"account[1] 주소") 하게되면
    // 돈을 입금 받을 수 있다.
    ```

---



### # 블록 뜯어보기

- 마지막 블록은 900 이였고, 상대방(account[1])에게 나의 계좌  account[0])으로 부터 송금을 하게 되면, 트랜젝션이 생기게 되고 다음블록 901 을 확인하면 트랜젝션이 일치하는 것을 확인 가능.

![1530773017095](C:\Users\Kchaos7\AppData\Local\Temp\1530773017095.png)

- 머클루트(검증)가 아닌 패트리샤 트리(검색)를 사용, 추적이 가능
- uncle block은 난이도가 일반 블록에 비해 낮아서 퇴출당하여 체인에 담기지 못함(뒤쳐지는 블록, 부하), 그래서 몇개 씩 채워야 함(depth). 계산해서 자식이 많은 노드를 블록에 넣어야함 즉, 혼자 떠돌지 못하게 챙겨감.
- 그래서 실제 블록을 보면 uncle reward 에 몇개 담겨있는 것을 볼 수 있다(블록에 블록이 담김)

---

##### 다음 시간 배울 내용

- 블록을 뜯고, 트랙잭션 확인(잔고를 계산하는 방식이 특이함, 자신한테 다시 돈을 돌려준다. In or Out)
- 돈을 송금하면 해당 그 돈이 전달되는 것이 아니라 새로운 돈을 받게됨![1530776720046](C:\Users\Kchaos7\AppData\Local\Temp\1530776720046.png)
  - 받은돈을 자신에게 보냄.(거스름돈)
- 합의 알고리즘

---

#### #20180705.txt

```
http://192.168.0.105/
http://192.168.0.105:8080

3일차 - 

VirtualBox - Ethereum 부팅
           - Putty 연결

* Ethereum Private Network 구축
1)IP 확인
 ifconfig -a
  enp0s3   10.0.2.15



 2) Desktop  IP 확인 : 시작->명령창 입력: cmd.exe
  ipconfig

  이더넷 어댑터 로컬 영역 연결 2:
   IP: 192.168.0.105
   서브넷마스크:255.255.255.0
   게이트웨이: 192.168.0.1
    
  3)Desktop 
   - 방화벽 해제

  4) Ethereum VM  - IP추가 작업
   - putty 연결
    ifcofig -a   (추가된 랜카드 확인 - enp0s8 )

sudo ifconfig enp0s8 ip netmask 255.255.255.0 up

      자신의 Desktop ip + 100 = max(254)

sudo ifconfig enp0s8 192.168.0.205 netmask 255.255.255.0 up
sudo route add  default gw 192.168.0.1

ping 192.168.0.x
     


5) geth 실행
 - rpcaddr 0.0.0.0  rpcport 8545

 - ps -eaf | grep geth
 
 * Peer 연결 조건
 - genesis 블록이 같아야 하며
 - networkid 가 같아야 함

nohup geth --networkid 4689 --nodiscover --datadir /home/user01/data_testnet --rpc  --rpcaddr "0.0.0.0" --rpcport 8545  --rpccorsdomain "*" --rpcapi "admin,db,eth,miner,net,personal,web3" --verbosity 6  2>> /home/user01/data_testnet/geth.log &


  

6) Peer연결
    Node#1                Node#2
  admin.nodeInfo


> admin.nodeInfo.enode
"enode://c4843e6a6cfd6526edc7c33731ac3a4ec46ed33a95939387668d4c6f1f9610a377829c0f453c9846a9826f236494258c13dc743c7c846423d2c2a8075ec9ca56@[::]:30303?discport=0"
>

@[::]:30303
-접속할 Node#1 IP 주소 입력

@192.168.0.205:30303

admin.nodeInfo.enode 나온  enode 전체값을
메모장에 복사 후


@[::]:30303 이 부분을 Node#1 의 IP 수정


http://192.168.0.105/upload
http://192.168.0.105:8080/upload

자신의 이름 폴더 :node1_enode값.

admin.nodeInfo.enode 이 정보를 Node#2 전달



  Node#2 작업
  - node#1 값 복사후
  >admin.addPeer("enode://c4843e6a6cfd6526edc7c33731ac3a4ec46ed33a95939387668d4c6f1f9610a377829c0f453c9846a9826f236494258c13dc743c7c846423d2c2a8075ec9ca56@192.168.0.205:30303?discport=0
")

  


   연결 확인 - Node#1, Node#2
   > net.peerCount
   > admin.peers
   > admin.removePeer('<peer_id>')

  

* eth.blockNumber

* Node#1              Node#2
---------------------------------
공통작업
1) 랜카드 IP 추가
 ifconfig -a  (랜카드 추가 확인)
 sudo ifconfig enp0s8 192.168.0.xx netmask 255.255.255.0 up
 sudo route add default gw 192.168.0.1

 ping node#2

2)데이터 디렉토리 생성
  mkdir data_testnet
  cd data_testnet

3) 제네시스 블록 생성 및 초기화
   vi genesis.json
  geth --datadir /path/  init  /genesis.json-path/


4) geth 데몬 실행
 
nohup geth --networkid 4689 --nodiscover --datadir /home/user01/data_testnet --rpc  --rpcaddr "0.0.0.0" --rpcport 8545  --rpccorsdomain "*" --rpcapi "admin,db,eth,miner,net,personal,web3" --verbosity 6  2>> /home/user01/data_testnet/geth.log &

실행 확인
ps -eaf | grep geth

로그 확인
tail -f geth.log


다른 터미널(putty)
geth attach rpc:http://192.168.0.x:8545
>

5)계정 생성
>personal.newAccount("pass0")   
                      personal.newAccount("pass3")

>personal.newAccount("pass1")    
                      personal.newAccount("pass4")

6) Peer 연결
>admin.nodeInfo.enode 결과를
 메모장으로 저장
 -@[:]:30303 이부분에 node#1의 IP 설정

                     admin.addPeer("enode값 추가")
연결 확인
>net.peerCount
>admin.peers


7)  Node#1              Node#2
 >eth.blockNumber       >eth.blockNumber
 
 >miner.start()
 >eth.mining
 >miner.stop()
 >eth.getBalance(eth.accounts[0])

8)송금
 >eth.coinbase            >eth.coinbase

 >eth.getBalance(eth.accounts[0])
 >eth.getBalance(eth.accounts[1]) 

 (1)node#1  송금
   
 eth.accounts[0] -> eth.accounts[1]

-web3.fromWei(eth.getBalance(eth.accounts[0]),"ether")

 - personal.unlockAccount(eth.accounts[0])
 - eth.sendTransaction({from:eth.accounts[0],
                        to:eth.accounts[1],
                 value:web3.toWei(10,"ether)}) 
  => TxID확인
  
   - eth.getTransaction("TxID")
   => blockNumber:  없음...아직 채굴되지 않음.

 
  (2)채굴
  - miner.start()
   - eth.getTransaction("TxID")
   => blockNumber: xxx

   - miner.stop()

                         (3) Node#2
                        - 블록확인
  -eth.blockNumber        -eth.blockNumber

   eth.getBlock(숫자)     eth.getBlock(숫자)


   (4)
                      Node#2
                       eth.accounts[1] 주소를
                       메모장 -> Node#1 전달
       
   eth.accounts[0] -> Node#2  eth.accounts[1]

eth.sendTransaction({from:eth.accounts[0],
                        to:"",

  - 채굴
                    
                          (3) Node#2
                        - 블록확인
  -eth.blockNumber      -eth.blockNumber
                        eth.getBalance(eth.accounts[1])   




 >eth.blockNumber       >eth.blockNumber 

```

