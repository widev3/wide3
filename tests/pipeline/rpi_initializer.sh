sudo apt update -y
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt install wget -y
sudo apt install cmake -y
sudo apt install build-essential -y

cd ~
wget https://github.com/drowe67/codec2/archive/refs/tags/1.2.0.zip
unzip 1.2.0.zip
cd codec2-1.2.0
mkdir build
cd build
cmake ..
make -j $(nproc)
sudo make install
sudo ldconfig
cd ~
rm -rf codec2-1.2.0
rm -rf 1.2.0.zip

cd ~
wget https://www.sdrplay.com/software/SDRplay_RPi_Scripts_v0.3.zip
mkdir SDRplayAPI
unzip SDRplay_RPi_Scripts_v0.3.zip -d SDRplayAPI
sed -i 's/ARM32-3.07.2.run/ARM64-3.07.1.run/g' ./SDRplayAPI/1installAPI.sh
sh ./SDRplayAPI/1installAPI.sh
sudo systemctl start sdrplay
cd ~
rm -rf SDRplayAPI
rm -rf SDRplay_RPi_Scripts_v0.3.zip
rm -rf SDRplay_RSP_API-ARM64-3.07.1.run

sudo apt update -y
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt install libglfw3 -y
sudo apt install libglfw3-dev -y
sudo apt install libfftw3-3 -y
sudo apt install libfftw3-dev -y
sudo apt install libvolk2-dev -y
sudo apt install libzstd-dev -y
sudo apt install libairspy-dev -y
sudo apt install libairspyhf-dev -y
sudo apt install librtaudio-dev -y
sudo apt install libhackrf-dev -y
sudo apt install libiio-dev -y
sudo apt install libad9361-dev -y
sudo apt install librtlsdr-dev -y

cd ~
git clone https://github.com/AlexandreRouma/SDRPlusPlus
# wget https://github.com/AlexandreRouma/SDRPlusPlus/archive/refs/tags/nightly.zip
# unzip nightly.zip
cd SDRPlusPlus
mkdir build
cd build

rm -rf *
cmake .. \
  -DOPT_BUILD_AIRSPY_SOURCE=OFF \
  -DOPT_BUILD_AIRSPYHF_SOURCE=OFF \
  -DOPT_BUILD_AUDIO_SOURCE=OFF \
  -DOPT_BUILD_BLADERF_SOURCE=OFF \
  -DOPT_BUILD_FILE_SOURCE=OFF \
  -DOPT_BUILD_HACKRF_SOURCE=OFF \
  -DOPT_BUILD_HERMES_SOURCE=OFF \
  -DOPT_BUILD_LIMESDR_SOURCE=OFF \
  -DOPT_BUILD_PERSEUS_SOURCE=OFF \
  -DOPT_BUILD_PLUTOSDR_SOURCE=ON \
  -DOPT_BUILD_RFSPACE_SOURCE=OFF \
  -DOPT_BUILD_RTL_SDR_SOURCE=ON \
  -DOPT_BUILD_RTL_TCP_SOURCE=OFF \
  -DOPT_BUILD_SDRPLAY_SOURCE=ON \
  -DOPT_BUILD_SDRPP_SERVER_SOURCE=ON \
  -DOPT_BUILD_SOAPY_SOURCE=OFF \
  -DOPT_BUILD_SPECTRAN_SOURCE=OFF \
  -DOPT_BUILD_SPECTRAN_HTTP_SOURCE=OFF \
  -DOPT_BUILD_SPYSERVER_SOURCE=ON \
  -DOPT_BUILD_USRP_SOURCE=OFF \
  -DOPT_BUILD_ANDROID_AUDIO_SINK=OFF \
  -DOPT_BUILD_AUDIO_SINK=OFF \
  -DOPT_BUILD_NETWORK_SINK=OFF \
  -DOPT_BUILD_NEW_PORTAUDIO_SINK=OFF \
  -DOPT_BUILD_PORTAUDIO_SINK=OFF \
  -DOPT_BUILD_ATV_DECODER=OFF \
  -DOPT_BUILD_FALCON9_DECODER=OFF \
  -DOPT_BUILD_M17_DECODER=OFF \
  -DOPT_BUILD_METEOR_DEMODULATOR=OFF \
  -DOPT_BUILD_RADIO=OFF \
  -DOPT_BUILD_WEATHER_SAT_DECODER=OFF \
  -DOPT_BUILD_DISCORD_PRESENCE=OFF \
  -DOPT_BUILD_FREQUENCY_MANAGER=OFF \
  -DOPT_BUILD_RECORDER=OFF \
  -DOPT_BUILD_RIGCTL_CLIENT=OFF \
  -DOPT_BUILD_RIGCTL_SERVER=ON \
  -DOPT_BUILD_SCANNER=OFF \
  -DOPT_BUILD_SCHEDULER=OFF

make -j 1
sudo make install
sudo ldconfig
cd ~
rm -rf ~/.config/sdrpp/ #in case of previous installations
rm -rf SDRPlusPlus-nightly

SERVICE_NAME=sdrpp_server
sudo bash -c "cat > /etc/systemd/system/$SERVICE_NAME.service" <<EOL
[Unit]
Description=$SERVICE_NAME
After=network.target

[Service]
ExecStart=/usr/bin/sdrpp --server --port 56153
WorkingDirectory=/home/wow
StandardOutput=inherit
StandardError=inherit
Restart=always
User=wow

[Install]
WantedBy=multi-user.target
EOL

sudo systemctl daemon-reload
sudo systemctl enable $SERVICE_NAME.service
sudo systemctl start $SERVICE_NAME.service

cd ~
rm -rf whistle_of_wind
git clone https://github.com/gttrcr/whistle_of_wind
cd whistle_of_wind
git config -f .gitmodules submodule.control/keypad/despyner.url https://github.com/gttrcr/despyner.git
git config -f .gitmodules submodule.control/server/despyner.url https://github.com/gttrcr/despyner.git
git submodule update --init --recursive
cd control/server
sudo apt install python3-pip -y
python3 -m venv u
source u/bin/activate
pip3 install -r requirements.txt

SERVICE_NAME=control_server
sudo bash -c "cat > /etc/systemd/system/$SERVICE_NAME.service" <<EOL
[Unit]
Description=$SERVICE_NAME
After=network.target

[Service]
ExecStart=/usr/bin/bash /home/wow/whistle_of_wind/control/server/$SERVICE_NAME.sh
WorkingDirectory=/home/wow
StandardOutput=inherit
StandardError=inherit
Restart=always
User=wow

[Install]
WantedBy=multi-user.target
EOL

sudo systemctl daemon-reload
sudo systemctl enable $SERVICE_NAME.service
sudo systemctl start $SERVICE_NAME.service