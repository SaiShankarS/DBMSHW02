<hr>
<h1>List of Pets</h1>
<ul>
    %for pet in pets:
        <li>{{pet["name"]}} -- {{pet["kind"]}}</li>
    %end
</ul>
<h1>Table of Pets</h1>
<table>
    %if len(pet) > 0:
        %for key in list(pets[0].keys())[1:]:
            <th>{{key}}</th>
        %end
    %end
    %for pet in pets:
        <tr>
            <td>{{pet["name"]}}</td>
            <td>{{pet["kind"]}}</td>
        </tr>
    %end
</table>
<hr>