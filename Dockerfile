FROM python:3.10.12
WORKDIR /src
COPY src/ /src
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]