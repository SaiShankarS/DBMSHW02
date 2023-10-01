<html>
<body>
<h2>Shopping List</h2>
<hr/>
<table>
% for item in shopping_list:
  <tr>
  <td>{{str(item['description'])}}</td>
  <td><a href="/update/{{str(item['id'])}}">update</a></td>
  <td><a href="/delete/{{str(item['id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/add">Add a new item</a>
<hr/>
</body>
</html>