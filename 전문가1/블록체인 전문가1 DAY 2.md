# 블록체인 전문가1 DAY 2



## DAY 1 Setting



# monitor.html(up.ver)

```
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>block view</title>
<script src="./javascripts/web3.min.js"></script>
<script>
var web3 = new Web3();
var provider = new web3.providers.HttpProvider("http://172.17.144.222:8545");
web3.setProvider(provider);
web3.eth.defaultAccount = web3.eth.accounts[0];

console.log("accounts[0]:" + web3.eth.defaultAccount);

var stop = false;

function startMonitor() {
     stop = false;
     var startBlockNo = web3.eth.blockNumber - 20;  
     var table = document.getElementById('list');

     var i = startBlockNo;
     for(; i < web3.eth.blockNumber;i++){
        var result = web3.eth.getBlock(i);             
        insertBlockRow(result, table,i);
     }

     setTimeout(function() {
          watchBlock(table,i);
         }, 10000);

}

function watchBlock(table, blockNumber) {
      if(stop) {
           return;
       }

   if(blockNumber == web3.eth.blockNumber){
     setTimeout(function(){
        watchBlock(table, blockNumber);
      } ,10000);
    }

   var result = web3.eth.getBlock(blockNumber);
   insertBlockRow(result,table,blockNumber);
   setTimeout(function(){
        watchBlock(table,++blockNumber);
     },10000);


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
	if (result.transactions.length > 0) {
	insertTranRow(result.transactions, td);
	}
}


function insertTranRow(transactions, td) {
	var allData = "";
       	 for (var i = 0; i < transactions.length; i++) {
var data= web3.eth.getTransaction(transactions[i])
      allData += JSON.stringify(data);                  
		
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

![1531271403470](C:\Users\Kchaos7\AppData\Local\Temp\1531271403470.png)

![1531297050523](C:\Users\Kchaos7\AppData\Local\Temp\1531297050523.png)

---

## 지갑 서비스 (wallet.html)

```
<!Doctype html>
<html>
<head>
<meta charset="UTF-8">

//web3라이브러리 로딩
<script src="./javascripts/web3.min.js"></script>
<script type="text/javascript">
 //web3 연결 
var web3 = new Web3();
var provider = new web3.providers.HttpProvider("http://172.17.144.222:8545");
web3.setProvider(provider);
web3.eth.defaultAccount = web3.eth.accounts[0]; 
    
// 잔고를 출력합니다.
function refreshBalance() { 
 // tablePlace를 초기화하고 계좌수 만큼 테이블의 행을 생성합니다.
  document.getElementById("tablePlace").innerText = " ";
  var idiv = document.createElement('div');
  document.getElementById("tablePlace").appendChild(idiv);

   //we3  코드
		
  }

// 사용자의 계좌들을 select로 만듭니다.
 function makeSelect() { 
  var list = web3.eth.accounts;
  var select =  document.getElementById('accounts');

	for(var i = 0; i<list.length; i++){
			var opt=document.createElement('option');
			opt.value = list[i];
			opt.innerHTML = list[i];
			select.appendChild(opt);
		}
	}

 function send(){ 
 var address = document.getElementById('accounts').value;
 var toAddress = document.getElementById('toaddr').value;

  //web3 코드 

 }
</script>
<style>
table {    border-collapse: collapse;    border: 4px solid #bbb;	width: 100%;}
tr:nth-child(even){background-color: #ccc}
td, h1 {	padding: 8px;    text-align: left;}
input, select {
    padding: 6px 10px;
    margin: 4px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 3px;
    box-sizing: border-box;
}
button:hover {  background-color: gold;}
</style>
</head>

<body>
    <h1>ETHER Wallet</h1>
	<div id="tablePlace"></div>
	<h4>송신처  <select id="accounts"></select> </h4>
	<h4>수신처  <input type="text" id="toaddr" size="40" value=""></h4>
    <h4>금액  <input id="amount" type="number"/> ETHER</h4>
	<h4>password <input id="pass" type="password"/>
	<button onClick="javascript:send()">Send</button></h4>
	<script>
	refreshBalance();
	makeSelect();
	</script>
</body>
</html>

```

![1531271742402](C:\Users\Kchaos7\AppData\Local\Temp\1531271742402.png)



[ethereum_API](https://github.com/ethereum/wiki/wiki/JavaScript-API)



```
<!Doctype html>
<html>
<head>
<meta charset="UTF-8">
//web3.js 자바스크립트 라이브러리 연동
<script src="./javascripts/web3.min.js"></script>

<script type="text/javascript">
//web3 연동
var web3 = new Web3();
var provider = new web3.providers.HttpProvider("http://172.17.144.222:8545");
web3.setProvider(provider);
web3.eth.defaultAccount = web3.eth.accounts[0];

    
// 잔고를 출력합니다.
function refreshBalance() { 
 // tablePlace를 초기화하고 계좌수 만큼 테이블의 행을 생성합니다.
  document.getElementById("tablePlace").innerText = " ";
  var idiv = document.createElement('div');
  document.getElementById("tablePlace").appendChild(idiv);
  
  var list = web3.eth.accounts;
  var total = 0;
  var input="<table>";
  for(var i=0; i < list.length ;i++){
   var tempB = parseFloat(web3.fromWei(web3.eth.getBalance(list[i]),"ether"));
   input += "<tr><td>" + list[i] + "</td><td>"+ tempB + "ETHER</td></tr>";
   total += tempB;
   }

   input += "<tr><td><strong>TOTAL</strong></td><td><strong>"+ total +"ETHER</strong></td></tr></table>";

   idiv.innerHTML = input;

   web3.eth.filter('latest').watch(function(){
          refreshBalance();
     });
		
  }

// 사용자의 계좌들을 select로 만듭니다.
function makeSelect() { 
  var list = web3.eth.accounts;

  var select =  document.getElementById('accounts');
  for(var i = 0; i<list.length; i++){
  var opt=document.createElement('option');
  opt.value = list[i];
  opt.innerHTML = list[i];
  select.appendChild(opt);
  }
}

 function send(){ 
 var address = document.getElementById('accounts').value;
 var toAddress = document.getElementById('toaddr').value;

  //web3 코드
var amount = web3.toWei(document.getElementById('amount').value,"ether");
//pw 받아서 unlock
if(web3.personal.unlockAccount(address, document.getElementById('pass').value)) {
	//sendTransaction - API check
	//web3.eth.sendTransaction(transactionObject [, callback])
	web3.eth.sendTransaction({from: address, to: toAddress, value: amount}, function(err, result){ 
		if(!err)
			console.log('Transaction Success!::' + result);
		else
			console.log(err);
	});
}

 }
</script>
<style>
table {    border-collapse: collapse;    border: 4px solid #bbb;	width: 100%;}
tr:nth-child(even){background-color: #ccc}
td, h1 {	padding: 8px;    text-align: left;}
input, select {
    padding: 6px 10px;
    margin: 4px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 3px;
    box-sizing: border-box;
}
button:hover {  background-color: gold;}
</style>
</head>

<body>
    <h1>ETHER Wallet</h1>
	<div id="tablePlace"></div>
	<h4>송신처  <select id="accounts"></select> </h4>
	<h4>수신처  <input type="text" id="toaddr" size="40" value=""></h4>
    <h4>금액  <input id="amount" type="number"/> ETHER</h4>
	<h4>password <input id="pass" type="password"/>
	<button onClick="javascript:send()">Send</button></h4>
	<script>
	refreshBalance();
	makeSelect();
	</script>
</body>
</html>

```





![1531273780862](C:\Users\Kchaos7\AppData\Local\Temp\1531273780862.png)



```
> eth.accounts
["0xc53ba2e65a1682163c332b6efc74eea3ebf3edc1", "0x470db71c77bae52d72342f837f83d1             be8cd11bbd"]

> eth.sendTransaction(from:eth.accounts[0], to:eth.accounts[1], value:web3)
(anonymous): Line 1:25 Unexpected token : (and 2 more errors)

> personal.unlockAccount(eth.accounts[0])
Unlock account 0xc53ba2e65a1682163c332b6efc74eea3ebf3edc1
Passphrase:
true

> eth.sendTransaction({from:eth.accounts[0], to:eth.accounts[1], value:web3.toWei(30,"ether")})
"0xcfeaaaf483cbe159e7fc4e9f38b7b9047caf76d58732b3a523f03e66109c4048"

> miner.start()
null
> miner.stop()

```

![1531275319182](C:\Users\Kchaos7\AppData\Local\Temp\1531275319182.png)



> java scrypt 라이브러리 연동 
>
> 딜리버리 시스템을 통해 좀 더 원활한 접속 가능.(동시접속) - 훨씬 빠르게 전송됨.
>
> ```
> <script src="https://cdn.jsdelivr.net/gh/ethereum/web3.js/dist/web3.min.js"></script>
> ```



---

# Solidity 기본문법(이더리움 베이직, p142)

## 1.기본 자료형

-메모리 공간 확보

-정수형 - int(=int256, 부호 있는, 양&음), uint(=uint256, 부호 없는, 양)

  - 자료형의 크기

    uint8 (8비트 - 0 ~255). 

    솔리디티는 실수 자료형 지원X.

    > 자료형 잘못 사용시 오버플로우/언더플로우 발생.



- nohup에서 Password.txt  만든 것 추가 port 8545 뒤에  추가

  ```
  /*password.txt*.
  pass0
  pass1
  pass2
  pass3
  ```

  

  ```
  --unlock '0,1,2,3' --password '/home/user01/smartcontract_testnet/password.txt
  
  nohup geth --networkid 4649 --nodiscover --datadir /home/user01/smartcontract_testnet --rpc --rpcaddr "172.17.144.222" --rpcport 8545 --unlock '0,1' --password '/home/user01/smartcontract_testnet/password.txt' --rpccorsdomain "*" --rpcapi "admin,db,eth,debug,miner,net,shh,txpool,personal,web3" --verbosity 5 2>> /home/user01/smartcontract_testnet/geth.log &
  
  
  //verbosity 6에서 5로 변경
  ```

  자동으로 비번풀리게 만들어놈

  ```
  /*DataTypeDemo.sol*/
  pragma solidity ^0.4.18;
  
  contract DataTypeDemo {
      function getValueType() public pure returns (uint8) {
          uint8 a;
          a = 255;
          
          uint8 b = a;
          b = 255;
          a = a + b;
          return a;
      }
  }
  //오버플로우 발생.
  ```

  

![1531284526015](C:\Users\Kchaos7\AppData\Local\Temp\1531284526015.png)



-  address 형 자료형

  balance, transfer, send 내장함수를 이용시 20 바이트의 주소 자료형 제공

  //이름없는 함수,  ether 전송 가능 함수

  ```
   function() public payable {           //익명 처리하는 콜백 함수, payabel 조회, 전송, 수정 
   }
  ```

  //익명 처리하는 콜백 함수, payabel 조회, 전송, 수정 //잔고를 요청하면 실행한 사람의 잔고를 보여준다. //this-자기 자기 자신

  ```
  /*AddressTypeDemo.sol*/
  
  pragma solidity ^0.4.18;
  
  contract AddressTypeDemo {
      //
      function() public payable {
      }
      
      function getBalance(address _target) public view returns(uint)  {
          
          if(_target == address(0)){
              _target = this;  //this - 
          }
            return _target.balance;
      }
  }
  ```

  ![1531285600737](C:\Users\Kchaos7\AppData\Local\Temp\1531285600737.png)

  -비밀번호 nohup 에서 풀어놨기 때문에 pending 시 miner.start()만 하게되면 컨트랙트 성사되어 실행됨

  -address 값에 account[0]  주소 기입하면 해당 주소의 잔고 출력.



- 배열(array)-같은자료형의 묶음
- 튜플(tuple)-서로다른 자료형의 묶음



- 함수 - 기능
  - function 함수명(파라미터/매개변수/) 옵션(-가시성) //기능 { }
- 생성자 - constructor
        - 특수함수
        - function 컨트랙트이름 { } //역할 : 값의 초기화
- -0.4.22 에서는 constructor 함수명



```
/*AddressTypeDemo.sol*/
pragma solidity ^0.4.18;

contract FunctionDemo {
    uint result;
    address from;
    address to;
    
    function operation() public payable returns (uint){
         result = sum(5,10);
    }
    
    function sum(uint a, uint b) public payable returns (uint) {
         result = a + b;
         return result;
    }

    function FunctionDemo(uint _result, address _from, address _to) public {
    result = _result;
    from = _from;
    to =_to;
    } 
}
```

![1531286813445](C:\Users\Kchaos7\AppData\Local\Temp\1531286813445.png)





- /*FunctionDemo.sol*/
- 배열이 가장 중요 -> gas price 



## 배열

-같은 자료형의 묶음

​	uint[3] var;

-1,2,3 차원 배열까지

-unit[3] myArray = [0,1,2];  //선언과 동시 초기화

---

-**정적 배열** : 처음 크기가 정해진 배열

uint[3] myArray = [0,1,2]

-**동적 배열** : 실행시 크기가 정해지는 배열 (가스비 계산

uint[] myArray2; //가스비 계산에 더 효율적

---

-length : 길이, push : 배열의 마지막에  값 추가.

---

-**저장소(storage) 배열** : 블록체인 종료되어도 EVM 내부에 남아있음, 재사용 가능, 컨트랙트 실행 이후 유지, default 

uint[] memory myArray2; //가스비 계산에 더 효율적



-**메모리(memory) 배열** : 명시적 키워드 memory, 컨트랙트 실행 이후 소멸(gas 소모량 적음)

uint[] memory myArray2; //가스비 계산에 더 효율적

---

**상태변수** - 저장소에 저장 (static), 클래스, 프로그램 내에서 실행되는 변수

(멤버변수)

**지역변수** - 저장소, 메모리, 함수 내부에서만 실행되는 변수



- ##### 매핑

  - 데이터=값으로 이루어진 형태 (키=값)
  - mapping(키 자료형=>data 자료형 ) 매핑이름;
  - 선언,접근,입력 등
  - mapping(address=>uint) public balance;

  ​                        (주소형, 정수형)

  ​                 balance->("0xadsds",100)

- ##### 구조체

  - 배열 : 같은 자료형의 묶음
  - 튜플 : 서로 다른 자료형의 묶음
  - 구조체 :같거나 서로 다르면서 복합적으로 묶음. (사용자 정의 자료형=>자바의 클래스)

- ##### 상속

  - 코드강화, 코드 간결화
  - 다중상속
    - 다형성
    - override(메소드 재정의) - 상속
    - overload(메소드 다중정의) - 함수여러개

- ##### 기본 내장 키워드

  - 특수변수 및 함수
  - msg.sender(address) : 송신자의 주소
  - msg.value(uint) : 송금액을 wei 단위 변환
  - tx.gasprice(uint) : 거래의 가스 가격
  - tx.origin(address) : 거래를 보내 송신자의 주소 반환
  - tx .number(uint) : 현재 블록이 몇번째 블록인지 반환

- ##### 이벤트 처리

  - 로그 남기기
  - event  이벤트명 '

---

## 자신의 코인 생성

```
/* Shinyspear Coin 생성 */
pragma solidity ^0.4.18;

contract ShinyspearCoin {
	//1. 상태 변수
	string public name;								// 코인 이름
	string public symbol;							// 코인 단위
	uint8 public decimals;							// 코인의 소수점 자리수
	uint256 public totalSupply;						// 코인 총량
	mapping (address=>uint256) public balanceOf;	 // 각 주소의 잔고
	
	//각 주소의 잔고
	
	//2. 이벤트 설정 - 송금(transfer))
	event Transfer(address indexed from, address indexed to, uint256 value);
	
	//3. 생성자
function ShinyspearCoin(uint256 _supply ,string _name ,string  _symbol ,uint8 _decimals) public { 
		balanceOf[msg.sender] = _supply;
		totalSupply = _supply;
		name = _name;
		symbol = _symbol;
		decimals = _decimals;
		}
	
	//4. 송금
	function transfer(address _to, uint256 _value) public { 
		//부정송금 확인
		if(balanceOf[msg.sender] < _value) revert();	//송신자 주소 반환됨
		if(balanceOf[_to] + _value < balanceOf[_to]) revert();
		
		//송금하는 주소와 송금받은 주소의 잔고 갱신
		balanceOf[msg.sender] -= _value;
		balanceOf[_to] += _value;
	
	//이벤트 알림
    Transfer(msg.sender, _to, _value);
	}
}

```

```
/*이건 내가 예전에 짰던 블랙맘바 코인*/
pragma solidity ^0.4.20;    //solidity version
//ref. https://blog.naver.com/soolmini/221247998381
contract SimpleToken
{
    address public owner;   
    
    string public name;     
    uint public decimals;
    string public symbol;
    uint public totalSupply;
    uint private E18 = 1000000000000000000;
    
    mapping (address => uint) public balanceOf;
    
    function SimpleToken() public
    {
        name = "BlackMambaToken";
        decimals = 18;
        symbol = "BMT";
        totalSupply = 1000000000 * E18;
        owner = msg.sender;
        
        balanceOf[msg.sender] = totalSupply;
    }
}
```

![1531294653861](C:\Users\Kchaos7\AppData\Local\Temp\1531294653861.png)

![1531294743811](C:\Users\Kchaos7\AppData\Local\Temp\1531294743811.png)

![1531294860176](C:\Users\Kchaos7\AppData\Local\Temp\1531294860176.png)![1531295403424](C:\Users\Kchaos7\AppData\Local\Temp\1531295403424.png)

> 현재 account[0]에 10000개가 있고 위에 송신측을 account[0]으로 셋팅하고 아래 transfer 수신측 주소, 돈을 넣으면 전송된다

![1531295778970](C:\Users\Kchaos7\AppData\Local\Temp\1531295778970.png)

```
/*Transaction Log*/

[
	{
		"from": "0x851c65e279390abc6dbbc3ae2b8c6e0ee4b7fb66",
		"topic": "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
		"event": "Transfer",
		"args": {
			"0": "0xc53BA2E65a1682163C332b6EFc74eeA3Ebf3edc1",
			"1": "0x470DB71c77BAe52d72342f837f83d1bE8CD11Bbd",
			"2": "200",
			"from": "0xc53BA2E65a1682163C332b6EFc74eeA3Ebf3edc1",
			"to": "0x470DB71c77BAe52d72342f837f83d1bE8CD11Bbd",
			"value": "200",
			"length": 3
		}
	}
]
```



![1531296403781](C:\Users\Kchaos7\AppData\Local\Temp\1531296403781.png)

> +대신 - 넣으면 계속 돈이 감소되어 언더플로우 발생, 돈 어마어마하게 발생

![1531296452727](C:\Users\Kchaos7\AppData\Local\Temp\1531296452727.png)



---

##### 20180711.txt

```
http://192.168.0.105/
http://172.17.138.113:8080/

- 20180711_news.txt

* geth실행, npm start 
- web3.js 기본 사용
- monitor.html 
- wallet.html

https://github.com/ethereum/wiki/wiki/JavaScript-API

> eth.sendTransaction({from:eth.accounts[0], to:eth.accounts[1], value:web3.toWei(10,"ether")})

> personal.unlockAccount(eth.accounts[0]);




* Solidity 기본 문법(p142)
1)기본자료형
 - 메모리 공간을 확보
  
 정수형 - int(=int256), uint(=uint256)
        - 자료형의 크기
          uint8 (8비트 - 0~255)   

 솔리디티는 실수 자료형 지원하지 않음

->자료형을 잘못 사용하면
  오버플로우/언더플로우
          

- address형 자료형
  balance, transfer, send 내장함수를 이용시
  20바이트의 주소 자료형 제공.


//이름없는 함수, ether전송 가능함수
//this - 자기자신

0x79afb6633e31e94c1b59c3b3e4390c9ff27f9786

 배열(array)  -같은 자료형 묶음
 튜플(tuple) - 서로 다른 자료형을 묶음
 - 

함수 - 기능
 function 함수명(파라메터/매개변수/) 옵션(-가시성,상태) returns(출력매개변수){
   //기능
  }
 
 
생성자 - constructor
       - 특수함수
         function 함수명-컨트랙트이름  { 
           //역할 - 값의 초기화
         }

 -0.4.22 부터는 constructor 함수명


  switch-case 문 없음

*배열(array)
- 같은 자료형의 묶음
  uint[3] var;
- 1,2,3 차원 배열까지.
- uint[3] myArray = [0,1,2] ;//선언과 동시 초기화

- 정적배열 : 처음크기가 정해진 배열
  동적배열 : 실행 시 크기가 정해지는 배열
            (가스비 계산)
  uint[3] myArray = [0,1,2]
  uint[] myArray2;

- length  : 길이,  push : 배열의 마지막에 값 추가


- 저장소(storage)배열 : 컨트랙트 종료될때까지.
                        재사용 가능.
                        default.

  메모리(memory) 배열: -컨트랙트 실행이후 지워짐
                       memory 키워드
  
   uint[3] myArray = [0,1,2];
   uint[3] memory myArray = [0,1,2]
  

   상태변수 - 저장소에 저장 (static)
   (멤버변수)  -클래스, 프로그램내에서 실행되는 변수


   지역변수 - 저장소, 메모리
           =>함수내에서 실행되는 변수
 

* 매핑
 - 데이터=값으로 이루어진 형태
   키=값

  mapping(키 자료형=> data 자료형) 매핑이름;
  선업, 접근, 입력 등

   mapping(address =>uint) public balance;
          (주소형,정수형)
    balance  ->("0xadsds",100)


* 구조체
- 배열: 같은 자료형의 묶음.
  튜플 : 서로 다른 자료형의 묶음

 구조체:  같거나 서로 다르면서 복합적으로 묶음.
  (사용자 정의 자료형 =>자바의 클래스

  묶음 안의 접근은 접근지정자:.

   public - 가시성(접근제한자)

  struct personal{
               bool isMale;

         }

* 상속
  나 is 부모 컨트랙트{

  }
 
 - 목적: 코드강화, 코드간결화
 - 다중 상속



   메소드 재정의(override)  - 상속
  


* 기본 내장 키워드
  -특수변수 및 함수
  msg.sender(address) :송신자의 주소
  msg.value(uint) : 송금액을 wei 단위 반환
  tx.gasprice(uint) :거래의 가스 가격
  tx.origin(address): 거래를 보내 송신자의 주소 반환
 
  block.number(uint):  현재 블록이 몇번째 블록인지 순서 반환
  
* 이벤트 처리
- 로그 남기기

  event 이벤트명 ;


  코드내에서 이벤트명;















nohup geth --networkid 4649 --nodiscover --datadir /home/user01/smartcontract_testnet --rpc --rpcaddr "192.168.0.x" --rpcport 8545  --unlock '0,1,2,3' --password '/home/user01/smartcontract_testnet/password.txt' --rpccorsdomain "*" --rpcapi "admin,db,eth,debug,miner,net,shh,txpool,personal,web3" --verbosity 5 2>>/home/user01/smartcontract_testnet/geth.log &



* 자신의 코인 생성

pragma solidity ^0.4.18;

contract BluewindCoin {   
  //1. 상태변수
  string public name;       //코인 이름
  string public symbol;       //코인 단위
  uint8 public decimals;       //코인의 소수점 자리수
  uint256 public totalSupply;   //코인 총량
  mapping (address=>uint256) public balanceOf;
  //각 주소의 잔고

  //2.이벤트 설정 - 송금(transfer)
 event Transfer(address indexed from, address indexed to, uint256 value);

  //3. 생성자
  function BluewindCoin(uint256 _supply,string _name,string _symbol,uint8 _decimals ) public {
    balanceOf[msg.sender] = _supply;     
    name = _name;
    symbol = _symbol;
    decimals = _decimals;
    totalSupply = _supply;
  } 


  //4. 송금
   function transfer(address _to, uint256 _value) public {
    //부정송금 확인

     if(balanceOf[msg.sender] < _value ) revert();
     
     if(balanceOf[_to] + _value < balanceOf[_to]) revert();


    //송금하는 주소와 송금받는 주소의 잔고 갱신   
     balanceOf[msg.sender] -= _value;
     balanceOf[_to] += _value;
  
   //이벤트 알림
   Transfer(msg.sender, _to, _value);
  }
}

```

