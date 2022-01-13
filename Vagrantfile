# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
 # The most common configuration options are documented and commented below.
 # For a complete reference, please see the online documentation at
 # https://docs.vagrantup.com.

 # Every Vagrant development environment requires a box. You can search for
 # boxes at https://vagrantcloud.com/search.

 #이미지 코드
 config.vm.box = "ubuntu/bionic64"

 #특정 버전 유지를 위한 코드 :특정 작성 시점에 버전을 이용하므로 위 이미지 안깨진대
 config.vm.box_version = "~> 20191107.0.0"

#포트 지정
 config.vm.network "forwarded_port", guest: 8000, host: 8000

 config.vm.provision "shell", inline: <<-SHELL
  #충돌 발생 위험의 자동 업데이트를 비활성화? 하는 코드
   systemctl disable apt-daily.service
   systemctl disable apt-daily.timer

   #우분투 처음 실행 시 업데이트 코드
   sudo apt-get update
   #python 3 가상환경 및 zip 설치 코드 : zip은 나중에 압축하는 zip파일 만드는데 사용하는 듯
   sudo apt-get install -y python3-venv zip

   #bash aliases file 생성
   touch /home/vagrant/.bash_aliases
   if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
     #python 3을 vagrant 사용자를 위한 기본 python 버전으로 설정
     # = 기본으로 python을 실행할 때마다 여기서는 python 3을 자동 실행한다는 뜻 : 편리!
     echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
     echo "alias python='python3'" >> /home/vagrant/.bash_aliases
   fi
 SHELL
end
