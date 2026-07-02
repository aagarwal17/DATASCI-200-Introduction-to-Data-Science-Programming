function loadDoc(fileToGet, number) {
    var cellNo = "showNotes"+number;
	var filename = fileToGet;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById(cellNo).innerHTML = this.responseText;
            this.responseText;
        }
    };
    xhttp.open("GET", fileToGet, true);
    xhttp.send(); 
}
