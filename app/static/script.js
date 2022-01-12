
var ws = new WebSocket("ws://localhost:8000/api/v1/ws");
ws.onmessage = function(event) {
    var messages = document.getElementById('messages')
    var message = document.createElement('li')
    var dataFromJson = JSON.parse(event.data)
    let dataString = dataFromJson.id + '.'+ ' ' + "message " + " - " + dataFromJson.message
    var content = document.createTextNode(dataString)
    message.appendChild(content)
    messages.appendChild(message)
};
function sendMessage(event) {
    var input = document.getElementById("messageText")
    if (!input.value){
        window.alert('Inter your value')
        return false
    }
    ws.send(input.value)
    input.value = ''
    event.preventDefault()
}
