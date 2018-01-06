# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.box_check_update = false
  config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  config.vm.provider "virtualbox" do |vb|
    # Customize the amount of memory on the VM
    vb.memory = "1024"
  end

  config.vm.provision "docker" do |d|
    # Installs Docker and pulls pocketinternet images
    # https://www.vagrantup.com/docs/provisioning/docker.html
    d.pull_images "pocketinternet/http-static:0.2"
    d.pull_images "pocketinternet/demo-dns:0.2"
    d.pull_images "pocketinternet/client:0.2"
    d.pull_images "pocketinternet/bird:0.2"
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get install --no-install-recommends --no-install-suggests -y python-pip python-setuptools
    cd /vagrant
    python setup.py develop
    pocketinternet configure-docker
  SHELL
end
