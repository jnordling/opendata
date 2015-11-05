Vagrant.configure(2) do |config|
  config.vm.box = "hashicorp/precise32"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.synced_folder "./", "/home/apps/"
  config.vm.provision :shell, path: "ona_ubuntu_setup.sh"
end
