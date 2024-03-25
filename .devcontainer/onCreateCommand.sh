#!/usr/bin/env bash

sudo apt-get update && sudo apt-get install -y \
    bash-completion \

# Install pyenv
curl https://pyenv.run | bash

echo '
if [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi

export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

eval "$(pyenv virtualenv-init -)"
' >> ~/.bashrc
