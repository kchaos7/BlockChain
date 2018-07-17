# 블록체인 전문가1 DAY 3

## 블랙리스트 기능 추가

```
/* Shinyspear Coin 생성 */
pragma solidity ^0.4.18;
/* 
블랙리스트 추가
특정 주소를 블랙리스트에 추가해서
거래 하지 못하도록, 필요하면 블랙리스트 삭제 기능
블랙리스트 추가한 가상화폐
*/
contract ShinyspearCoin {
	//1. 상태 변수
	string public name;								// 코인 이름
	string public symbol;							// 코인 단위
	uint8 public decimals;							// 코인의 소수점 자리수
	uint256 public totalSupply;						// 코인 총량
	mapping (address => uint256) public balanceOf;	 // 각 주소의 잔고
	
	//+
	mapping(address => int8) public blackList;		//블랙리스트 맵핑
	address public owner = msg.sender;						   //소유자 주소
	
	modifier onlyOwner() {
	    if(msg.sender != owner) revert();
	    _;										//modifier는 _; 로 끝나야함
	}
	
	//2. 이벤트 설정 - 송금(transfer))
	event Transfer(address indexed from, address indexed to, uint256 value);
	event BlackListed(address indexed target);
	event DeletedFromBlackList(address indexed target);
	event RejectPaymentFromBlackListAddr(address indexed from, address indexed to, uint256 value);
	event RejectPaymentToBlackListAddr(address indexed from, address indexed to, uint256 value);
	

    function ShinyspearCoin(uint256 _supply, string _name, string _symbol, uint8 _decimals) public {
    balanceOf[msg.sender] = _supply;     
    name = _name;
    symbol = _symbol;
    decimals = _decimals;
    totalSupply = _supply;
    } 
		
	//+블랙리스트 등록 - 주소
	function blackListing(address _addr) public onlyOwner {	//소유자만 블랙리스트 추가 가능
        blackList[_addr] = 1;
        BlackListed(_addr);
	}
	
	//+블랙리스트 제거 - 주소
	function deleteFromBlackList(address _addr) public onlyOwner {		//소유자만 블랙리스트 삭제 가능
        blackList[_addr] = -1;
        DeletedFromBlackList(_addr);
	}
	
	//4. 송금
	function transfer(address _to, uint256 _value) public { 
		//부정송금 확인
		
		//+블랙리스트에 존재하는 계정 송금 안되도록 구현
		if(balanceOf[msg.sender] < _value) revert();	//송신자 주소 반환됨
		if(balanceOf[_to] + _value < balanceOf[_to]) revert();
		
		if(blackList[msg.sender] > 0) {
		    //event
		       RejectPaymentFromBlackListAddr(msg.sender, _to, _value);
		}
		else if(blackList[_to] > 0) {
	        RejectPaymentToBlackListAddr(msg.sender, _to, _value);
         
		}
		else {
		 balanceOf[msg.sender] -= _value;
			balanceOf[_to] += _value;
		//송금하는 주소와 송금받은 주소의 잔고 갱신		
	
	//이벤트 알림
    Transfer(msg.sender, _to, _value);
	}
}
}
```

> blacklist를 설정하게되면 1이 할당되고, 송금을 해도 송금이 되지 않는다.

![1531371853451](C:\Users\Kchaos7\AppData\Local\Temp\1531371853451.png)

> deploy 하게되면 pending 되고 miner.start() 하여 체결시킴

![1531371885185](C:\Users\Kchaos7\AppData\Local\Temp\1531371885185.png)

![1531371951264](C:\Users\Kchaos7\AppData\Local\Temp\1531371951264.png)

> account[1] 주소에 100이더 보내면  아래 balanceOf이 100 이 된다.



##### 블랙리스트추가

![1531372015229](C:\Users\Kchaos7\AppData\Local\Temp\1531372015229.png)

![1531372057023](C:\Users\Kchaos7\AppData\Local\Temp\1531372057023.png)

> 디버깅 로그에 이벤트로 블랙리스트 추가된 것 확인 가능

![1531372119859](C:\Users\Kchaos7\AppData\Local\Temp\1531372119859.png)

> 송금을 하면 로그에 송금 거절 된 것 확인 가능



##### 블랙리스트 해제

![1531372169261](C:\Users\Kchaos7\AppData\Local\Temp\1531372169261.png)

![1531372189429](C:\Users\Kchaos7\AppData\Local\Temp\1531372189429.png)

> 해제 된 것 확인 가능

> 다시 송금하게 되면 정상적으로 송금됨

![1531372250192](C:\Users\Kchaos7\AppData\Local\Temp\1531372250192.png)



---



## 송금 수수료

```
/* Shinyspear Coin 생성 */
pragma solidity ^0.4.18;
/* 
블랙리스트 추가
특정 주소를 블랙리스트에 추가해서
거래 하지 못하도록, 필요하면 블랙리스트 삭제 기능
블랙리스트 추가한 가상화폐
*/
contract ShinyspearCoin {
	//1. 상태 변수
	string public name;								// 코인 이름
	string public symbol;							// 코인 단위
	uint8 public decimals;							// 코인의 소수점 자리수
	uint256 public totalSupply;						// 코인 총량
	mapping(address => uint256) public balanceOf;	 // 각 주소의 잔고
	//+
	mapping(address => int8) public blackList;		//블랙리스트 맵핑
	address public owner = msg.sender;						   //소유자 주소
	
	modifier onlyOwner() {
	    if(msg.sender != owner) revert();
	    _;										//modifier는 _; 로 끝나야함
	}
	
	mapping(address => int8) public cashbackRate;
	
	//2. 이벤트 설정 - 송금(transfer))
	event Transfer(address indexed from, address indexed to, uint256 value);
	event BlackListed(address indexed target);
	event DeletedFromBlackList(address indexed target);
	event RejectPaymentFromBlackListAddr(address indexed from, address indexed to, uint256 value);
	event RejectPaymentToBlackListAddr(address indexed from, address indexed to, uint256 value);

    function ShinyspearCoin(uint256 _supply, string _name, string _symbol, uint8 _decimals) public {
    balanceOf[msg.sender] = _supply;     
    name = _name;
    symbol = _symbol;
    decimals = _decimals;
    totalSupply = _supply;
    } 
		
	//+블랙리스트 등록 - 주소
	function blackListing(address _addr) public onlyOwner {	//소유자만 블랙리스트 추가 가능
        blackList[_addr] = 1;
        BlackListed(_addr);
	}
	
	//+블랙리스트 제거 - 주소
	function deleteFromBlackList(address _addr) public onlyOwner {		//소유자만 블랙리스트 삭제 가능
        blackList[_addr] = -1;
        DeletedFromBlackList(_addr);
	}
	
	//++송금 수수료
	function setCashbackRate(int8 _rate) public {
		if(_rate < 1) {
            _rate = -1;
		}
		else if(_rate > 100) {
            _rate = 100;
		}
		cashbackRate[msg.sender] = _rate;
		
		if(_rate < 1)
			_rate = 0; 
	}
	
	//4. 송금
	function transfer(address _to, uint256 _value) public { 
		//부정송금 확인
		
		//+블랙리스트에 존재하는 계정 송금 안되도록 구현
		if(balanceOf[msg.sender] < _value) revert();	//송신자 주소 반환됨
		if(balanceOf[_to] + _value < balanceOf[_to]) revert();
		
		if(blackList[msg.sender] > 0) {
		    //event
		       RejectPaymentFromBlackListAddr(msg.sender, _to, _value);
		}
		else if(blackList[_to] > 0) {
	        RejectPaymentToBlackListAddr(msg.sender, _to, _value);
		}
		else {
			uint256 cashback = 0;
			if(cashbackRate[_to] > 0)
				cashback = _value/100 * uint256(cashbackRate[_to]);
			balanceOf[msg.sender] -= (_value - cashback);
			balanceOf[_to] += (_value - cashback);
		//송금하는 주소와 송금받은 주소의 잔고 갱신		
	
	//이벤트 알림
    Transfer(msg.sender, _to, _value);
	}
}
}
```

![1531373267159](C:\Users\Kchaos7\AppData\Local\Temp\1531373267159.png)

![1531373322932](C:\Users\Kchaos7\AppData\Local\Temp\1531373322932.png)

> 송금하게 되면 account[0]에게 수수료가 들어온다 ( 초기 3960->3970)



##### 송금 수수료 이벤트 설정

![1531375368876](C:\Users\Kchaos7\AppData\Local\Temp\1531375368876.png)

```
/* Shinyspear Coin 생성 */
pragma solidity ^0.4.18;
/* 
블랙리스트 추가
특정 주소를 블랙리스트에 추가해서
거래 하지 못하도록, 필요하면 블랙리스트 삭제 기능
블랙리스트 추가한 가상화폐
*/
contract ShinyspearCoin {
	//1. 상태 변수
	string public name;								// 코인 이름
	string public symbol;							// 코인 단위
	uint8 public decimals;							// 코인의 소수점 자리수
	uint256 public totalSupply;						// 코인 총량
	mapping(address => uint256) public balanceOf;	 // 각 주소의 잔고
	//+
	mapping(address => int8) public blackList;		//블랙리스트 맵핑
	address public owner = msg.sender;						   //소유자 주소
	
	modifier onlyOwner() {
	    if(msg.sender != owner) revert();
	    _;										//modifier는 _; 로 끝나야함
	}
	
	mapping(address => int8) public cashbackRate;
	
	//2. 이벤트 설정 - 송금(transfer))
	event Transfer(address indexed from, address indexed to, uint256 value);
	event BlackListed(address indexed target);
	event DeletedFromBlackList(address indexed target);
	event RejectPaymentFromBlackListAddr(address indexed from, address indexed to, uint256 value);
	event RejectPaymentToBlackListAddr(address indexed from, address indexed to, uint256 value);
	event SetCashback(address indexed from, int8 rate);
	event Cashback(address indexed from, address indexed to, uint256 value);

    function ShinyspearCoin(uint256 _supply, string _name, string _symbol, uint8 _decimals) public {
    balanceOf[msg.sender] = _supply;     
    name = _name;
    symbol = _symbol;
    decimals = _decimals;
    totalSupply = _supply;
    owner = msg.sender;
    } 
		
	//+블랙리스트 등록 - 주소
	function blackListing(address _addr) public onlyOwner {	//소유자만 블랙리스트 추가 가능
        blackList[_addr] = 1;
        BlackListed(_addr);
	}
	
	//+블랙리스트 제거 - 주소
	function deleteFromBlackList(address _addr) public onlyOwner {		//소유자만 블랙리스트 삭제 가능
        blackList[_addr] = -1;
        DeletedFromBlackList(_addr);
	}
	
	//++송금 수수료
	function setCashbackRate(int8 _rate) public {
		if(_rate < 1) {
            _rate = -1;
		}
		else if(_rate > 100) {
            _rate = 100;
		}
		cashbackRate[msg.sender] = _rate;
		
		if(_rate < 1)
			_rate = 0; 
		SetCashback(msg.sender, _rate);
	}
	
	//4. 송금
	function transfer(address _to, uint256 _value) public { 
		//부정송금 확인
		
		//+블랙리스트에 존재하는 계정 송금 안되도록 구현
		if(balanceOf[msg.sender] < _value) revert();	//송신자 주소 반환됨
		if(balanceOf[_to] + _value < balanceOf[_to]) revert();
		
		if(blackList[msg.sender] > 0) {
		    //event
		       RejectPaymentFromBlackListAddr(msg.sender, _to, _value);
		}
		else if(blackList[_to] > 0) {
	        RejectPaymentToBlackListAddr(msg.sender, _to, _value);
		}
		else {
			uint256 cashback = 0;
			if(cashbackRate[_to] > 0)
				cashback = _value/100 * uint256(cashbackRate[_to]);
			balanceOf[msg.sender] -= (_value - cashback);
			balanceOf[_to] += (_value - cashback);
		//송금하는 주소와 송금받은 주소의 잔고 갱신		
	
	//이벤트 알림
    Transfer(msg.sender, _to, _value);
    Cashback(_to, msg.sender, cashback);
	}
}
}
```

![1531375321855](C:\Users\Kchaos7\AppData\Local\Temp\1531375321855.png)



---

## Debugger

##### Instructions

현재 스마트 컨트랙트 바이트 코드, EVM의 OP코드로 출력

다음 OP 코드가 명령어



##### Locals

로컬 변수와 매개 변수가 출력



##### State

상태변수 



##### Detail

Instructions 실행. 명령어가 진행되면서 명령어가 실행하는 상세 정보 출력



##### vm  trace step

전체 트랜잭션 중에서 현재 vm의 스탭



##### executation step

메세지 콜에서 진행 순서



##### gas

현재 명령어에서 필요한 가스



##### stack

EVM 스택 상ㅌ태



##### Storage Completely loaded

현재 스마트 컨트랙트에서 변경된 상태 변수를 출력



##### Memory

컨트랜트 실행중 사용중인 메모리



##### Call Data

EOA가 스마트 컨트랙트 함수를 호출할 때 전달된 콜 데이터들



##### Call Stack

메시지 콜 스택 출력



##### Return

디버그 상태에서 RETURN Opcode에 값이 존재하면 출력



##### Full Storage change

상태가 변경된 상태변수 값 모두 출력



##### BP(Break Point) 

중단점 설정 , web3 에서는 X, JavascryptVM에서만 가능

---



## voteContract.sol (p350, 수정할 것 많음)

ser01@ubuntu:~/web3$ sudo npm start
[sudo] password for user01:

> web3@0.0.0 start /home/user01/web3
> node ./bin/www

#### 예제. 추가 할 것

```
pragma solidity ^0.4.18;

contract voteContract {

mapping (address => bool) voters; // 하나의 계정 당 한 번의 투표만 가능
mapping (string => uint) candidates; // 후보자의 득표수를 저장합니다.
mapping (uint8 => string) candidateList; // 후보자의 리스트입니다.

uint8 numberOfCandidates; // 총 후보자의 수입니다.
address contractOwner;



function voteContract() public {
  contractOwner = msg.sender;
   }

    // 후보자를 추가하는 함수입니다.
function addCandidate(string cand) public {
        bool add = true;
        for (uint8 i = 0; i < numberOfCandidates; i++) {
        
            // 문자열 비교는 해쉬함수(sha3)를 통해서 할 수 있습니다.
            // 솔리더티에는 문자열 비교에 대한 특별한 함수가 없습니다.
            //if(sha3(candidateList[i]) == sha3(cand)){
            //    add = false; break;
            //}
            
        if(keccak256(candidateList[i]) == keccak256(cand)){
            add = false; break;
            }
        }

        if(add) {
            candidateList[numberOfCandidates] = cand;
            numberOfCandidates++;
        }
    }

    // 투표를 하는 함수입니다.
function vote(string cand) public {
// 하나의 계정은 한번의 투표만 결과에 반영됩니다.
if(voters[msg.sender]) { }
else{
 voters[msg.sender] = true;
 candidates[cand]++;
        }
    }

    // 이미 투표했는지 확인합니다.
    function alreadyVoted() public view returns(bool) {
        if(voters[msg.sender])
            return true;
        else
            return false;
    }

    //후보자의 수를 리턴합니다.
function getNumOfCandidates() public view returns(uint8) {
        return numberOfCandidates;
    }

    //번호에 해당하는 후보의 이름을 리턴합니다.
function getCandidateString(uint8 number) public view returns(string) {
    return candidateList[number];
    }

    //후보의 득표수를 리턴합니다.
    function getScore(string cand) public view returns(uint) {
        return candidates[cand];
    }

    //컨트랙트를 삭제합니다.
    function killContract() public  {
     if(contractOwner == msg.sender)
          selfdestruct(contractOwner);
    }
}
```



```
/*Detail - ABI*/	vote.html에 대체

[
	{
		"constant": false,
		"inputs": [
			{
				"name": "cand",
				"type": "string"
			}
		],
		"name": "addCandidate",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "killContract",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "cand",
				"type": "string"
			}
		],
		"name": "vote",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "alreadyVoted",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "number",
				"type": "uint8"
			}
		],
		"name": "getCandidateString",
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
		"constant": true,
		"inputs": [],
		"name": "getNumOfCandidates",
		"outputs": [
			{
				"name": "",
				"type": "uint8"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "cand",
				"type": "string"
			}
		],
		"name": "getScore",
		"outputs": [
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







```
<!Doctype html>
<html>
<head>
<meta charset="UTF-8">
<script type="text/javascript" src="./javascripts/web3.min.js"></script>
<script type="text/javascript">
   
    var Web3 = require('web3');
    var web3 = new Web3();
    web3.setProvider(new web3.providers.HttpProvider("http://172.17.144.222:8545"));
	var vc = web3.eth.contract(
		[
	{
		"constant": false,
		"inputs": [
			{
				"name": "cand",
				"type": "string"
			}
		],
		"name": "addCandidate",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "killContract",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "cand",
				"type": "string"
			}
		],
		"name": "vote",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "alreadyVoted",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "number",
				"type": "uint8"
			}
		],
		"name": "getCandidateString",
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
		"constant": true,
		"inputs": [],
		"name": "getNumOfCandidates",
		"outputs": [
			{
				"name": "",
				"type": "uint8"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "cand",
				"type": "string"
			}
		],
		"name": "getScore",
		"outputs": [
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
		).at("0x3fd93cda1fcd67110efeca339dfdf77396ae8ce3");	

	function showList(){
		// tablePlace를 초기화하고 계좌수 만큼 테이블의 행을 생성합니다.
		document.getElementById("table1").innerText = " ";
		/*
		var idiv = document.createElement('div');
		document.getElementById("table1").appendChild(idiv);
  */
		var table=document.getElementById("table1");
		var length = vc.getNumOfCandidates();
		//console.log("2: " + length);
		for(var i=0;i<length;i++){
			var candidate = vc.getCandidateString(i);
			var row=table.insertRow();
			var cell1=row.insertCell(0);
			var cell2=row.insertCell(1);
			cell1.innerHTML = candidate;
			cell2.innerHTML = vc.getScore(candidate);
			}

		web3.eth.filter('latest').watch(function(){
        	showList();
	    });
	}
	function vote(){
	var candidate=document.getElementById("candidate").value;
	var account=document.getElementById("account").value;
	web3.eth.defaultAccount = account;
	if(web3.personal.unlockAccount(account,document.getElementById('pass').value)){
		var alreadyVoted=vc.alreadyVoted();
		console.log(alreadyVoted);
		if(alreadyVoted)
			alert("이미 투표하셨습니다.");
		else
			vc.vote(candidate,function(err,result){ 
				if(!err) alert("트랜잭션이 성공적으로 전송되었습니다.|n"+result)});		
	}
	}
	function addCand(){
		var candidate=document.getElementById("candidate").value;
		var account=document.getElementById("account").value;
		if(web3.personal.unlockAccount(account,document.getElementById('pass').value)){
			vc.addCandidate(candidate,{from:account,gas:2000000},function(err,result){ 
				if(!err) alert("트랜잭션이 성공적으로 전송되었습니다.|n"+result)
			});	
		}
	}
	
	// 사용자의 계좌들을 select로 만듭니다.
function makeSelect() { 
  var list = web3.eth.accounts;

  var select =  document.getElementById('account');
  for(var i = 0; i<list.length; i++){
  var opt=document.createElement('option');
  opt.value = list[i];
  opt.innerHTML = list[i];
  select.appendChild(opt);
  }
}

</script>
<style>
table {    border-collapse: collapse;    border: 4px solid #bbb;	width: 50%;}
tr:nth-child(even){background-color: #ccc}
input, select {
    padding: 6px 10px;
    margin: 4px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 3px;
    box-sizing: border-box;}
button:hover {  background-color: gold;}
</style>
</head>
<body onload="showList()">
    <h1>블록체인 투표</h1>
	<div>
	<!-- 계정: <input type="text" id="account"> -->
	
	계정: <select id="account"></select>
	<script>
	makeSelect();
	</script>
<!--	패스워드: <input type="password" id="pass" value="pass0">	</div><br> -->
	패스워드: <input type="password" id="pass">	</div><br>
	<div> <input type="text" id="candidate">
	<button onClick="vote()">투표하기</button> 
	<button onClick="addCand()">후보 추가하기</button> </div>
	<table id="table1" border="1">
		<tr>
			<th> candidate</th>
			<th> vote</th>
		</tr>
	</table>
	<!-- <script>
	showList();
	</script> -->
</body>
</html>

```

> //at(~) 부분에 CA 입력할 것, CA는 Deploy 했을 때 뜨는 contract 주소복사



![1531381653120](C:\Users\Kchaos7\AppData\Local\Temp\1531381653120.png)	

![1531387500917](C:\Users\Kchaos7\AppData\Local\Temp\1531387500917.png)

![1531382102445](C:\Users\Kchaos7\AppData\Local\Temp\1531382102445.png)

> http://172.17.144.222:3000/monitor.html

> abcd/efgh 후보를 추가했기 때문에 트랜잭션 2개 생성





