# We start from the Miniconda image
FROM debian:buster

# Install necessary packages
RUN apt-get update &&\
    apt-get install -y \
    libxext6 \
    libxrender1 \
    wget

# Create vagrant user
RUN groupadd -g 1000 vagrant &&\
    useradd -m -g 1000 -u 1000 vagrant
USER vagrant

# Install Miniconda
RUN cd $HOME &&\
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh &&\
    bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda &&\
    rm Miniconda3-latest-Linux-x86_64.sh

# Set the default shell to bash
SHELL ["/bin/bash", "-c"]

# Install RDKit through conda
RUN source $HOME/miniconda/bin/activate &&\
    conda create -y -c rdkit -n rdkit-env rdkit libboost=1.65.1 &&\
    conda deactivate

# Activate the conda environment by default
RUN echo "source $HOME/miniconda/bin/activate rdkit-env" > ~/.bashrc

# Default working directory and command
WORKDIR /vagrant
CMD /bin/bash