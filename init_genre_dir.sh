mkdir $1
cd $1
while read dirname others; do
    mkdir "$dirname"
done < ../../genres.txt
cd ../..
