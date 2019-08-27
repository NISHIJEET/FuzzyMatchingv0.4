
function uploaded() {
    console.log('Uploaded');

    if (window.location.href.indexOf('Input') !== -1) {
        console.log('Input');
        document.getElementById("input").style.borderBottom = "4px solid orange";
    }
}

function showExcel() {
    if (document.getElementById('table_1').rows.length !== 0) {
        document.getElementById("fileTitle1").innerHTML = "Source Data";
        document.getElementById("fileTitle2").innerHTML = "ITM Data";
    }
}

function ValidateFiles() {
    var strDataDisplay = document.getElementById('DisplayTable').innerHTML.trim();
    var strTest = "No data".trim();
    if (strDataDisplay == strTest){
        alert("Please upload the source and  ITM file before proceeding further");
        return false;
    }
    else{
        return true;
    }
}