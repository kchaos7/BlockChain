# 블록체인 전문가1 DAY 1

## IPFS란 무엇인가?

> The InterPlanetary File System (IPFS) is a peer-to-peer distributed file system that seeks to connect all computing devices with the same system of files. In some ways, IPFS is similar to the Web, but IPFS could be seen as a single BitTorrent swarm, exchanging objects within one Git repository. In other words, IPFS provides a high throughput content addressed block storage model, with content addressed hyper links. This forms a generalized Merkle DAG, a data structure upon which one can build versioned file systems, blockchains, and even a Permanent Web. IPFS combines a distributed hashtable, an incentivized block exchange, and a self-certifying namespace. IPFS has no single point of failure, and nodes do not need to trust each other.

> IPFS (InterPlanetary File System)는 모든 컴퓨팅 장치를 동일한 파일 시스템으로 연결하려고 하는 P2P 분산 파일 시스템입니다. 어떤 면에서는 IPFS는 웹과 비슷하지만, 한 Git 레포지트리의 오브젝트를 교환하는 단일 비트토렌트 스웜 (파일의 고유 식별자와 파일을 소유하고 있는 피어 목록)으로도 볼 수 있습니다. 즉, IPFS는 content addressed 하이퍼 링크를 이용하여 높은 처리량을 가진 content addressed 블록 스토리지 모델을 제공합니다. 이는 버전 관리되는 파일 시스템, 블록 체인, 영구적인 웹 페이지를 구축할 수 있는 자료 구조인 일반화된 Markle DAG의 형태를 가집니다. IPFS는 분산 해시 테이블과 인센티브화된 블록 교환과 자체 인증 네임스페이스를 합친 것입니다. IPFS는 단일 실패 지점이 없으며, 각자의 노드들은 서로 신뢰할 필요가 없습니다.
>
> 기본적인 파일 시스템은 NTFS(New Technology File System)

---

## 이더리움 환경 구축해보자 !

##### shared-전문가1-스마트컨트랙트.pdf(33p~)

- 랜카드에 ip 추가



- 우선 cmd에서 ipconfig

  ![1531183525348](C:\Users\Kchaos7\AppData\Local\Temp\1531183525348.png)

```
//아직 랜카드가 추가 안된 상태
user01@ubuntu:~$ ifconfig -a
enp0s3    Link encap:Ethernet  HWaddr 08:00:27:de:84:b5
          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fede:84b5/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:5607 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1327 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:6462910 (6.4 MB)  TX bytes:101459 (101.4 KB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:160 errors:0 dropped:0 overruns:0 frame:0
          TX packets:160 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:11840 (11.8 KB)  TX bytes:11840 (11.8 KB)

//랜카드 추가 작업 (IP,GateWay)
user01@ubuntu:~$ sudo ifconfig enp0s8 172.17.144.222 netmask 255.255.255.0 up
[sudo] password for user01:
user01@ubuntu:~$ sudo route add default gw 172.17.0.1
SIOCADDRT: Network is unreachable
user01@ubuntu:~$ ifconfig -a
enp0s3    Link encap:Ethernet  HWaddr 08:00:27:de:84:b5
          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fede:84b5/64 Scope:Link
          UP BROADCAST RUNNINifG MULTICAST  MTU:1500  Metric:1
          RX packets:5996 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1544 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:6494238 (6.4 MB)  TX bytes:125615 (125.6 KB)

//정보가 추가된 것을 볼 수 있다 중요함
enp0s8    Link encap:Ethernet  HWaddr 08:00:27:11:ad:25
          inet addr:172.17.144.222  Bcast:172.17.144.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fe11:ad25/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:1411 errors:0 dropped:14 overruns:0 frame:0
          TX packets:8 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:102683 (102.6 KB)  TX bytes:648 (648.0 B)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:160 errors:0 dropped:0 overruns:0 frame:0
          TX packets:160 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:11840 (11.8 KB)  TX bytes:11840 (11.8 KB)
```



- mkdir smartcontract_testnet 생성 및 제네시스 파일

  ```
  user01@ubuntu:~$ mkdir smartcontract_testnet
  user01@ubuntu:~$ cd smartcontract_testnet/
  user01@ubuntu:~/smartcontract_testnet$ vi genesis.json
  
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



- 초기화 

  geth --datadir /home/user01/smartcontract_testnet/ init /home/user01/smartcontract_testnet/genesis.json

  ```
  user01@ubuntu:~/smartcontract_testnet$ geth --datadir /home/user01/smartcontract_testnet/ init /home/user01/smartcontract_testnet/genesis.json
  
  INFO [07-10|09:54:18] Maximum peer count                       ETH=25 LES=0 total=25
  INFO [07-10|09:54:18] Allocated cache and file handles         database=/home/user01/smartcontract_testnet/geth/chaindata cache=16 handles=16
  INFO [07-10|09:54:18] Writing custom genesis block
  INFO [07-10|09:54:18] Persisted trie from memory database      nodes=0 size=0.00B time=3.014µs gcnodes=0 gcsize=0.00B gctime=0s livenodes=1 livesize=0.00B
  INFO [07-10|09:54:18] Successfully wrote genesis state         database=chaindata                                         hash=5704d0…9bc5b0
  INFO [07-10|09:54:18] Allocated cache and file handles         database=/home/user01/smartcontract_testnet/geth/lightchaindata cache=16 handles=16
  INFO [07-10|09:54:18] Writing custom genesis block
  INFO [07-10|09:54:18] Persisted trie from memory database      nodes=0 size=0.00B time=2.3µs   gcnodes=0 gcsize=0.00B gctime=0s livenodes=1 livesize=0.00B
  INFO [07-10|09:54:18] Successfully wrote genesis state         database=lightchaindata                                         hash=5704d0…9bc5b0
  ```



- 트리 확인 sudo apt install tree

  ![1531184256077](C:\Users\Kchaos7\AppData\Local\Temp\1531184256077.png)

  

- geth 실행

  rpcaddr 는 자신의 아이피로 변경

  ```
  nohup geth --networkid 4649 --nodiscover --datadir /home/user01/smartcontract_testnet --rpc --rpcaddr "172.17.144.222" --rpcport 8545 --rpccorsdomain "*" --rpcapi "admin,db,eth,debug,miner,net,shh,txpool,personal,web3" --verbosity 6 2>>/home/user01/smartcontract_testnet/geth.log &
  ```

  ![1531184395287](C:\Users\Kchaos7\AppData\Local\Temp\1531184395287.png)



- geth 데몬 실행 확인

  ps -eaf | grep geth

  ![1531184436108](C:\Users\Kchaos7\AppData\Local\Temp\1531184436108.png)



- Putty 하나 더 실행 하여 attach

  geth attach rpc:http://172.17.144.222:8545

  ![1531184600234](C:\Users\Kchaos7\AppData\Local\Temp\1531184600234.png)



- 기존 Putty 에서는 tail -f geth.log 모니터링

  ![1531184676016](C:\Users\Kchaos7\AppData\Local\Temp\1531184676016.png)

> 구축 완료!

---



##  계정만들고 채굴, 관리 해보자 ! (Attach putty에서 실행)

- 계정 생성

```
> personal.newAccount("pass0")
"0xc53ba2e65a1682163c332b6efc74eea3ebf3edc1"

> eth.accounts
["0xc53ba2e65a1682163c332b6efc74eea3ebf3edc1"]

> personal.newAccount("pass1")
"0x470db71c77bae52d72342f837f83d1be8cd11bbd"

> eth.accounts
["0xc53ba2e65a1682163c332b6efc74eea3ebf3edc1", "0x470db71c77bae52d72342f837f83d1be8cd11bbd"]

```



- 잔고 확인

  ```
  > eth.getBalance(eth.accounts[0])
  0
  
  > eth.getBalance(eth.accounts[1])
  0
  ```



- 채굴자 확인

  ```
  > eth.coinbase
  "0xc53ba2e65a1682163c332b6efc74eea3ebf3edc1"
  
  //accounts[0]이 채굴자 인 것을 확인 할 수 있다.
  ```



- 채굴 시작(Log putty에서 percentage = 100 되어야 채굴 시작됨)



---

## Remix 

- percentage 기다리는 동안 Remix 들어가서 Setting / 4.18-commit으로

  ![1531186026960](C:\Users\Kchaos7\AppData\Local\Temp\1531186026960.png)

- run 에서 web3 Povider 선택하여 http://172.17.144.222:8545

![1531186186937](C:\Users\Kchaos7\AppData\Local\Temp\1531186186937.png)

- 하지만 url : https://remix.ethereum.org 는 보안 때문에 s 빼서 http://remix~~ 로 해야함.

- 계정 2개가 생성된 것을 볼 수 있음( 원래 2명인데 버그여서 4명으로 보임 )

- MyFirstContract.sol 생성

  ```
  pragma solidity ^0.4.18;
  contract MyFirstContract {
     string fName;
     uint age;
     
     function setInstructor(string _fName, uint _age) public {
          fName = _fName;
          age = _age;
       }
      
      function  getInstructor() view public returns (string, uint){
            return (fName, age);
      }
      }
  ```

  

  ![1531187227472](C:\Users\Kchaos7\AppData\Local\Temp\1531187227472.png)

  - 메모장에 복사



![1531187363391](C:\Users\Kchaos7\AppData\Local\Temp\1531187363391.png)![1531187415195](C:\Users\Kchaos7\AppData\Local\Temp\1531187415195.png)

> lock 된 상태

```
//Unlock 시작
> personal.unlockAccount(eth.accounts[0])
Unlock account 0xc53ba2e65a1682163c332b6efc74eea3ebf3edc1
Passphrase:
true
> miner.start()	//채굴 시작
```

![1531187686909](C:\Users\Kchaos7\AppData\Local\Temp\1531187686909.png)

> pending 상태였다가 주소가 생김. 
>
> 이제`>`miner.stop() 해주자 !





![1531191193265](C:\Users\Kchaos7\AppData\Local\Temp\1531191193265.png)



CA (스마트 컨트랙트 주소) -

0xb84b94d8bf4c9c913a4ae73c1916e3ea3339934f 



## 웹사이트 구축 + Web3.js

- node.js



- Putty 하나 더 생성(현재 Log, Attach 존재)

- nodejs

- ```
  user01@ubuntu:~$ ls
  go  my_ethereum  nohup.out  smartcontract_testnet
  user01@ubuntu:~$ nodejs -v
  v4.2.6
  user01@ubuntu:~$ npm -v
  3.5.2
  user01@ubuntu:~$ sudo npm install express-generator -g
  [sudo] password for user01:
  /usr/local/bin/express -> /usr/local/lib/node_modules/express-generator/bin/express-cli.js
  /usr/local/lib
  └─┬ express-generator@4.16.0
    ├── commander@2.13.0
    ├── ejs@2.5.7
    ├─┬ minimatch@3.0.4
    │ └─┬ brace-expansion@1.1.11
    │   ├── balanced-match@1.0.0
    │   └── concat-map@0.0.1
    ├─┬ mkdirp@0.5.1
    │ └── minimist@0.0.8
    └── sorted-object@2.0.1
  user01@ubuntu:~$ sudo ln -s /usr/bin/nodejs  /usr/local/bin/node
  user01@ubuntu:~$ express web3		//자동으로 web3 폴더에 뼈대 생성
  
  
    warning: the default view engine will not be jade in future releases
    warning: use `--view=jade' or `--help' for additional options
  
     create : web3/
     create : web3/public/
     create : web3/public/javascripts/
     create : web3/public/images/
     create : web3/public/stylesheets/
     create : web3/public/stylesheets/style.css
     create : web3/routes/
     create : web3/routes/index.js
     create : web3/routes/users.js
     create : web3/views/
     create : web3/views/error.jade
     create : web3/views/index.jade
     create : web3/views/layout.jade
     create : web3/app.js
     create : web3/package.json
     create : web3/bin/
     create : web3/bin/www
  
     change directory:
       $ cd web3
  
     install dependencies:
       $ npm install
  
     run the app:
       $ DEBUG=web3:* npm start		//자동으로 웹사이트 다 만들어짐
  
  user01@ubuntu:~/web3$ npm install	//필요한 패키지 설치
  ... 생략 ...
  
  user01@ubuntu:~/web3$ ls
  app.js  bin  node_modules  package.json  public  routes  views
  user01@ubuntu:~/web3$ DEBUG=web3 npm start
  
  > web3@0.0.0 start /home/user01/web3
  > node ./bin/www
  
  
  ```

  http://172.17.144.222: 3000 (브라우저 검색)

  ![1531188687413](C:\Users\Kchaos7\AppData\Local\Temp\1531188687413.png)



- shared-전문가-1일차-web3_library.
- light는 bignumber crypto utp 필요.
- 우리는 min 사용.
- [D:\블록체인\shared\전문가1\1일차\web3_library\web3.js-develop\dist\web3.min.js]
- 업로드 가능한 프로그램 필요.
- [D:\블록체인\shared\전문가1\1일차\WinSCP-5.13.2-Setup.exe] 는 업로드 프로그램



![1531189692801](C:\Users\Kchaos7\AppData\Local\Temp\1531189692801.png)

- 파일 집어넣기 min.js

![1531189789259](C:\Users\Kchaos7\AppData\Local\Temp\1531189789259.png)

![1531189768841](C:\Users\Kchaos7\AppData\Local\Temp\1531189768841.png)



- [D:\블록체인\shared\전문가1\1일차\demo_code] 에 있는 html 파일 2개 public  내부(/home/user01/web3/public)로 끌어서 이동

  ![1531189915909](C:\Users\Kchaos7\AppData\Local\Temp\1531189915909.png)



- 주소 뒤에 해당 html 파일 이름 넣어주면 현재 Linux에 public 폴더 내에 html 파일 있어서 적용 된다.![1531190642455](C:\Users\Kchaos7\AppData\Local\Temp\1531190642455.png)

- web3_demo_최종.html

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  
      <style>
      body {
      background-color:#F0F0F0;
      padding: 2em;
      font-family: 'Raleway','Source Sans Pro', 'Arial';
  }
  .container {
      width: 50%;
      margin: 0 auto;
  }
  label {
      display:block;
      margin-bottom:10px;
  }
  input {
      padding:10px;
      width: 50%;
      margin-bottom: 1em;
  }
  button {
      margin: 2em 0;
      padding: 1em 4em;
      display:block;
  }
  
  #instructor {
      padding:1em;
      background-color:#fff;
    
      </style>
  
      <script src="https://cdn.jsdelivr.net/gh/ethereum/web3.js/dist/web3.min.js"></script>
  
  </head>
  <body>
      <div class="container">
  
          <h1>개인정보입력</h1>
  
          <h2 id="instructor"></h2>
  
          <label for="name" class="col-lg-2 control-label">Instructor Name</label>
          <input id="name" type="text">
  
          <label for="name" class="col-lg-2 control-label">Instructor Age</label>
          <input id="age" type="text">
  
          <button id="button">Update Instructor</button>
  
  
      </div>
      <script src="https://code.jquery.com/jquery-3.3.1.js"></script>
      <script>
       //1. web3 provider 설정
       //  if (typeof web3 !== 'undefined') {
       //    web3 = new Web3(web3.currentProvider);
       //    } else {
       //   web3 = new Web3(new Web3.providers.HttpProvider("http://172.17.144.222:8545"));
       //    }
       
       //web3 api-0.20.3
       var web3 = new Web3();
       var provider = new web3.providers.HttpProvider("http://172.17.144.222:8545");
          // 1.IP 주소 넣고
       web3.setProvider(provider);
       
        console.log('Version:', web3.version.api);
        
       web3.eth.defaultAccount = web3.eth.accounts[0];
       console.log("accounts:"+ web3.eth.defaultAccount);
      
       //2. ABI 로딩
     
       // var coinbase = web3.eth.coinbase;
       // var balance = web3.eth.getBalance(coinbase);    
       
      //accounts:undefined
      //리턴값이 없다는 의미
      
      
       // var ContractABI = web3.eth.contract(ABI).at('CA');
          //2. ABI Remix에서 compile-detail-ABI 복사 해서 [  ....  ] 내부에 복사
       var InstructorContract = web3.eth.contract([
  	{
  		"constant": false,
  		"inputs": [
  			{
  				"name": "_fName",
  				"type": "string"
  			},
  			{
  				"name": "_age",
  				"type": "uint256"
  			}
  		],
  		"name": "setInstructor",
  		"outputs": [],
  		"payable": false,
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"constant": true,
  		"inputs": [],
  		"name": "getInstructor",
  		"outputs": [
  			{
  				"name": "",
  				"type": "string"
  			},
  			{
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"payable": false,
  		"stateMutability": "view",
  		"type": "function"
  	}
  ]).at('0xb84b94d8bf4c9c913a4ae73c1916e3ea3339934f');		//Contract address
  //3. Remix에서 복사했던 CA 주소 입력
     console.log(InstructorContract);
     
     InstructorContract.getInstructor(function(error,result){
      if(!error){
         console.log("result:"+ result);
         $("#instructor").html(result[0]+ '(' + result[1]+'years old)');
      
      }else{
       console.log(error);
       }
     });
     
      
  //    $("#button").click( function(error, result){
  //      web3.eth.defaultAccount = web3.eth.accounts[0];
  //     if(!error){
  //      console.log("click:");
  //      InstructorContract.setInstructor($("#name").val(), $("#age").val());
  //    }else{
  //     console.log("click error:" + error);
  //     }
  //   });
       
        $("#button").click(function()
          {
        web3.eth.defaultAccount = web3.eth.accounts[0];
        InstructorContract.setInstructor($("#name").val(), $("#age").val());
     });
       
      </script>
      
      </body>
      </html>
      
  ```

  ```
  //코드 내부에 ABI 대체
  [
  	{
  		"constant": false,
  		"inputs": [
  			{
  				"name": "_fName",
  				"type": "string"
  			},
  			{
  				"name": "_age",
  				"type": "uint256"
  			}
  		],
  		"name": "setInstructor",
  		"outputs": [],
  		"payable": false,
  		"stateMutability": "nonpayable",
  		"type": "function"
  	},
  	{
  		"constant": true,
  		"inputs": [],
  		"name": "getInstructor",
  		"outputs": [
  			{
  				"name": "",
  				"type": "string"
  			},
  			{
  				"name": "",
  				"type": "uint256"
  			}
  		],
  		"payable": false,
  		"stateMutability": "view",
  		"type": "function"
  	}
  ]
  ```

  

  ![1531197077868](C:\Users\Kchaos7\AppData\Local\Temp\1531197269425.png)

  > ```
  > > personal.unlockAccount(eth.accounts[0])
  > Unlock account 0xc53ba2e65a1682163c332b6efc74eea3ebf3edc1
  > Passphrase:
  > true
  > > miner.start()
  > null
  > 
  > ```
  >
  > Personal.unlock... 후 miner.start() 하여 채굴 시작한 뒤 Name, Age Update 하고 새로고침 하면 상단에 뜨는 것을 볼 수 있다.



---



# Mist

![1531198789703](C:\Users\Kchaos7\AppData\Local\Temp\1531198789703.png)"Ethereum Wallet.exe" --rpc http://172.17.144.222:8545

- 로딩 후 바로 launch 



![1531199469715](C:\Users\Kchaos7\AppData\Local\Temp\1531199469715.png)

- 작성 후 하단 deploy(배포 클릭)

  ![1531199516516](C:\Users\Kchaos7\AppData\Local\Temp\1531199516516.png)

- miner.start()

  ![1531199629160](C:\Users\Kchaos7\AppData\Local\Temp\1531199629160.png)

- ![1531199644572](C:\Users\Kchaos7\AppData\Local\Temp\1531199644572.png)





- 예제 2. sayhello, goodbye

  가시성

  ![1531200514973](C:\Users\Kchaos7\AppData\Local\Temp\1531200514973.png)

  

  ```
  pragma solidity ^0.4.18;
  
  contract HelloEthereum {
      string message ="hello";
      string goodbye = "잘가";
  
  function sayHello() public view returns (string) {
  	return message;
  }
  
  function setChangeHello(string _message) public payable {
  	message = _message;
  }
  
  function sayGoodBye() public view returns (string) {
  	return goodbye;
  }
  
  function setChangeGoodbye(string _goodbye) public payable {
  	goodbye = _goodbye;
  }
  }
  ```

  ![1531200307722](C:\Users\Kchaos7\AppData\Local\Temp\1531200307722.png)



- 함수 선택해서 돌려보자, sayhello 함수 실행 -> miner.start()

  ![1531200706181](C:\Users\Kchaos7\AppData\Local\Temp\1531200706181.png)

  - 비밀번호는 accounts[0]의 pw

![1531201107069](C:\Users\Kchaos7\AppData\Local\Temp\1531201107069.png)





- 예제3

  ```
  pragma solidity ^0.4.18;
  
  contract Greeter {
      string helloKorean ="안녕";
      string goodbyeKorean = "잘가";
      string helloEnglish = "Hello";
      string goodbyeEnglish= "GoodBye";
  
  function sayHello(uint8 lang) public view returns (string) {
  	if(lang==0)
  	    return helloKorean;
      if(lang==1)
          return helloEnglish;
      return "";
  }
  
  function sayGoodbye(uint8 lang) public view returns (string) {
  	if(lang==0)
  	    return goodbyeKorean;
      if(lang==1)
          return goodbyeEnglish;
      return "";
  }
  
  function setChangeHello(uint8 lang, string _hello) public {
      	  if(lang==0)
      		    helloKorean = _hello;
    		  if(lang==1)
         		 helloEnglish = _hello;
  }
  
  function setChangeGoodBye(uint8 lang, string _goodbye) public {
       	if(lang==0)
         		 goodbyeKorean = _goodbye;
     		 if(lang==1)
         		 goodbyeEnglish = _goodbye;
  } 
  }
  ```

  - ![1531203373449](C:\Users\Kchaos7\AppData\Local\Temp\1531203373449.png)

![1531203586806](C:\Users\Kchaos7\AppData\Local\Temp\1531203586806.png)



![1531203841991](C:\Users\Kchaos7\AppData\Local\Temp\1531203841991.png)







---





## 다시 솔리디티



![1531204516882](C:\Users\Kchaos7\AppData\Local\Temp\1531204516882.png)

> Solidity에서 작업한 것 저장하기 위해 F12(개발자도구)-Application-Local Storage
>
> 탐색기 %localappdata% 검색 Google-Chrome-User Data-Default-Local Storage
>
> lebeldb 브라우져 통해 복구







---

##### monitor.html

//블록 조회

```
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>block view</title>
//web3.js 자바스크립트 라이브러리 연동


//여기부터
<script src="./javascripts/web3.min.js"></script>
<script>
//web3 연동

var web3 = new Web3();
var provider = new web3.providers.HttpProvider("http://172.17.144.222:8545");
web3.setProvider(provider);
web3.eth.defaultAccount = web3.eth.accounts[0];

console.log("accounts[0]:" + web3.eth.defaultAccount);

//여기까지 작성

function startMonitor() {
}

function watchBlock(table, blockNumber) {
}


function insertBlockRow(result, table) {
	var row = table.insertRow();
	var td = row.insertCell(0);
	td.innerHTML = result.number;
	var td = row.insertCell(1);
	td.innerHTML = new Date(parseInt(result.timestamp, 16) * 1000).toString();
	var td = row.insertCell(2);
	td.innerHTML = result.hash;
	var td = row.insertCell(3);
	td.innerHTML = result.nonce;
	var td = row.insertCell(4);
	//if (result.transactions.length > 0) {
	//insertTranRow(result.transactions, td);
	//}
}


function insertTranRow(transactions, td) {
	var allData = "";
	for (var i = 0; i < transactions.length; i++) {
		//트랜잭션 코드 입력
	}
	td.innerHTML = "<input type='text' value='" + allData + "' /></td>";
}

function stopWatch() {
	stop = true;
}
</script>
</head>
<body>
	<br />
	<input type="button" value="start" onclick="startMonitor();" />
	<input type="button" value="stop" onclick="stopWatch();" />
	<table id="list" border="1">
		<tr>
			<th>Block<br />Number</th>
			<th>TimeStamp</th>
			<th>BlockHash</th>
			<th>Nonce</th>
			<th>Transaction</th>
		</tr>
	</table>
</body>
</html>

```

-WinScp 업로드, url monitor.html 추가

![1531207594252](C:\Users\Kchaos7\AppData\Local\Temp\1531207594252.png)

> 주소 나오면 성공.





---

##### 20180710.txt

```
* VirtualBox-Ethereum 부팅
 - 



http://192.168.0.105/
http://172.17.138.113:8080/

- 스마트컨트랙트_20180710_최기용.pdf

smartcontract_testnet

geth --datadir /home/user01/smartcontract_testnet/  init /home/user01/smartcontract_testnet/genesis.json

nohup geth --networkid 4649 --nodiscover --datadir /home/user01/smartcontract_testnet --rpc --rpcaddr "192.168.0.x" --rpcport 8545 --rpccorsdomain "*" --rpcapi "admin,db,eth,debug,miner,net,shh,txpool,personal,web3" --verbosity 6 2>>/home/user01/smartcontract_testnet/geth.log &

geth 데몬 실행 확인
$ ps -eaf | grep geth


putty 두대
1) attach 접속
geth attach rpc:http://192.168.0.x:8545
2) tail -f geth.log 모니터링


> personal.newAccount("pass0")
"0x79afb6633e31e94c1b59c3b3e4390c9ff27f9786"
> personal.newAccount("pass1")
"0x86acdef43f7b87e9a515f5d66d0c1c6e9dfb4b56"



> eth.coinbase
"0x79afb6633e31e94c1b59c3b3e4390c9ff27f9786"


[
	{
		"constant": false,
		"inputs": [
			{
				"name": "_fName",
				"type": "string"
			},
			{
				"name": "_age",
				"type": "uint256"
			}
		],
		"name": "setInstructor",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getInstructor",
		"outputs": [
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]


CA - 
0xd88a2c45ed03498341f3c8cafa2fd94f39a05d0d




* 웹사이트 구축 + Web3.js 
- nodejs + web3.js
1. nodejs와 npm 설치 확인
nodejs -v
npm -v

2) nodejs의 express 웹 페이지 구축 모듈 설치
sudo npm install express-generator -g
sudo ln -s /usr/bin/nodejs /usr/local/bin/node

3) express 웹프레임워크를 이용한 웹 서비스 구축
express web3
cd web3
npm install

4) 웹서버 시작
DEBUG=web3 npm start
http://192.168.0.x.:3000


npm install web3@0.20.4





//변수 생성
string message ="hello";
string goodbye = "잘가";

function sayHello() public pure returns(string){
    return message;
}

function changeHello(string _message) {
   message = _message;
}

function sayGoodBye() {
   return goodbye;
}

function changeGoodbye(string _goodbye) {
   goodbye = _goodbye;
}



pragma solidity ^0.4.18;

contract Greeter {

//변수
   string helloKorean="안녕";
   string goodbyeKorean="잘가";
   string helloEnglish="Hello";
   string goodbyeEnglish="Goodbye";



  function sayHello(uint8 lang) public view returns(string){
      if(lang ==0)
         return helloKorean;
      if(lang ==1)
         return helloEnglish;
       return "";  
      }
   
  function changeHello(uint8 lang, string _hello) public  {
    if(lang == 0)
       helloKorean =_hello;
    if(lang ==1)
       helloEnglish = _hello;
  }
  
  function sayGoodBye(uint8 lang) public view returns(string) {
   if(lang == 0)
      return goodbyeKorean;
    if(lang ==1)
     return goodbyeEnglish;
   
   return "";
}

function changeGoodbye(uint8 lang, string _goodbye) public  {
  if(lang ==0)
  goodbyeKorean = _goodbye;
  if(lang ==1)
   goodbyeEnglish = _goodbye;
}

  
  
}




[
	{
		"constant": true,
		"inputs": [
			{
				"name": "lang",
				"type": "uint8"
			}
		],
		"name": "sayHello",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "lang",
				"type": "uint8"
			},
			{
				"name": "_goodbye",
				"type": "string"
			}
		],
		"name": "changeGoodbye",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "lang",
				"type": "uint8"
			},
			{
				"name": "_hello",
				"type": "string"
			}
		],
		"name": "changeHello",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "lang",
				"type": "uint8"
			}
		],
		"name": "sayGoodBye",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]

```

