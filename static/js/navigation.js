// Hightlight select tab in main navigation
function myfunc() {

    if ((window.location.href.indexOf('Source') !== -1) || (window.location.href.indexOf('SelectColumns') !== -1) || (window.location.href.indexOf('CommonField') !== -1)) {
        document.getElementById("main_input").style.pointerEvents = "none";
        document.getElementById("main_config").style.pointerEvents = "none";
        document.getElementById("main_output").style.pointerEvents = "none";
        document.getElementById("main_input").style.cursor = "default";
        document.getElementById("main_config").style.cursor = "default";
        document.getElementById("main_output").style.cursor = "default";
        document.getElementById("main_input_link").style.color = "black";
        document.getElementById("main_input").style.backgroundColor = "white";
    }

    if ((window.location.href.indexOf('ConcatCommonFields') !== -1) || (window.location.href.indexOf('ConcatFields') !== -1) || (window.location.href.indexOf('CatFieldSelection') !== -1) || (window.location.href.indexOf('ReplaceWords') !== -1) || (window.location.href.indexOf('ControlSettings') !== -1)) {
        document.getElementById("main_output").style.pointerEvents = "none";
        document.getElementById("main_output").style.cursor = "default";
        document.getElementById("main_config").style.pointerEvents = "none";
        document.getElementById("main_config").style.cursor = "default";
        document.getElementById("main_config").style.backgroundColor = "white";
        document.getElementById("main_input").style.pointerEvents = "visible";
        document.getElementById("main_input").style.cursor = "pointer";
        document.getElementById("main_input").style.backgroundColor = "rgb(31, 78, 120)";
        document.getElementById("main_input_link").style.color = "white";
        document.getElementById("main_config_link").style.color = "black";

    }

    if ((window.location.href.indexOf('ConcatCommonFields') !== -1) || (window.location.href.indexOf('ConcatFields') !== -1) || (window.location.href.indexOf('CatFieldSelection') !== -1) || (window.location.href.indexOf('ReplaceWords') !== -1) || (window.location.href.indexOf('ControlSettings') !== -1)) {
        document.getElementById("main_config").style.backgroundColor = "white";
        document.getElementById("main_config_link").style.color = "black";


    }

    if (window.location.href.indexOf('Output') !== -1) {
        document.getElementById("main_input").style.pointerEvents = "visible";
        document.getElementById("main_input").style.cursor = "pointer";
        document.getElementById("main_config").style.pointerEvents = "visible";
        document.getElementById("main_config").style.cursor = "pointer";
        document.getElementById("main_output").style.pointerEvents = "none";
        document.getElementById("main_output").style.cursor = "default";
        document.getElementById("main_output").style.backgroundColor = "white";
        document.getElementById("main_output_link").style.color = "black";
        document.getElementById("main_input_link").style.color = "white";
        document.getElementById("main_config_link").style.color = "white";
    }
    // Highlight subnavigation

    if (window.location.href.indexOf('ConcatCommonFields') !== -1) {
        document.getElementById("columns").style.color = "black";
        document.getElementById("1").style.backgroundColor = "white";
    }
    if (window.location.href.indexOf('CatFieldSelection') !== -1) {
        document.getElementById("concate").style.color = "black";
        document.getElementById("2").style.backgroundColor = "white";
    }

    if (window.location.href.indexOf('PreRun') !== -1) {
        document.getElementById("prerun").style.color = "black";
        document.getElementById("3").style.backgroundColor = "white";
    }
    if (window.location.href.indexOf('ReplaceWords') !== -1) {
        document.getElementById("replacewords").style.color = "black";
        document.getElementById("4").style.backgroundColor = "white";
    }
    if (window.location.href.indexOf('ControlSettings') !== -1) {
        document.getElementById("csettings").style.color = "black";
        document.getElementById("5").style.backgroundColor = "white";
    }

    if (window.location.href.indexOf('Output') !== -1) {
        document.getElementById("output").style.color = "black";
        document.getElementById("output").style.backgroundColor = "white";
        document.getElementById("main_input_link").style.color = "white";
        document.getElementById("main_config_link").style.color = "white";
    }
}

