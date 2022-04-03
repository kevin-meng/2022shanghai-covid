FROM openeuler/openeuler:21.09

# Update repo
COPY ./deploy/openEuler.repo /etc/yum.repos.d/openEuler.repo
RUN yum -y update
# Install pip
RUN curl -fsSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py && rm ./get-pip.py
# Build and deploy
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["streamlit", "run", "app.py"]
