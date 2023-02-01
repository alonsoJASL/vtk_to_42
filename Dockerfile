FROM continuumio/miniconda3:latest
LABEL maintainer="<j.solislemus@kcl.ac.uk>"

RUN apt update --fix-missing && \ 
	apt install -y --no-install-recommends build-essential curl libsm6 libxrender-dev libgl1-mesa-glx && \  
	apt clean && rm -rf /var/lib/apt/lists/* && \ 
	conda create -n vtk910 python=3.8 -y && \ 
	conda install -c conda-forge vtk==9.1.0 -n vtk910 && \
	conda clean -afy && \  
	curl https://sh.rustup.rs --output /tmp/rust_setup.sh && \ 
	chmod +x /tmp/rust_setup.sh && /tmp/rust_setup.sh -yq && \ 
	$HOME/.cargo/bin/cargo install ripgrep 

COPY . /code/
WORKDIR /code/

ENV PATH="/opt/conda/envs/vtk910/bin:$PATH"
ENV PYTHONPATH="${PYTHONPATH}:/code"

CMD ["-h"]
ENTRYPOINT ["/opt/conda/envs/vtk910/bin/python3", "-u", "/code/entrypoint.py"]
