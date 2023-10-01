<html>
<body>
<hr/>
<form action="/update" method="post">
  <input type="hidden" name="id" value="{{str(item['id'])}}"/>
  <p>Description:<input name="description" value="{{item['description']}}"/></p>
  <p><button type="submit">Submit</button></p>
<form>
<hr/>
<body>
</html>