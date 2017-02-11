#!/bin/bash

function setvars(){
    new_user_name="";
    new_users_public_ssh_key="";
}

function init(){
    local new_user_name;
    setvars;
    clear;
    create_line_across_terminal;
    add_new_user;
    setup_ssh_key_for_new_user;
    create_script_to_delete_default_pi_user;
}

function add_new_user(){
    sudo adduser --disabled-login --gecos "" "$new_user_name"
    echo "$new_user_name    ALL = NOPASSWD: ALL" >> /etc/sudoers;
}

function setup_ssh_key_for_new_user(){
    cd ..;
    cd $new_user_name;
    mkdir .ssh;
    printf "$new_users_public_ssh_key" >> .ssh/authorized_keys;
    chmod 700 .ssh/
    chmod 600 .ssh/authorized_keys
    chown -R $new_user_name:$new_user_name .ssh
    cd ..;
    cd pi/;
}

function create_script_to_delete_default_pi_user(){
    cd ..;
    cd $new_user_name;
    cat << 'EOF' >> delete_default_pi_user.bash;
#!/bin/bash

function init(){
    del_default_pi_user;
    delete_this_script;
}
function del_default_pi_user(){
    sudo deluser --force --remove-all-files pi;
}

function delete_this_script(){
    cd ~;
    local script_name;
    script_name=`basename "$0"`;
    rm -rf ./$script_name;
}

init;

EOF
}

function create_line_across_terminal(){
    printf '\n%*s\n\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -;
}

init
