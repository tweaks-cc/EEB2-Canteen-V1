class MenuObj {
    constructor(dates, dateWithIndex, menu) {
        // Initialize the 'dates' property with the array of dates wich each have the property false attached, which is needed later for the datefinding
        this.dates = dates
        this.dateToMenu = dateWithIndex
        this.menu = menu
    }
    
    //Here come the methods for the class
        
        sortDates() {
            // Sort the 'dates' array in ascending order
            this.dates.sort((a, b) => sorter(a) - sorter(b));
        }

        //returns either the date after the one given or that the given is the newest
        findDateAfter(givendate) {
            //If given not in array, put it in
            if (!this.dates.includes(givendate)) { this.dates.push(givendate); var pop = true }
            this.sortDates();
            // Gets index of given and returns the result
            let indexOfGiven = this.dates.indexOf(givendate);

            if (indexOfGiven >= this.dates.length - 1)
                 { var answer = false; }
            else { var answer = [this.dates[indexOfGiven + 1], "Is the next date after"]; };

            if (pop) { this.dates.splice(indexOfGiven, 1) }
            return answer
        }

        //returns either the date befor the one given or that the given is the oldest
        findDateBefore(givendate) {
            //If given not in array, put it in
            if (!this.dates.includes(givendate)) { this.dates.push(givendate); var pop = true }
            this.sortDates();
            // Gets index of given and returns the result
            let indexOfGiven = this.dates.indexOf(givendate);

            if (indexOfGiven == 0)
                 { var answer = false; }
            else { var answer = [this.dates[indexOfGiven - 1], "Is the next date before"]; };

            if (pop) { this.dates.splice(indexOfGiven, 1) }
            return answer
        }

        findSpecDate(givendate) {
            if (this.dates.includes(givendate)) {return true}
            else {return false}
        }

        menuOfDate(date) {
            let menu = this.menu[this.dateToMenu[date]]
            if (menu[5] == date) { menu.splice(5, 1); return menu}
        }
}

//creates the menu Object
const menu = new MenuObj(Object.keys(importedEssensDictDE[1]), importedEssensDictDE[1], importedEssensDictDE[2]);

//Sorts dates
function sorter(dateval) {
    //3202, 02, 01
    //Year reversed, Month, Day
    date = dateval.split(".");
    return date[2].split("").reverse().join("") + date[1] + date[0];
}

function specDateButton(dateInputVal) {
    //convert inputdate to our format
    dateInputVal.split("-")
    dateGFormat = `${ dateInputVal[2] }.${ dateInputVal[1] }.${ dateInputVal[0] }}`
    if (menu.dates.includes(dateGFormat)) {showMenu(dateGFormat)}
}

function showMenu(date) {
    let menu = menu.menuOfDate(date)
    date.split(".")
    let formatiertesdatum = `${menu[0]}, the ${date[0]}.${date[1]}`
    document.getElementById("Datum").innerHTML   = formatiertesdatum
    document.getElementById("Suppe").innerHTML   = menu[1]
    document.getElementById("Haupt1").innerHTML  = menu[2]
    document.getElementById("Haupt2").innerHTML  = menu[3]
    document.getElementById("Haupt3").innerHTML  = menu[4]
    document.getElementById("Dessert").innerHTML = menu[5]
}

function startup() {

    //startup

    if (menu.findSpecDate(dateTodayStr)) {
        showMenu(dateTodayStr)
    }
        //maybe inform about after and before
    else if (menu.findDateAfter(dateTodayStr)) {
        showMenu(menu.findDateAfter(dateTodayStr))
    }
    else {
        showMenu(menu.findDateBefore(dateTodayStr))
    }
}

/*
Playground


*/