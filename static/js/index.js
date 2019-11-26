//Check if data got selected or not in input file section
function showExcel() {
    if (document.getElementById('table_1').rows.length !== 0) {
        document.getElementById("fileTitle1").innerHTML = "Source Data";
        document.getElementById("fileTitle2").innerHTML = "ITM Data";
    }
}

//Validate if source and ITM is selected or not
function ValidateFiles() {
    var strDataDisplay = document.getElementById('DisplayTable').innerHTML.trim();
    var strTest = "No data".trim();
    if (strDataDisplay == strTest) {
        alert("Please upload the source and  ITM file before proceeding further");
        return false;
    }
    else {
        return check();
    }
}

//Check if user has selected common columns or not and if not entire data should flow to the next page along with column names
function ValidateCommonFileds() {
    var strValues = $("#DDLActivites").children("option").filter(":selected").text();
    console.log("ab");
    // if (strValues == "") {
    //     alert("Please select common fields before proceeding further");
    //     return false;
    // }
    // else {
    //     return true;
    // }
    return True
}

//In Concate filed: check if new field name is given or not, fields are selected to concat or not, and new column is already present in the table or not
function ValidateReplaceField() {
    var bool = false;
    var strValue = document.getElementById('fname').value;
    var strColValues = $("#DDLActivites").children("option").filter(":selected").text().length;
    console.log(strValue);
    if (strValue == "") {
        console.log(strValue);
        alert("Please provide a field name");
        return false;
    }
    else if (strColValues == 0) {
        alert("Please select values before concat");
        return false;
    }
    var i;
    var options;
    var op;
    options = document.getElementById('DDLActivites').options;
    for (i = 0; i < options.length; i++) {
        op = options[i].text;
        op = String(op).toLowerCase();
        console.log(op);
        strValue = String(strValue).toLowerCase();
        console.log(strValue)
        if (op == strValue) {
            bool = true;
            break;
        }
    }
    if (bool) {
        alert("Column name already exists");
        return false;
    }
    return true;
}

//Create UI for columns not selected as category to define weights
function GetColumnsToWeight() {

    var i;
    var options;
    var op;
    console.log("abc");
    options = document.getElementById('SelectCatColumns').options;

    for (i = 0; i < options.length; i++) {
        op = options[i].text;
        document.getElementById(op).style.display = "block";
    }
    options = $("#SelectCatColumns").val();
    for (i = 0; i < options.length; i++) {
        op = options[i]
        document.getElementById(op).style.display = "none";
    }
    document.getElementById('weights').style.display = "block";
}

function validateIfcatIsSelected() {
    var strColValues = $("#SelectCatColumns").children("option").filter(":selected").text().length;

    if (strColValues == 0) {
        alert("Select columns as categorical columns");
        return false;
    }
}

function check() {
    if (document.getElementById("message").innerText == "False") {
        alert("No common columns");
        return false;
    }
}

//Checks if controls settings are not left blank
function validateControlSetting() {
    console.log('a');
    if ((document.getElementById('matches') == "") &&
        (document.getElementById('mimMQ') == "") &&
        (document.getElementById('drop') == "") &&
        (document.getElementById('goodmatch') == "") &&
        (document.getElementById('moderatematch') == "")) {

        alert("Required all inputs");
        return false;

    }
}

function saveNotes() {
    var Notes;
    Notes = document.getElementById("Notes").innerText;
    console.log(Notes);
}

//validate if user has given weights to all field or not
// function ValidateIfWeightisEmpty() {
//     var weight_boxes;
//     var weights = document.getElementsByName("weights")
//     weight_boxes = document.getElementsByName("weights_box")
//     var i ;
//     for (i=0;i<weights.length;i++){
//         if (weights[i].style.display == "block"){
//             if (weight_boxes[i].value == ""){
//                 alert("Please do not leave weights blank")
//                 return false;
//             }
//         }
//     }
// }
//
//

function ValidateCategory() {
    var strValues = $("#SelectCatColumns").children("option").filter(":selected").text();
    console.log("ab");
    return true;
}

function DisplayAlert() {
    console.log("Shikha");
  {
        console.log("Shikha");
        alert("jgfsjak");
    }



}