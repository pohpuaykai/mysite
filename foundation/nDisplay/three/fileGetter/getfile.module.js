class FileGetter {
    /* OG from https://www.w3schools.com/js/js_ajax_intro.asp
    function loadDoc() {
      const xhttp = new XMLHttpRequest();
      xhttp.onload = function() {
        document.getElementById("demo").innerHTML = this.responseText;
        }
      xhttp.open("GET", "ajax_info.txt", true);
      xhttp.send();
    }
    
    */
    
    constructor(filepath, connection_type) { //object is self, filepath is the path on disk, connection_type is HTTP: GET...
        this.xhttp = new XMLHttpRequest();
        var responseText = null;
        this.xhttp.onreadystatechange = function() {
            if (this.readyState == 4) {
                responseText = this.responseText;
            }
        }
        this.xhttp.open(connection_type, filepath, false); //true means async
        this.xhttp.send();
        this.responseText = responseText;
    }
    
    
}

export { FileGetter };