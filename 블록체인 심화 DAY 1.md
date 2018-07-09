# 블록체인 심화 DAY 1

참고 : www.archive.org](http://www.archive.org) > 모든 사이트 정보 get / DB site

 

노트북 gstep 와이파이 들어가서 172.17.138.113:8080 

### <실습 준비 작업>

desktop : 5.0.28 VirtualBox > Oracle 신뢰 check

notebook : 5.0.28 설치, 오류나면 5.2.12 설치

------

### virtual box 설치 후

파일-환경설정-옆버튼눌러서 확장 패키지 설치

Orac le_VM_...Extension 5.0.28-111378a 확장 패키지

------

### Virtualbox

머신-추가

(Blockchain.zip 압축 해제 된 폴더에서 BlockChain 추가)

------

### Virtualbox

툴바 > 스냅샷 > 네 개의 스냅샷 확인 > bitcoin core 선택 > 복원, 현재 가상머신상태 스냅샷 체크 해제

(Linux, BitCoin, Ethereum, HyperLedger)

복원 후 아이콘 우클릭 > 저장된 상태 삭제 클릭 > 실행

가상머신 계정: user01/qwer1234

------

### putty

127.0.0.1 port 번호 1234

블록체인 연결

리눅스 직접 만지지 않고, putty로  실행 

Bitcoin 디렉터리 내 노드 한개 만들어져 있음

만들어져있는 소스 통해 데몬 생성 가능

/*

pw설정 꿀팁 :

!25=i=u.

(pw:느낌이 오는 아이는 너다ㅋㅋㅋ)

*/

------

### [BitcoinBlockInfo](https://www.blockchain.com/ko/explorer)

![1530583052069](C:\Users\Kchaos7\AppData\Local\Temp\1530583052069.png)99997번 블록 Transaction(거래 수) 2번 밖에 없기 때문에 실습하기 좋다, 실제로는 1개

![1530583480669](C:\Users\Kchaos7\AppData\Local\Temp\1530583480669.png)

-  거래가 한번 이뤄진 것을 확인 할 수 있다.

![1530583469758](C:\Users\Kchaos7\AppData\Local\Temp\1530583469758.png)



### [EtherScan](https://etherscan.io/)

![1530583150357](C:\Users\Kchaos7\AppData\Local\Temp\1530583150357.png)

------

------

------

## § Putty 실습

if you want access putty, you have to access VirtualBox Bitcoin .

-  testnet :  인터넷 상에서 동작하는 테스트 네트워크, 테스트용 BTC 사용, 대량의 블록체인이 존재하기 때문에 처음 시작할 때 모든 데이터 취득.

- regtest : 로컬 PC 내에서의 테스트 네트워크, 계정 생성 및 채굴, 블록체인 초기화도 쉽게 하기 위한 실험용.

  

### #데몬 실행 [-daemon]

```
user01@ubuntu:~$ bitcoind -regtest -daemon 	//데몬 실행

Bitcoin server starting

```

-  100 블록이 경과하지 않으면 송금 등에 이용 불가.



### #블록 수 확인 [getblockcount]

```
user01@ubuntu:~$ bitcoin-cli -regtest getblockcount	

101
```



```
user01@ubuntu:~$ bitcoin-cli -regtest generate 101
[
  "393dce66181e355b4eb346a58a5b6897c2ba695b3c64518f70fa65998c115951",
  "520c50c14eb3b600fdd1dee8c4edf778d4305d02e6cbf86f4c73cd8985312c3a",
  "6d646dd1ea69125b098f49fa42696a25e24066c57c7cf7ddebe4d34ef367e7ee",
  "3d32830ef2d7827df6bc781c8896b6ad1c66babb5494c60dfab04fabb702e262",
  "1f829cb6cd510239d5467cc9b517202981e7dcd1d4315dad49f2df3385eef137",
  "67bf9e6052fa2218cd4da6bf0e936eb93d6dba60befdba12e16d0426fd70f4ce",
  "6f8fb7332ab92f96f659487556ddb2e790863a4d9c2cd0af2b7f1c481cde3405",
  "0f82bf1aa44d8ef2280706cfd2335f2e3fd304bf4cb3b5067359fe7f93e3ab92",
  "752d4c99f883b3bd39dd827a1300cfe7fe98df607fdd53627b1df7105e9c8585",
  "500793477c3618c3197ef3338332e5c61151785791bce25d7fae8a5713a5e56e",
  "18515d8a2fab1fce137cb753cb6da9adbe9915d2407b9dd242242654736b3ddf",
  "3a9a6395fc89426cb3271b5eea9c1e34b976a3f41cba3c1d45a553b5b15600f1",
  "03496288f12bcee47f7343ecff32ce643b8e5f03d85e77698a50b25c6ec9c118",
  "7c2ad5c92c1f4981831eb07543697d13b0f9f5c5712a9d212dc6eaf1ba7e0e65",
  "34396bef03a9891b2f6a1266fdd5850f21384861d6467d06f3d73271ef92438d",
  "0833fb2a6880889f9ab7c0affa76423dd9aeaf500b0ca0cc769064da2d6feda7",
  "6aebdad484a781ad1e8512cc57f8923010001dc2d1dae23a8699862a3fa254ca",
  "27ea531dd5e7882bf3e3b4915a54b8df508d1098bc5ace88496b8e2e2913c524",
  "254a410d5122d1b72168fc2d87e7648c3f3d8bd0e62f277a80b8040f0e006e87",
  "7084fffc7e082c93e8a85812a95d0820ddcc62adb1a005a66e923653c31debb6",
  "23c79160d489cd8fb75dcd5c10d1a737a70762b995f82db035982ed0fe978137",
  "0022fb86beaf8dfdea69838a3e2845db308a1729d03093d341559bbcad21bbd3",
  "2460ac8af7d64bd3561d3a7564f19f7ae99f4a3ad22b39042a7b1d93720a2a5f",
  "3b0012470939cef9f5d29f9b38dc99dc960900f3783e1482952e39f02b113c87",
  "587bb72e1d187eddaca6e70e82ba9c4bc59b26a95dfd55c2cd8c4e772e625100",
  "4412d564a13b683266ca6136a7d6ab9c3611c566576d25477039d43ec0aa9539",
  "33cd0383849d67bd1d7f2baa380c6b8ffe4e26fa3b7ac9fe69d7ca2cc2824e58",
  "59e5c9260e0d329f6c34913f6fe6da32e345df2ab8e082ae8289b4aa75ef7fad",
  "36cf6e91fc4c9db9b9172b671ae2e41e2bfab61faeae1f84e4fb0a0568c564aa",
  "2dbfd917c20e397833b37486bf8482733d3f39473d831ae5c7aa4a23fa4e3db5",
  "5df1d27b804246ce92060c3421a1137fa21956f26200b28dcea6e2d3cad1c839",
  "0bc9d08f83538e58ab3400a8dbda54813e5daecf2daae5d062d24c9abcc38cfc",
  "2bbf44b5303cded84678d63a469fd4c766c0c31cdbfbcbc08bbe8c58c7813dd5",
  "5af6f1f983df58080826b9f739c271591f47605efa95845b81f837277cea1773",
  "32e6acef4e6a7d9e83048f9cc663ad7f682f38f8ca8df178b0c1260b58bab1b1",
  "15a929ea7501c64834805d9743fb9f36baa56e55ccf6f93dfdc04c417816bf6a",
  "3fe71839b3d2c16bede3faa904b84eb592933379f4ebfd9fd983817c48b3bfa4",
  "127a6cc7aff20779826c299933da9f79c453b835027854683bddc84d2fd62b18",
  "7312c325818ac28e95ef3c13b35fdb11751b1ac9a64b725d1146d6086eec8c21",
  "30cb9f9e5dba629ab76009a466c95b6afdd8b4c725b96dbc9ac01edafc629dfe",
  "148cebbaa47e2bfc9293412e40ee1f2636d2f981687115867e1056d0de603459",
  "7c812283c7669320aa37c550b9780ca9f962eea2b4febe2d3436f84e36c60628",
  "25e58cd7241f8ba0793a3f180667b87a9ac2ec30aa2d6b4362e7fcd77183a539",
  "7acb9931024a3dbd0f43e7509927f222d69f3dff0439e714a73d6446c693fb2e",
  "7f4fcc21b042cce205ae672bae179cbccbb4724165ad8c5445e036a73ad8aeb2",
  "4c09f4dd187b678a87ce8e46e7b3118cfe6b596703b5a5381bcc0a87d6bb8951",
  "18d6a9969aba87a40eb4b1a7075d5700ac720ba4c9568503fc6f57b084dc81d0",
  "5607b8f8926a61050d8150317cb7b5e915c626edf1b387c6cc10f8b9a99d4ec3",
  "21d0f12ed2a0da134c783b16d12a0f221b61986e96d849ce19177f725d99cb86",
  "20ad658aec3e3a918c017dbc1b38f5f6ffb61a4bc936c44bd5005919d1e9fc2f",
  "37d64da1649836ce7399ccb47306147e4a589902784fd3b2450efa3c3dcdd416",
  "5d5024a71b109a0e298b884b9e4eb5eac1a8c43bf50f3c6e1cb4853f03891001",
  "7f73b9ef94c2e4901b0d8a45454673904f566d57c0aca4e7438dbb7eee9ee71a",
  "41e79e731bc83db74f1ea293b26d25f2816110dd17b9ef477e43ed88fb0075d4",
  "2b1da8131ba2b07124a85d0422fa63621fcb39d44b8b0813ce0e853790e8ddd3",
  "5aa66a39fd39211e563cc5425c0cea14effdc216a8a59364aa1744a4e9b3e078",
  "21f2b771bd1b66924b769dd4f5205e3db34ffd2cdc406ba2e7f370b1e8ee9e30",
  "40128f1cf83242f1eeb0fb2345bb44671971e6909dce497c3dc6c884dee5d28e",
  "2241ebeaa0acd605685abe0b2f0105a95281b18ab4f557a983cb869087734ce1",
  "60b4b2a68e2ac80cb0f98d2d01f5da5c10d20a25109e7e9b05aef7558f14a865",
  "519d258657344bb0b35a830d8fe3747c5dc7ee023800e781654cd5a381c91bfa",
  "65acedc2ee43d3cb2023814ff31c53f12a979dbbfb3314f9b6253e2a32dd2658",
  "3edd201210b02800becdc76deba64128f80b7a0d0899c7ab5c0cf26cf6acc5d2",
  "169bd4bd934940fdaa7bd009da19145e1d70517103231710e37b28da9977a13b",
  "2bcbbba3eff5a0b2c1571f795b1fc929c03dc8f9c0e043ae876f92011547da15",
  "78d17626744f31ef516121492465dfecf2debad4a7ab405eb97f019ac9f9c140",
  "61e7f323436e9f691d9db9706e5ead1ba4ed97d7c5fd5a3038856eb3b8f9959d",
  "5372642ff8b6e850a1ccc26c7edd3f31f908242598650a83be2fd856afdaa3fb",
  "73ee65d917e34519c8b71f485e2033d97c62ccee38fdc8dc0cc53aa790da019b",
  "0bd53ec274836c10f1666e65c4f905b8286a5d31c668226c7b28a6a98d8e0040",
  "3edd68336970ab95d0fb5202d1aeedbb7ff96473cdb6b7ccc842de06ee1d5807",
  "7226d8f6bb5b31b9295b056c555f7a92ddb9a998e95ef711d0e7e2d1e6ba77bb",
  "1f588b42e1894b67ee2e04bfadea3aed3500595de804ab27e7034d13eec0d26c",
  "458c70182c3b43f24798d731ae6c2eaaf62bfc492d18b754cdd7ce19dfa94a14",
  "3210c2b957f564c32775d45d08f604d30fba254c0e29727b2a3126c9ee49a233",
  "10ecba232651de480b2f75c4e621a309162aea93445d494f595978b724a62edb",
  "347218978a9e75bdfc3a368ae8285fe6233f25c1917da74743e1c83503df907a",
  "3e52e066bf4d1a8fa4e572857caaceadbb83b2f40c1bff97e277603eee7b1c87",
  "025bdff809818be0f5d9cad3b0bb95cbd0e7cdabc24715c3a694a22a29c807aa",
  "6e41bf7e9d686fa0f1d0d5d581cd2b4864aa7992bc263aad0379efbb93174146",
  "5945f7b51d798e9f0392f8736ab5b846e711520cd405f1b6f8b077637f66543a",
  "271f21bde7cd623667785b0bec2d2880b74562e9072ddcd9d94d8cd9f03fe44f",
  "61a1cf3885e8091afa3f64d7ab3026474e5a8375dca310b4a4ee0fd00fd4b20a",
  "0abb31e283989656c58b7d2ad803d82aae34884925b1a618f9a3b011ca2db13e",
  "57d1de8743952ab58bd2ca1a05c83485ea599a45e62f808a533dce8c69d67aac",
  "4311cb1ce4159875275b8ad100bb756f92a18ef4f767b0f4ed35030464df8919",
  "59c8b16296d12d8e071300c6c69f8b59015aad92b810a464d5c71776a5cc8d8b",
  "08ec66e54f5c5087c3a24a80692cc56acbf2cea6f105287ede09a4096008b236",
  "586e2e7113834f46763591781190964a9618fd9f257cdf28160b303e31d0cec3",
  "4d7e6c07ad8f3196ab363fae2c59bde6741b1d0635e56388618f06e202781501",
  "31683cc99658cc1f2c44565c71fab7deed491e67909dcc0bfbe8bf6311768da2",
  "0597d5fc92c94342fdec29435d7edd66df53da537da8deb9591c687b3d123e26",
  "2d8def80de50adbcb34eb67b38ca1ba30223b354940e5fd246e9ba70a2f21841",
  "6caad7e1025b9cd6b3e26f4be4f2a16f7130b3acc63bb2b671fc9d2a78b137c2",
  "7379498b4b3c5417e59bcec41fbe2da5e492015afb97495c9bc3a5979c1ea368",
  "7b051e5cc8318dd50a8690aaa2a0796ecc1a47bf8a97d5fed1692f4e54b93e9d",
  "613c8eaa79271d01e86a88ad8da85992954e9331cadbfa5e6d6ee316b83e0b0b",
  "48a940ac1a8c20af6d380e701b370e3b9bd86b51a7f586ac8237566105f89745",
  "7ad4866bb30dea649e6a57221551c87e576764a82e3afc54e8046df89b3c0634",
  "5a37751c5d1016bd6d1d1806a43435a4850901f0023a65e801d5c37d83b01b03",
  "4f6daa27c53136c918e94bea8fa981bf97e6158ef527489b557d120f188ac5e1"
]

user01@ubuntu:~$ bitcoin-cli -regtest getblockcount
202

```

### #블록 해시 구하기 [getblockhash 블록번호]

```
user01@ubuntu:~$ bitcoin-cli -regtest getblockhash 202
4f6daa27c53136c918e94bea8fa981bf97e6158ef527489b557d120f188ac5e1
```



### #계좌 생성 [getnewaddress]

```

user01@ubuntu:~$ bitcoin-cli -regtest getnewaddress test100
2N7EHkYKrLbKqDybPY6cFoXXJ3ts4ArAKGb	//공개키

user01@ubuntu:~$ bitcoin-cli -regtest getnewaddress test200
2NCPnDMEeKkHRujxZGiFoxvp9SpSfVnHAAA	//공개키

```

- 지갑 만들 때  생기는 공개키가 생성된다
- 돈을 붙혀야 하기 위해 해당 공개키를 알아야 한다.



### #잔액 확인 [getbalance]

```
user01@ubuntu:~$ bitcoin-cli -regtest getbalance

5050.00000000
```

```
user01@ubuntu:~$ bitcoin-cli -regtest getbalance test100
0.00000000
user01@ubuntu:~$ bitcoin-cli -regtest getbalance test200
0.00000000
```

-  현재 새로 만든 계정 test100, 200 에는 잔고가 없는 것을 볼 수 있음.
   -  Q. Linux 실행X ?

### #송금 [sendtoaddress 송금자 공개키]

-  계정 생성을 통해 알아낸 공개키로 송금.

```
user01@ubuntu:~$ bitcoin-cli -regtest sendtoaddress 2N7EHkYKrLbKqDybPY6cFoXXJ3ts4ArAKGb 10
07d2bf7027e3337a9222c849f8ad2431215ffe96c52c226919dec73830d6e4a4

```

- 현재 test100(공개키 : 2N7EHkYKrLbKqDybPY6cFoXXJ3ts4ArAKGb) 에게 10 코인 송금.
- 아래 뜨는 해시는 Transaction hash.

```
user01@ubuntu:~$ bitcoin-cli -regtest sendtoaddress 2NCPnDMEeKkHRujxZGiFoxvp9SpSfVnHAAA 10
a0bde38296a7a055492836a80ddbddce441e7b5a3422650cf52269f743e4f254

```

-  현재 test200(공개키 : 2N7EHkYKrLbKqDybPY6cFoXXJ3ts4ArAKGb) 에게 10 코인 송금.
-  아래 뜨는 해시는 Transaction hash.
-  하지만 잔고 확인 했을 때, 채굴 되지 않아서 잔고가 0 임.



### #Transaction 확인 [listunspent]

```
user01@ubuntu:~$ bitcoin-cli -regtest listunspent 0 | more
```

 "txid": "a0bde38296a7a055492836a80ddbddce441e7b5a3422650cf52269f743e4f254",
    "vout": 0,
    "address": "2NCPnDMEeKkHRujxZGiFoxvp9SpSfVnHAAA",
    "label": "test200",
    "account": "test200",
    "redeemScript": "00145efe8229afaaa20cf13f6830930dcf88557f69cd",
    "scriptPubKey": "a914d2089e2de9666a6ddc848b9f40c0c6e84fa7d4af87",
    "amount": 10.00000000,
    "confirmations": 0,
    "spendable": true,
    "solvable": true,
    "safe": true

confirmation 0 인것 test200 확인 가능, 채굴 되지 않은 상태



### #채굴 [generate]

```
user01@ubuntu:~$ bitcoin-cli -regtest generate 1
[
  "38c2e6305e89b911f86f9c9d14f562fc30d6abc96460ba54f0f4f0f27d0d75dd"
]
user01@ubuntu:~$ bitcoin-cli -regtest getblockhash 203
38c2e6305e89b911f86f9c9d14f562fc30d6abc96460ba54f0f4f0f27d0d75dd

```

- 미확정 트랜잭션을 확정하기 위해 채굴 실행
- 채굴을 시켜 이제 test100과 test200에 돈을 넣어줌
- generate 1을통해 블록 하나 채굴하였고 다음 블록해시 203이 생성된 것을 확인 가능



### #최종 잔고확인

```
user01@ubuntu:~$ bitcoin-cli -regtest getbalance test100
10.00000000

user01@ubuntu:~$ bitcoin-cli -regtest getbalance test200
10.00000000
```

-  test100, 200에 10 코인들이 송금된 것을 확인 할 수 있다.





------

### #블록생성 및 블록확인 요약본

- regtest : localtest  network

- 기본적으로 100개의 블록을 생성한 후 테스트

- 블록생성 및 블록확인

  - 블록생성(채굴) : genertate

  - ```
    user01@ubuntu:~$ bitcoin-cli -regtest generate 100
    [
      &quot;36a320505ab5b1df7ac102b6ee2907cd59719d4815a1654f5c4b26367ade2b47&quot;,
      &quot;2cdce9cd6b910c38b4531138cea4ac21127c7100d166ad03c15febe246bb4a87&quot;,
      &quot;75185437eb08b981646320ad1251aebe3cc12812ff2cf5f6517cf2aa1718cf91&quot;,
      &quot;0d154a6c7c86f4d7f1cb9c715667592a58aacb389735d5017ef5424ab468de88&quot;,
      &quot;638cd9959ec53c467254d79267ee913b575c70111cde77476171da25105502b8&quot;,
      &quot;31b8c0bf0b365181d7884947d56e573c2b6782ad987e42f9c01bc3dc48679cc9&quot;,
      &quot;25453286dc6ba33f237c7dbbeab479cb7b5a931c202c2979dbbedf1b0c1d3449&quot;,
      &quot;59a827ac5cac47f719b1347cc38e96cb67da794cbdadd4be8b6e55535b6c03a1&quot;,
      &quot;2f8f9c997924f5af6f14ff96fef76ed348cfa879cfe035e1c29b0b425483f055&quot;,
      &quot;004d1de5ed056c86195660138c61589c33b219819b51f1eadb74b2cd93d1e911&quot;,
      &quot;302814f0e2b4eaf0872b688c9d89edbf6f5cdd07ce4df3fe14eaa7abc5a5741d&quot;,
      &quot;2ee987fb0e7da65e8de20127d297bd45fc1e4fad191095dc5534c0dc41eed4c0&quot;,
      &quot;4ee2e46f9282974e0c14bb94d1557b6078752574394acc1db1c2d19e1bae2c07&quot;,
      &quot;2594984b4cb517b3f23b027001692ed92b99d81068bc3a3fafbe7362d29ad320&quot;,
      &quot;688866da5cc1b8c5de3fa6f346ec0579094479fd73bd6da33b827478efe14bc5&quot;,
      &quot;31a61824bf5c966fd0b08f514f10e3a9155a93c9c1a827e290382d57ba056988&quot;,
      &quot;4c1d743a2d13d2756cce3974e5d052df45ff91f647388aff54fe6060d0b1c732&quot;,
      &quot;2ffaab3c108ce73312c28fb911f13ec3134bf7827f6d6ff5e7e4fa3c81aac60b&quot;,
      &quot;22bbabc21498f423000a0557e4184d78848a056201759411995b448fe48738cb&quot;,
      &quot;46cae4520ebddbb1d699b754e9c3059d7c8dd79881a9223f30c4775a3a1dcfe2&quot;,
      &quot;65793133eeab47df2d74be8ba1d6e83da87362215e35abf73482fe58e549b04f&quot;,
      &quot;25e99580f7fd0c933b20e0478ca68f6b8b298c928f059d0f16f19b8582e5707e&quot;,
      &quot;1c3a048b471896dd8a39c6598416fbc4225653f761cc51f952f9b89933d3d9cb&quot;,
      &quot;7149f7f7d4e41d4c3685a6a91827f6c326d3dd858bbe1ceee361a1d73d74ab48&quot;,
      &quot;757b249ee46e72fc82b75b0239611b313408b815e616b9a45d2535d59834184d&quot;,
      &quot;054cbc381420c47111ca1da15d14d9c9ba8d89c1c40de760a0d87a0e7ed53b5f&quot;,
      &quot;0857cdb21e99cab262002f9f5882e68b65a9f6c52aa04df0bea345c6c26a962d&quot;,
      &quot;122f35cdf9b261826706242bfddc7235b5dd8948b44f36611f62b455f7eac052&quot;,
      &quot;72d8b2f9f6e21c4d76b7cb05d4e5368e730fc89393fde49c93a8a140162f07fe&quot;,
      &quot;651c7509c7fbcdde2d69f06b590ab8e71829271ba99b9d851f9716288af285c6&quot;,
      &quot;3bbe6269a339e6905475afadb47b69d00a6482e0821db73e91ead70a2d553912&quot;,
      &quot;083b8bab621ccb31224542242bdcccf0234f69435d563f00b01ab2fa047af051&quot;,
      &quot;0e06ce7b299f472194049160059236df79a920fb456fc83a50ca0bd589bb1e92&quot;,
      &quot;0e9cc636103aa94d27cc2b4d8ce0ecf6e2296dcef874f8f5aab9485da0db3079&quot;,
      &quot;154336fccd5d1bcea86b7c2d420bf72e8227e534ec5edec7fa3ad3b08cd3f24e&quot;,
      &quot;3f269ae494c5909da34d933bc7bbb446e08cf25d2852a3ea05d60ae92846da30&quot;,
      &quot;2d0d0f9df90ae7c6599abb7c28a02b5f1ea9c6b2852fc390ba75ea15b71e65e7&quot;,
      &quot;51ac1f1ee703536bc6e036a5ebf886136e1b142254e8ab2296817788c14fbc4a&quot;,
      &quot;27fbca78c9dd4d2be5e923f4478d418542e7c0ec889d23074d286885cdc6a57e&quot;,
      &quot;444a2b16b741e2623bc31100a10ea72667636499b49f5ea63299092f689632b9&quot;,
      &quot;467cfeb1c326bf06c377bb386bb428996e5453f6aada581f7b95da1dff7b24aa&quot;,
      &quot;181cc3188211a02a00df1e7ac286b866540bf53f815fbd7cd6b84544f3ae6a7b&quot;,
      &quot;6d245f8b7702794e302d58bccbb2d4d9fe31f14e0a5eb0d6e28ef05c74630724&quot;,
      &quot;4e1b596fb5b3e126c7aa47a7d686603db37c84fbf3bb783bdca0656ac2b0cbf9&quot;,
      &quot;5519a609b4266b1ed7c36a3f739b6919bff6fadb6036a11cd310bccbcaada44b&quot;,
      &quot;76f0e7fac2b8847614788907c91a529fcbbe162146be2f4a2d17802c6e9e23ef&quot;,
      &quot;16c51909788daee18bc9d280345ecde220cd989f644c835c7cb6517330791ad2&quot;,
      &quot;2b4928a418aade6c972bc62802239e81debb8b805da4a80109ef2f5dce8d6893&quot;,
      &quot;7274b19de238cc22079490c2ed90ccf2f507e1ca2d759227b7e460a9703be82e&quot;,
      &quot;6fe28fc15d9df7b3582cdee498a5f1bb3c6a8709ddffd02361d25c42f3ae75b0&quot;,
      &quot;0915665914bc91791af4d1206e29247d7c31e53349e46f5f8da890eead25568d&quot;,
      &quot;5f4b1464161b560a6b78244d517e531c9b5b33712469b998603429a660f8bd30&quot;,
      &quot;398ac70d9143e84c4f9fdbafc7079da50b0d51488e0a8c3a798df929666afc6e&quot;,
      &quot;0b9172d34eafe07a0259775118177af8834c6feb8b51b0b81e6e836033362bde&quot;,
      &quot;3488e74b315472c1035a87cfa33fa438b3bee64969fc7124394dff364d897549&quot;,
      &quot;73df85861a1aea7b5eec7de81619303d6ccf51e02f7a4aab04687e9b3191d0ed&quot;,
      &quot;580883b5cd68a44f2d828726c0be79b6fd9d07280656110a90946b2ff3fd6ebc&quot;,
      &quot;74f6aa3941e4b1dcfca82809b53fe5ba5ea7ea41801161230d969b73cacd3c14&quot;,
      &quot;7842f0249effce35ba184bd7e0bb3ede6ca58d91d7080aa383aba705be94c857&quot;,
      &quot;6a4101d89bfd58405b6b795bfbb66f22b4a461bc644152d234de2e5c199e807e&quot;,
      &quot;3d865babe30cc2793e7ae555d454394edd4f30798315d9c33d5dd45ab4bfd938&quot;,
      &quot;49a09498b8640bf73401b1cd2947ff38c00b62b2294b5d7f3b257308ec7c2a8a&quot;,
      &quot;7e754e4fd25f02339573b07a4f0a009b06618dff20cb76e1e177c15b18629d81&quot;,
      &quot;6cdc6aa2f2343571ab973ff9db75df20ca99462b6273baae9fd99081e8f8ba69&quot;,
      &quot;5cf8c5f475b774f52ceaffddd1c8720fddd2d658c07023a35df5ae4783bd734f&quot;,
      &quot;2a1d1186e689a05ce27e7cdb7753fb29fcfdfa2a56dc10dc265237862abf70dc&quot;,
      &quot;3c01818948c5b3a5f920180f88a43189cfe8011eae0addaee86da13c9fb8a479&quot;,
      &quot;4c0de3539566c276145d8f2e23580bcf0e1ed4aff7aa99e319ba6d06d1337605&quot;,
      &quot;50645a766cedde49a3278fba755fb802d9e7d48c33b4c23bddc7e0ccd92f51e9&quot;,
      &quot;77a3480d0f0d78460ce4ce4c9c0952f08489857fac1219963776e5b2dda3f3b3&quot;,
      &quot;33b39fb6c9402ee8eea4eab59e63fce42364da5545d55c3ea1c74f7ee222e2db&quot;,
      &quot;124a6c984243911bf9aaf50d5c2462669b7b2cb7f6c0985a834bfa5f0cd85abc&quot;,
      &quot;1a4d9be7d17c937567be9929b39c28048b7ad833a54945dffea8966a9dfbaca6&quot;,
      &quot;60a54a5c3ea5702ef5979a47eb87a5f52e5421fc3280c0033622e72b7bb14b0a&quot;,
      &quot;2e2941b3a77c2a5a66c38099945af9a5cda0477482bdb139daffece63912450e&quot;,
      &quot;1561299f4ebd2d369b59efbb1e109b9f54e3f70bad3370dbe9cfc0dfbea457e4&quot;,
      &quot;49238d492926eabe369a7615a4bea6db57ee5b2fa6fc59747d8e5d33a0969f92&quot;,
      &quot;2541f968414d25f603a88541a86f55c373c8ca5452e51a00c019cf0b09431dc3&quot;,
      &quot;550f91dc6905c5bfd5175a55707d5118ff4c22e194bd9394a3ae97e6fca45ce5&quot;,
      &quot;749f61fa20dad98cfe1e82f8edc656ab995c9b88b2ff8e8e0af0164ad79dc714&quot;,
      &quot;6c47f807038c66a8e424ee3170232481bc270099098ca7ca8858ee7b9ef8d1ab&quot;,
      &quot;2a6b4e07388a29fbcbf3796d6fea9cf5b517b74f8333da82b7ab60e48d79017e&quot;,
      &quot;3e4bf13689c4576c4189ba8d4341c48c698318c877ee8180729ddded1bb1512c&quot;,
      &quot;086e0ea59ab89415980c44491b9fadf5caceb4f51cf6a5e59fd249b4a5b6edf2&quot;,
      &quot;2679795ef32cc2ec93f598dd6580ba7b53704bcb729c35f9dbf99824183e76c1&quot;,
      &quot;0db32c845a5257ae8a1036c5b38b28e3207b624ac2ddd14f83c6af40598524bb&quot;,
      &quot;551416fc38c16760f81a60324a41f071570178a579d34766d0afed111181f2c7&quot;,
      &quot;01d063c412f2f389cadb55fc89ee5bafe8ae212f6521599000f77191f2cc2f78&quot;,
      &quot;45ba605ae1889e7613985fdcb0f58bc5f821e76fa80ee91b2875d86d2829e0fd&quot;,
      &quot;08cd14ad97a8b226174187aa508e5db68f89a0ba12d317bea1663dbd27f47b3b&quot;,
      &quot;20c3f4108f60dc17f9fe3edd784d1d571fb1c69779ee9edd6aa1a05b8e615af6&quot;,
      &quot;709d8ba3d36904300e74352a5b8fc47c546b2b6e41bafe13f5b1219aaa5af55f&quot;,
      &quot;54523465842f3e259347498f48509eac42ad18f159b1da7aceb85e50fac275dc&quot;,
      &quot;29fc1a3bbc614adb91d8bf5a9593c0329fb8f45ef3e19b25065c329d32d7b59e&quot;,
      &quot;68d2eb42283e2ff358f36c9886a38de9dd8919b81fb52d9f862afb9cacefff09&quot;,
      &quot;4766c2af985a4a503e4cfb613950357def1428ca2d2941745cc6c541bcd2e8a8&quot;,
      &quot;78bf0f2210954336dfc951da5ccf1c34459f1fea2d8a8cc751ad2d38e769a816&quot;,
      &quot;3e17624dd43ef37a9f2b8b586ea9dd7aa9987469ade8c5fdfc53087f0504c699&quot;,
      &quot;623ceaa56c8e2e9e3434f0afb3a521c7875a906eeb86acdeb083e2999e29d4a8&quot;,
      &quot;185a2c2403d4738cca8902686e309507b115063f8e48dc79493726d443a237f9&quot;
    ] 
    ```

    블록 100개 생성

  - 블록확인 : getblockcount

  - ```
    user01@ubuntu:~$ bitcoin-cli -regtest getblockcount
    303
    ```

    해당 블록 해시 확인 : getblockhash

    ```
    user01@ubuntu:~$ bitcoin-cli -regtest getblockhash 303
    185a2c2403d4738cca8902686e309507b115063f8e48dc79493726d443a237f9
    ```

    : 마지막 블록(303)의 해시값을 출력

  - 해당 해시 정보 확인 : getblock  해시값

    ```
    user01@ubuntu:~$ bitcoin-cli -regtest getblock 185a2c2403d4738cca8902686e309507b115063f8e48dc79493726d443a237f9
    {
      "hash": "185a2c2403d4738cca8902686e309507b115063f8e48dc79493726d443a237f9",
      "confirmations": 1,
      "strippedsize": 228,
      "size": 264,
      "weight": 948,
      "height": 303,
      "version": 805306369,
      "versionHex": "30000001",
      "merkleroot": "ac86f15f13cf2b73a644ff4fb26e089e533d2baca2c67be59c4593a1f7ce8c3e",
      "tx": [
        "ac86f15f13cf2b73a644ff4fb26e089e533d2baca2c67be59c4593a1f7ce8c3e"
      ],
      "time": 1530587674,
      "mediantime": 1530587673,
      "nonce": 1,
      "bits": "207fffff",
      "difficulty": 4.656542373906925e-10,
      "chainwork": "0000000000000000000000000000000000000000000000000000000000000260",
      "previousblockhash": "623ceaa56c8e2e9e3434f0afb3a521c7875a906eeb86acdeb083e2999e29d4a8"
    }
    ```

    "previousblockhash": "623ceaa56c8e2e9e3434f0afb3a521c7875a906eeb86acdeb083e2999e29d4a8"

    : 이전 블록 해시가 구조체 안에 할당됨

    ```
    user01@ubuntu:~$ bitcoin-cli -regtest getblockhash 302
    623ceaa56c8e2e9e3434f0afb3a521c7875a906eeb86acdeb083e2999e29d4a
    ```

  - 계정 생성 : getnewaddress  계정명

    - 계정의 공개키 주소 값

      ```
      user01@ubuntu:~$ bitcoin-cli -regtest getnewaddress testuser101
      2N83N5zoGnAYWSp8MCwLZuA8Yw1HQi63zTf
      user01@ubuntu:~$ bitcoin-cli -regtest getnewaddress testuser102
      2Mt2cKk84QkNpMkGiksXoFcuEevYsNipCAT
      ```

  - 비밀키 확인 : dumpprivkey 해쉬값

    ```
    user01@ubuntu:~$ bitcoin-cli -regtest dumpprivkey 2N83N5zoGnAYWSp8MCwLZuA8Yw1HQi63zTf
    cRb2sKVHGeJEbXfZvpbTkZF3YYCDcmA7T4MH7cfXMDYzwByvt2Do
    
    ```

    비밀키를 확인 할 수 있다.

  - 잔고확인 : getbalance

    - node가 채굴자/계정 생성 : bitcoin-cli -regtest getbalance -> 채굴자 주인의 전체 잔고
    - 계정 잔고 : bitcoin-cli -regtest getbalance 계정 -> 해당 계정의 전체 잔고

    ```
    user01@ubuntu:~$ bitcoin-cli -regtest getbalance
    8750.00000000
    user01@ubuntu:~$ bitcoin-cli -regtest getbalance testuser101
    0.00000000
    user01@ubuntu:~$ bitcoin-cli -regtest getbalance testuser102
    0.00000000
    
    ```

  - 송금 : Transaction 발생 

    - sendtoaddress 수신자주소(해쉬) 금액

      - 트랜잭션 식별번호(TxId) 생성

      - ```
        user01@ubuntu:~$ bitcoin-cli -regtest sendtoaddress 2N83N5zoGnAYWSp8MCwLZuA8Yw1HQi63zTf 100	//testuser1 에게 100 사토시
        d6e781f58a4e555e5dbadceb63bb823e6892f75d471453a7c483850bcb9afb9d
        user01@ubuntu:~$ bitcoin-cli -regtest sendtoaddress 2Mt2cKk84QkNpMkGiksXoFcuEevYsNipCAT 10 //testuser2 에게 10 사토시
        ed206326f0370b36701d04144eff7db81fd221466eb6adecd493226497582c47
        
        ```

        송금을 하게 되면서 수수료가 발생하게되고, 보내는 사람한테 발생하고, 받는 사람은 상관 없음. 

        - 송금액 금액과는 관련없고, 트랜잭션의 사이즈에 의해 할당
        - 0.0005BTC 정도 발생 (수수료 없는 거래소도 있음)

        

        하지만 getbalance를 했을 때 아직 채굴이 미확정 되었고, 거래 장부에는 testuser101에게 100사토시 testuser102에가게 10사토시를 보낸 기록이 남아있음, 따로 채굴을 통해서 확정시켜줘야 함.

  - listunspent : 블록 체결 list

  - ```
    user01@ubuntu:~$ bitcoin-cli -regtest listunspent 0 10
    [
      {
        "txid": "ed206326f0370b36701d04144eff7db81fd221466eb6adecd493226497582c47",
        "vout": 0,
        "address": "2N8DZaLbEQkFjcJ1NCNMtQUpPsLVfzgvnBX",
        "redeemScript": "001467e6d7d94d9b75dbbf8884879d03a2272044c73c",
        "scriptPubKey": "a914a43967c5c4685351db94448ab4009f970867391b87",
        "amount": 14.99996240,
        "confirmations": 0,
        "spendable": true,
        "solvable": true,
        "safe": true
      },
      {
        "txid": "ed206326f0370b36701d04144eff7db81fd221466eb6adecd493226497582c47",
        "vout": 1,
        "address": "2Mt2cKk84QkNpMkGiksXoFcuEevYsNipCAT",
        "label": "testuser102",
        "account": "testuser102",
        "redeemScript": "0014a3e4d03f981a91863486b8fe4d22f0b97cf2b242",
        "scriptPubKey": "a91408955ceff23df25e7323476167ae97e665b7771487",
        "amount": 10.00000000,
        "confirmations": 0,
        "spendable": true,
        "solvable": true,
        "safe": true
      },
      {
        "txid": "d6e781f58a4e555e5dbadceb63bb823e6892f75d471453a7c483850bcb9afb9d",
        "vout": 0,
        "address": "2N3j4fHYMo2MGQXhzTzNXcbCgKttTUbixnk",
        "redeemScript": "00149071e7c86a8f15af2e8c9af08a41dcd493419c66",
        "scriptPubKey": "a91472f51e575c14c3213181ae8d8539244ed03216bb87",
        "amount": 9.99992120,
        "confirmations": 0,
        "spendable": true,
        "solvable": true,
        "safe": true
      },
      {
        "txid": "d6e781f58a4e555e5dbadceb63bb823e6892f75d471453a7c483850bcb9afb9d",
        "vout": 1,
        "address": "2N83N5zoGnAYWSp8MCwLZuA8Yw1HQi63zTf",
        "label": "testuser101",
        "account": "testuser101",
        "redeemScript": "0014b8dbdac8fd2dadc83947b2d633459cb62cf1f13f",
        "scriptPubKey": "a914a24ba7cf5f1c3dfb6e44317877fe0bb7782ee2bf87",
        "amount": 100.00000000,
        "confirmations": 0,
        "spendable": true,
        "solvable": true,
        "safe": true
      }
    ]
    ```

    confirm 되지 않은 것 0.

    - 현재 채굴자

      ```
      user01@ubuntu:~$ bitcoin-cli -regtest getbalance
      8749.99988360
      
      ```

    - 블록해시

      - 송금확인 - listunspent 0 10 (0~10개 confirm)

      - 블록개수확인 - getblockcount

      - 블록해시 - getblockhash 블록번호

      - 블록해시내용 - getblock

      - ```
        user01@ubuntu:~$ bitcoin-cli -regtest generate 1
        [
          "325406a8af2754fe5466fb3f20905c9dda6d0835661e1f4391343c37befff78c"
        ]
        user01@ubuntu:~$ bitcoin-cli -regtest listunspent 0 10
        [
          {
            "txid": "ed206326f0370b36701d04144eff7db81fd221466eb6adecd493226497582c47",
            "vout": 0,
            "address": "2N8DZaLbEQkFjcJ1NCNMtQUpPsLVfzgvnBX",
            "redeemScript": "001467e6d7d94d9b75dbbf8884879d03a2272044c73c",
            "scriptPubKey": "a914a43967c5c4685351db94448ab4009f970867391b87",
            "amount": 14.99996240,
            "confirmations": 1,
            "spendable": true,
            "solvable": true,
            "safe": true
          },
          {
            "txid": "ed206326f0370b36701d04144eff7db81fd221466eb6adecd493226497582c47",
            "vout": 1,
            "address": "2Mt2cKk84QkNpMkGiksXoFcuEevYsNipCAT",
            "label": "testuser102",
            "account": "testuser102",
            "redeemScript": "0014a3e4d03f981a91863486b8fe4d22f0b97cf2b242",
            "scriptPubKey": "a91408955ceff23df25e7323476167ae97e665b7771487",
            "amount": 10.00000000,
            "confirmations": 1,
            "spendable": true,
            "solvable": true,
            "safe": true
          },
          {
            "txid": "d6e781f58a4e555e5dbadceb63bb823e6892f75d471453a7c483850bcb9afb9d",
            "vout": 0,
            "address": "2N3j4fHYMo2MGQXhzTzNXcbCgKttTUbixnk",
            "redeemScript": "00149071e7c86a8f15af2e8c9af08a41dcd493419c66",
            "scriptPubKey": "a91472f51e575c14c3213181ae8d8539244ed03216bb87",
            "amount": 9.99992120,
            "confirmations": 1,
            "spendable": true,
            "solvable": true,
            "safe": true
          },
          {
            "txid": "d6e781f58a4e555e5dbadceb63bb823e6892f75d471453a7c483850bcb9afb9d",
            "vout": 1,
            "address": "2N83N5zoGnAYWSp8MCwLZuA8Yw1HQi63zTf",
            "label": "testuser101",
            "account": "testuser101",
            "redeemScript": "0014b8dbdac8fd2dadc83947b2d633459cb62cf1f13f",
            "scriptPubKey": "a914a24ba7cf5f1c3dfb6e44317877fe0bb7782ee2bf87",
            "amount": 100.00000000,
            "confirmations": 1,
            "spendable": true,
            "solvable": true,
            "safe": true
          }
        ]
        
        ```

        confirm 된 것을 확인.(채굴됨) generate 1을 통해 블록 하나씩 생성, confirm도 같이 증가되는 것을 볼 수 있다. 

        ```
        
        user01@ubuntu:~$ bitcoin-cli -regtest getblockcount
        307
        user01@ubuntu:~$ bitcoin-cli -regtest getblockhash 307
        7088cdf8beb384184136b11c48cc76d416b4e16c78d50a1127737aa532874926
        user01@ubuntu:~$ bitcoin-cli -regtest getblock 7088cdf8beb384184136b11c48cc76d416b4e16c78d50a1127737aa532874926
        {
          "hash": "7088cdf8beb384184136b11c48cc76d416b4e16c78d50a1127737aa532874926",
          "confirmations": 1,
          "strippedsize": 228,
          "size": 264,
          "weight": 948,
          "height": 307,
          "version": 805306369,
          "versionHex": "30000001",
          "merkleroot": "f7475a4011511f765fbf17a35632520bea0990da5c6e195f81ecfac743aaa167",
          "tx": [
            "f7475a4011511f765fbf17a35632520bea0990da5c6e195f81ecfac743aaa167"
          ],
          "time": 1530597107,
          "mediantime": 1530587674,
          "nonce": 4,
          "bits": "207fffff",
          "difficulty": 4.656542373906925e-10,
          "chainwork": "0000000000000000000000000000000000000000000000000000000000000268",
          "previousblockhash": "1d8909adb482e043bf5010cc2d15d77ab1ca2ccc5d669ecef2fff615fb869622"
        }
        
        ```

        : 현재 블록 개수 확인(getblockcount)하였고, 마지막이 307이라는 것을 확인, 해당 307블록 해시 값 확인하기 위해(getblockhash) 사용하여 해시 값 도출 하여 해당 해시 블록의 정보(getblock) 통해 그 블록안에 어떤 거래가 남아 있는지 확인 가능함.

------

### #.bitcoin 디렉터리

```
user01@ubuntu:~$ cd .bitcoin
user01@ubuntu:~/.bitcoin$ ls
blocks  regtest  wallets
user01@ubuntu:~/.bitcoin$ cd regtest/
user01@ubuntu:~/.bitcoin/regtest$ cd blocks/
user01@ubuntu:~/.bitcoin/regtest/blocks$ ls
blk00000.dat  index  rev00000.dat
user01@ubuntu:~/.bitcoin/regtest/blocks$ ls -al
total 17420
drwx------ 3 user01 user01     4096 Apr 14 17:27 .
drwx------ 5 user01 user01     4096 Jul  3 14:55 ..
-rw------- 1 user01 user01 16777216 Jul  3 14:51 blk00000.dat
drwx------ 2 user01 user01     4096 Jul  3 11:17 index
-rw------- 1 user01 user01  1048576 Jul  3 14:51 rev00000.dat

```



[BlockChain](www.blockchain.com)

:블록체인 Transaction 확인 사이트

- product > explorer >  최신 블록 클릭
- 계속 거래된 Transaction 들을 모아서 (10분 간) 하나에 블록에 넣게됨
- 채굴을 1등 한 사람에게만 이익금 발생(다른 채굴자들에게 할당되지 못함)

[Coding ground](www.tutorialspoint.com)

: Ideone 같은 코딩 사이트

------



### #MerkleTree_python

머클루트 건들기 위해 사용 transaction 잡혔고 두개 합쳐서 머클루트 만들어지는 것을 보여주기 위해 Test

shared 에서 가져오기 파이썬파일

vi merkelTreeDemo.py

복붙하고 

python MerkleTreeDemo.py  컴파일



BlockChain 사이트 99997 검색해보면 결과값과 머클루트값 동일

------



### #하드포크 & 소프트포크

- 하드포크 : 강력한 업그레이드 방식, 기능이나 잘못된 거래 기록됐을때 완전 패치하기 위해 두갈래로 나눔

- 소프트 포크 : 기존 체인 그대로 직어내서 수정하여 다시 체인에 덧붙이는 기술

  +세그윗 : 거래기록에서 서명부분 분리해 거래내역 포함할 수 있게 만드는 작업

  +언리미티드는 블록 크기 자체만 변경



------



### #빅엔디안 & 리틀엔디안

- 빅엔디안 : R >>> L ,메모리 시작 주소에 상위 바이트 부터 기록
- 리틀엔디안 : R <<< L , 메모리 시작 주소가 하위 바이트부터 기록

------

### #블록헤더

- 블록헤더

- ```
  getblock "blockhash" ( verbosity )
  
  If verbosity is 0, returns a string that is serialized, hex-encoded data for  block 'hash'.
  If verbosity is 1, returns an Object with information about block <hash>.
  If verbosity is 2, returns an Object with information about block <hash> and  information about each transaction.
  
  Arguments:
  1. "blockhash"          (string, required) The block hash
  2. verbosity              (numeric, optional, default=1) 0 for hex encoded da ta, 1 for a json object, and 2 for json object with transaction data
  
  Result (for verbosity = 0):
  "data"             (string) A string that is serialized, hex-encoded data for  block 'hash'.
  
  Result (for verbosity = 1):
  {
    "hash" : "hash",     (string) the block hash (same as provided)
    "confirmations" : n,   (numeric) The number of confirmations, or -1 if the  block is not on the main chain
    "size" : n,            (numeric) The block size
    "strippedsize" : n,    (numeric) The block size excluding witness data
    "weight" : n           (numeric) The block weight as defined in BIP 141
    "height" : n,          (numeric) The block height or index
    "version" : n,         (numeric) The block version
    "versionHex" : "00000000", (string) The block version formatted in hexadeci mal
    "merkleroot" : "xxxx", (string) The merkle root
    "tx" : [               (array of string) The transaction ids
       "transactionid"     (string) The transaction id
       ,...
    ],
    "time" : ttt,          (numeric) The block time in seconds since epoch (Jan  1 1970 GMT)
    "mediantime" : ttt,    (numeric) The median block time in seconds since epo ch (Jan 1 1970 GMT)
    "nonce" : n,           (numeric) The nonce
    "bits" : "1d00ffff", (string) The bits
    "difficulty" : x.xxx,  (numeric) The difficulty
    "chainwork" : "xxxx",  (string) Expected number of hashes required to produ ce the chain up to this block (in hex)
    "previousblockhash" : "hash",  (string) The hash of the previous block
    "nextblockhash" : "hash"       (string) The hash of the next block
  }
  
  Result (for verbosity = 2):
  {
    ...,                     Same output as verbosity = 1.
    "tx" : [               (array of Objects) The transactions in the format of  the getrawtransaction RPC. Different from verbosity = 1 "tx" result.
           ,...
    ],
    ,...                     Same output as verbosity = 1.
  }
  
  Examples:
  > bitcoin-cli getblock "00000000c937983704a73af28acdec37b049d214adbda81d7e2a3 dd146f6ed09"
  > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", " method": "getblock", "params": ["00000000c937983704a73af28acdec37b049d214adbd a81d7e2a3dd146f6ed09"] }' -H 'content-type: text/plain;' http://127.0.0.1:833 2/
  
  ```

  

  - #### version

    - 블록버전, 4byte(DataType : int32_t)

      : 프로토콜의 업그레이드 및 변경 사항을 추적하는데 사용

      

  - #### previousblockhash

    - 이전 블록 해시

      : 블록체인의 이전 블록 헤더의 해시, 32byte(DataType : char[32])

      Little-endian format(R<<<L)

      SHA256(SHA256()) hash 적용(길이 64자* 4byte)

      이전 블록에 대한 연결이며 체인을 보호

      (이 블록 헤더를 변경하지 않고 이전블록 헤더 변경 불가함.)

      

  - #### merklehash

  - #### time(TimeStamp)

    - 블록의 생성 시간, 4byte(DataType : uint32_t)

      : 해당 시간에 그 데이터가 존재했음을 증명.

      타임 스탬프는 miners에 의해 선택

      miners가 헤더를 해싱하기 시작한 Unix epoch 시간

      두 시간 이상 헤더가 있는 블록을 허용 X

      타임 스탬프는 이전 11개 블록의 중간 타임 스탬프보다 크고 네트워크 조정시간 + 2시간 보다 작은 경우 유효한 것으로 간주

      네트워크 조정 시간은 연결된 모든 노드에서 반환 한 타임 스탬프의 중간 값

      Mediantime 은 가장 최근 블록 앞에 있는 11개 블록 타임 스탬프의 중간 시간.

      ​	+DCode 파일을 통해 Unix 32bit Little Endian 타입 (Hexa 값) or Unix Numeric value(숫자) 으로 입력하면 해당 시간 확인 가능. (한국은 UTC + 9시간 적용)

    - /* smart contract timestamp manipulation attack, smart contract front running attack*/

    - 블록이 만들어 지기 전 과정이 해킹에 취약함

  - #### bits

    - 난이도 목표 : 작업증명 난이도,

  - #### nonce 

    - 소프웨어 버젼, 이전 블록 해시,  머클 트리 해시, 블록 생성시간(TimeStamp), 채굴 난이도,  Nonce를 포함하고 있고 이 6가지 요소들이 중요함

------



### #마무리

vmware -> linux 스냅샷

계정 동일 >> 아무것도 없는 Linux 에서 작동 >> 나만의 bitcoin 데몬 설치

















































### 명령어 모음

user01@ubuntu:~$ bitcoin-cli --help
Bitcoin Core RPC client version v0.16.99.0-5f2a399

Usage:
  bitcoin-cli [options] <command> [params]  Send command to Bitcoin Core
  bitcoin-cli [options] -named <command> [name=value] ... Send command to Bitcoin Core (with named arguments)
  bitcoin-cli [options] help                List commands
  bitcoin-cli [options] help <command>      Get help for a command

Options:

  -?
       This help message

  -conf=<file>
       Specify configuration file. Relative paths will be prefixed by datadir
       location. (default: bitcoin.conf)

  -datadir=<dir>
       Specify data directory

  -getinfo
       Get general information from the remote server. Note that unlike
       server-side RPC calls, the results of -getinfo is the result of
       multiple non-atomic requests. Some entries in the result may
       represent results from different states (e.g. wallet balance may
       be as of a different block from the chain state reported)

Chain selection options:

  -regtest
       Enter regression test mode, which uses a special chain in which blocks
       can be solved instantly. This is intended for regression testing
       tools and app development.

  -testnet
       Use the test chain

  -named
       Pass named instead of positional arguments (default: false)

  -rpcclienttimeout=<n>
       Timeout in seconds during HTTP requests, or 0 for no timeout. (default:
       900)

  -rpcconnect=<ip>
       Send commands to node running on <ip> (default: 127.0.0.1)

  -rpcpassword=<pw>
       Password for JSON-RPC connections

  -rpcport=<port>
       Connect to JSON-RPC on <port> (default: 8332 or testnet: 18332)

  -rpcuser=<user>
       Username for JSON-RPC connections

  -rpcwait
       Wait for RPC server to start

  -rpcwallet=<walletname>
       Send RPC for non-default wallet on RPC server (needs to exactly match
       corresponding -wallet option passed to bitcoind)

  -stdin
       Read extra arguments from standard input, one per line until EOF/Ctrl-D
       (recommended for sensitive information such as passphrases).
       When combined with -stdinrpcpass, the first line from standard
       input is used for the RPC password.

  -stdinrpcpass
       Read RPC password from standard input as a single line.  When combined
       with -stdin, the first line from standard input is used for the
       RPC password.



------

## #Linux 에 bitcoincore 적용

```
user01@ubuntu:~$ sudo mkdir bitcoincore

[sudo] password for user01:

user01@ubuntu:~$ cd bitcoincore/

user01@ubuntu:~/bitcoincore$ sudo mkdir src

user01@ubuntu:~/bitcoincore$ cd src/

user01@ubuntu:~/bitcoincore/src$ sudo git clone https://github.com/bitcoin/bitcoin.git

user01@ubuntu:~/bitcoincore/src$ sudo apt-get update

```

### #gcc 설치

```
user01@ubuntu:~/bitcoincore/src$ sudo apt-get install build-essential automake pkg-config libevent-dev bsdmainutils -y
```

### #openssh 설치

```
user01@ubuntu:~/bitcoincore/src$ sudo apt-get install libtool autotools-dev autoconf

user01@ubuntu:~/bitcoincore/src$ sudo apt-get install libssl-dev

```

### #Boost설치

```
user01@ubuntu:~/bitcoincore/src$sudo apt-get install libboost-all-dev
```

### #libdb4.8 설치

```
user01@ubuntu:~/bitcoincore/src$sudo add-apt-repository ppa:bitcoin/bitcoin

user01@ubuntu:~/bitcoincore/src$sudo apt-get update

user01@ubuntu:~/bitcoincore/src$sudo apt-get install libdb4.8-dev

user01@ubuntu:~/bitcoincore/src$sudo apt-get install libdb4.8++-dev

```



### #관련라이브러리 설치

```
user01@ubuntu:~/bitcoincore/src$sudo apt-get install libminiupnpc-dev

user01@ubuntu:~/bitcoincore/src$sudo apt-get install libqrencode-dev

```



### #GUI 라이브러리 설치

```
user01@ubuntu:~/bitcoincore/src$sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools libprotobuf-dev protobuf-compiler
```



### #빌드

```
user01@ubuntu:~/bitcoincore/src$ cd bitcoin/

user01@ubuntu:~/bitcoincore/src/bitcoin$sudo ./autogen.sh

user01@ubuntu:~/bitcoincore/src/bitcoin$sudo ./configure

user01@ubuntu:~/bitcoincore/src/bitcoin$sudo make

user01@ubuntu:~/bitcoincore/src/bitcoin$sudo make install

```



### #테스트 네트워크

- testnet 

  - 인터넷 상에서 동작하는 테스트 네트워크

  - 테스트용 BTC사용, 대량의 블록체인이 존재하기 때문에 처음 시작할때 모든 데이터 취득

    

- regtest

  -  로컬PC내에서의 테스트 네트워크

  - 계정 생성 및 채굴

  - 블록체인 초기화도 쉽게 하기 위한 실험용

    


 터미널에서
 bitcoind -regtest -daemon

다른 터미널에서 bitcoin-cli로 접속

---

### #20180703.txt

```

* USB의 블록체인 폴더 Desktop에 복사

 c:\블록체인
 -Blockchain.zip 압축해제


*3주 자료실 - 즐겨찾기
- 접속여부 확인

Desktop 사용자 - 유선
http://192.168.0.105/


노트북 사용자 - 무선
http://172.17.138.113:8080


* 환경 구축
- Desktop 사용자는 
  필히 VirtualBox-5.0.28-111378-Win.exe 설치

 =>신뢰할 수 있는 Oracle Driver 체크


- 노트북 사용자는 VirtualBox-5.0.28-111378-Win.exe 설치후

  에러 발생하면 삭제후 
  VirtualBox-5.2.12-122591-Win.exe 최신버전으로 업데이트


* VirtualBox설치 후
 - 메뉴 바 -> 파일 -> 환경설정 -> 확장 -> 옆 버튼 눌러서
   확장 패키지 설치 -> 
   Oracle_VM_VirtualBox_Extension_Pack-5.0.28-111378a.vbox-extpack

* VirtualBox
 - 메뉴 바 -> 머신 -> 추가 
    (Blockchain.zip 압축해제 폴더에서 Blockchain.vbox 선택)

* VirtualBox
 - 툴바 -> 스냅 샷 -> 네개의 스냅샷 확인

 - bitcoin core 선택 -> 가상머신 복원

 
  가상머신 계정
  user01/qwer1234





test100  //사용자
2N7EHkYKrLbKqDybPY6cFoXXJ3ts4ArAKGb


test200
2NCPnDMEeKkHRujxZGiFoxvp9SpSfVnHAAA

비트코인
 -regtest : localtest network
=>기본적으로 100개의 블록을 생성한 후 테스트

* 블록생성 및 블록확인
1)블록생성(채굴) : generate
2)블록 개수      : getblockcount

3) 계정 생성 :  getnewaddress 계정명
   - 계정의 공개키 주소 
 bitcoin-cli -regtest getnewaddress testuser101
2N83N5zoGnAYWSp8MCwLZuA8Yw1HQi63zTf
 
bitcoin-cli -regtest getnewaddress testuser102
2Mt2cKk84QkNpMkGiksXoFcuEevYsNipCAT



4) 잔고확인 : getbalance
 - node가 채굴자/계정 생성 : bitcoin-cli -regtest getbalance
 - 계정 잔고 : bitcoin-cli -regtest getbalance 계정명


5) 송금 - 트랜잭션 발생 :  sendtoaddress 받는사람주소 금액
  - 트랜잭션 식별번호(TxId)생성
 100
279aff1e3145d409debeffdd60caec289f9d3a8a35c1f44c73d60b635a59768a

 10
15294ba46ff677d9bd7d2fbad1189ae51f2755eca72a4c905b01a95f66dcbc20

=> 수수료 발생 ; 보내는 사람 발생, 받은 사람은 상관없음
   - 송금액 금액과는 관련 없음
   - 트랜잭션의 사이즈
     0.0005 BTC


bitcoin-cli -regtest getbalance
8749.99988800


블록해시
4f693b461febf632ba01bf951d953d5cbd68716bd3d4e2fe64d9785af2cbf557"


1) 송금확인  - listunspent 0 10
2) 블록개수확인 -  getblockcount

3) 블록해시   -  getblockhash 304

4) 블록해시내용 -  getblock  해시값
 




* 타임스탬프
목적: 해당 시간에 그 데이터가 존재했음을 증명
      이전 타임 스탬프를 강화하는 형태로 체인형성



  "time": 1530596876,
  "mediantime": 1530591723,
```

