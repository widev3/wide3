sudo apt install build-essential -y
sudo apt install cmake -y
wget https://github.com/AlexandreRouma/SDRPlusPlus/archive/refs/tags/nightly.zip
unzip nightly.zip
rm -rf nightly.zip
cd SDRPlusPlus-nightly #SDRPlusPlus-nightly
mkdir build
cd build #SDRPlusPlus-nightly/build

sudo apt install libzstd-dev -y
sudo apt install libairspy-dev -y
sudo apt install libairspyhf-dev -y
sudo apt install libhackrf-dev -y
sudo apt install libiio-dev -y
sudo apt install libad9361-dev -y
sudo apt install librtlsdr-dev -y
sudo apt install portaudio19-dev -y

wget https://github.com/drowe67/codec2/archive/refs/tags/1.2.0.zip
unzip 1.2.0.zip
cd codec2-1.2.0 #SDRPlusPlus-nightly/build/codec2-1.2.0
mkdir build
cd build #SDRPlusPlus-nightly/build/codec2-1.2.0/build
cmake ..
make -j $(nproc)
sudo make install
sudo ldconfig
cd .. #SDRPlusPlus-nightly/build/codec2-1.2.0
cd .. #SDRPlusPlus-nightly/build
rm -rf codec2-1.2.0

wget https://www.sdrplay.com/software/SDRplay_RPi_Scripts_v0.3.zip
mkdir SDRplayAPI
unzip SDRplay_RPi_Scripts_v0.3.zip -d SDRplayAPI
sed -i 's/ARM32-3.07.2.run/ARM64-3.07.1.run/g' ./SDRplayAPI/1installAPI.sh
sh ./SDRplayAPI/1installAPI.sh
sudo systemctl start sdrplay

rm -rf *
cmake .. -DOPT_BUILD_SOAPY_SOURCE=OFF 
make -j $(nproc)
sudo make install
sudo ldconfig
cd ~
rm -rf SDRPlusPlus-nightly

wget https://github.com/gttrcr/whistle_of_wind/archive/refs/tags/25.08.27.zip