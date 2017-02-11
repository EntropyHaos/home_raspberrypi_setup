#!/bin/bash

function init(){
    local admin_user_name="";
    do_update;
    do_non_interactive_dist_upgrade;
    setup_apache;
    setup_git;
    delete_this_script;
}

function do_update(){
    sudo apt-get update;
}

function do_non_interactive_dist_upgrade(){
    DEBIAN_FRONTEND=noninteractive sudo apt-get -o Dpkg::Options::="--force-confnew" --force-yes -fuy dist-upgrade;    
}

function setup_apache(){
    cd ~;
    sudo apt-get install apache2 -y;
    cd /var/www/html;
    sudo chown $admin_user_name: index.html;
    cd ..;
    sudo chown $admin_user_name: html/;
    cd ~;
}

function setup_git(){
    sudo add-apt-repository ppa:git-core/ppa -y
    sudo apt-get update
    sudo apt-get install git -y
    git --version
}

function delete_this_script(){
    cd ~;
    local script_name;
    script_name=`basename "$0"`
    rm -rf ./$script_name;
}

init
