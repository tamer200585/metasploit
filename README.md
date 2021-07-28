pkg install ruby -y

pkg install root-repo -y

pkg install unstable-repo -y

pkg install git -y

git clone https://github.com/tamer200585/metasploit

cd metasploit

mv metasploit.sh ~

cd ..

chmod +x metasploit.sh

./metasploit.sh
