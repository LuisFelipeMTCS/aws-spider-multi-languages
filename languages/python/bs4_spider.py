import requests
import boto3

URL = "https://www.cnnbrasil.com.br/entretenimento/the-new-york-times-elege-os-100-melhores-filmes-do-seculo-21-confira/"
BUCKET = "aws-data-lake-portfolio"

def fetch_html():
    response = requests.get(URL)
    response.raise_for_status()
    return response.text

def save_to_s3_html(html, spider_name="BeautifulSoup"):
    s3 = boto3.client("s3")

    # Nome fixo do arquivo, sem timestamp
    key = f"raw/{spider_name}_spider.html"

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=html.encode("utf-8"),
        ContentType="text/html"
    )

    print(f"✅ HTML bruto salvo em s3://{BUCKET}/{key}")

if __name__ == "__main__":
    html = fetch_html()
    save_to_s3_html(html, spider_name="BeautifulSoup")
