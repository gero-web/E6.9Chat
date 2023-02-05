sessionStorage.setItem("name_room","test_boxName");
let user_username = sessionStorage.getItem("username")
const box_name = sessionStorage.getItem("name_room");
const url = "ws://localhost:8000/ws/chat/" + box_name ;

let chatSocket = new WebSocket(url);

function onClickTableRoom(e){
    const td = e.getElementsByTagName("td")[0].textContent;
    
    sessionStorage.setItem("name_room",td);
    reloadSocket();
   
 }
 


const SocketMessageOn = () => {
chatSocket.onmessage = (e) => {
    const data = JSON.parse(e.data);
 
    if(data && Array.isArray(data)){
        data.forEach(element => {
            document.querySelector('#chat-text').value += "sent by:" + element["username"] + "\n" + "message:\n" + element["message"] + "\n";
        });
    }else if (data) {
        document.querySelector('#chat-text').value += "sent by:" + data["username"] + "\n" + "message:\n" + data["message"] + "\n";
    } 
   
}
}

function reloadSocket(){
    if( chatSocket.readyState == chatSocket.OPEN)
    {
        chatSocket.close();
        document.querySelector('#chat-text').value = ""
    }   
    
    let boxNme = sessionStorage.getItem("name_room");
    let link = "ws://localhost:8000/ws/chat/" + boxNme ;
    chatSocket = null;
    chatSocket = new WebSocket(link);
    SocketMessageOn();

}


document.querySelector('#submit').onclick = (e)=>{
    const messageInputDom = document.querySelector('#input');
    const  message = messageInputDom.value;
    chatSocket.send(JSON.stringify(
        {
            'message':message,
            'username':user_username,
        }
    ));
};


