# Client

## Setup on a raspberry controller

1. On the raspberry

    ```bash
    sudo apt update -y
    sudo apt upgrade -y
    sudo apt autoremove -y
    curl -sSL https://dot.net/v1/dotnet-install.sh | bash /dev/stdin --channel LTS
    echo 'export DOTNET_ROOT=$HOME/.dotnet' >> ~/.bashrc
    echo 'export PATH=$PATH:$HOME/.dotnet' >> ~/.bashrc
    source ~/.bashrc
    sudo mkdir -p /opt/Client
    sudo chown wow:wow /opt/Client
    ```

2. On the dev machine

    ```bash
    dotnet publish -c Release
    scp -r bin/Release/net8.0/* wow@192.168.1.95:/opt/Client/
    cat dotnet-client.service | ssh wow@192.168.1.95 "sudo tee /etc/systemd/system/dotnet-client.service"
    ```

3. On the raspberry

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable dotnet-client.service
    sudo systemctl start dotnet-client.service
    sudo systemctl status dotnet-client.service
    journalctl -u dotnet-client.service
    ```
