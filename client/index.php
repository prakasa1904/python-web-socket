<html>
<head>
	<script type="text/javascript">
	var ws = new WebSocket('ws://localhost:8000/ws/foobar?subscribe-user');
	ws.onopen = function() {
		console.log("websocket connected");
	};
	ws.onmessage = function(e) {
		console.log("Received: " + e.data);
	};
	ws.onerror = function(e) {
		console.error(e);
	};
	ws.onclose = function(e) {
		console.log("connection closed");
	}
	function send_message(msg) {
		ws.send(msg);
	}
	</script>
</head>
<body>
	<div>Halaman Client</div>
</body>
</html>