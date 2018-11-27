mkdir data/
cd data/
mkdir mp3/
cd mp3/

echo Downloading first archive...
wget http://mi.soi.city.ac.uk/datasets/magnatagatune/mp3.zip.001
echo Downloading second archive...
wget http://mi.soi.city.ac.uk/datasets/magnatagatune/mp3.zip.002
echo Downloading third archive...
wget http://mi.soi.city.ac.uk/datasets/magnatagatune/mp3.zip.003
echo Extracting archives...
unzip -qq mp3.zip.001
unzip -qq mp3.zip.002
unzip -qq mp3.zip.003

echo Moving mp3 files to data/mp3
find . -name "*.mp3" -exec mv "{}" ./ \;
rm -rf */ 
rm *.zip*

cd ..
mkdir csv/
cd csv/
wget http://he3.magnatune.com/info/song_info.csv
cd ../..

./init_genre_dir.sh data/wav
python3 util/make_wav.py

./init_genre_dir.sh data/spectogram
python3 util/make_spectogram.py
