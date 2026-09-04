function analyzeEmails(){
    let emails = document.getElementById("emailInput").value;

    fetch("/analyze",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({emails:emails})
    })
    .then(res=>res.json())
    .then(response=>{
        let data = response.data;
        let table = document.getElementById("resultTable");
        let container = document.getElementById("tableContainer");
        let summary = document.getElementById("summary");

        table.innerHTML="";
        data.forEach(item=>{
            let row = `
            <tr>
            <td>${item.email}</td>
            <td>${item.domain}</td>
            <td>${item.domain_type}</td>
            <td>${item.person}</td>
            <td>${item.university}</td>
            <td>${item.company}</td>
            </tr>`;
            table.innerHTML += row;});

        summary.innerHTML = `Total Valid Emails: ${response.total_valid} | Total Invalid Emails: ${response.total_invalid}`;
        container.style.display="block";});
}

function downloadExcel(){
    window.location.href = "/download";
}
