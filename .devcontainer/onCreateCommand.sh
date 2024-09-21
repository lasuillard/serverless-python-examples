#!/usr/bin/env bash

# Install pyenv
curl https://pyenv.run | bash

sudo apt-get update && sudo apt-get install -y \
    bash-completion

echo '
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

eval "$(pyenv virtualenv-init -)"
' >> ~/.bashrc
