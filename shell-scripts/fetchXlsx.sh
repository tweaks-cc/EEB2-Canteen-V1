#! /usr/bin/env sh

br="printf \n"

weekNum="$(printf $((
$(date +%-W) - $(date +%-W -d "$(date +%Y)/$(date +%m)/01")
)))"
dir=../auswerten-python/menues
bakDir=$dir/backup-inputs

fetch() {
	file=input-wn$(date +%W -d "$1 Weeks")-m$(date +%m -d "$1 Weeks")-y$(date +%Y -d "$1 Weeks").xlsx

	printf "$(tput setaf 4)Fetching $(tput smul)https://www.woluweparents.org/wp-content/uploads/$(date +%Y -d "-1 Month")/$(date +%m -d "-1 Month")/$(tput bold)Semaine-$(date +%W -d "$1 Weeks")-$(date +%d -d "Sunday -6 Days $1 Weeks")-$(env LC_TIME=fr_FR.UTF-8 date +%B -d "Sunday -6 Days $1 Weeks" | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y)-$(date +%d -d "Sunday -2 Days $1 Weeks")-$(env LC_TIME=fr_FR.UTF-8 date +%B -d "Sunday -2 Days $1 Weeks" | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y).xlsx$(tput sgr0)\n" \
	\
	; curl -f https://www.woluweparents.org/wp-content/uploads/$(date +%Y -d "-1 Month")/$(date +%m -d "-1 Month")/Semaine-$(date +%W -d "$1 Weeks")-$(date +%d -d "Sunday -6 Days $1 Weeks")-$(env LC_TIME=fr_FR.UTF-8 date +%B -d "Sunday -6 Days $1 Weeks" | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y)-$(date +%d -d "Sunday -2 Days $1 Weeks")-$(env LC_TIME=fr_FR.UTF-8 date +%B -d "Sunday -2 Days $1 Weeks" | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y).xlsx -o $dir/$file \
	\
	&& printf "$(tput setaf 2)Fetched to $dir/$(tput bold)$file$(tput sgr0)\n\n" \
	|| printf "$(tput bold setaf 1)Unable to fetch$(tput sgr0)\n\n" \
	\
	; printf "$(tput setaf 4)Fetching $(tput smul)https://www.woluweparents.org/wp-content/uploads/$(date +%Y)/$(date +%m)/$(tput bold)Semaine-$(date +%W -d "$1 Weeks")-$(date +%d -d "Sunday -6 Days $1 Weeks")-$(env LC_TIME=fr_FR.UTF-8 date +%B -d "Sunday -6 Days $1 Weeks" | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y)-$(date +%d -d "Sunday -2 Days $1 Weeks")-$(env LC_TIME=fr_FR.UTF-8 date +%B -d "Sunday -2 Days $1 Weeks" | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y).xlsx$(tput sgr0)\n" \
	\
	; curl -f https://www.woluweparents.org/wp-content/uploads/$(date +%Y)/$(date +%m)/Semaine-$(date +%W -d "$1 Weeks")-$(date +%d -d "Sunday -6 Days $1 Weeks")-$(env LC_TIME=fr_FR.UTF-8 date +%B -d "Sunday -6 Days $1 Weeks" | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y)-$(date +%d -d "Sunday -2 Days $1 Weeks")-$(env LC_TIME=fr_FR.UTF-8 date +%B -d "Sunday -2 Days $1 Weeks" | cut -c 1-4 | iconv -t ASCII//TRANSLIT)-$(date +%Y).xlsx -o $dir/$file \
	\
	&& printf "$(tput setaf 2)Fetched to $dir/$(tput bold)$file$(tput sgr0)\n\n" \
	|| printf "$(tput bold setaf 1)Unable to fetch$(tput sgr0)\n\n"
}

if [[ -e $bakDir ]] ; then
	mv -f $dir/input-*.xlsx $bakDir	
else
	mkdir -p $bakDir
	mv -f $dir/input-*.xlsx $bakDir
fi

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
