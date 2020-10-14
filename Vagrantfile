Vagrant.configure("2") do |config|
    # Based on the official Hashicorp Ubuntu box image
    config.vm.box = "hashicorp/bionic64"
    # Provision with ansible
    config.vm.provision "ansible" do |ansible|
      ansible.playbook = "provisioning/playbook.yml"
      # Tell Ansible to use python version 3
      ansible.extra_vars = { ansible_python_interpreter:"/usr/bin/python3" }
    end
    # Sets a private IP address
    config.vm.network "private_network", ip: "192.168.50.3"
  end