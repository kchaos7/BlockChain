#  블록체인 전문가1 DAY 4 (FINAL)



## 코인 & 토큰

### 코인 

- 독립된 블록체인 네트워크(메인넷)를 소유한 경우를 코인이라고 함.
- ex) 비트코인, 이더리움, 스팀
- 지불 수단



### 토큰

- 독립된 블록체인 네트워크(메인넷)을 소유하지 않은 경우.

- 소유 개념이 포함된 자산(주식)

- ex)EOS

  - 즉, 플랫폼에서 서로 호환 가능한 규격을 만들다 보니 ERC20

  - Ethereum Request for Comment, and 20

    - 규격 6개 중 1개만 만족하면 됨.
    - `totalSupply` [Get the total token supply]
    - `balanceOf(address _owner) constant returns (uint256 balance)` [Get the account balance of another account with address *_owner*]
    - `transfer(address _to, uint256 _value) returns (bool success)` [Send *_value* amount of tokens to address *_to*]
    - `transferFrom(address _from, address _to, uint256 _value) returns (bool success)`[Send *_value* amount of tokens from address *_from* to address *_to*]
    - `approve(address _spender, uint256 _value) returns (bool success)` [Allow *_spender* to withdraw from your account, multiple times, up to the *_value* amount. If this function is called again it overwrites the current allowance with *_value*]
    - `allowance(address _owner, address _spender) constant returns (uint256 remaining)` [Returns the amount which *_spender* is still allowed to withdraw from *_owner*]

    

- 시큐리티 토큰 

  - 증권과 관련된 형태의 코인.

  - 가치 상승할 가능성에 근거하여 판매. 

  - Equity(에쿼티 토큰), 소유권 증명.

  -  주식을 가지고 있는 형태와 같은 효과.

    ​	

- 유틸리티 토큰

  - 미래에 창출할 서비스와 제품에 대한 접근권을 가지는 코인.
  - 개발된 제품은 아니지만 가치가 상승할 것을 기대하면서 투자(ICO) 하는것.
  - (도토리 같은 것).



- 처음에는 주식처럼 시큐리티 토큰을 썼지만 규제하면서 유틸리티 토큰으로 바꿈.



- 코인 : 화폐, 토큰 : 전자주식



- 메인넷 절차
  - ICO 공모 : 플랫폼을 빌려서 Dapp
  - 토큰 발행
  - 독자적인 생태계 구축을(메인넷) : 지갑 생성
  - 코인으로 전환
- ERC20 & ERC721 & ERC1155
  - ERC20 : 호환 가능한 토큰
  - ERC721 : 호환 불가능한 토큰
    - 크립토 키티 게임
    - 각각 고유한 가치를 부여해서 서로 대체 불가.
    - 하나 하나 토큰(고양이)은 서로 다른 가치의 토큰
    - ERC1155 : ERC20 + ERC 721

---

## SimpleToken.sol

```
pragma solidity ^0.4.18;

contract SimpleToken {
    //state var
    
    address owner;
    string public constant name = "MyCoin";
    string public constant symbol = "mc";
    uint8 public constant decimals = 0;
    
    mapping(address => uint) public balanceOf;
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    
    function transfer(address _to, uint _value) public payable {
        address _from = msg.sender;
        require(_to != address(0));
        require(balanceOf[_from] >= _value);
        
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        
        Transfer(_from, _to, _value);
    }
    
    function SimpleToken() public {
        balanceOf[msg.sender] = 100000;
    }
    
    function killcontract() public {
        if(owner == msg.sender)
        selfdestruct(owner);
    }
}
```

![1531449213388](C:\Users\Kchaos7\AppData\Local\Temp\1531449213388.png![1531449440001](C:\Users\Kchaos7\AppData\Local\Temp\1531449440001.png)

![1531449464388](C:\Users\Kchaos7\AppData\Local\Temp\1531449464388.png)

---



## vote_candidate.sol

```html
<!Doctype html>
<html>
<head>
<meta charset="UTF-8">
<script type="text/javascript" src="./javascripts/lib/bignumber.min.js"></script>
<script type="text/javascript" src="./javascripts/web3.min.js"></script>
<script type="text/javascript">
   
    var web3 = new Web3();
    var provider = new web3.providers.HttpProvider("http://172.17.144.222:8545");
    web3.setProvider(provider);
    console.log(web3);
    var vc = web3.eth.contract([
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
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
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
]).at("0xf14ed2a241af0d02507b1ffb69d1ce0ac7bd7f69");

function makeSelect() {

	var list = web3.eth.accounts;
	var select = document.getElementById('accounts');
	
	for(var i = 0; i < list.length; i++) {
		var opt = document.createElement('option');
		opt.value = list[i];
		opt.innerHTML = list[i];
		select.appendChild(opt);
	}

}

	function showCandidateList() {
		var selectCandidate = document.getElementById('candidates');
		var length = vc.getNumOfCandidates();
		for(var i = 0; i < length; i++) {
			var optionCandidate = document.createElement('option');
			optionCandidate.value = vc.getCandidateString(i);
			optionCandidate.innerHTML = vc.getCandidateString(i);
			selectCandidate.appendChild(optionCandidate);
		}
	}

	function showList(){
		var table=document.getElementById("table1");
		var length = vc.getNumOfCandidates();
		console.log(length);
		for(var i=0;i<length;i++){
			var candidate = vc.getCandidateString(i);
			var row=table.insertRow();
			var cell1=row.insertCell(0);
			var cell2=row.insertCell(1);
			cell1.innerHTML = candidate;
			cell2.innerHTML = vc.getScore(candidate);
			console.log(vc.getCandidateString(i));
		}
	}

	function vote(){
	var candidate=document.getElementById("candidates").value;
	var account=document.getElementById("accounts").value;
	web3.eth.defaultAccount = account;
	if(web3.personal.unlockAccount(account,document.getElementById('pass').value)){
		var alreadyVoted=vc.alreadyVoted();
		console.log(alreadyVoted);
		if(alreadyVoted)
			alert("이미 투표하셨습니다.");
		else
			vc.vote(candidate,function(err,result){ if(!err) alert("트랜잭션이 성공적으로 전송되었습니다.|n"+result)});		
	}
	}
	function addCand(){
		var candidate=document.getElementById("candidate").value;
		var account=document.getElementById("accounts").value;
		if(web3.personal.unlockAccount(account,document.getElementById('pass').value)){
			vc.addCandidate(candidate,{from:account,gas:2000000},function(err,result){ if(!err) alert("트랜잭션이 성공적으로 전송되었습니다.|n"+result)});	
		}

		console.log('add candidate : ' + account);
	}
</script>
<style>
table {    
	border-collapse: collapse;    
	border: 4px solid #bbb;	
	width: 50%;
}
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
<body>
    <h1>블록체인 투표</h1>
	<div>
	계정: <select id="accounts" name="accounts"></select><br> 
	패스워드: <input type="password" id="pass">	</div><br>
	<div> 
	<select id="candidates" name="candidates"></select>&nbsp;&nbsp;<button onClick="vote()">투표하기</button></div>
	<div>
	<input type="text" id="candidate">
	<button onClick="addCand()">후보 추가하기</button>
	</div>
	<fieldset>
	<legend>투표결과</legend>
	<table id="table1" />
	</fieldset>
	<script>
	makeSelect();
	showCandidateList(); 
	showList();
	</script>
</body>
</html>
	
```

> IP, ABI, CA 붙혀서 바꾸고 deploy 하여 pending일 때, miner.start(),  마찬가지로 창 띄워서 후보자 등록후 miner.start()하면 추가됨



![1531461571647](C:\Users\Kchaos7\AppData\Local\Temp\1531461571647.png)

```

```

