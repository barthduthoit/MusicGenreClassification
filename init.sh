mkdir -p data/mp3
mkdir data/plots
mkdir data/models
echo Downloading first archive...
wget -q --show-progress http://mi.soi.city.ac.uk/datasets/magnatagatune/mp3.zip.001 -P data/mp3
echo Downloading second archive...
wget -q --show-progress http://mi.soi.city.ac.uk/datasets/magnatagatune/mp3.zip.002 -P data/mp3
echo Downloading third archive...
wget -q --show-progress http://mi.soi.city.ac.uk/datasets/magnatagatune/mp3.zip.003 -P data/mp3
echo Extracting archives...
cat data/mp3/mp3.zip.001 > data/mp3/mp3.zip
cat data/mp3/mp3.zip.002 >> data/mp3/mp3.zip
cat data/mp3/mp3.zip.003 >> data/mp3/mp3.zip
unzip -qq data/mp3/mp3.zip -d data/mp3

echo '\nMoving mp3 files to data/mp3...'
find . -name "*.mp3" -exec mv "{}" ./data/mp3 \;
rm -rf data/mp3/*/ 
rm data/mp3/*.zip*

mkdir data/csv/
echo '\nDownloading csv data...'
wget -q http://he3.magnatune.com/info/song_info.csv -P data/csv

./init_genre_dir.sh data/wav
echo '\nConverting mp3s to wavs...'
python3 util/make_wav.py
