const table_user = document.getElementById("table_user").getElementsByTagName('tbody')[0];
const urlUsers = "http://127.0.0.1:8000/list_user"
const list_users =  fetch(urlUsers);


list_users.then( res =>{
  return res.json()

}).then(data => {
    
    data.forEach(item => {
        let tr = '<tr onclick="onClickTableRoom(this);"> <th scope="row">' +  item[0] + '</th>'+ '<td>' + item[1] + '</td> </tr>';
        table_user.innerHTML += tr;
    });
  
})


