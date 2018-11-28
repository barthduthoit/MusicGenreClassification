mkdir $1
while read dirname others; do
    mkdir "$1/$dirname"
done < genres.txt
