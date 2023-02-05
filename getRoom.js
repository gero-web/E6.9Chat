const table_room = document.getElementById("table_room").getElementsByTagName('tbody')[0];
const urlRoom = "http://127.0.0.1:8000/room/"
const list_room =  fetch(urlRoom);


list_room.then( res =>{
  return res.json()

}).then(data => {
    
    data.forEach(item => {
        let tr = '<tr onclick="onClickTableRoom(this);"> <th scope="row">' +  item["id"] + '</th>'+ '<td>' + item["name_room"] + '</td> </tr>';
        table_room.innerHTML += tr;
    });
  
})


