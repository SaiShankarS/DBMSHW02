<html>
    <body>
        <h1>List of Pets</h1>
        <ul>
        % for item in data:
            <li>{{item[1] + ' - ' + item[2]}}</li>
        % end
        </ul>
        <h1>Table of Pets</h1>
        <table>
        % for name in names[1:]:
            <th>{{name}}</th>
        % end
        % for item in data:
            <tr>
                <td>{{item[1]}}</td>
                <td>{{item[2]}}</td>
            <tr>
        % end
        </table>
    </body>
</html>