FROM heroku/miniconda

# Grab requirements.txt.
ADD ./requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install -qr /tmp/requirements.txt

# Add our code
ADD ./ /opt/webapp/
WORKDIR /opt/webapp

RUN conda install scikit-learn
RUN conda install cython
RUN conda install m2w64
RUN conda install numpy
RUN conda install pandas
RUN conda install scipy
RUN conda install statsmodels
RUN conda install fbprophet


CMD gunicorn --bind 0.0.0.0:$PORT wsgi
