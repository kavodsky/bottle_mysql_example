<table class="table table-striped" id="result">
<caption><h3>First 10 Results</h3></caption>
    <thead>
        <tr>            
            <th>First Name</th>
            <th>Last Name</th>
            <th> Average Salary</th>
        </tr>
    </thead>
    </tbody>
        <% for row in rows: %>
            <tr>                
                <td>{{row[0]}}</td>
                <td> {{row[1]}}</td>
                <td>{{row[2]}} USD</td>
            </tr>
        <% end %>
    </tbody>
</table> 
