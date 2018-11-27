mkdir data/
cd data/
mkdir mp3/
cd mp3/

echo('Downloading first archive...')
wget http://mi.soi.city.ac.uk/datasets/magnatagatune/mp3.zip.001
echo('Downloading second archive...')
wget http://mi.soi.city.ac.uk/datasets/magnatagatune/mp3.zip.002
echo('Downloading third archive...')
wget http://mi.soi.city.ac.uk/datasets/magnatagatune/mp3.zip.003
echo('Extracting archives...')
unzip mp3.zip.001
unzip mp3.zip.002
unzip mp3.zip.003

find . -name "*.mp3" -exec mv "{}" ./ \;
rm -rf */ 
