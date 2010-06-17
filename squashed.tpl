<!DOCTYPE html>
<html>
<head>
	<title>{{title}} - squashed!</title>
	<link rel="stylesheet" type="text/css" href="/static/squash.css" />
</head>

<body>
	<div id="container">
		<div>
			<form action="/shorten/" method="POST">
				<input type="text" name="url" id="urlfield" />
				<input type="image" src="/static/squash_btn.png" id="button" alt="Submit button" value="Submit" />
			</form>
		</div>
		<div id="result">{{result}}</div>
	</div>
	<div id="footer">Tinkered by Kenny Shen (<a href='http://www.northpole.sg'>www.northpole.sg</a>). <br />Powered by <a href='http://bottle.paws.de'>Bottle</a> and <a href='http://opensource.plurk.com/LightCloud'>Lightcloud</a>, written in <a href='http://www.python.org'>Python</a>.</div>
</body>
</html>