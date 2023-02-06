#!/bin/bash

br="printf "\n""

file=input-$(date +%W -d "$1 Weeks")-$(date +%Y -d "$1 Weeks").xlsx
dir=../auswerten-python/menues
bakDir=$dir/backup-inputs
weekNum="$(printf $((
$(date +%-W) - $(date +%-W -d "$(date +%Y)/$(date +%m)/01")
)))"

fetch() {
	curl -f https://www.woluweparents.org/wp-content/uploads/$(date +%Y -d "-1 Month")/$(date +%m -d "-1 Month")/Semaine-$(date +%W -d "$1 Weeks")-$(date +%d -d "Sunday -6 Days $1 Weeks")-$(env LC_TIME=fr_FR.UTF-8 date +%B -d "Sunday -6 Days $1 Weeks" | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y)-$(date +%d -d "Sunday -2 Days $1 Weeks")-$(env LC_TIME=fr_FR.UTF-8 date +%B -d "Sunday -2 Days $1 Weeks" | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y).xlsx -o $dir/$file \
	|| curl -f https://www.woluweparents.org/wp-content/uploads/$(date +%Y)/$(date +%m)/Semaine-$(date +%W -d "$1 Weeks")-$(date +%d -d "Sunday -6 Days $1 Weeks")-$(env LC_TIME=fr_FR.UTF-8 date +%B -d "Sunday -6 Days $1 Weeks" | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y)-$(date +%d -d "Sunday -2 Days $1 Weeks")-$(env LC_TIME=fr_FR.UTF-8 date +%B -d "Sunday -2 Days $1 Weeks" | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y).xlsx -o $dir/$file
}

mv -f $dir/input-*.xlsx $bakDir

if [[ $weekNum == 0 ]] ; then
	fetch +0
	fetch +1
	fetch +2
	fetch +3
	fetch +4
elif [[ $weekNum == 1 ]] ; then
	fetch -1
	fetch +0
	fetch +1
	fetch +2
	fetch +3
elif [[ $weekNum == 2 ]] ; then
	fetch -2
	fetch -1
	fetch +0
	fetch +1
	fetch +2
elif [[ $weekNum == 3 ]] ; then
	fetch -3
	fetch -2
	fetch -1
	fetch +0
	fetch +1
elif [[ $weekNum == 4 ]] ; then
	fetch -4
	fetch -3
	fetch -2
	fetch -1
	fetch +0
else
	echo "not found"
fi
