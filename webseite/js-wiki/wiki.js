var pagecontent = {}
//Create a new object to interact with the server
async function search(item) {
    document.getElementById("errorspacing").style.display = "none"
    document.getElementById("showsearch").style.display   = "none"
    document.getElementById("search1").style.display      = "none"
    document.getElementById("search2").style.display      = "none"
    document.getElementById("search3").style.display      = "none"
    document.getElementById("search4").style.display      = "none"
    document.getElementById("search5").style.display      = "none"
    pagecontent = {}
    console.log()
    var xhr = new XMLHttpRequest();

    
    var url = `https://${sprache["wiki"]}.wikipedia.org/w/api.php?action=query&rvparse=1&prop=extracts&origin=*&exintro&explaintext&format=json&generator=search&gsrnamespace=0&gsrlimit=5&gsrsearch='${item}'`;

    // Provide 3 arguments (GET/POST, The URL, Async True/False)
    xhr.open('GET', url, true);

    // Once request has loaded...
    xhr.onload = function () {
        // Parse the request into JSON
        var data = JSON.parse(this.response);
        
        return
        try {
            var test = data.query[0]
        }
        catch() {
            console.log("hello error")
            document.getElementById("showsearch").innerHTML       = sprache["wikisearcherror"]
            document.getElementById("errorspacing").style.display = "inline"
            return
        }
        // Log the data object
        //console.log(data);
        
        
        // Log the page objects
        //console.log(data.query.pages)

        // Loop through the data object
        // Pulling out the titles of each page
        var x = 1
        for (var i in data.query.pages) {
            pagecontent[data.query.pages[i].title] = data.query.pages[i].extract
            //console.log(data.query.pages[i].extract)
            document.getElementById(`search${x}`).innerText = data.query.pages[i].title
            x++
        }
        console.log(pagecontent)
        document.getElementById("search1").style.display = "inline"
        document.getElementById("search2").style.display = "inline"
        document.getElementById("search3").style.display = "inline"
        document.getElementById("search4").style.display = "inline"
        document.getElementById("search5").style.display = "inline"
    }
    // Send request to the server asynchronously
    xhr.send();
}