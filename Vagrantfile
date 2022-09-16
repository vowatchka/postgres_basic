# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/focal64"

    config.vm.network "forwarded_port", guest: 5432, host: 54320

    config.vm.provider "virtualbox" do |vb|
        vb.customize ["modifyvm", :id, "--uart1", "0x3F8", "4"]
        vb.customize ["modifyvm", :id, "--uartmode1", "file", File::NULL]
        vb.memory = 2048
    end

    config.vm.provision "ansible_local" do |ansible|
        ansible.verbose = "vv"
        ansible.playbook = "vagrant/provisioning/provision.yml"
    end
end
