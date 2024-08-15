#!/bin/bash
if [ $(which docker) ]; 
then
    echo "Docker está instalado"
else
    echo "Docker não está instalado"
    echo "Instalando docker através do script oficial, disponível em: https://docs.docker.com/engine/install/ubuntu/"
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
      $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    echo "Adicionando grupo docker para remover a necessidade do comando sudo, disponível em: https://docs.docker.com/engine/install/linux-postinstall/"
    sudo groupadd docker
    sudo usermod -aG docker $USER
    exec "$SHELL"
    docker run hello-world
fi