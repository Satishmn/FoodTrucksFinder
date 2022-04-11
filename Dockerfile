# 1. Base image
FROM python:3.9.12

# 2. Copy files
COPY . /src

# 3. Install dependencies
RUN pip install pandas
RUN pip install streamlit
RUN pip install plotly