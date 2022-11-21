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
    var xhr = new XMLHttpRequest();

    
    var url = `https://${sprache["wiki"]}.wikipedia.org/w/api.php?action=query&rvparse=1&prop=extracts&origin=*&exintro&explaintext&format=json&generator=search&gsrnamespace=0&gsrlimit=5&gsrsearch='${item}'`;

    // Provide 3 arguments (GET/POST, The URL, Async True/False)
    xhr.open('GET', url, true);

    // Once request has loaded...
    xhr.onload = function () {
        // Parse the request into JSON
        var data = JSON.parse(this.response);
        
        try {
            var test = data.query[0]
        }
        catch (err) {
            if (err.name == "TypeError") {
                console.log("page item not found")
                document.getElementById("showsearch").innerHTML       = sprache["wikisearcherror"]
                document.getElementById("showsearch").  style.display = "block"
                document.getElementById("errorspacing").style.display = "block"
                return
            }
            else {
                console.log(err)
            }
        }

        // Loop through the data object
        // Pulling out the titles of each page
        var x = 1
        for (var i in data.query.pages) {
            if (data.query.pages[i])
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