# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.box_check_update = false
  config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  config.vm.provider "virtualbox" do |vb|
    # Customize the amount of memory on the VM:
    vb.memory = "2048"
  end

  config.vm.provision "shell", inline: <<-SHELL
    # apt-get update
    apt-get install --no-install-recommends --no-install-suggests python-pip python-setuptools
    pip install docker-compose
  SHELL

  config.vm.provision "docker" do |d|
    # Installs Docker by default
    # https://www.vagrantup.com/docs/provisioning/docker.html
  end
end
